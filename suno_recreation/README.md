# Architectural music — Suno recreation pack

Eight source videos are covered. The door-knocker video, `DdZlT3TIx3q.mp4`, is excluded. All nine source-file contents match the original checksums. The architectural-features clip has been renamed to `bargeboard.mp4`; the manifest records both names.

This GitHub snapshot contains text files only. Source videos, extracted audio, stems, sampled images and other binary media remain in the local workspace and are not included; links to those assets require that workspace.

This is a source-grounded transcription and a set of **recreation recipes**, not a verified musical score or a promise of identical Suno output. The source lyrics are separated from suggested performance instructions. Uncertain words, repetition counts, instrumental identifications, and tonal estimates are called out in each track.

## How to use the pack

1. Read the timed `source_transcript.txt` alongside `analysis.md` for the best-supported words, timing and uncertainty notes.
2. Treat `lyrics.txt` as a practical Suno arrangement, not a verbatim transcript: repeated hooks may be expanded or normalized, and uncertain lines are identified in `analysis.md`. In Suno's **Custom** mode, paste `style.txt` into **Styles** and `lyrics.txt` into **Lyrics**. Bracketed section/delivery tags are instructions, not words transcribed from the video.
3. Use the pronunciation guide to correct a difficult word. If Suno mispronounces an architectural term, try the corresponding phonetic spelling in place of that word. Keep the conventional spelling in your saved transcript.
4. Start around **135–136 BPM**. If that sounds too fast against the source, make a second take around **67–68 BPM** with a half-time feel; the two readings are supported by onset estimates on the same audio, and their relation does not establish the original meter. Straight 4/4 is only a reconstruction setting.
5. Treat each track’s key-profile candidates as experiments, not source keys. Compare one feature at a time: phrase placement and word stress, vocal tone, backing groove, then fills and effects. Keep successful wording while changing one instruction per attempt.
6. Short durations, pronunciation respellings, and bracketed directions are requests to the generator. They do not guarantee exact timing, pitches, timbre, or sound effects. If a spoken punchline or isolated effect is essential, it may need a separate edit after generation.

Suno also has an [official API platform](https://platform.suno.com/), verified on 2026-09-24. Its public page advertises a REST API for songs, covers and mashups. Account eligibility, prices, quotas and request parameters were not verified behind sign-in; no API calls have been made.

Suno documents separate custom lyrics and Styles inputs in [Custom Mode](https://help.suno.com/en/articles/3726721) and the [own-lyrics guide](https://help.suno.com/en/articles/2415873). Unwanted elements can be entered in **Advanced Options → Exclude**, as documented in [Suno's exclusion guide](https://help.suno.com/en/articles/3161921). Suggested exclusions for these recipes: `long intro, extended instrumental solo, extra verses, wordless choir, excessive melisma`.

## Evidence and limits

- **Directly checked:** the nine-file inventory; durations and audio/video streams; source checksums; selected frames and on-screen captions, including the exclusion and specialist spellings.
- **Transcription evidence:** local Whisper large-v3-turbo on the audio, followed by short overlapping chunks, targeted checks, and an independent Vosk/Kaldi comparison. The Vosk small and higher-capacity models both produced noisy raw hypotheses; the large model completed five clips before a disk-space failure. Neither model justified changing the caption-guided transcript. Captions correct obvious speech-recognition substitutions. Captions are evidence of intended text; they do not by themselves prove every syllable was sung that way.
- **Audio descriptions:** local MOSS-Audio model interpretations of successive excerpts. These are model inferences. Instrument names, accent judgments, and texture descriptions are not direct listening by the writing assistant.
- **Rhythm:** librosa beat tracking was cross-checked against onset-envelope autocorrelation with a different estimator. These share the same source signal and related onset features; they are not independent human beat counts. Both support a pulse near 135 BPM, with half-time ambiguity.
- **Tonality:** pitch-class profile comparisons provide candidates only. Voice, percussion overtones, short duration, sampled speech, and weak tonal material can bias them. The guide does not present them as established keys or chord progressions.
- **Pronunciation:** broad performance respellings and stress guidance, informed by recognizer outputs and the captioned wordplay. They are not a narrow IPA transcription of the singer. Unresolved vowel details are marked.
- **Melody:** phrase contour and delivery recipes, with explicit uncertainty, rather than invented note sequences. pYIN checks on estimated vocals, original mixes and harmonic-only audio retained too few reliable frames to recover a continuous melody; no exact vocal score or verified harmony transcription is claimed.
- **Listening aids:** each track has 8-second PCM excerpts and a waveform/onset-strength plot under `evidence/listen_cues/`. These make source intervals easier to inspect; they are navigation and signal summaries, not a substitute for perceptual listening or score transcription. The current work environment can play the audio but does not expose speaker output for me to hear, so subjective musical descriptions remain attributed to the audio model or framed as proposed prompt choices.
- **Second pass:** Demucs estimated vocals/backing, followed by targeted model queries, strengthens the broad electronic description for seven clips and the Windows reading “oriel too”. Guttae instrumentation remains ambiguous. These results and remaining failures are documented in [METHODS.md](evidence/METHODS.md).
- **Presentation:** file and local-link checks pass. Browser policy blocked the local HTML preview, so visual layout and copy/playback interaction remain untested.
- **Suno validation:** prompts have been prepared, not generated or tested in a Suno account.

The raw evidence and analysis scripts are in `evidence/`. The manifest records SHA-256 hashes of every original. Full-file recognizer errors are retained there for auditability; use the corrected track reports rather than those raw transcripts.

## Tracks

| Track | Original file ID | Duration | Copy-ready files |
|---|---|---:|---|
| [Flaunching](tracks/01_flaunching/analysis.md) | `Dc1uBZahhts` | 15.81s | [Styles](tracks/01_flaunching/style.txt) · [Lyrics](tracks/01_flaunching/lyrics.txt) · [Pronunciation](tracks/01_flaunching/pronunciation.md) |
| [Guttae / Good Day](tracks/02_guttae/analysis.md) | `Dc8axxYIC3k` | 22.29s | [Styles](tracks/02_guttae/style.txt) · [Lyrics](tracks/02_guttae/lyrics.txt) · [Pronunciation](tracks/02_guttae/pronunciation.md) |
| [Corbel / Bargeboard / Architectural Features](tracks/03_corbel_bargeboard/analysis.md) | `DcRZB_PBFkr` | 38.01s | [Styles](tracks/03_corbel_bargeboard/style.txt) · [Lyrics](tracks/03_corbel_bargeboard/lyrics.txt) · [Pronunciation](tracks/03_corbel_bargeboard/pronunciation.md) |
| [Columns / Classical Orders](tracks/04_columns/analysis.md) | `DcYTYvMBSMn` | 53.62s | [Styles](tracks/04_columns/style.txt) · [Lyrics](tracks/04_columns/lyrics.txt) · [Pronunciation](tracks/04_columns/pronunciation.md) |
| [Doors](tracks/05_doors/analysis.md) | `DcbYsWLhhdZ` | 64.69s | [Styles](tracks/05_doors/style.txt) · [Lyrics](tracks/05_doors/lyrics.txt) · [Pronunciation](tracks/05_doors/pronunciation.md) |
| [Windows](tracks/06_windows/analysis.md) | `DcqWhZtBIEI` | 67.01s | [Styles](tracks/06_windows/style.txt) · [Lyrics](tracks/06_windows/lyrics.txt) · [Pronunciation](tracks/06_windows/pronunciation.md) |
| [Echinus / Entasis](tracks/07_echinus_entasis/analysis.md) | `DcvxvGDhSeb` | 22.48s | [Styles](tracks/07_echinus_entasis/style.txt) · [Lyrics](tracks/07_echinus_entasis/lyrics.txt) · [Pronunciation](tracks/07_echinus_entasis/pronunciation.md) |
| [Hall House](tracks/08_hall_house/analysis.md) | `DdLxzBIoJ8F` | 49.97s | [Styles](tracks/08_hall_house/style.txt) · [Lyrics](tracks/08_hall_house/lyrics.txt) · [Pronunciation](tracks/08_hall_house/pronunciation.md) |

[Read the complete guide](COMPLETE_GUIDE.md) · [Open the listening and copying page](index.html)
