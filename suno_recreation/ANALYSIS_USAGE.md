# Usage audit: Instagram-song analysis

This matrix reports the usage visible in the local Codex rollout records and the analysis artifacts. It distinguishes Codex token accounting, Codex task elapsed time, model-reported inference timers, and shell-command wall time; those quantities are not interchangeable.

## Scope and measurement rules

- **Codex thread:** `01a0d3c3-922a-7ab2-bc0f-04821057413c`, working in this repository. The detailed log is the rotated rollout `rollout-2026-09-24T16-18-01-01a0d3c3-922a-7ab2-bc0f-04821057413c_01a0d3c7-ccfd-76d2-9984-d6abc23fa306.jsonl`; a short preceding rollout contains an aborted start and no token records.
- **Snapshot:** latest token record inspected was at **2026-09-24 21:47:04 UTC**. The final log-audit turn was still open, so its duration and token counts are a snapshot, not a final total.
- **Token counts:** per-stage counts sum the last `turn_token_usage` recorded for each Codex task turn in that stage. `cached input` is a subset of input, not extra tokens. `reported total` is the total recorded by Codex; `reasoning output` is listed separately because the telemetry reports it separately. Input includes system/developer context, conversation history, and tool context, so it is not a count of user-written words or unique new content.
- **Task elapsed seconds:** sum of each turn's logged `task_started` to `task_complete` interval. This includes waiting that occurred inside a running turn. It excludes gaps between turns. The unfinished audit turn is measured only through the latest token record.
- **Other models:** prefer a model's own `runtime_s` or `generation_s` fields when present. Where only a command duration exists, it is shell wall time for that invocation and may include model loading, decoding, file I/O, or waiting. Concurrent command durations can overlap; do not add them as unique elapsed time.

## Codex usage by work phase

Phases are assigned by task-start timestamps and the user request being handled. Automatic goal continuations are grouped with the associated work. Token columns are exact log aggregates at the snapshot; durations are rounded to whole seconds.

| Work phase | Turns | Codex task elapsed | Input tokens (cached subset) | Output tokens | Reasoning output | Codex-reported total |
|---|---:|---:|---:|---:|---:|---:|
| Initial eight-track transcription, pronunciation, and music analysis | 2 | 2,453 s (40m 53s) | 11,044,750 (10,581,888) | 60,962 | 12,845 | 11,105,712 |
| Suno API research, credential-provider clarification, and ASR/model evaluation | 14 | 3,188 s (53m 08s) | 40,912,148 (40,241,408) | 95,053 | 46,007 | 41,007,201 |
| Repository setup, text-only commit constraint, and video packaging | 6 | 1,795 s (29m 55s) | 18,949,891 (18,610,688) | 56,596 | 23,413 | 19,006,487 |
| Door Knockers analysis, descriptive evidence renames, reference checker, cleanup, and push | 1 | 2,053 s (34m 13s) | 17,402,958 (17,116,672) | 68,948 | 33,195 | 17,471,906 |
| Apple and Android ringtone creation | 1 | 231 s (3m 51s) | 2,053,363 (2,025,472) | 8,540 | 3,039 | 2,061,903 |
| Answer about remaining analysis work | 1 | 14 s | 134,977 (97,024) | 392 | 0 | 135,369 |
| Current Codex-log audit (open at snapshot) | 1 | At least 558 s (9m 18s) | 3,817,619 (3,755,008) | 22,178 | 13,634 | 3,839,797 |
| **Thread total through the snapshot** | **26** | **At least 10,292 s (2h 51m 32s) of task intervals** | **94,315,706 (92,428,160)** | **312,669** | **132,133** | **94,628,375** |

The overall log span from the first task start (**14:18:02 UTC**) to the latest token record (**21:47:04 UTC**) is **26,942 seconds (7h 29m 02s)**. That is elapsed calendar time, not continuous work. The difference between the log span and summed task intervals is time between recorded task turns and is not attributed here to user idle time, model inference, or any one cause. The cached-input share is about **98%** of logged input; repeated large conversation/context blocks therefore dominate the raw input count. These figures should not be interpreted as 94 million newly authored tokens.

## Other-model and signal-tool timing

| Model / tool | Recorded work | Time | What the timer means and what it does not mean |
|---|---|---:|---|
| Whisper large-v3-turbo via MLX | Full, chunked, and targeted passes across the original clips, plus Door Knockers full and targeted passes | **974.1 s** across five timed transcription commands | Sum of command wall durations in the rollout log: 202.6 + 192.1 + 73.6 + 491.1 + 14.8 s. These include startup/model loading and Python work; no per-clip inference-only timer was saved. The 491.1 s Door Knockers pass is especially a command-level elapsed measurement. |
| Qwen2-Audio-7B MLX attempt | Model snapshot/download command, then `caption_audio.py` attempt | **592.6 s** and **709.6 s**, respectively | The attempt produced no completed descriptions and was abandoned after the model download ran out of disk space. The command intervals overlapped in the rollout, so the values must not be added into a single elapsed total. This time yielded no report evidence. |
| MOSS-Audio-4B Thinking MLX | 18 original-mix excerpts plus 13 separated-stem interpretations | **229.96 s** summed from artifact `generation_s` fields | Generation-loop time only. Audio encoding, feature extraction, model load, and other setup are excluded, so this is a lower bound on total MOSS compute time. Model repository download command: **223.4 s**, separate setup activity. |
| Vosk small English ASR | Outputs cover nine source clips; eight files have runtime metadata | **19.79 s** summed from the eight available per-file `runtime_s` values | Recorded recognizer time. The Door Knockers Vosk output has no runtime field, so its time is unknown rather than zero. Model download/setup is not included. Output is retained as a noisy independent comparison. |
| Vosk English 0.22 ASR | Five of nine source clips | **53.85 s** summed from per-file `runtime_s` | Recorded recognizer time; coverage is partial. The model archive download command took **553.7 s**, which is setup time, not inference. |
| Demucs / HDEMUCS separation | Estimated vocals/backing for nine clips | **58.77 s** summed from per-track stem metadata | Per-file model-inference timers. Model load, audio extraction, and file writing are excluded. The enclosing batch commands took longer. |
| Apple Speech attempt | Door Knockers fallback transcription | **121.35 s** command wall time | Timed out without a transcript. It did not contribute transcript evidence. |
| pYIN vocal-pitch tracking | Nine clips | **12.32 s** summed from per-track `runtime_s` | Signal-processing runtime, not a language-model call and not an exact melody transcription. |
| Suno generation/API | No generation request was made | **0 s recorded** | The API was researched, but no call was made, no credits were spent, and no generated Suno output was evaluated. |

No token counts for Whisper, MOSS, Vosk, Demucs, Qwen2-Audio, or Apple Speech are present in the inspected Codex logs or artifacts. Those systems' seconds cannot be converted into tokens from this evidence.

## Per-video recorded runtimes

These are the available per-track timers from Vosk, MOSS, separation, and pYIN artifacts. Whisper was run in batches, so its command time cannot be apportioned accurately by video from these logs. A dash means no runtime record for that track/model, not zero processing time.

| Track | Vosk small (s) | Vosk large (s) | MOSS generation (s) | Stem separation (s) | pYIN pitch (s) | Sum of these recorded per-track timers (s) |
|---|---:|---:|---:|---:|---:|---:|
| Flaunching | 1.42 | 2.12 | 21.27 | 2.54 | 3.97 | 31.32 |
| Guttae / Good Day | 1.53 | 4.02 | 36.50 | 3.54 | 0.34 | 45.93 |
| Corbel / Bargeboard | 2.39 | 9.11 | 21.51 | 6.10 | 0.55 | 39.67 |
| Columns / Classical Orders | 3.78 | 18.44 | 25.27 | 8.33 | 0.78 | 56.61 |
| Doors | 2.44 | 20.16 | 28.12 | 10.13 | 0.91 | 61.76 |
| Windows | 4.39 | — | 30.92 | 10.53 | 1.00 | 46.83 |
| Echinus / Entasis | 1.56 | — | 19.91 | 3.58 | 0.32 | 25.37 |
| Hall House | 2.27 | — | 25.53 | 7.58 | 0.69 | 36.07 |
| Door Knockers | — | — | 20.93 | 6.44 | 3.77 | 31.14 |

The per-track subtotal is only the sum of timers actually stored in artifacts. It excludes Whisper, model downloads, model initialization, OCR, chroma/tempo analysis, and other uninstrumented work; it is not a full per-video runtime. Door Knockers Whisper and targeted ASR are only available as batched command durations above.

## Interpretation limits

The logs support exact Codex token totals and task-interval measurements at the stated snapshot. Other-model timings have mixed precision: some are self-reported inner-loop timers, some are command wall durations, and some failed attempts only have elapsed command time. These measures can overlap and have different start/stop boundaries. In particular, there is no defensible single total for “all model seconds” without double-counting concurrent work or mixing setup with inference. The external models' interpretation quality is not measured by their runtime or token accounting.
