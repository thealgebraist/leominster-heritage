# Door Knockers

Source: [door-knockers.mp4](../../source_videos/door-knockers.mp4) · **37.70 seconds** · [extracted audio](../../evidence/audio/DdZlT3TIx3q.wav)

## Listening/navigation aids

- [Waveform and onset-strength overview (navigation aid, not a score)](../../evidence/listen_cues/DdZlT3TIx3q/waveform_onsets.png)
- [8-second source-audio excerpts with relative time ranges](../../evidence/listen_cues/DdZlT3TIx3q/)

The excerpts are PCM slices from the existing mono analysis WAV. The plot shows amplitude and spectral onset strength; it does not establish notes, instrumentation, meter, or a transcription. Use the original stereo/video for final listening checks.

## Transcript and timing

| Approx. source time | Best-supported words / event |
|---|---|
| 0.0–1.8 | K.K. Knockers! |
| 2.1–4.9 | Big knockers, small knockers, long knockers too. |
| 4.9–8.6 | Funny little knockers staring back at you. |
| 8.6–12.1 | Brass knockers, iron knockers, some as big as your head. |
| 12.1–14.8 | On the door, I said. |
| 15.8–19.2 | Polish your knockers, give them a shine. |
| 19.2–22.7 | Show me your knockers, I’ll show you mine. |
| 22.7–23.6 | Knock, knock! |
| 24.2–25.2 | Who’s there? |
| 25.4–26.5 | Door furniture. |
| 26.5–27.4 | Behave! |
| 27.4–35.9 | Musical tail; no further intelligible words recovered. |

Punctuation is editorial. Caption timing and sung-word timing can differ. Bracketed uncertainty notes above are not sung text.

## Pronunciation and vocal phrasing

| Word / phrase | Broad sound / stress guide | Delivery and evidence |
|---|---|---|
| K.K. | KAY-kay | Two letter names, brisk pickup before Knockers. |
| Knockers | NOK-uhz | Two syllables, first stress; keep the final r non-rhotic for the apparent British-style delivery, though the singer’s accent is not independently established. |
| Big / small / long knockers | BIG / SMAWL / LONG NOK-uhz | Three parallel, strongly accented list items; keep each adjective distinct. |
| Funny little knockers, staring back at you | FUN-ee LIT-ul NOK-uhz, STAIR-ing BAK at YOO | Quick unstressed middle syllables; land on YOU. |
| Brass / iron knockers | BRASS / EYE-urn NOK-uhz | Iron is two syllables in the suggested rendition; separate the paired material names. |
| Some as big as your head, on the door I said | sum uz BIG uz yuh HED, on thuh DAW eye SED | Maintain the head/said rhyme across the phrase break. |
| Polish your knockers, give them a shine | POH-lish yuh NOK-uhz, giv thum uh SHYN | Polish is the verb with first-syllable stress; let shine carry the rhyme. |
| Show me your knockers, I’ll show you mine | SHOH mee yuh NOK-uhz, ayl SHOH yuh MYN | Parallel show me / I’ll show you phrasing; emphasize the final mine. |
| Knock, knock! Who’s there? | NOK NOK! HOOZ thair? | Switch to a short spoken knock-knock exchange. |
| Door furniture. Behave! | DAW FUR-ni-chuh. bih-HAYV! | Dry spoken punchline followed by a sharp admonishing response. |

Broad respellings are performance targets; they do not establish every vowel of the recorded accent. Capital letters indicate stress, not a request to shout.

## Music, tone, rhythm, and effects

**Voice and delivery — model interpretation:** Audio-model interpretation: an energetic male-sounding rhythmic speaking/chanting voice carries most of the verse, followed by a short spoken knock-knock exchange. Voice identity, accent, and the number of performers are not independently established.

**Melody and phrase shape:** The verses move through repeated list-shaped phrases and rhyming couplets, with little evidence of a long sustained melody. Keep the list on a narrow speech-sung pitch cell, give “head / said” and “shine / mine” a similar phrase-ending contour, then sharply change to spoken dialogue. These contours are reconstruction directions, not recovered notes.

**Rhythm:** Onset analysis estimates a pulse near 136 BPM; 68 BPM is a possible half-time reading. Short phrases and repeated word accents dominate. Use straight 4/4 only as a generation setting; the source meter and swing are not verified. Autocorrelation candidates: 135.3 BPM (peak score 0.58), 67.7 BPM (peak score 0.57), 90.1 BPM (peak score 0.51). These are relative peak scores, not probabilities; both tempo estimates use the same audio and cannot confirm one another independently.

**Tonality and harmony:** The mixed-audio key-profile correlations are weak and closely spaced (C minor 0.33, C-sharp minor 0.33, C-sharp major 0.31). No stable tonic, mode, or chord progression is supported. Use a simple comic backing without naming a key. Mixed-audio pitch-class profile candidates: C minor (0.33), D♭ minor (0.33), D♭ major (0.31). These numbers are correlation scores, not probabilities. They are retained for experimentation, not stated as verified keys. An exact chord sequence and note-by-note melody have not been established.

**Section-level chroma comparison:** The mix and estimated backing have weak, closely ranked and changing candidates. No stable tonic or mode is supported; use the brisk speech-rhythm as the reconstruction anchor and leave key and chords flexible. The table gives only each signal's top profile candidate; the full ranked candidates, method and caveats are in [section_tonality.json](../../evidence/section_tonality.json) and [section_tonality.py](../../evidence/section_tonality.py). Scores are correlations, not probabilities.

| Time window | Original mix harmonic | Estimated backing harmonic |
|---|---|---|
| 0–8s | C minor (0.47) | C major (0.45) |
| 8–16s | C♯ major (0.44) | C♯ major (0.43) |
| 16–24s | C minor (0.34) | C♯ minor (0.36) |
| 24–32s | C minor (0.33) | C minor (0.34) |
| 32–36s | A♯ minor (0.35) | C major (0.37) |



**Instrumentation and timbre — model interpretation:** The audio model describes a beat-led backing and speculates about drums, bass, keyboard/synth or chiptune-like sounds; its descriptions differ between excerpts. Ask for a light electronic beat with a simple low pulse and short bright accents, while treating exact instruments as uncertain.

**Production, sound effects, and edits:** The clear changes are vocal edits/dialogue around the knock-knock exchange and final Behave punchline. The model reports no distinct non-musical effect with confidence; do not add a door knock sound unless desired as a prompt choice.

**Arrangement recipe:** Deliver the main text as a cheeky, briskly rhymed comic verse, with each adjective list snapping to the beat. Keep the K.K. pickup short, make “head / said” and “shine / mine” the phrase-ending rhymes, then break into a spoken knock-knock call and response. Drop the register for “Door furniture” and finish with a separate emphatic “Behave!” before the instrumental tail.

## Source uncertainties and reconstruction choices

- Whisper large-v3-turbo and the independently run Vosk small English model agree on the long verse and knock-knock exchange despite Vosk substitutions. Sampled on-screen captions directly support K.K., Knockers, Funny Little Knockers, Big Knockers, Small Knockers, Long Knockers, Iron Knockers, Show me your Knockers, Who’s There?, Door Furniture and Behave. Caption OCR is noisy and does not settle every syllable; “On the door, I said” is primarily audio-recognizer evidence.
- The opening is captioned “K.K.” followed by “Knockers”; punctuation as “K.K. Knockers!” is editorial.
- The video stream lasts 37.7 seconds, but its AAC audio ends at about 35.9 seconds; the final visual tail has no source audio.

The musical recipe adds explicit directions where the source analysis is incomplete. “Suggested” features are prompt-design choices, not recovered measurements. The copy-ready lyric file expands some repeated motifs to a practical arrangement and omits unresolved nonverbal passages; use the timed transcript as the evidence record.

## Paste into Suno: Styles

```text
Cheeky comic novelty patter song, around 136 BPM from onset analysis, with a brisk bounce and clear male English speech-singing. Snap the repeated big/small/long knockers list to a compact rhythmic pitch cell; rhyme “head / said” and “shine / mine” with matched phrase endings. Use a light electronic drum pulse, simple low bass and sparse bright keyboard accents, but keep exact instruments flexible. Break into a dry spoken “Knock, knock / Who’s there?” exchange, drop the punchline to “Door furniture,” then hit “Behave!” distinctly. About 36 seconds; short intro and instrumental tail, no extra verses.
```

## Paste into Suno: Lyrics

```text
[Quick spoken pickup]
K.K. Knockers!
[Bouncy rhythmic verse]
Big knockers, small knockers, long knockers too
Funny little knockers staring back at you
Brass knockers, iron knockers, some as big as your head
On the door, I said
[Rhyming couplet]
Polish your knockers, give them a shine
Show me your knockers, I’ll show you mine
[Spoken knock-knock exchange]
Knock, knock!
Who’s there?
Door furniture
[Spoken punchline]
Behave!
[Instrumental tail]
```

## Optional phonetic lyric variant

`lyrics_phonetic.txt` replaces specialist words with broad sound-based spellings. Use it only if ordinary spelling is mispronounced. These respellings are suggested generator inputs, not a certified transcription of the recorded phonemes.

## First comparison after generating

Check K.K. at the opening, the adjective-list timing, both rhyme pairs, and the pauses in the knock-knock exchange. The file captions corroborate the joke lines, but do not establish exact musical notes or instruments.

## Audio-model evidence

Raw excerpt interpretations are preserved below as evidence links. They are not independent listening verification, and their incidental lyric guesses are not the corrected transcript. The recipe above prefers broad timbral descriptions when instrument identifications conflict.

- [Sampled-frame OCR results (automated and noisy)](../../evidence/ocr_results/door-knockers.json)
- [Sampled source-frame contact sheet](../../evidence/frames/DdZlT3TIx3q.jpg)
- [Pitch tracking diagnostic](../../evidence/pitch/door-knockers.json): 2.0% of frames passed the strict voicing filter; too sparse to establish a complete melody.
- [Independent small-model Vosk ASR output (raw; noisy)](../../evidence/asr_vosk/door-knockers.json)
- [0.0–24.0s model interpretation](../../evidence/audio_descriptions/door-knockers_00.json)
- [24.0–35.9s model interpretation](../../evidence/audio_descriptions/door-knockers_24.json)
