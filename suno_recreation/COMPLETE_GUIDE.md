# Architectural music — complete recreation guide

Read [README.md](README.md) for evidence limits and Suno instructions.


---

# Flaunching

Source: [Dc1uBZahhts.mp4](../account_mp4/Dc1uBZahhts.mp4) · **15.81 seconds** · [extracted audio](evidence/audio/Dc1uBZahhts.wav)

## Listening/navigation aids

- [Waveform and onset-strength overview (navigation aid, not a score)](evidence/listen_cues/Dc1uBZahhts/waveform_onsets.png)
- [8-second source-audio excerpts with relative time ranges](evidence/listen_cues/Dc1uBZahhts/)

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

**Section-level chroma comparison:** The two 8-second windows disagree across the original mix and separated backing; no stable center is supported. The table gives only each signal's top profile candidate; the full ranked candidates, method and caveats are in [section_tonality.json](evidence/section_tonality.json) and [section_tonality.py](evidence/section_tonality.py). Scores are correlations, not probabilities.

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

- [Separated-backing interpretation](evidence/second_pass/Dc1uBZahhts_backing.json)
- [Sampled-frame OCR results (automated and noisy)](evidence/ocr_results/Dc1uBZahhts.json)
- [Sampled source-frame contact sheet](evidence/frames/Dc1uBZahhts.jpg)
- [Targeted vocal interpretation](evidence/second_pass/Dc1uBZahhts_vocals.json)
- [Pitch tracking diagnostic](evidence/pitch/Dc1uBZahhts.json): 3.8% of frames passed the strict voicing filter; too sparse to establish a complete melody.
- [Independent small-model Vosk ASR output (raw; noisy)](evidence/asr_vosk/Dc1uBZahhts.json)
- [Higher-capacity Vosk ASR output (raw; noisy)](evidence/asr_vosk_large/Dc1uBZahhts.json)
- [Original-mix and harmonic pitch tracking diagnostic](evidence/pitch/Dc1uBZahhts_mix_check.json)
- [0.0–15.8s model interpretation](evidence/audio_descriptions/Dc1uBZahhts_00.json)


---

# Guttae / Good Day

Source: [Dc8axxYIC3k.mp4](../account_mp4/Dc8axxYIC3k.mp4) · **22.29 seconds** · [extracted audio](evidence/audio/Dc8axxYIC3k.wav)

## Listening/navigation aids

- [Waveform and onset-strength overview (navigation aid, not a score)](evidence/listen_cues/Dc8axxYIC3k/waveform_onsets.png)
- [8-second source-audio excerpts with relative time ranges](evidence/listen_cues/Dc8axxYIC3k/)

The excerpts are PCM slices from the existing mono analysis WAV. The plot shows amplitude and spectral onset strength; it does not establish notes, instrumentation, meter, or a transcription. Use the original stereo/video for final listening checks.

## Transcript and timing

| Approx. source time | Best-supported words / event |
|---|---|
| 0.0–5.9 | Guttae! … Guttae! … Guttae! |
| 5.9–10.5 | Rapid chopped two-syllable hook, heard as “Guttae/Gootay” or repeated “good day” by different Whisper passes; exact words and count unresolved. |
| 10.5–11.3 | Good day! |
| 11.4–12.1 | Guttae! |
| 12.2–13.3 | Too many guttae! |
| 14.0–18.3 | Guttae! Guttae! Guttae! Guttae! [approximately four further calls] |
| 18.3–22.3 | Ending / title-card tail; no further reliable lyric recovered. |

Punctuation is editorial. Caption timing and sung-word timing can differ. Bracketed uncertainty notes above are not sung text.

## Pronunciation and vocal phrasing

| Word / phrase | Broad sound / stress guide | Delivery and evidence |
|---|---|---|
| Guttae | GUH-tay / guh-TAY | Whisper and the separated-vocal model (“gotay”) support a final AY sound, not eye. Exact first vowel and stress vary/are unresolved; preserve the good-day pun. |
| Good day | guh-DAY | Two short syllables, matching the rhythm and sound of guttae. |
| Too many guttae | too MEN-ee GUH-tay | Speed through too many, land on the two-syllable architectural word. |

Broad respellings are performance targets; they do not establish every vowel of the recorded accent. Capital letters indicate stress, not a request to shout.

## Music, tone, rhythm, and effects

**Voice and delivery — model interpretation:** High-energy male calls and chants, with forceful attacks and apparent grunted or percussive vocal sounds. The model interprets much of it as speech/shouting rather than sustained singing. The captioned guttae/good day pun is more reliable than the model’s literal “go” transcription.

**Melody and phrase shape:** A tiny two-syllable motif is repeated and compressed into a rapid middle cluster. The important melodic identity is the recurring short inflection and vowel, not a long tune. Suggested rendition: a short lower pickup into a stronger AY syllable, then clipped repeats of that same cell. The exact source pitches and stress distribution are not established.

**Rhythm:** A fast regular pulse near 135 BPM is supported by two signal-analysis methods; 67–68 BPM is the corresponding half-time interpretation. Short syllables and repeated words carry the rhythmic interest. Use straight 4/4 as a reconstruction setting; the original meter and precise swing ratio are not verified. Autocorrelation candidates: 67.7 BPM (peak score 0.56), 135.7 BPM (peak score 0.54), 90.3 BPM (peak score 0.54). These are relative peak scores, not probabilities; both tempo estimates use the same audio and cannot confirm one another independently.

**Tonality and harmony:** Pitch content is too ambiguous for a reliable key. Treat this as a predominantly rhythmic vocal hook over a minimal tonal backing. A strong one- or two-chord loop is a proposed starting point, not a recovered progression. Mixed-audio pitch-class profile candidates: C minor (0.39), G major (0.37), A♭ major (0.37). These numbers are correlation scores, not probabilities. They are retained for experimentation, not stated as verified keys. An exact chord sequence and note-by-note melody have not been established.

**Section-level chroma comparison:** G major ranks first in both signals through 0–16 s; the short ending window disagrees (C major in the mix, F major in the backing). Treat G as an early-section experiment, not a whole-track key. The table gives only each signal's top profile candidate; the full ranked candidates, method and caveats are in [section_tonality.json](evidence/section_tonality.json) and [section_tonality.py](evidence/section_tonality.py). Scores are correlations, not probabilities.

| Time window | Original mix harmonic | Estimated backing harmonic |
|---|---|---|
| 0–8s | G major (0.40) | G major (0.40) |
| 8–16s | G major (0.46) | G major (0.59) |
| 16–22s | C major (0.38) | F major (0.58) |

**Instrumentation and timbre — model interpretation:** Electronic beat and low synthetic pulse are consistently reported. The vocal itself supplies much of the perceived rhythm; the model also hears boom-like vocalizations/grunts. No specific acoustic instruments are established.

**Production, sound effects, and edits:** Stuttered/chopped repetitions and abrupt voice-like exclamations are central to the interpretation. The words versus grunts in the densest middle section remain uncertain. Keep effects short and rhythmically attached to the hook rather than adding a large cinematic transition.

**Arrangement recipe:** A two-syllable vocal motif treated as the main rhythmic instrument. Start with widely separated calls, compress into a short stuttered cluster, interrupt with the near-homophone “good day”, then use “too many” as a spoken pickup and repeat the hook. Preserve the gaps; do not turn the tiny text into a long verse.

## Source uncertainties and reconstruction choices

- The chopped middle has clear repeated two-syllable calls but uncertain wording: full/short Whisper variants render them as Gootay/Guttae, while the targeted pass hears repeated “good day”. The good-day/guttae homophone makes this difficult to settle from ASR; exact count and whether the phrase alternates remain unresolved. The Suno version chooses repeated Guttae for a compact motif, not a claimed exact transcript.
- “Good Day” is directly visible at about 10.5 seconds. The sound is interpreted as close to “guttae”, so spelling alone cannot identify every occurrence.

The musical recipe adds explicit directions where the source analysis is incomplete. “Suggested” features are prompt-design choices, not recovered measurements. The copy-ready lyric file expands some repeated motifs to a practical arrangement and omits unresolved nonverbal passages; use the timed transcript as the evidence record.

## Paste into Suno: Styles

```text
Playful male vocal chant over a minimal punchy electronic beat, about 135 BPM. A tiny two-syllable guh-tay hook is the main musical motif: spaced calls at first, a tight stuttering cluster in the middle, then the near-homophone good day as a comic spoken interruption. Clear consonants, energetic rounded vowels, short pitch inflections, little sustained melody. Synthetic low pulse and crisp percussion; brief percussive vocal grunts can support the rhythm. Return to spaced guttae calls after too many guttae. Around 22 seconds; compact and repetitive.
```

## Paste into Suno: Lyrics

```text
[Spaced rhythmic calls]
Guttae!
Guttae!
Guttae!
[Quick chopped chant]
Guttae, guttae, guttae, guttae
Guttae, guttae
[Spoken interjection]
Good day!
[Chant]
Guttae!
Too many guttae!
Guttae!
Guttae!
Guttae!
Guttae!
[Short instrumental ending]
```

## Optional phonetic lyric variant

`lyrics_phonetic.txt` replaces specialist words with broad sound-based spellings. Use it only if ordinary spelling is mispronounced. These respellings are suggested generator inputs, not a certified transcription of the recorded phonemes.

## First comparison after generating

Compare the two-syllable vowel pattern and the good-day pun before the backing. Match spaced versus chopped sections; the expanded repeat counts in the Suno version are provisional.

## Audio-model evidence

Raw excerpt interpretations are preserved below as evidence links. They are not independent listening verification, and their incidental lyric guesses are not the corrected transcript. The recipe above prefers broad timbral descriptions when instrument identifications conflict.

- [Separated-backing interpretation](evidence/second_pass/Dc8axxYIC3k_backing.json)
- [Sampled-frame OCR results (automated and noisy)](evidence/ocr_results/Dc8axxYIC3k.json)
- [Sampled source-frame contact sheet](evidence/frames/Dc8axxYIC3k.jpg)
- [Targeted vocal interpretation](evidence/second_pass/Dc8axxYIC3k_vocals.json)
- [Pitch tracking diagnostic](evidence/pitch/Dc8axxYIC3k.json): 0.8% of frames passed the strict voicing filter; too sparse to establish a complete melody.
- [Independent small-model Vosk ASR output (raw; noisy)](evidence/asr_vosk/Dc8axxYIC3k.json)
- [Higher-capacity Vosk ASR output (raw; noisy)](evidence/asr_vosk_large/Dc8axxYIC3k.json)
- [Original-mix and harmonic pitch tracking diagnostic](evidence/pitch/Dc8axxYIC3k_mix_check.json)
- [0.0–22.3s model interpretation](evidence/audio_descriptions/Dc8axxYIC3k_00.json)


---

# Corbel / Bargeboard / Architectural Features

Source: [bargeboard.mp4](../account_mp4/bargeboard.mp4) · **38.01 seconds** · [extracted audio](evidence/audio/DcRZB_PBFkr.wav)

## Listening/navigation aids

- [Waveform and onset-strength overview (navigation aid, not a score)](evidence/listen_cues/DcRZB_PBFkr/waveform_onsets.png)
- [8-second source-audio excerpts with relative time ranges](evidence/listen_cues/DcRZB_PBFkr/)

The excerpts are PCM slices from the existing mono analysis WAV. The plot shows amplitude and spectral onset strength; it does not establish notes, instrumentation, meter, or a transcription. Use the original stereo/video for final listening checks.

## Transcript and timing

| Approx. source time | Best-supported words / event |
|---|---|
| 0.0–3.5 | Corbel, corbel, corbel, corbel / Bargeboard, bargeboard. |
| 3.6–7.0 | Corbel, corbel, corbel, corbel / Bargeboard, bargeboard. |
| 7.1–10.7 | Mullion repeated [approximately four calls]. |
| 10.7–14.5 | Brace repeated [rapid calls; exact count unresolved]. |
| 14.6–16.3 | Quatrefoil, quatrefoil. |
| 16.4–18.1 | Quoin repeated [exact count unresolved]. |
| 18.2–19.7 | String course, string course. |
| 19.8–26.0 | Buttress repeated [caption remains visible through about 26s; exact spoken-call count uncertain]. |
| 26.0–28.5 | Corbel, corbel, corbel, corbel / Bargeboard, bargeboard. |
| 28.5–30.1 | Mullion, mullion. |
| 30.1–32.0 | Brace, brace. |
| 32.0–33.0 | Finial! |
| 33.0–38.0 | Musical/end-card tail; no further reliable words recovered. |

Punctuation is editorial. Caption timing and sung-word timing can differ. Bracketed uncertainty notes above are not sung text.

## Pronunciation and vocal phrasing

| Word / phrase | Broad sound / stress guide | Delivery and evidence |
|---|---|---|
| Corbel | KOR-buhl | Two compact syllables; four evenly spaced calls. |
| Bargeboard | BAHJ-bawd | Two strong word components; broad British non-rhotic rendition is a suggested performance choice. |
| Mullion | MUL-yun | Compress to two sung syllables, rather than mull-ee-on. |
| Brace | BRAYSS | One syllable, crisp BR onset; useful for repeated percussive hits. |
| Quatrefoil | KAT-er-foyl | Recognizer approximations “cutterfoil” support three syllables; first vowel is not narrowly verified. |
| Quoin | KOYN | One syllable, like coin, not kwoyn. |
| String course | STRING kawss | Two beats/syllabic attacks; clipped STRING and a longer COURSE. |
| Buttress | BUT-riss | Two syllables; emphatic first, weaker second. |
| Finial | FIN-ee-ul | Three syllables ending the sequence as a punchline; caption corrects ASR “video”. |

Broad respellings are performance targets; they do not establish every vowel of the recorded accent. Capital letters indicate stress, not a request to shout.

## Music, tone, rhythm, and effects

**Voice and delivery — model interpretation:** Clipped male chants/calls with apparent changes of pitch or vocal character. The model alternately describes unison/layered voices and contrasting male calls; the recording does not establish how many performers produced them.

**Melody and phrase shape:** The short nouns form distinct rhythmic cells: quick two-syllable corbel repeats, longer bargeboard replies, then a succession of new word shapes. The model hears small rises and falls rather than extended lyrical melody. Suggested rendition: retain a narrow repeated-note chant, contrast the slower replies, and put a slightly broader accent on finial. No exact intervals are recovered.

**Rhythm:** A fast regular pulse near 135 BPM is supported by two signal-analysis methods; 67–68 BPM is the corresponding half-time interpretation. Short syllables and repeated words carry the rhythmic interest. Use straight 4/4 as a reconstruction setting; the original meter and precise swing ratio are not verified. Autocorrelation candidates: 134.7 BPM (peak score 0.66), 67.3 BPM (peak score 0.66), 90.0 BPM (peak score 0.38). These are relative peak scores, not probabilities; both tempo estimates use the same audio and cannot confirm one another independently.

**Tonality and harmony:** One excerpt model suggests a major-like sound, but its instrumental account conflicts with a later excerpt and the key profiles are close. Use a light repetitive tonal centre as a reconstruction choice, without treating G major or C minor as established. Mixed-audio pitch-class profile candidates: G major (0.58), C minor (0.56), C major (0.54). These numbers are correlation scores, not probabilities. They are retained for experimentation, not stated as verified keys. An exact chord sequence and note-by-note melody have not been established.

**Section-level chroma comparison:** The leading profiles shift from G major to C major in the mix, and the final short window disagrees sharply between mix and backing. No single track-wide key is supported. The table gives only each signal's top profile candidate; the full ranked candidates, method and caveats are in [section_tonality.json](evidence/section_tonality.json) and [section_tonality.py](evidence/section_tonality.py). Scores are correlations, not probabilities.

| Time window | Original mix harmonic | Estimated backing harmonic |
|---|---|---|
| 0–8s | G major (0.69) | G major (0.62) |
| 8–16s | C major (0.58) | C minor (0.52) |
| 16–24s | C major (0.61) | C minor (0.60) |
| 24–32s | C major (0.59) | G major (0.55) |
| 32–38s | C♯ minor (0.62) | F major (0.73) |

**Instrumentation and timbre — model interpretation:** The final portion is described as an electronic beat and synthesized backing. The first portion is inconsistently described as nearly vocal-only, so backing prominence may be low or obscured by the voice. Use sparse synthetic low notes and short percussive accents as a conservative recipe; specific instrumental sources are unresolved.

**Production, sound effects, and edits:** Abrupt emphasis, repeated vocal syllables and a short isolated final exclamation are supported by the transcript. Compression, doubling, and small room/reverb effects are model suggestions, not measured production settings. No named TV programme or original music source has been identified.

**Arrangement recipe:** A catalogue chant built out of short repeated cells. Contrast fast COR-bel pulses with slower BARGe-board responses, move through the other nouns as new rhythmic motifs, then reprise the opening and end with an isolated three-syllable FIN-ee-ul. Use stop/start spaces and short punctuating fills rather than long melodic lines.

## Source uncertainties and reconstruction choices

- The captions establish the sequence of specialist nouns that the full recognizer omitted. Repetition counts in the middle remain approximate. The caption “Buttress” stays visible from about 20 to 26 seconds; the number of spoken repetitions cannot be read from one sustained caption.
- The four initial corbels are supported by the short-chunk pass; the full pass incorrectly inserted a fifth.

The musical recipe adds explicit directions where the source analysis is incomplete. “Suggested” features are prompt-design choices, not recovered measurements. The copy-ready lyric file expands some repeated motifs to a practical arrangement and omits unresolved nonverbal passages; use the timed transcript as the evidence record.

## Paste into Suno: Styles

```text
Fast comic architectural catalogue chant, about 135 BPM. Upfront clearly articulated male English calls, clipped and rhythmic with small pitch inflections. Four quick corbel calls answered by two broader bargeboard calls. Give mullion, brace, quatrefoil, quoin, string course and buttress their own repeated rhythmic cells, then reprise the opening. Sparse punchy electronic percussion, simple synth bass, short bright accents; the words dominate the mix. Slight vocal layering is an optional texture. Finish with an isolated emphatic finial and a short tail, roughly 38 seconds overall.
```

## Paste into Suno: Lyrics

```text
[Rhythmic chant]
Corbel, corbel, corbel, corbel
Bargeboard, bargeboard
Corbel, corbel, corbel, corbel
Bargeboard, bargeboard
[New repeated motif]
Mullion, mullion, mullion, mullion
Brace, brace, brace, brace
Brace, brace, brace, brace
Quatrefoil, quatrefoil
Quoin, quoin, quoin, quoin
String course, string course
[Longer accented calls]
Buttress!
Buttress!
Buttress!
[Reprise]
Corbel, corbel, corbel, corbel
Bargeboard, bargeboard
Mullion, mullion
Brace, brace
[Final exclamation]
Finial!
[Short ending]
```

## Optional phonetic lyric variant

`lyrics_phonetic.txt` replaces specialist words with broad sound-based spellings. Use it only if ordinary spelling is mispronounced. These respellings are suggested generator inputs, not a certified transcription of the recorded phonemes.

## First comparison after generating

Compare the length ratio of corbel to bargeboard and the change of motif for every new term. Confirm the uncertain brace/quoin repeat counts; avoid accepting the ASR substitutions price or video.

## Audio-model evidence

Raw excerpt interpretations are preserved below as evidence links. They are not independent listening verification, and their incidental lyric guesses are not the corrected transcript. The recipe above prefers broad timbral descriptions when instrument identifications conflict.

- [Separated-backing interpretation](evidence/second_pass/bargeboard_backing.json)
- [Sampled-frame OCR results (automated and noisy)](evidence/ocr_results/DcRZB_PBFkr.json)
- [Sampled source-frame contact sheet](evidence/frames/DcRZB_PBFkr.jpg)
- [Pitch tracking diagnostic](evidence/pitch/DcRZB_PBFkr.json): 0.3% of frames passed the strict voicing filter; too sparse to establish a complete melody.
- [Independent small-model Vosk ASR output (raw; noisy)](evidence/asr_vosk/DcRZB_PBFkr.json)
- [Higher-capacity Vosk ASR output (raw; noisy)](evidence/asr_vosk_large/DcRZB_PBFkr.json)
- [Original-mix and harmonic pitch tracking diagnostic](evidence/pitch/DcRZB_PBFkr_mix_check.json)
- [0.0–24.0s model interpretation](evidence/audio_descriptions/DcRZB_PBFkr_00.json)
- [24.0–38.0s model interpretation](evidence/audio_descriptions/DcRZB_PBFkr_24.json)


---

# Columns / Classical Orders

Source: [DcYTYvMBSMn.mp4](../account_mp4/DcYTYvMBSMn.mp4) · **53.62 seconds** · [extracted audio](evidence/audio/DcYTYvMBSMn.wav)

## Listening/navigation aids

- [Waveform and onset-strength overview (navigation aid, not a score)](evidence/listen_cues/DcYTYvMBSMn/waveform_onsets.png)
- [8-second source-audio excerpts with relative time ranges](evidence/listen_cues/DcYTYvMBSMn/)

The excerpts are PCM slices from the existing mono analysis WAV. The plot shows amplitude and spectral onset strength; it does not establish notes, instrumentation, meter, or a transcription. Use the original stereo/video for final listening checks.

## Transcript and timing

| Approx. source time | Best-supported words / event |
|---|---|
| 0.0–7.0 | Column, column, Doric column / Tuscan, Tuscan. [twice] |
| 7.0–12.8 | Ah—Corinthian / Ionic, Ionic. |
| 12.8–19.7 | Pilaster, pilaster, Doric pilaster / Capital, capital. [twice] |
| 19.7–25.3 | Ah—Palladio / Ionic, Ionic. |
| 25.3–32.8 | Fluted, fluted, Doric column / Tuscan, Tuscan. [twice] |
| 32.8–37.8 | Ah—Corinthian / Ionic, Ionic. |
| 37.8–44.5 | Capital, capital, Corinthian / Shaft, shaft. [twice] |
| 44.5–49.2 | Ah—Composite / Palladio! |
| 49.2–53.6 | Musical/end-card tail. |

Punctuation is editorial. Caption timing and sung-word timing can differ. Bracketed uncertainty notes above are not sung text.

## Pronunciation and vocal phrasing

| Word / phrase | Broad sound / stress guide | Delivery and evidence |
|---|---|---|
| Column | KOL-um | Two syllables; the written n is silent. |
| Doric column | DOR-ik KOL-um | Four syllables in a compact rhythmic unit. |
| Tuscan | TUS-kun | Two clipped syllables. |
| Corinthian | kuh-RIN-thee-un | Strong RIN, then two light syllables; can compress the ending toward th-yun at speed. |
| Ionic | eye-ON-ik | Three syllables, central stress. |
| Pilaster | pih-LAS-tuh | Stress LAS; do not substitute “I lost a”, an ASR error. |
| Capital | KAP-ih-tuhl | Three quick syllables, strong KAP. |
| Palladio | puh-LAH-dee-oh | Four syllables, strong LAH and a rounded held final OH. |
| Fluted | FLOO-tid | Two syllables; long OO. |
| Shaft | SHAHFT | One long open vowel for a suggested British rendition; the source vowel is not narrowly verified. |
| Composite | kum-POZ-it | Three syllables, central stress, not COM-poh-site. |
| Ah | AAAH | Open sustained vowel before the longer architectural name. |

Broad respellings are performance targets; they do not establish every vowel of the recorded accent. Capital letters indicate stress, not a request to shout.

## Music, tone, rhythm, and effects

**Voice and delivery — model interpretation:** Theatrical male rhythmic speech-singing, with tightly articulated list words and broader open-vowel exclamations. The model agrees on energetic chant-like delivery but disagrees on whether the percussion is instrumental or vocal.

**Melody and phrase shape:** Each block contrasts rapid catalogue syllables with a sustained Ah and a longer technical name. This contrast is directly supported by the lyric timing and vocalized Ah detections. The model hears speech-like pitch changes and changing phrase contours. Suggested rendition: use one short recurring list motif, open the register and vowel for Ah, then resolve the longer name back into the next list. Exact pitch heights and intervals remain unverified.

**Rhythm:** A fast regular pulse near 135 BPM is supported by two signal-analysis methods; 67–68 BPM is the corresponding half-time interpretation. Short syllables and repeated words carry the rhythmic interest. Use straight 4/4 as a reconstruction setting; the original meter and precise swing ratio are not verified. Autocorrelation candidates: 67.4 BPM (peak score 0.64), 89.9 BPM (peak score 0.57), 134.7 BPM (peak score 0.56). These are relative peak scores, not probabilities; both tempo estimates use the same audio and cannot confirm one another independently.

**Tonality and harmony:** The strongest mixture profile is B-flat major, ahead of E-flat major, but this is still a heuristic result from a vocal-heavy clip. A bright major-like setting is a reasonable experiment; B-flat major can be tried as a test key, not stated as the original. No harmonic progression is recovered. Mixed-audio pitch-class profile candidates: B♭ major (0.71), E♭ major (0.54), E♭ minor (0.42). These numbers are correlation scores, not probabilities. They are retained for experimentation, not stated as verified keys. An exact chord sequence and note-by-note melody have not been established.

**Section-level chroma comparison:** E-flat/B-flat profile labels recur across most sections in both signals, while major/minor mode and the strongest member of that family vary. An E-flat/B-flat tonal palette is a more cautious prompt test than a single asserted key. The table gives only each signal's top profile candidate; the full ranked candidates, method and caveats are in [section_tonality.json](evidence/section_tonality.json) and [section_tonality.py](evidence/section_tonality.py). Scores are correlations, not probabilities.

| Time window | Original mix harmonic | Estimated backing harmonic |
|---|---|---|
| 0–8s | D♯ minor (0.57) | D♯ major (0.71) |
| 8–16s | D♯ major (0.72) | D♯ major (0.71) |
| 16–24s | A♯ major (0.71) | D♯ major (0.64) |
| 24–32s | D♯ major (0.66) | D♯ major (0.67) |
| 32–40s | A♯ major (0.71) | A♯ major (0.63) |
| 40–48s | D♯ major (0.69) | D♯ major (0.68) |
| 48–54s | D♯ major (0.73) | A♯ major (0.78) |

**Instrumentation and timbre — model interpretation:** At least a rhythmic low/percussive backing is indicated. One model excerpt hears drums, bass and synths; another hears beatboxing/sample-like percussion. Prefer a hybrid description—tight synthetic/vocal-like percussion and a low pulse—over claiming a live bass guitar or drum kit.

**Production, sound effects, and edits:** Possible mild reverb or short delay on the voice. The final Palladio exclamation is followed by a sparse ending and a low percussive cue according to the short tail analysis. Specific delay times and effect devices are not known.

**Arrangement recipe:** Four catalogue blocks using the same compact rhythmic template. Two brisk list phrases are followed by a broader held “Ah” and a more melodic long name. Reuse the rhythmic cell for column/pilaster/fluted/capital, with short Tuscan or shaft answers. Keep the long vowels at the end of each block distinct from the clipped list delivery.

## Source uncertainties and reconstruction choices

- Specialist spellings are supported by the captions; ASR variants “biloster”, “dory”, and “I love you” have been corrected to the captioned terms.
- Timings are approximate section boundaries; rapid sung syllables need not align exactly with the animated captions.

The musical recipe adds explicit directions where the source analysis is incomplete. “Suggested” features are prompt-design choices, not recovered measurements. The copy-ready lyric file expands some repeated motifs to a practical arrangement and omits unresolved nonverbal passages; use the timed transcript as the evidence record.

## Paste into Suno: Styles

```text
Quirky theatrical male catalogue song, about 135 BPM, brisk straight rhythm. Precisely articulated short speech-sung lists contrast with broad sustained open-vowel Ah exclamations and elongated architectural names. Reuse the same compact motif for column, pilaster, fluted and capital sections. Light punchy electronic beat, low bass pulse, dry vocal-like percussion and sparse bright keyboard accents; keep the lead upfront. Try an E-flat/B-flat-centered, major-leaning palette but leave the exact mode and chord sequence flexible; this is a section-chroma experiment, not a confirmed key. Emphasise kuh-RIN-thee-un, eye-ON-ik and puh-LAH-dee-oh clearly. End with composite then Palladio and a short low percussive stop, roughly 54 seconds.
```

## Paste into Suno: Lyrics

```text
[Rhythmic verse]
Column, column, Doric column
Tuscan, Tuscan
Column, column, Doric column
Tuscan, Tuscan
[Held melodic exclamation]
Ah, Corinthian
Ionic, Ionic
[Rhythmic verse]
Pilaster, pilaster, Doric pilaster
Capital, capital
Pilaster, pilaster, Doric pilaster
Capital, capital
[Held melodic exclamation]
Ah, Palladio
Ionic, Ionic
[Rhythmic verse]
Fluted, fluted, Doric column
Tuscan, Tuscan
Fluted, fluted, Doric column
Tuscan, Tuscan
[Held melodic exclamation]
Ah, Corinthian
Ionic, Ionic
[Rhythmic verse]
Capital, capital, Corinthian
Shaft, shaft
Capital, capital, Corinthian
Shaft, shaft
[Held final exclamation]
Ah, composite
Palladio!
[Short ending]
```

## Optional phonetic lyric variant

`lyrics_phonetic.txt` replaces specialist words with broad sound-based spellings. Use it only if ordinary spelling is mispronounced. These respellings are suggested generator inputs, not a certified transcription of the recorded phonemes.

## First comparison after generating

Compare the clipped list sections with the sustained Ah passages. Preserve the syllable counts in pilaster, Corinthian, Ionic, composite and Palladio. Treat the B-flat key suggestion as optional.

## Audio-model evidence

Raw excerpt interpretations are preserved below as evidence links. They are not independent listening verification, and their incidental lyric guesses are not the corrected transcript. The recipe above prefers broad timbral descriptions when instrument identifications conflict.

- [Separated-backing interpretation](evidence/second_pass/DcYTYvMBSMn_backing.json)
- [Sampled-frame OCR results (automated and noisy)](evidence/ocr_results/DcYTYvMBSMn.json)
- [Sampled source-frame contact sheet](evidence/frames/DcYTYvMBSMn.jpg)
- [Pitch tracking diagnostic](evidence/pitch/DcYTYvMBSMn.json): 10.3% of frames passed the strict voicing filter; too sparse to establish a complete melody.
- [Independent small-model Vosk ASR output (raw; noisy)](evidence/asr_vosk/DcYTYvMBSMn.json)
- [Higher-capacity Vosk ASR output (raw; noisy)](evidence/asr_vosk_large/DcYTYvMBSMn.json)
- [Original-mix and harmonic pitch tracking diagnostic](evidence/pitch/DcYTYvMBSMn_mix_check.json)
- [0.0–24.0s model interpretation](evidence/audio_descriptions/DcYTYvMBSMn_00.json)
- [24.0–48.0s model interpretation](evidence/audio_descriptions/DcYTYvMBSMn_24.json)
- [48.0–53.6s model interpretation](evidence/audio_descriptions/DcYTYvMBSMn_48.json)


---

# Doors

Source: [DcbYsWLhhdZ.mp4](../account_mp4/DcbYsWLhhdZ.mp4) · **64.69 seconds** · [extracted audio](evidence/audio/DcbYsWLhhdZ.wav)

## Listening/navigation aids

- [Waveform and onset-strength overview (navigation aid, not a score)](evidence/listen_cues/DcbYsWLhhdZ/waveform_onsets.png)
- [8-second source-audio excerpts with relative time ranges](evidence/listen_cues/DcbYsWLhhdZ/)

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

**Section-level chroma comparison:** Both signals rank F minor first in 0–16 s, C minor in 16–32 s, then F minor through most of 32–64 s. This repeated section pattern supports testing an F-minor / C-minor contrast, but does not prove a chord progression or tonal function. The table gives only each signal's top profile candidate; the full ranked candidates, method and caveats are in [section_tonality.json](evidence/section_tonality.json) and [section_tonality.py](evidence/section_tonality.py). Scores are correlations, not probabilities.

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
Comic electronic door chant, about 135 BPM. Upfront male English voice, crisp spoken-sung one-word door hook with a long rounded vowel, repeated on a compact pitch cell. Change the adjective pickups while keeping the door motif stable. Try an F-minor tonal home, briefly shifting toward C minor in the middle before returning; these are section-profile candidates, not verified chords. Simple synth bass and programmed drum groove, short bright keyboard stabs. Use dry spoken questions and answers, sudden small pauses, and a sharp cat flap interruption. Toward the end add a brief bright game-like arpeggio or chime texture, pause after and one more, then a drawn-out Dumbledore punchline and one final door. Roughly 65 seconds; no extra verses.
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

- [Separated-backing interpretation](evidence/second_pass/DcbYsWLhhdZ_backing.json)
- [Sampled-frame OCR results (automated and noisy)](evidence/ocr_results/DcbYsWLhhdZ.json)
- [Sampled source-frame contact sheet](evidence/frames/DcbYsWLhhdZ.jpg)
- [Targeted vocal interpretation](evidence/second_pass/DcbYsWLhhdZ_vocals.json)
- [Pitch tracking diagnostic](evidence/pitch/DcbYsWLhhdZ.json): 22.3% of frames passed the strict voicing filter; too sparse to establish a complete melody.
- [Independent small-model Vosk ASR output (raw; noisy)](evidence/asr_vosk/DcbYsWLhhdZ.json)
- [Higher-capacity Vosk ASR output (raw; noisy)](evidence/asr_vosk_large/DcbYsWLhhdZ.json)
- [Original-mix and harmonic pitch tracking diagnostic](evidence/pitch/DcbYsWLhhdZ_mix_check.json)
- [0.0–24.0s model interpretation](evidence/audio_descriptions/DcbYsWLhhdZ_00.json)
- [24.0–48.0s model interpretation](evidence/audio_descriptions/DcbYsWLhhdZ_24.json)
- [48.0–64.7s model interpretation](evidence/audio_descriptions/DcbYsWLhhdZ_48.json)


---

# Windows

Source: [DcqWhZtBIEI.mp4](../account_mp4/DcqWhZtBIEI.mp4) · **67.01 seconds** · [extracted audio](evidence/audio/DcqWhZtBIEI.wav)

## Listening/navigation aids

- [Waveform and onset-strength overview (navigation aid, not a score)](evidence/listen_cues/DcqWhZtBIEI/waveform_onsets.png)
- [8-second source-audio excerpts with relative time ranges](evidence/listen_cues/DcqWhZtBIEI/)

The excerpts are PCM slices from the existing mono analysis WAV. The plot shows amplitude and spectral onset strength; it does not establish notes, instrumentation, meter, or a transcription. Use the original stereo/video for final listening checks.

## Transcript and timing

| Approx. source time | Best-supported words / event |
|---|---|
| 0.0–6.9 | Window repeated [four principal calls, with possible extra chopped repetitions]. |
| 7.0–10.9 | Mullion, muntin, meeting rail, transom. |
| 10.9–14.8 | Window, window, what have you got? / Mullion in the middle, glazing in the lot. |
| 14.8–19.4 | Casement! / Is that a casement? / Yes, a casement! |
| 19.4–21.3 | Open it out, shut it again. |
| 21.4–24.9 | Stay, fastener, hinge, pane. |
| 24.9–28.4 | Rail, stile, glazing bar / Rail, stile, glazing bar. |
| 28.4–30.5 | Sash goes up, sash comes down. |
| 30.5–35.7 | Sash cord! / Where's it gone? / In the box. / Obviously. |
| 35.7–38.6 | Window repeated [exact count unresolved]. |
| 38.7–42.2 | Fanlight, sidelight, oriel [possibly followed by “too”; unresolved]. |
| 42.2–48.6 | Bay window, bow window / What does it do? / Lets in light. / Very good. |
| 49.7–55.0 | Casement! / Is that a casement? / Yes, a casement! |
| 56.9–60.4 | Mullion, muntin, transom, pane. |
| 60.4–64.4 | Open the window / Shut it again. |
| 64.4–67.0 | Musical/end-card tail. |

Punctuation is editorial. Caption timing and sung-word timing can differ. Bracketed uncertainty notes above are not sung text.

## Pronunciation and vocal phrasing

| Word / phrase | Broad sound / stress guide | Delivery and evidence |
|---|---|---|
| Window | WIN-doh | Two syllables, strong WIN; same motif whenever it returns. |
| Mullion / muntin | MUL-yun / MUN-tin | Both two syllables; distinguish L-y from NT. |
| Meeting rail / transom | MEE-ting RAYL / TRAN-zum | Strong first word beats; transom is two syllables. |
| What have you got? | wot-uv-yuh GOT | Compress unstressed syllables before GOT. |
| Mullion in the middle, glazing in the lot | MUL-yun in thuh MID-ul, GLAY-zing in thuh LOT | Quick syllabic delivery with MID and LOT accented. |
| Casement | KAYSS-munt | Two syllables; KAYSS remains clear in the question and answer. |
| Stay / fastener / hinge / pane | STAY / FAS-uh-nuh / HINJ / PAYN | Fastener has a silent t; keep the listed objects separate. |
| Rail / stile / glazing bar | RAYL / STYL / GLAY-zing BAH | Stile sounds like style; glazing begins GL, not BL. |
| Sash cord | SASH KAWD | Two strongly accented words, not sash gone or sashcorn. |
| Where's it gone? In the box. Obviously. | WAIRZ it GON? in thuh BOKS. OB-vee-us-lee. | Treat as a brief spoken dialogue with small gaps. |
| Fanlight / sidelight / oriel | FAN-lyt / SYD-lyt / OR-ee-ul | Two, two, then three syllables; the possible following too remains uncertain. |
| Bay window / bow window | BAY WIN-doh / BOH WIN-doh | Bow rhymes with go, not cow. |
| Lets in light. Very good. | LETS in LYT. VEH-ree GUD. | Dry spoken answer then approving response; not “lesson lie”. |

Broad respellings are performance targets; they do not establish every vowel of the recorded accent. Capital letters indicate stress, not a request to shout.

## Music, tone, rhythm, and effects

**Voice and delivery — model interpretation:** Male rhythmic speech/singing with contrasting spoken characters or pitch registers. The model repeatedly hears theatrical call-and-response delivery; the deeper obviously aside contrasts with quicker lists. Actual performer count and regional accent are unresolved.

**Melody and phrase shape:** The recurring two-syllable window phrase anchors the catalogue. Short noun lists alternate with question/answer exchanges, creating contour through speech rather than a continuous sung tune. Suggested contours: lift the casement question, settle the yes answer, and lower/flatten obviously. These are practical performance instructions; the source contour has not been transcribed note for note.

**Rhythm:** A fast regular pulse near 135 BPM is supported by two signal-analysis methods; 67–68 BPM is the corresponding half-time interpretation. Short syllables and repeated words carry the rhythmic interest. Use straight 4/4 as a reconstruction setting; the original meter and precise swing ratio are not verified. Autocorrelation candidates: 134.6 BPM (peak score 0.64), 67.3 BPM (peak score 0.55), 89.8 BPM (peak score 0.47). These are relative peak scores, not probabilities; both tempo estimates use the same audio and cannot confirm one another independently.

**Tonality and harmony:** The mixture gives G major and G minor as the leading candidates; that establishes neither one conclusively. The broad effect is energetic and comic. For a first generation use a simple repeating tonal backing; test G as a centre only if an explicit key is useful. Mixed-audio pitch-class profile candidates: G major (0.73), G minor (0.66), B minor (0.42). These numbers are correlation scores, not probabilities. They are retained for experimentation, not stated as verified keys. An exact chord sequence and note-by-note melody have not been established.

**Section-level chroma comparison:** G is the leading tonic label throughout nearly all lyric sections in both signals, but major/minor rankings switch. A G-centered backing with mode left flexible is a testable recreation choice. The table gives only each signal's top profile candidate; the full ranked candidates, method and caveats are in [section_tonality.json](evidence/section_tonality.json) and [section_tonality.py](evidence/section_tonality.py). Scores are correlations, not probabilities.

| Time window | Original mix harmonic | Estimated backing harmonic |
|---|---|---|
| 0–8s | G minor (0.65) | G minor (0.61) |
| 8–16s | G minor (0.69) | G minor (0.74) |
| 16–24s | G minor (0.67) | G major (0.73) |
| 24–32s | G minor (0.74) | G minor (0.74) |
| 32–40s | G major (0.86) | G major (0.81) |
| 40–48s | G minor (0.79) | G minor (0.80) |
| 48–56s | G minor (0.79) | G minor (0.77) |
| 56–64s | G minor (0.71) | G minor (0.70) |
| 64–67s | A minor (0.44) | F major (0.74) |

**Instrumentation and timbre — model interpretation:** Early/middle excerpts consistently suggest an electronic low line and bright synth backing. The last excerpt instead describes brass/woodwind-like stabs. It is safer to request short bright, slightly brassy synthetic accents than to claim a real brass or woodwind ensemble.

**Production, sound effects, and edits:** Breathy inhalation/gasp-like sounds and abrupt dialogue interjections are reported in the middle. The final excerpt reports reverberant or broadcast-like texture, but its claims of tape hiss and provenance are not verified. Preserve short gaps and character changes; exact sampled sources and effect settings remain unknown.

**Arrangement recipe:** Alternate compact sung catalogue phrases with a miniature spoken question-and-answer routine. Use the two-syllable window as a recurring melodic/rhythmic anchor. Give casement a short call, a questioning rise in “Is that a casement?”, then a conclusive answer; those contours are suggested reconstruction directions, not a note transcription. Run the lists quickly, leave space around obviously and very good, and finish with two contrasting commands.

## Source uncertainties and reconstruction choices

- “Oriel” is caption-confirmed. Whisper alternatives include too/through; one second model returns “oriel too”, while the caption sequence is not clear enough to settle a following word. The Suno version tentatively uses “too”.
- The exact window repeat count after “obviously” is uncertain. The copy-ready pattern uses four calls.
- Architectural spellings were corrected using captions: glazing, stile, pane, sash cord, muntin, fastener.

The musical recipe adds explicit directions where the source analysis is incomplete. “Suggested” features are prompt-design choices, not recovered measurements. The copy-ready lyric file expands some repeated motifs to a practical arrangement and omits unresolved nonverbal passages; use the timed transcript as the evidence record.

## Paste into Suno: Styles

```text
Playful theatrical window song, about 135 BPM, clear male English rhythmic speech-singing over a compact electronic groove. Keep a G-centered pitch collection with major/minor color flexible; section profiles favor G but do not settle the mode or chords. A recurring WIN-doh hook anchors fast architectural lists. Alternate sung calls with dry comic dialogue: Casement, Is that a casement, Yes a casement; give Obviously a lower deadpan delivery and Very good a brief spoken reply. Tight programmed percussion, simple synth bass, bright short slightly brassy keyboard stabs. Narrow vocal motifs and speech-like pitch changes, occasional brief breath or gasp accents. End firmly with Open the window, Shut it again. Around 67 seconds; keep all dialogue audible.
```

## Paste into Suno: Lyrics

```text
[Rhythmic hook]
Window, window, window, window!
[Quick list]
Mullion, muntin, meeting rail, transom
Window, window, what have you got?
Mullion in the middle, glazing in the lot
[Call and response]
Casement!
Is that a casement?
Yes, a casement!
Open it out, shut it again
[Rhythmic list]
Stay, fastener, hinge, pane
Rail, stile, glazing bar
Rail, stile, glazing bar
Sash goes up, sash comes down
[Spoken exchange]
Sash cord!
Where's it gone?
In the box
Obviously
[Hook]
Window, window, window, window!
[Rhythmic list]
Fanlight, sidelight, oriel too
Bay window, bow window
[Spoken exchange]
What does it do?
Lets in light
Very good
[Call and response]
Casement!
Is that a casement?
Yes, a casement!
[Closing list]
Mullion, muntin, transom, pane
Open the window
Shut it again!
[Short ending]
```

## Optional phonetic lyric variant

`lyrics_phonetic.txt` replaces specialist words with broad sound-based spellings. Use it only if ordinary spelling is mispronounced. These respellings are suggested generator inputs, not a certified transcription of the recorded phonemes.

## First comparison after generating

Compare the question/answer spacing, the lower obviously aside and the final commands. Confirm the short word after oriel before calling the transcript exact; avoid turning every line into a smooth sung chorus.

## Audio-model evidence

Raw excerpt interpretations are preserved below as evidence links. They are not independent listening verification, and their incidental lyric guesses are not the corrected transcript. The recipe above prefers broad timbral descriptions when instrument identifications conflict.

- [Separated-backing interpretation](evidence/second_pass/DcqWhZtBIEI_backing.json)
- [Sampled-frame OCR results (automated and noisy)](evidence/ocr_results/DcqWhZtBIEI.json)
- [Sampled source-frame contact sheet](evidence/frames/DcqWhZtBIEI.jpg)
- [Targeted vocal interpretation](evidence/second_pass/DcqWhZtBIEI_vocals.json)
- [Pitch tracking diagnostic](evidence/pitch/DcqWhZtBIEI.json): 1.8% of frames passed the strict voicing filter; too sparse to establish a complete melody.
- [Independent small-model Vosk ASR output (raw; noisy)](evidence/asr_vosk/DcqWhZtBIEI.json)
- [Original-mix and harmonic pitch tracking diagnostic](evidence/pitch/DcqWhZtBIEI_mix_check.json)
- [0.0–24.0s model interpretation](evidence/audio_descriptions/DcqWhZtBIEI_00.json)
- [24.0–48.0s model interpretation](evidence/audio_descriptions/DcqWhZtBIEI_24.json)
- [48.0–67.0s model interpretation](evidence/audio_descriptions/DcqWhZtBIEI_48.json)


---

# Echinus / Entasis

Source: [DcvxvGDhSeb.mp4](../account_mp4/DcvxvGDhSeb.mp4) · **22.48 seconds** · [extracted audio](evidence/audio/DcvxvGDhSeb.wav)

## Listening/navigation aids

- [Waveform and onset-strength overview (navigation aid, not a score)](evidence/listen_cues/DcvxvGDhSeb/waveform_onsets.png)
- [8-second source-audio excerpts with relative time ranges](evidence/listen_cues/DcvxvGDhSeb/)

The excerpts are PCM slices from the existing mono analysis WAV. The plot shows amplitude and spectral onset strength; it does not establish notes, instrumentation, meter, or a transcription. Use the original stereo/video for final listening checks.

## Transcript and timing

| Approx. source time | Best-supported words / event |
|---|---|
| 0.0–3.8 | Echinus, entasis / Echinus, entasis. |
| 3.8–6.5 | A bulbous end / A gently swelling shaft. |
| 6.8–9.2 | Echinus, entasis. |
| 9.2–11.8 | A bulbous end / A gently swelling shaft. |
| 12.2–14.8 | A gently swelling shaft. |
| 16.0–18.7 | A gently swelling / swirling shaft [word unresolved; captions and one targeted pass support swelling, another chunk hears swirling]. |
| 18.7–22.5 | Musical/end-card tail. |

Punctuation is editorial. Caption timing and sung-word timing can differ. Bracketed uncertainty notes above are not sung text.

## Pronunciation and vocal phrasing

| Word / phrase | Broad sound / stress guide | Delivery and evidence |
|---|---|---|
| Echinus | ek-EYE-nuhs (UK) / ih-KY-nuhs (US) | Three syllables, middle stress. Cambridge lists these regional pronunciations. The UK form is a reasonable target for this British architectural context, but the recording vowel is not clear enough here to confirm which form was sung; the audio model’s “etchinoss” is not accepted as standard. |
| Entasis | EN-tuh-sis | Three syllables, first stress; consistent with the dictionary IPA /ˈɛntəsɪs/. Whisper supports the spelling, while the audio model’s “and tossiss” is a recognition error, not a pronunciation guide. |
| A bulbous end | uh BUL-bus END | Three stressed/unstressed word units; keep END as a distinct noun, not just “and”. |
| A gently swelling shaft | uh JENT-lee SWEL-ing SHAHFT | Six syllables; compact gently/swelling, lengthen the final shaft. |

Cambridge lists UK echinus /ekˈaɪ.nəs/ and US /ɪˈkaɪ.nəs/; [Wiktionary records entasis /ˈɛntəsɪs/](https://en.wiktionary.org/wiki/entasis). These standard pronunciations are helpful targets, not proof of the recorded vowels. Capital letters indicate stress, not a request to shout.

## Music, tone, rhythm, and effects

**Voice and delivery — model interpretation:** Male, energetic and slightly theatrical, with a chant-like speech-sung delivery. The model characterizes the performance as dominated by rhythm and articulation rather than separate sustained notes.

**Melody and phrase shape:** Paired three-syllable names alternate with a short phrase and a longer answer ending in shaft. Repetition of “a gently swelling shaft” supplies the ending motif. Suggested rendition: make the technical terms springy and compact, then gently lengthen the final shaft vowel in each response. Actual pitch intervals and any terminal glide are not measured.

**Rhythm:** A fast regular pulse near 135 BPM is supported by two signal-analysis methods; 67–68 BPM is the corresponding half-time interpretation. Short syllables and repeated words carry the rhythmic interest. Use straight 4/4 as a reconstruction setting; the original meter and precise swing ratio are not verified. Autocorrelation candidates: 136.3 BPM (peak score 0.59), 68.2 BPM (peak score 0.57), 90.8 BPM (peak score 0.52). These are relative peak scores, not probabilities; both tempo estimates use the same audio and cannot confirm one another independently.

**Tonality and harmony:** C major is the leading mixed-audio profile, but C minor also scores meaningfully. Use a light repetitive tonal setting; C major is an optional trial key rather than a verified source key. The vocal rhythm is better established than the harmony. Mixed-audio pitch-class profile candidates: C major (0.69), C minor (0.53), G major (0.50). These numbers are correlation scores, not probabilities. They are retained for experimentation, not stated as verified keys. An exact chord sequence and note-by-note melody have not been established.

**Section-level chroma comparison:** The opening favors G major; later windows are weaker and the original mix and separated backing disagree. No stable whole-track key is supported. The table gives only each signal's top profile candidate; the full ranked candidates, method and caveats are in [section_tonality.json](evidence/section_tonality.json) and [section_tonality.py](evidence/section_tonality.py). Scores are correlations, not probabilities.

| Time window | Original mix harmonic | Estimated backing harmonic |
|---|---|---|
| 0–8s | G major (0.69) | G major (0.65) |
| 8–16s | C minor (0.50) | G minor (0.52) |
| 16–22s | B minor (0.35) | F major (0.55) |

**Instrumentation and timbre — model interpretation:** The model identifies synthetic drum, bass and keyboard-like textures. It does not identify an acoustic lead instrument with adequate support. Keep the backing sparse enough to retain all three syllables of each technical word.

**Production, sound effects, and edits:** A short swoosh-like sound near the ending is reported by the model. Digital/clean overall texture is plausible, but the exact processor is unknown. The most important audible form is the spaced repetition of the final line, supported by both recognizer passes.

**Arrangement recipe:** Pair two three-syllable technical terms as a repeating melodic cell. Answer with two descriptive phrases, the second longer and ending in the punchline shaft. Repeat that final phrase twice with space between repetitions, allowing its last vowel to carry the ending. Avoid adding new verses.

## Source uncertainties and reconstruction choices

- The caption explicitly supplies “A Bulbous End”. ASR merges this with the next line as “a bulbous and a gently…”. The corrected transcript follows the captioned noun phrase.
- Near 16–19 seconds, captions say “A Gently Swelling Shaft”; one targeted recognizer hears “swelling”, while another chunk hears “swirling”. The word is marked uncertain in the source transcript; the Suno lyric uses the caption-supported “swelling”.
- Phonetic guidance for echinus and entasis is a broad pronunciation target, not a measured phoneme transcript.

The musical recipe adds explicit directions where the source analysis is incomplete. “Suggested” features are prompt-design choices, not recovered measurements. The copy-ready lyric file expands some repeated motifs to a practical arrangement and omits unresolved nonverbal passages; use the timed transcript as the evidence record.

## Paste into Suno: Styles

```text
Short quirky electronic chant, about 135 BPM. Clearly enunciated male English speech-singing, slightly theatrical. Pair the three-syllable motifs ih-KY-nus and EN-tuh-sis; answer with A bulbous end and A gently swelling shaft. Narrow rhythmic vocal contour, compact consonants and a longer final shaft vowel. Sparse synthetic bass, punchy programmed drums and light keyboard accents. Repeat the final descriptive phrase with small spaces between calls; optional short swoosh at the end. Suggested light major mood, roughly 22 seconds, no added verses.
```

## Paste into Suno: Lyrics

```text
[Paired rhythmic motif]
Echinus, entasis
Echinus, entasis
[Answering phrase]
A bulbous end
A gently swelling shaft
[Repeat motif]
Echinus, entasis
A bulbous end
A gently swelling shaft
[Refrain]
A gently swelling shaft
[Brief pause, final refrain]
A gently swelling shaft
[Short ending]
```

## Optional phonetic lyric variant

`lyrics_phonetic.txt` replaces specialist words with broad sound-based spellings. Use it only if ordinary spelling is mispronounced. These respellings are suggested generator inputs, not a certified transcription of the recorded phonemes.

## First comparison after generating

Check the actual vowels and stress of echinus and entasis against the source. Keep “end” audible as a noun and do not let the generator merge it into “and”.

## Audio-model evidence

Raw excerpt interpretations are preserved below as evidence links. They are not independent listening verification, and their incidental lyric guesses are not the corrected transcript. The recipe above prefers broad timbral descriptions when instrument identifications conflict.

- [Separated-backing interpretation](evidence/second_pass/DcvxvGDhSeb_backing.json)
- [Sampled-frame OCR results (automated and noisy)](evidence/ocr_results/DcvxvGDhSeb.json)
- [Sampled source-frame contact sheet](evidence/frames/DcvxvGDhSeb.jpg)
- [Targeted vocal interpretation](evidence/second_pass/DcvxvGDhSeb_vocals.json)
- [Pitch tracking diagnostic](evidence/pitch/DcvxvGDhSeb.json): 4.8% of frames passed the strict voicing filter; too sparse to establish a complete melody.
- [Independent small-model Vosk ASR output (raw; noisy)](evidence/asr_vosk/DcvxvGDhSeb.json)
- [Original-mix and harmonic pitch tracking diagnostic](evidence/pitch/DcvxvGDhSeb_mix_check.json)
- [0.0–22.5s model interpretation](evidence/audio_descriptions/DcvxvGDhSeb_00.json)


---

# Hall House

Source: [DdLxzBIoJ8F.mp4](../account_mp4/DdLxzBIoJ8F.mp4) · **49.97 seconds** · [extracted audio](evidence/audio/DdLxzBIoJ8F.wav)

## Listening/navigation aids

- [Waveform and onset-strength overview (navigation aid, not a score)](evidence/listen_cues/DdLxzBIoJ8F/waveform_onsets.png)
- [8-second source-audio excerpts with relative time ranges](evidence/listen_cues/DdLxzBIoJ8F/)

The excerpts are PCM slices from the existing mono analysis WAV. The plot shows amplitude and spectral onset strength; it does not establish notes, instrumentation, meter, or a transcription. Use the original stereo/video for final listening checks.

## Transcript and timing

| Approx. source time | Best-supported words / event |
|---|---|
| 0.0–4.1 | Hall house, hall house / Have you visited a hall house? |
| 4.1–7.3 | Front door, back door / Let's see your cross passage. |
| 7.4–10.3 | Hall house, hall house. |
| 11.0–14.5 | Open hall, nice and wide / Service end, at the side. |
| 14.5–18.1 | Upper end, lower end / Show me where your screens have been. |
| 18.1–19.9 | Hall house, hall house. |
| 20.0–23.2 | Smoke-blackened all the way / Big old hearth, what can I say? |
| 23.4–25.1 | Inserted floor, oh behave! |
| 25.8–28.7 | Hall house, hall house. |
| 28.7–32.8 | Front door, back door / Straight through the cross passage. |
| 32.8–34.4 | Hall house, hall house. |
| 34.4–38.1 | Nice big frame, plenty of bays / Service end, seen better days. |
| 38.1–41.0 | Solar upstairs / Very private. |
| 41.0–43.9 | Hall house, hall house. |
| 44.2–46.9 | Have you visited a hall house? |
| 46.9–48.65 | Short audio tail; the audio stream ends at approximately 48.65s. |
| 48.65–49.97 | Video-only tail; no source audio stream remains. |

Punctuation is editorial. Caption timing and sung-word timing can differ. Bracketed uncertainty notes above are not sung text.

## Pronunciation and vocal phrasing

| Word / phrase | Broad sound / stress guide | Delivery and evidence |
|---|---|---|
| Hall house | HAWL HOWSS | Two strong syllables; hall and house have different vowels. Clearly articulate the H of house. |
| Have you visited a hall house? | hav-yuh VIZ-it-id uh HAWL HOWSS | Quick unstressed lead-in; three syllables in visited, then the two-word hook. |
| Front door, back door | FRUNT DAW, BAK DAW | Four deliberate word attacks. |
| Let's see your cross passage | lets SEE yuh KROSS PAS-ij | Cross passage has three syllables; avoid swallowing the final ij. |
| Open hall, nice and wide | OH-pun HAWL, NYSS un WYD | Rhyming phrase end on wide. |
| Service end, at the side | SUR-vis END, at thuh SYD | Two syllables in service; side matches wide. |
| Upper end, lower end | UP-uh END, LOH-uh END | Parallel rhythmic cells. |
| Show me where your screens have been | SHOH mee WAIR yuh SKREENZ hav BIN | Screens is one syllable. Bin/been vowel is a broad suggested rendition, not established exact vowel. |
| Smoke-blackened all the way | SMOHK BLAK-und awl thuh WAY | Blackened is two syllables, not “black and”. |
| Big old hearth, what can I say? | BIG ohld HAHth, wot kun eye SAY | Hearth has the heart vowel in the suggested British rendition, not the earth vowel. |
| Inserted floor, oh behave | in-SUR-tid FLAW, oh bih-HAYV | Emphasise the comic oh behave as its own aside. |
| Nice big frame, plenty of bays | NYSS big FRAYM, PLEN-tee uv BAYZ | Keep the frame/bays stresses clear. |
| Service end, seen better days | SUR-vis END, SEEN BET-uh DAYZ | Rhymes days with bays. |
| Solar upstairs, very private | SOH-luh up-STAIRZ, VEH-ree PRY-vit | Solar is the room name, two syllables; private two syllables. |

Broad respellings are performance targets; they do not establish every vowel of the recorded accent. Capital letters indicate stress, not a request to shout.

## Music, tone, rhythm, and effects

**Voice and delivery — model interpretation:** An upfront, relatively dry male voice with conversational, clearly enunciated rhythmic delivery. The model hears pitch bends and dramatic pauses; the lyric pattern includes separate comic asides.

**Melody and phrase shape:** Hall house is the recurring two-word refrain, while the verse moves quickly through rhyming phrases. The source sequence supports repeated couplet-length units, changing to spoken asides on oh behave and very private. Suggested rendition: broaden the two stresses of HALL HOUSE, keep the descriptive lines on a narrow patter melody, and briefly drop the aside into speech. Exact notes and a sung range are not established.

**Rhythm:** A fast regular pulse near 135 BPM is supported by two signal-analysis methods; 67–68 BPM is the corresponding half-time interpretation. Short syllables and repeated words carry the rhythmic interest. Use straight 4/4 as a reconstruction setting; the original meter and precise swing ratio are not verified. Autocorrelation candidates: 136.5 BPM (peak score 0.58), 68.2 BPM (peak score 0.57), 90.8 BPM (peak score 0.51). These are relative peak scores, not probabilities; both tempo estimates use the same audio and cannot confirm one another independently.

**Tonality and harmony:** Whole-mixture key correlations are weak and nearly tied; no key or major/minor mode is established. Preserve a simple low tonal backing and the rhythmic phrasing rather than forcing a supposedly exact progression. The model’s mood descriptions range from lively/quirky to slightly dark, so the recreation can keep a playful deadpan tone without prescribing a dark minor mode. Mixed-audio pitch-class profile candidates: A♭ major (0.37), D♭ minor (0.37), C minor (0.34). These numbers are correlation scores, not probabilities. They are retained for experimentation, not stated as verified keys. An exact chord sequence and note-by-note melody have not been established.

**Section-level chroma comparison:** C minor ranks first in most windows, but scores are modest and the 8–16 s and ending windows vary. C-minor-leaning backing is an experiment, not a verified key. The table gives only each signal's top profile candidate; the full ranked candidates, method and caveats are in [section_tonality.json](evidence/section_tonality.json) and [section_tonality.py](evidence/section_tonality.py). Scores are correlations, not probabilities.

| Time window | Original mix harmonic | Estimated backing harmonic |
|---|---|---|
| 0–8s | C minor (0.44) | C minor (0.48) |
| 8–16s | C♯ major (0.39) | G♯ major (0.44) |
| 16–24s | C minor (0.41) | C minor (0.48) |
| 24–32s | C minor (0.43) | C minor (0.45) |
| 32–40s | C minor (0.38) | C minor (0.43) |
| 40–48s | C major (0.42) | C minor (0.40) |

**Instrumentation and timbre — model interpretation:** The model consistently describes an electronic beat and synthesized low line, with occasional higher chime-like accents. It also suggests sampler-like percussion, but specific 808 hardware and named game associations are unsupported and omitted from the recipe.

**Production, sound effects, and edits:** Short whoosh-like transitions and chime-like accents are model-reported possibilities. The dry foreground voice, pauses, and comic asides are the more stable description. No identifiable original game, show, artist or sample source has been established.

**Arrangement recipe:** A recurring two-word refrain interleaved with short rhyming descriptive couplets. Keep the narrative syllabic and brisk; broaden the two strong beats of hall house. Let oh behave and very private become spoken comic asides. Repeat the opening question at the end, rather than adding a conventional new chorus.

## Source uncertainties and reconstruction choices

- “Service end, seen better days” is supported by repeated audio recognition and the visible “Seen Better Days” caption; punctuation is editorial.
- The audio stream lasts 48.645 seconds although the video lasts 49.967 seconds; the final 1.32 seconds are not missing transcription. A short ASR chunk mishears hall house as whorehouse. The persistent caption and other audio passes establish hall house.

The musical recipe adds explicit directions where the source analysis is incomplete. “Suggested” features are prompt-design choices, not recovered measurements. The copy-ready lyric file expands some repeated motifs to a practical arrangement and omits unresolved nonverbal passages; use the timed transcript as the evidence record.

## Paste into Suno: Styles

```text
Deadpan comic architectural patter song, about 135 BPM. Upfront clearly articulated male English rhythmic speech-singing, dry and conversational with small pitch bends. A broad two-beat HALL HOUSE refrain returns between quick rhyming descriptive couplets. Minimal electronic drum groove, low synth pulse, sparse bright chime-like accents. Let Oh behave and Very private become isolated spoken asides with small pauses; keep cross passage, hearth and solar intelligible. Reprise Have you visited a hall house at the ending. Around 50 seconds, compact arrangement with no new chorus or extra verses.
```

## Paste into Suno: Lyrics

```text
[Hook]
Hall house, hall house
Have you visited a hall house?
Front door, back door
Let's see your cross passage
Hall house, hall house
[Verse]
Open hall, nice and wide
Service end, at the side
Upper end, lower end
Show me where your screens have been
[Hook]
Hall house, hall house
[Verse]
Smoke-blackened all the way
Big old hearth, what can I say?
Inserted floor
[Spoken aside]
Oh behave!
[Hook]
Hall house, hall house
Front door, back door
Straight through the cross passage
Hall house, hall house
[Verse]
Nice big frame, plenty of bays
Service end, seen better days
Solar upstairs
[Spoken aside]
Very private
[Final hook]
Hall house, hall house
Have you visited a hall house?
[Short ending]
```

## Optional phonetic lyric variant

`lyrics_phonetic.txt` replaces specialist words with broad sound-based spellings. Use it only if ordinary spelling is mispronounced. These respellings are suggested generator inputs, not a certified transcription of the recorded phonemes.

## First comparison after generating

Compare the two strong hall-house syllables, the patter speed of the couplets, and the pauses around oh behave and very private. Check that hearth does not become earth and solar remains a two-syllable room name.

## Audio-model evidence

Raw excerpt interpretations are preserved below as evidence links. They are not independent listening verification, and their incidental lyric guesses are not the corrected transcript. The recipe above prefers broad timbral descriptions when instrument identifications conflict.

- [Separated-backing interpretation](evidence/second_pass/DdLxzBIoJ8F_backing.json)
- [Sampled-frame OCR results (automated and noisy)](evidence/ocr_results/DdLxzBIoJ8F.json)
- [Sampled source-frame contact sheet](evidence/frames/DdLxzBIoJ8F.jpg)
- [Pitch tracking diagnostic](evidence/pitch/DdLxzBIoJ8F.json): 4.6% of frames passed the strict voicing filter; too sparse to establish a complete melody.
- [Independent small-model Vosk ASR output (raw; noisy)](evidence/asr_vosk/DdLxzBIoJ8F.json)
- [Original-mix and harmonic pitch tracking diagnostic](evidence/pitch/DdLxzBIoJ8F_mix_check.json)
- [0.0–24.0s model interpretation](evidence/audio_descriptions/DdLxzBIoJ8F_00.json)
- [24.0–48.0s model interpretation](evidence/audio_descriptions/DdLxzBIoJ8F_24.json)
