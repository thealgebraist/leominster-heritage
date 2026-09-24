# Analysis record

Date: 2026-09-24. Source directory: `/Users/anders/projects/barge/account_mp4`.

## Source handling

All original videos were read only. `manifest.json` records source SHA-256 hashes, ffprobe streams, and durations. Audio was extracted by FFmpeg as mono 16 kHz PCM WAV for recognition. This is an analysis copy, not a lossless preservation copy of the original stereo audio. Keep the original videos for auditory comparison and any later production work.

The excluded door-knocker video is `DdZlT3TIx3q.mp4`. Identification is supported by the initial contact sheet and `excluded_knockers.jpg`. An audio copy was created during inventory, before exclusion; no lyrics or music packet was made for it.

## Lyrics and captions

1. MLX Whisper large-v3-turbo, English, deterministic first pass with word timestamps (`asr/`).
2. Eight-second sections with half-second overlaps (`asr_chunks/`). These are the same model, not an independent recognizer.
3. Targeted short sections with an architectural-vocabulary prompt and temperature fallback (`asr_targeted/`). A vocabulary prompt may bias recovery toward the expected terms, so it is not treated as independent proof.
4. Video frames sampled at two per second through FFmpeg. Tesseract and Apple Vision produced OCR records. A yellow-text mask was also used. Selected frames were visually inspected to resolve specialist spellings and intended phrase boundaries.

Known failure: the full-file recognizer hallucinated long strings of “door” and “guttae”, omitted most of the middle architectural-feature sequence, and confused unusual nouns. Those outputs are retained but not silently accepted. Some exact repeat counts remain unresolved.

The first Apple AVFoundation attempt could not decode the source VP9 streams (error -11869 / -12430). FFmpeg frame extraction bypassed that limitation. OCR of the resulting frames was possible; sparse text and animated captions still cause omissions and false text.

## Rhythm and tonality

`analyze_signal.py` computes an HPSS-assisted beat estimate and whole-mixture pitch-class profile correlations. `tempo_crosscheck.py` checks spectral-flux onset periodicity through SciPy autocorrelation and interpolated peaks without the beat tracker's tempo prior. Both support a strong ~135 BPM pulse. Half-time and subdivision aliases also occur. Neither method establishes meter or exact note values.

Pitch-class profiles are Krumhansl-style major/minor correlations on the harmonic estimate. Correlations are not calibrated probabilities. Mixed vocals, non-pitched sounds, limited duration, and rhythmic repetition can make the top key candidate wrong. No chord sequence, exact fundamental vocal range, or note-by-note melody was validated.

## Audio-description model and resource recovery

An initial attempt to download `mlx-community/Qwen2-Audio-7B-Instruct-4bit` failed with `No space left on device`. Its actual weight file was ~6.56 GB, larger than the model card's rough size claim. The failed download was stopped and its temporary partial file removed. It produced no audio descriptions and is not evidence for the reports.

The completed Whisper weight cache created for this task was also removed after the transcript passes; the transcripts remain. Existing unrelated models and source files were not removed.

The replacement is `RumiLabs/MOSS-Audio-4B-Thinking-MLX-4bit`, revision `35d32584136a619f3d4be37daaf3050b825202ec` (~2.96 GB repository). Its bundled inference code was inspected, and `caption_moss.py` runs its local audio encoder and text decoder on successive excerpts up to 24 seconds. Final response text is separated from model reasoning. This is model interpretation, not direct listening by the writing assistant. Specific instrument/genre/voice judgments can be wrong.

Model documentation: [MOSS-Audio upstream](https://github.com/OpenMOSS/MOSS-Audio), [community conversion](https://huggingface.co/RumiLabs/MOSS-Audio-4B-Thinking-MLX-4bit). The conversion's own README reports limitations in fine-grained music identification. Whisper implementation: [MLX Whisper](https://github.com/ml-explore/mlx-examples/tree/main/whisper).

## Output boundary

The conventional-spelling timed transcripts preserve unresolved readings. Suno lyric files are practical reconstruction arrangements, with explicitly identified choices for uncertain words/counts and added bracketed delivery instructions. Style files combine supported broad characteristics with proposed arrangement directions. They do not constitute an exact recreation of the recorded melody, harmony, voice, or edit effects.

No files have been uploaded to Suno, no credits spent, and no generated Suno audio evaluated.

## Separated stems and second pass

`separate_audio.py` extracts stereo 44.1 kHz audio and estimates vocals and backing with torchaudio's `HDEMUCS_HIGH_MUSDB_PLUS`. Eight-second chunks overlap by one second and are combined with weighted overlap. These are estimates, with audible-source leakage possible, not original multitracks. Per-file metadata and residual RMS are in `stems/`. The residual is approximately 3–7% of mixture RMS; this measures mixture reconstruction, not separation accuracy.

`moss_query.py` uses the same local audio model on the first 15 seconds of each backing stem and five targeted vocal passages. Prompts and unedited responses are in `second_pass/`. Seven backing responses favor electronic percussion/bass/synths. Guttae instead produces an acoustic/electronic ambiguity, now reflected in its report. These are repeated observations with the same audio-description model, not independent expert judgments.

The Windows query supports “oriel too”. Whisper full, short-chunk and targeted passes, plus the separated-vocal model, all return “soaping nicely” for Flaunching. The transcript uses “soaping”; “sloping” is documented only as an architectural-context guess, not the source reading. Both suggest “hold on” in Doors; Hodor remains only a contextual alternative. The Guttae vocal response loops into impossible repetition counts and is rejected for counting. The Echinus/Entasis response supplies uncertain phonetic approximations; it does not establish the conventional pronunciation as the actual recording. Speculation about games, television, magical incantations, or original provenance is discarded.

For the community MOSS conversion, NumPy loads the bundled compressed mel-filter asset because `mx.load` failed on that asset. The bundle's documented direct audio-token insertion is used; token-name aliases do not by themselves indicate incorrect audio insertion. Input audio-position counts are checked against encoded features. The initial open-thinking generation looped; completed runs close the thinking prefix, apply repetition control, and preserve the final response. These workarounds enable execution but do not validate music recognition accuracy.

## Pitch tracking check

`vocal_pitch.py` runs pYIN on the estimated vocal stems, retaining only voiced frames with probability at least 0.7 and an RMS floor. It retains only 0.3–22.3% of frames across these clips (mostly below 5%). Consequently, it is inadequate to recover a continuous melody or precise vocal range. Raw pitch tracks and per-phrase summaries are in `pitch/`; note quantiles are not promoted into the user-facing recipe as an exact melody. Sparse tracking is a failed validation of a score, not evidence that the recording has no melody.

## Source and presentation verification

The architectural-features source is now named `account_mp4/bargeboard.mp4`; its bytes match the original `DcRZB_PBFkr.mp4` SHA-256. The manifest preserves the original name and records `current_file`. All nine source hashes pass verification.

Hall House's audio stream ends at 48.645 seconds; its video lasts 49.967 seconds. The remaining video-only tail does not contain omitted source audio. Small differences between other WAV and container durations reflect codec/frame padding.

`verify_pack.py` verifies eight included packets, exclusion of the knocker clip, source hashes, text presence/length, excerpt coverage and the HTML's structure/local links. This is not semantic verification. A computer-use attempt to preview the local HTML was blocked by the browser URL security policy. No alternate browser route was attempted. Interactive behavior and visual layout remain untested.

Official API availability was checked on 2026-09-24: https://platform.suno.com/ advertises a REST API for songs, covers and mashups and redirects to account sign-in. Account eligibility, pricing, quotas and request schemas were not accessible without signing in. No Suno API calls were made.


Dictionary checks for the architectural terms Echinus/Entasis: Cambridge lists UK and US echinus variants at https://dictionary.cambridge.org/us/pronunciation/english/echinus; Wiktionary records English entasis IPA /ˈɛntəsɪs/ at https://en.wiktionary.org/wiki/entasis. These establish plausible conventional targets, not the recorded singer’s accent.

The macOS Speech framework reports `authorization=0` (`notDetermined`) while both English UK and English US recognizers are available and advertise on-device support. `check_apple_speech.swift` only queried status; it did not request permission or transcribe any audio. A future offline pass would require the user to grant macOS Speech Recognition access and the client to require on-device processing.


## Third recognizer comparison

To check whether Whisper's repeated-word hallucinations or specialist-word substitutions could be reduced locally, the independent Vosk/Kaldi `vosk-model-small-en-us-0.15` model was run offline on all eight included audio files with an unconstrained vocabulary. The unedited, timestamped hypotheses are in `asr_vosk/`; the recognizer, conversion, sample rate, and script are recorded there. This small US English model is a poor match for the source's specialist British architectural terms and music-backed chant: it changes Flaunching, produces unrelated phrases over the columns and windows lists, and cannot reliably count Door/Guttae repetitions. It agrees with parts of Hall House and the broad two-syllable guttae / good-day sound, but these matches do not settle the uncertain passages. No transcript was changed on the basis of Vosk alone. This negative comparison supports keeping the existing uncertain markers.

The official Vosk model index lists the first model as a 40 MB lightweight wideband US English model (Apache 2.0), rather than its larger high-accuracy server models: https://github.com/alphacep/vosk-space/blob/master/models.md. Archive SHA-256: `30f26242c4eb449f948e42cb302dd7a686cb29a3423a8367f99ff41780942498`. The archive and extracted weights were deleted after the comparison to recover disk space; the model URL, archive hash and raw outputs remain recorded in `asr_vosk/model_provenance.json`. Repeating the pass requires downloading and extracting those weights again.


A larger generic US English model, `vosk-model-en-us-0.22` (1.8 GB archive, Apache 2.0 on the official index), was downloaded for a higher-capacity comparison. It produced only five raw transcripts (Flaunching, Guttae, architectural features, Columns, Doors); its output still contains severe replacements and repetitions and does not resolve the uncertain words/counts. The sixth output file could not be written because the filesystem ran out of space while the large acoustic model was loaded. We removed its weights immediately afterward; no source files were modified. Its five raw results are in `asr_vosk_large/`, and the model URL, archive SHA-256 `47f9a81ebb039dbb0bd319175c36ac393c0893b796c2b6303e64cf58c27b69f6`, and completed-file list are recorded in `asr_vosk/model_large_provenance.json`. The remaining three clips have the complete small-model comparison in `asr_vosk/`; no large-model result is claimed for them. The partial high-capacity pass did not provide evidence to change the transcript.
