from pathlib import Path
import json
r=Path(__file__).resolve().parent
p=r/'music_notes.json';m=json.loads(p.read_text())
updates={
'Dc1uBZahhts':'A second query on the separated backing also identifies synthesized percussion and bass, with short bright keyboard/bell-like figures and possible boing/swoop effects. This supports the broad electronic recipe; its speculation about a game source is rejected.',
'Dc8axxYIC3k':'The separated-backing query conflicts with the mixture query: it suggests acoustic drums/hand percussion and a guitar-or-keyboard mallet-like figure. The instrument identity is unresolved. The common description is a steady bass foundation, a crisp beat and short bright pitched figures; acoustic versus synthetic sources are not established.',
'DcRZB_PBFkr':'The separated-backing query identifies a repetitive synth bassline, bright staccato synth figures and a regular dance beat. This strengthens the electronic backing interpretation where the foreground-vocal query was ambiguous. A four-on-the-floor pattern is model-reported, not independently counted.',
'DcYTYvMBSMn':'The separated-backing query identifies synth bass, electronic drums and synth figures. This is more consistent with an electronic backing than a purely beatboxed arrangement; it does not rule out vocal-like samples. A scratch-like texture is model-reported and tentative.',
'DcbYsWLhhdZ':'The separated-backing query also identifies synthesized bass and short pitched synth/vocal-like chops over a steady danceable rhythm. This strengthens the broad electronic description, without establishing the exact instruments or production chain.',
'DcqWhZtBIEI':'The separated-backing query also identifies electronic bass and synthesized rhythmic/pitched sounds. It supports the broad electronic description; later brassy timbres do not establish a live brass section.',
'DcvxvGDhSeb':'The separated-backing query suggests a funk/disco-like groove, prominent melodic bass, electronic percussion and staccato synth/brass-like figures. Electric bass versus synthesized bass remains unresolved. These are model interpretations, not instrument credits.',
'DdLxzBIoJ8F':'The separated-backing query also identifies electronic bass, drums and keyboard/synth sounds, with beep, glide and wah-like accents. This strengthens the broad timbral recipe; precise effects remain unverified.'}
for id,addition in updates.items():
 if id=='Dc8axxYIC3k':m[id]['instruments']=addition
 else:m[id]['instruments']+=' '+addition
m['Dc8axxYIC3k']['style']=m['Dc8axxYIC3k']['style'].replace('minimal punchy electronic beat','minimal punchy backing groove').replace('Synthetic low pulse and crisp percussion','Steady low bass pulse, crisp percussion and short bright mallet-like keyboard figures')
m['DcqWhZtBIEI']['check']=m['DcqWhZtBIEI']['check'].replace('Confirm the short word after oriel before calling the transcript exact','A second model supports oriel too, but source listening is still needed for certainty')
p.write_text(json.dumps(m,indent=2))
p=r/'track_data.py';s=p.read_text()
s=s.replace('Whisper and the separated-vocal model return “soaping nicely”; use it as the audio-supported source reading, and mark “sloping” only as an architectural-context guess.', 'Whisper and a second model on separated vocals both returned “soaping nicely”; “sloping nicely” is contextually plausible, but frames sampled every 0.05 seconds across the transition do not reveal a readable caption for this word.')
s=s.replace('Both recognizer passes strongly support a final AY sound, not eye.', 'Whisper and the separated-vocal model (“gotay”) support a final AY sound, not eye.')
s=s.replace('The sound is deliberately close to “guttae”,', 'The sound is interpreted as close to “guttae”,')
s=s.replace('“Hodor” is a plausible reading of ASR “hold on” in this door-pun context; it remains unconfirmed.', 'Both Whisper and the separated-vocal model return “hold on”; “Hodor” is a contextual alternative, not a recovered fact. The second model also reports an initial Ah vocalization.')
s=s.replace("('23.5–28.8','[Hodor?] / intervening vocal or effect passage; unresolved.')", "('23.5–28.8','Ah / [Hold on? Hodor?] / intervening vocal or effect passage; unresolved.')")
s=s.replace('“Oriel” is caption-confirmed; the following short word sounds like too/through to the recognizers and remains unresolved. The recreation version chooses “too”.', '“Oriel” is caption-confirmed. Whisper alternatives included too/through; the second model on separated vocals returns “oriel too”, strengthening that reading without proving it. The recreation version uses “too”.')
s=s.replace('Caption establishes spelling; the exact source first vowel is not verified.', 'Caption establishes spelling. This conventional KY target is not established as the recording pronunciation; the separated-vocal model approximates the word as “etchinoss”.')
s=s.replace('source middle-vowel quality needs listening confirmation.', 'the separated-vocal model approximates “and tossiss”. Source vowel quality and exact stress need listening confirmation.')
s=s.replace("('46.9–50.0','Musical/end-card tail.')", "('46.9–48.65','Short audio tail; the audio stream ends at approximately 48.65s.'),('48.65–49.97','Video-only tail; no source audio stream remains.')")
s=s.replace('A short ASR chunk mishears hall house as whorehouse.', 'The audio stream lasts 48.645 seconds although the video lasts 49.967 seconds; the final 1.32 seconds are not missing transcription. A short ASR chunk mishears hall house as whorehouse.')
p.write_text(s)
