# Doors

Source: [doors.mp4](../../source_videos/doors.mp4) · **64.69 seconds** · [extracted audio](../../evidence/audio/DcbYsWLhhdZ.wav)

## Listening/navigation aids

- [Waveform and onset-strength overview (navigation aid, not a score)](../../evidence/listen_cues/DcbYsWLhhdZ/waveform_onsets.png)
- [8-second source-audio excerpts with relative time ranges](../../evidence/listen_cues/DcbYsWLhhdZ/)

The excerpts are PCM slices from the existing mono analysis WAV. The plot shows amplitude and spectral onset strength; it does not establish notes, instrumentation, meter, or a transcription. Use the original stereo/video for final listening checks.

## Transcript and timing

| Approx. source time | Best-supported words / event |
|---|---|
| 0.0–6.3 | Door repeated [approximately seven calls]. |
| 6.3–7.6 | Green door, red door. |
| 7.6–10.6 | Door repeated; exact count unresolved. |
| 10.6–11.2 | Cat flap [likely; supported by two ASR passes and partial OCR at 11s]. |
| 11.2–12.4 | Blue door, black door. |
| 12.4–14.2 | Door repeated. |
| 14.2–16.4 | Back door, front door / Big door, small door. |
| 16.4–18.0 | Door repeated; two overlapping Whisper chunks hear a possible “trap door” near the end, but the word is not caption-confirmed. |
| 18.0–18.9 | Old door, new door. |
| 18.9–20.3 | Door repeated. |
| 20.3–23.5 | Stable door / Cellar door! |
| 23.5–28.8 | Ah! / hold on? / [Hodor?] / intervening vocal passage; the exact wording is unresolved. |
| 28.8–31.9 | Door, panel door [caption also says panelled], plank door. |
| 31.9–35.2 | Door, door, studded door, arched door. |
| 35.2–40.0 | Door, door, secret door / Where? / Behind the door. |
| 40.0–42.9 | Door repeated [approximately six calls]. |
| 42.9–45.9 | Green door, red door, blue door / Cat flap! |
| 46.0–50.3 | Door, door, door / And one more… |
| 51.5–59.3 | Dumbledore! [caption splits it as Dumble / Door; held/effected passage follows] |
| 59.4–61.3 | Door! |
| 61.3–64.7 | End-card/music tail. |

Punctuation is editorial. Caption timing and sung-word timing can differ. Bracketed uncertainty notes above are not sung text.

## Pronunciation and vocal phrasing

| Word / phrase | Broad sound / stress guide | Delivery and evidence |
|---|---|---|
| Door | DAW | One syllable with a long rounded vowel; avoid adding a separate duh-or syllable. |
| Green / red / blue / black door | GREEN DAW / RED DAW / BLOO DAW / BLAK DAW | Make the colour a pickup or accented first word, then repeat the identical door sound. |
| Back / front / big / small door | BAK DAW / FRUNT DAW / BIG DAW / SMAWL DAW | Crisp adjective; consistent long DAW. |
| Trap door | TRAP DAW | Two sharply articulated syllables; transcript status is tentative because only Whisper chunk passes suggest “trap”. |
| Old / new / stable / cellar door | OHLD DAW / NYOO DAW / STAY-buhl DAW / SEL-uh DAW | Stable and cellar are two syllables each. |
| Panel / plank / studded / arched door | PAN-uhl DAW / PLANK DAW / STUD-id DAW / AHCHT DAW | The source audio recognizer supports panel while captions use both panel and panelled. |
| Secret door; Where? Behind the door | SEE-krit DAW; WAIR? bih-HYND thuh DAW | Use a separate spoken questioning voice for Where if recreating the comic dialogue. |
| Cat flap | KAT FLAP | Two abrupt syllables; not “cut flop”. |
| And one more | und WUN MAW | Build anticipation by delaying the answer. |
| Dumbledore / Dumble-door | DUM-buhl-DAW | Three syllables; same long DAW as every other door. Preserve the pun. |
| Hodor? | HOH-daw? | Tentative identification only; a separate low spoken interjection is a reconstruction option, not confirmed text. |

Broad respellings are performance targets; they do not establish every vowel of the recorded accent. Capital letters indicate stress, not a request to shout.

## Music, tone, rhythm, and effects

**Voice and delivery — model interpretation:** An emphatic male voice uses the same short door sound repeatedly, with spoken/shouted comic interruptions and changes of intensity. Accent labels from the audio model are not reliable enough to fix a regional accent.

**Melody and phrase shape:** A one-word pitch-and-rhythm cell dominates, expanded with adjective pickups. Melodic movement is limited and largely follows speech intonation. Later Dumbledore lengthens the same door vowel into a punchline. Suggested rendition: retain one stable door motif, vary the preceding adjective, and save the largest lengthening and pause for the final pun; exact source notes are not established.

**Rhythm:** A fast regular pulse near 135 BPM is supported by two signal-analysis methods; 67–68 BPM is the corresponding half-time interpretation. Short syllables and repeated words carry the rhythmic interest. Use straight 4/4 as a reconstruction setting; the original meter and precise swing ratio are not verified. Autocorrelation candidates: 67.6 BPM (peak score 0.64), 134.9 BPM (peak score 0.62), 90.0 BPM (peak score 0.54). These are relative peak scores, not probabilities; both tempo estimates use the same audio and cannot confirm one another independently.

**Tonality and harmony:** The major/minor profile is essentially tied around C, so the original mode is unresolved. Use a repetitive low tonal loop and light comic mood as a starting point. Do not impose a long changing chord progression on the repeated one-word hook. Mixed-audio pitch-class profile candidates: C minor (0.57), C major (0.57), F minor (0.55). These numbers are correlation scores, not probabilities. They are retained for experimentation, not stated as verified keys. An exact chord sequence and note-by-note melody have not been established.

**Section-level chroma comparison:** Both signals rank F minor first in 0–16 s, C minor in 16–32 s, then F minor through most of 32–64 s. This repeated section pattern supports testing an F-minor / C-minor contrast, but does not prove a chord progression or tonal function. The table gives only each signal's top profile candidate; the full ranked candidates, method and caveats are in [section_tonality.json](../../evidence/section_tonality.json) and [section_tonality.py](../../evidence/section_tonality.py). Scores are correlations, not probabilities.

| Time window | Original mix harmonic | Estimated backing harmonic |
|---|---|---|
| 0–8s | F minor (0.72) | F minor (0.68) |
| 8–16s | F minor (0.72) | F minor (0.48) |
| 16–24s | C minor (0.46) | C minor (0.58) |
| 24–32s | C minor (0.67) | C minor (0.60) |
| 32–40s | F minor (0.69) | F minor (0.58) |
| 40–48s | F minor (0.62) | F minor (0.49) |
| 48–56s | F minor (0.63) | F minor (0.57) |
| 56–64s | F minor (0.56) | F minor (0.65) |

**Overlapping-window sensitivity check:** Overlapping windows soften the exact change: both signals favor F minor in the opening, show a transition around 14–18 s, favor C-centered profiles around 18–28 s (minor/major labels vary), and return to F-minor-like profiles near 28–32 s. Later windows contain weaker local variations. This supports testing a tonal contrast, not a proven chord progression. The check uses 4-second windows at 2-second hops, so it tests whether the 8-second result depends on one fixed cut; these overlapping windows are still not musical phrase boundaries. Full rankings and caveats: [rolling_tonality.json](../../evidence/rolling_tonality.json) and [rolling_tonality.py](../../evidence/rolling_tonality.py).

**Instrumentation and timbre — model interpretation:** Multiple excerpts describe a synthetic bass/melodic backing and programmed percussion. The final excerpt additionally hears bright 8-bit-like arpeggiation and chime-like accents; these are timbral descriptions rather than confirmed console hardware or synthesis methods.

**Production, sound effects, and edits:** Abrupt comic interruptions and a long punchline passage are visible in the structure. The model reports cartoon-like noises, short chimes and whooshes in the later portion. The 24–28-second vocal/effect event is still not reliably decoded; the safe recreation choice is a brief break, explicitly differing from an exact transcription.

**Arrangement recipe:** A one-word ostinato with adjective substitutions. Keep the same door vowel, pitch cell, and rhythm through most of the piece, then use pauses and character-like spoken interruptions for the puns. Broaden stable/cellar door, break briefly, resume the list, ask “Where?”, and build a delayed Dumbledore payoff before the final single door.

## Source uncertainties and reconstruction choices

- The original full ASR pass looped on “door” for 29 seconds and is unusable in that section. Short chunks plus captions recover the list, but do not establish every repetition count.
- The passage around 24–28 seconds is not reliably transcribed. Both Whisper and the separated-vocal model return “hold on”; “Hodor” is a contextual alternative, not a recovered fact. The second model also reports an initial Ah vocalization. The paste-ready version keeps an Ah/hold-on spoken break, marking the wording as uncertain rather than replacing the vocal with an instrumental break.
- An early “cat flap” at about 10.6 seconds is likely: two independent ASR passes agree, and OCR partially reads “Cat Fla…” on the sampled 11-second frame. Exact onset and the surrounding repetition count remain uncertain. The later cat flap is also supported by audio recognition and a caption.
- Two overlapping Whisper chunk passes suggest “trap door” shortly after “small door”, but captions show repeated Door labels and do not confirm trap. The Suno lyric includes the tentative phrase to preserve this plausible spoken line; verify by listening before treating it as established.
- Repeated door counts in the recreation version are rhythmic choices, not claimed exact counts.

The musical recipe adds explicit directions where the source analysis is incomplete. “Suggested” features are prompt-design choices, not recovered measurements. The copy-ready lyric file expands some repeated motifs to a practical arrangement and omits unresolved nonverbal passages; use the timed transcript as the evidence record.

## Paste into Suno: Styles

```text
Comic electronic door chant, about 135 BPM. Upfront male English voice, crisp spoken-sung one-word door hook with a long rounded vowel, repeated on a compact pitch cell. Change the adjective pickups while keeping the door motif stable. Try an F-minor-like opening, a C-centered middle around 18–28 seconds with minor/major color flexible, then a return toward F minor near the next door list; leave later harmony flexible. These are section-profile candidates, not verified chords. Simple synth bass and programmed drum groove, short bright keyboard stabs. Use dry spoken questions and answers, sudden small pauses, and a sharp cat flap interruption. Toward the end add a brief bright game-like arpeggio or chime texture, pause after and one more, then a drawn-out Dumbledore punchline and one final door. Roughly 65 seconds; no extra verses.
```

## Paste into Suno: Lyrics

```text
[Repeated rhythmic hook]
Door, door, door, door
Door, door, door
Green door, red door
Door, door, door, door
Cat flap!
Blue door, black door
Door, door, door
Back door, front door
Big door, small door
[Possible phrase; verify against source]
Trap door
Door, door, door
Old door, new door
Door, door, door
[Longer calls]
Stable door
Cellar door!
[Brief spoken break; wording uncertain]
Ah! Hold on!
Door, panel door, plank door
Door, door, studded door, arched door
Door, door, secret door
[Spoken question]
Where?
[Spoken answer]
Behind the door!
[Rhythmic hook]
Door, door, door, door, door, door
Green door, red door, blue door
[Sharp spoken interjection]
Cat flap!
[Chant]
Door, door, door
[Spoken buildup]
And one more...
[Pause, final exclamation]
Dumbledore!
[Musical tail]
Door!
[End]
```

## Optional phonetic lyric variant

`lyrics_phonetic.txt` replaces specialist words with broad sound-based spellings. Use it only if ordinary spelling is mispronounced. These respellings are suggested generator inputs, not a certified transcription of the recorded phonemes.

## First comparison after generating

Check the original repeated door count and the unresolved middle interjection. In generated audio, keep DAW consistent through Dumbledore and ensure the pause before the joke is retained.

## Audio-model evidence

Raw excerpt interpretations are preserved below as evidence links. They are not independent listening verification, and their incidental lyric guesses are not the corrected transcript. The recipe above prefers broad timbral descriptions when instrument identifications conflict.

- [Separated-backing interpretation](../../evidence/second_pass/doors_backing.json)
- [Sampled-frame OCR results (automated and noisy)](../../evidence/ocr_results/doors.json)
- [Sampled source-frame contact sheet](../../evidence/frames/DcbYsWLhhdZ.jpg)
- [Targeted vocal interpretation](../../evidence/second_pass/doors_vocals.json)
- [Pitch tracking diagnostic](../../evidence/pitch/doors.json): 22.3% of frames passed the strict voicing filter; too sparse to establish a complete melody.
- [Independent small-model Vosk ASR output (raw; noisy)](../../evidence/asr_vosk/doors.json)
- [Higher-capacity Vosk ASR output (raw; noisy)](../../evidence/asr_vosk_large/doors.json)
- [Original-mix and harmonic pitch tracking diagnostic](../../evidence/pitch/doors_mix_check.json)
- [0.0–24.0s model interpretation](../../evidence/audio_descriptions/doors_00.json)
- [24.0–48.0s model interpretation](../../evidence/audio_descriptions/doors_24.json)
- [48.0–64.7s model interpretation](../../evidence/audio_descriptions/doors_48.json)
