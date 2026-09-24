# Columns / Classical Orders

Source: [columns-classical-orders.mp4](../../source_videos/columns-classical-orders.mp4) · **53.62 seconds** · [extracted audio](../../evidence/audio/DcYTYvMBSMn.wav)

## Listening/navigation aids

- [Waveform and onset-strength overview (navigation aid, not a score)](../../evidence/listen_cues/DcYTYvMBSMn/waveform_onsets.png)
- [8-second source-audio excerpts with relative time ranges](../../evidence/listen_cues/DcYTYvMBSMn/)

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

**Section-level chroma comparison:** E-flat/B-flat profile labels recur across most sections in both signals, while major/minor mode and the strongest member of that family vary. An E-flat/B-flat tonal palette is a more cautious prompt test than a single asserted key. The table gives only each signal's top profile candidate; the full ranked candidates, method and caveats are in [section_tonality.json](../../evidence/section_tonality.json) and [section_tonality.py](../../evidence/section_tonality.py). Scores are correlations, not probabilities.

| Time window | Original mix harmonic | Estimated backing harmonic |
|---|---|---|
| 0–8s | D♯ minor (0.57) | D♯ major (0.71) |
| 8–16s | D♯ major (0.72) | D♯ major (0.71) |
| 16–24s | A♯ major (0.71) | D♯ major (0.64) |
| 24–32s | D♯ major (0.66) | D♯ major (0.67) |
| 32–40s | A♯ major (0.71) | A♯ major (0.63) |
| 40–48s | D♯ major (0.69) | D♯ major (0.68) |
| 48–54s | D♯ major (0.73) | A♯ major (0.78) |

**Overlapping-window sensitivity check:** Overlapping windows repeatedly favor E-flat major, with B-flat major profiles recurring in the mix and in some backing windows. This strengthens an E-flat/B-flat major-leaning prompt experiment, but does not establish chords or harmonic function. The check uses 4-second windows at 2-second hops, so it tests whether the 8-second result depends on one fixed cut; these overlapping windows are still not musical phrase boundaries. Full rankings and caveats: [rolling_tonality.json](../../evidence/rolling_tonality.json) and [rolling_tonality.py](../../evidence/rolling_tonality.py).

**Instrumentation and timbre — model interpretation:** At least a rhythmic low/percussive backing is indicated. One model excerpt hears drums, bass and synths; another hears beatboxing/sample-like percussion. Prefer a hybrid description—tight synthetic/vocal-like percussion and a low pulse—over claiming a live bass guitar or drum kit.

**Production, sound effects, and edits:** Possible mild reverb or short delay on the voice. The final Palladio exclamation is followed by a sparse ending and a low percussive cue according to the short tail analysis. Specific delay times and effect devices are not known.

**Arrangement recipe:** Four catalogue blocks using the same compact rhythmic template. Two brisk list phrases are followed by a broader held “Ah” and a more melodic long name. Reuse the rhythmic cell for column/pilaster/fluted/capital, with short Tuscan or shaft answers. Keep the long vowels at the end of each block distinct from the clipped list delivery.

## Source uncertainties and reconstruction choices

- Specialist spellings are supported by the captions; ASR variants “biloster”, “dory”, and “I love you” have been corrected to the captioned terms.
- Timings are approximate section boundaries; rapid sung syllables need not align exactly with the animated captions.

The musical recipe adds explicit directions where the source analysis is incomplete. “Suggested” features are prompt-design choices, not recovered measurements. The copy-ready lyric file expands some repeated motifs to a practical arrangement and omits unresolved nonverbal passages; use the timed transcript as the evidence record.

## Paste into Suno: Styles

```text
Quirky theatrical male catalogue song, about 135 BPM, brisk straight rhythm. Precisely articulated short speech-sung lists contrast with broad sustained open-vowel Ah exclamations and elongated architectural names. Reuse the same compact motif for column, pilaster, fluted and capital sections. Light punchy electronic beat, low bass pulse, dry vocal-like percussion and sparse bright keyboard accents; keep the lead upfront. Try an E-flat-major-like pitch center with recurring B-flat-major color; leave exact chords and harmonic function flexible, since these are profile candidates rather than a score. Emphasise kuh-RIN-thee-un, eye-ON-ik and puh-LAH-dee-oh clearly. End with composite then Palladio and a short low percussive stop, roughly 54 seconds.
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

- [Separated-backing interpretation](../../evidence/second_pass/columns-classical-orders_backing.json)
- [Sampled-frame OCR results (automated and noisy)](../../evidence/ocr_results/columns-classical-orders.json)
- [Sampled source-frame contact sheet](../../evidence/frames/DcYTYvMBSMn.jpg)
- [Pitch tracking diagnostic](../../evidence/pitch/columns-classical-orders.json): 10.3% of frames passed the strict voicing filter; too sparse to establish a complete melody.
- [Independent small-model Vosk ASR output (raw; noisy)](../../evidence/asr_vosk/columns-classical-orders.json)
- [Higher-capacity Vosk ASR output (raw; noisy)](../../evidence/asr_vosk_large/columns-classical-orders.json)
- [Original-mix and harmonic pitch tracking diagnostic](../../evidence/pitch/columns-classical-orders_mix_check.json)
- [0.0–24.0s model interpretation](../../evidence/audio_descriptions/columns-classical-orders_00.json)
- [24.0–48.0s model interpretation](../../evidence/audio_descriptions/columns-classical-orders_24.json)
- [48.0–53.6s model interpretation](../../evidence/audio_descriptions/columns-classical-orders_48.json)
