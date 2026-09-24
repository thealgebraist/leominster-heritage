# Flaunching

Source: [flaunching.mp4](../../source_videos/flaunching.mp4) · **15.81 seconds** · [extracted audio](../../evidence/audio/Dc1uBZahhts.wav)

## Listening/navigation aids

- [Waveform and onset-strength overview (navigation aid, not a score)](../../evidence/listen_cues/Dc1uBZahhts/waveform_onsets.png)
- [8-second source-audio excerpts with relative time ranges](../../evidence/listen_cues/Dc1uBZahhts/)

The excerpts are PCM slices from the existing mono analysis WAV. The plot shows amplitude and spectral onset strength; it does not establish notes, instrumentation, meter, or a transcription. Use the original stereo/video for final listening checks.

## Transcript and timing

| Approx. source time | Best-supported words / event |
|---|---|
| 0.0–1.5 | Flaunching, flaunching! |
| 1.7–3.0 | What's around your pot? |
| 3.2–3.8 | A flaunching! |
| 3.8–5.3 | Soaping nicely, keeping it dry. |
| 5.3–7.7 | Flaunching 'round your pot, up in the sky. |
| 9.6–10.8 | A flaunching! |
| 10.8–15.8 | No further intelligible words recovered; musical/video tail. |

Punctuation is editorial. Caption timing and sung-word timing can differ. Bracketed uncertainty notes above are not sung text.

## Pronunciation and vocal phrasing

| Word / phrase | Broad sound / stress guide | Delivery and evidence |
|---|---|---|
| Flaunching | FLAWN-ching | Two syllables; strong first syllable. FLAWN versus a rounder FLON vowel remains unverified. |
| What's around your pot? | wots uh-ROUND yuh POT | Light connecting words; punch POT. |
| A flaunching | uh FLAWN-ching | The little opening uh is a pickup, not the word air. |
| Soaping nicely, keeping it dry | SOH-ping NYSS-lee, KEE-ping it DRY | Both main ASR passes hear “soaping”. It may be intentional wordplay or a lyric different from the expected building term; do not silently replace it with “sloping”. |
| Flaunching round your pot, up in the sky | FLAWN-ching round yuh POT, up in thuh SKY | Short syllables leading to a held or accented SKY. |

Broad respellings are performance targets; they do not establish every vowel of the recorded accent. Capital letters indicate stress, not a request to shout.

## Music, tone, rhythm, and effects

**Voice and delivery — model interpretation:** Male, energetic and slightly nasal according to the audio model; delivery lies between speaking, chanting, and singing. English-language diction is prominent. A specific regional accent and the number of layered takes are not established.

**Melody and phrase shape:** The source text forms two short title calls, a question, an answer, a quick explanatory phrase and a final answer. The audio model describes narrow speech-like pitch movement rather than an elaborate tune. Suggested contour: keep the two title calls almost identical, let the question lift, and make the answer settle; give dry/sky longer phrase-ending vowels. Those directional choices are a recipe, not measured note intervals.

**Rhythm:** A fast regular pulse near 135 BPM is supported by two signal-analysis methods; 67–68 BPM is the corresponding half-time interpretation. Short syllables and repeated words carry the rhythmic interest. Use straight 4/4 as a reconstruction setting; the original meter and precise swing ratio are not verified. Autocorrelation candidates: 135.7 BPM (peak score 0.60), 67.7 BPM (peak score 0.49), 90.2 BPM (peak score 0.47). These are relative peak scores, not probabilities; both tempo estimates use the same audio and cannot confirm one another independently.

**Tonality and harmony:** Bright and playful in the model interpretation, with a compact repeating backing. The mixture does not support an unambiguous major/minor assignment. For generation, begin with a small cheerful tonal loop and let the voice dominate; avoid prescribing an unsupported chord progression. Mixed-audio pitch-class profile candidates: C minor (0.56), C major (0.47), G major (0.43). These numbers are correlation scores, not probabilities. They are retained for experimentation, not stated as verified keys. An exact chord sequence and note-by-note melody have not been established.

**Section-level chroma comparison:** The two 8-second windows disagree across the original mix and separated backing; no stable center is supported. The table gives only each signal's top profile candidate; the full ranked candidates, method and caveats are in [section_tonality.json](../../evidence/section_tonality.json) and [section_tonality.py](../../evidence/section_tonality.py). Scores are correlations, not probabilities.

| Time window | Original mix harmonic | Estimated backing harmonic |
|---|---|---|
| 0–8s | C minor (0.61) | G major (0.42) |
| 8–16s | G major (0.45) | C minor (0.38) |



**Instrumentation and timbre — model interpretation:** The model identifies a synthetic bass foundation, bright keyboard/synth-like sounds and punchy percussion. “Electronic novelty jingle” is better supported than a specific band lineup. An actual guitar, acoustic drum kit or named synthesizer is unverified.

**Production, sound effects, and edits:** The model reports cartoon-like boing/bleep sounds in the final seconds and possible subtle vocal processing. These effect identities are tentative. A brief stutter before the last title call is compatible with repeated ASR readings of an extra pickup. Visual lightning does not establish an audible thunder effect.

**Arrangement recipe:** A very short hook–question–answer jingle. Begin with two accented repetitions, put the question on a compact speech-like phrase, hit the answer, accelerate the explanatory line, and leave a short gap before the final answer. Keep the hook more memorable than the backing.

## Source uncertainties and reconstruction choices

- Whisper full, short-chunk and targeted passes agree on “soaping nicely”; the separated-vocal model also returned “soaping”. The sampled frames do not provide a readable caption for this word. Since “sloping” is only a contextual architectural guess, the source transcript and Suno lyric use the better audio-supported “soaping”, with the potential pun/error noted.
- The article before the last flaunching is less clear than the captioned earlier “A flaunching”.

The musical recipe adds explicit directions where the source analysis is incomplete. “Suggested” features are prompt-design choices, not recovered measurements. The copy-ready lyric file expands some repeated motifs to a practical arrangement and omits unresolved nonverbal passages; use the timed transcript as the evidence record.

## Paste into Suno: Styles

```text
Very short playful electronic novelty jingle, about 135 BPM, straight driving pulse. Upfront energetic male English vocal, slightly nasal, precisely articulated rhythmic speech-singing. Two punchy Flaunching calls, a compact question and answer, then a quick rhyming line landing on dry and sky. Narrow repeating vocal motif, short bright synth accents, simple synthetic bass and crisp programmed percussion. Brief gap before the last title call. Suggested finish: one small cartoon bleep or boing and a clean stop. Aim for roughly 16 seconds, with very little intro.
```

## Paste into Suno: Lyrics

```text
[Short rhythmic hook]
Flaunching, flaunching!
What's around your pot?
A flaunching!
[Quick rhythmic line]
Soaping nicely, keeping it dry
Flaunching round your pot, up in the sky
[Brief instrumental gap]
A flaunching!
[Short ending]
```

## Optional phonetic lyric variant

`lyrics_phonetic.txt` replaces specialist words with broad sound-based spellings. Use it only if ordinary spelling is mispronounced. These respellings are suggested generator inputs, not a certified transcription of the recorded phonemes.

## First comparison after generating

First compare the FLAWN-ching vowel, the little “a” pickup, the dry/sky phrase endings, and the spacing before the last hook. The audio-supported lyric is “soaping”; listen for whether it is an intentional pun or a different word.

## Audio-model evidence

Raw excerpt interpretations are preserved below as evidence links. They are not independent listening verification, and their incidental lyric guesses are not the corrected transcript. The recipe above prefers broad timbral descriptions when instrument identifications conflict.

- [Separated-backing interpretation](../../evidence/second_pass/flaunching_backing.json)
- [Sampled-frame OCR results (automated and noisy)](../../evidence/ocr_results/Dc1uBZahhts.json)
- [Sampled source-frame contact sheet](../../evidence/frames/Dc1uBZahhts.jpg)
- [Targeted vocal interpretation](../../evidence/second_pass/Dc1uBZahhts_vocals.json)
- [Pitch tracking diagnostic](../../evidence/pitch/Dc1uBZahhts.json): 3.8% of frames passed the strict voicing filter; too sparse to establish a complete melody.
- [Independent small-model Vosk ASR output (raw; noisy)](../../evidence/asr_vosk/Dc1uBZahhts.json)
- [Higher-capacity Vosk ASR output (raw; noisy)](../../evidence/asr_vosk_large/Dc1uBZahhts.json)
- [Original-mix and harmonic pitch tracking diagnostic](../../evidence/pitch/Dc1uBZahhts_mix_check.json)
- [0.0–15.8s model interpretation](../../evidence/audio_descriptions/Dc1uBZahhts_00.json)
