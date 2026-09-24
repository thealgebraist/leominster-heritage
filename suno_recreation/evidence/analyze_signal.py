import pathlib,json,numpy as np,librosa
from track_data import asset_stem
out=pathlib.Path('suno_recreation/evidence/signal');out.mkdir(exist_ok=True)
major=np.array([6.35,2.23,3.48,2.33,4.38,4.09,2.52,5.19,2.39,3.66,2.29,2.88]);minor=np.array([6.33,2.68,3.52,5.38,2.60,3.53,2.54,4.75,3.98,2.69,3.34,3.17])
for p in sorted(pathlib.Path('suno_recreation/evidence/audio').glob('*.wav')):
 y,sr=librosa.load(p,sr=22050); h,perc=librosa.effects.hpss(y)
 onset=librosa.onset.onset_strength(y=perc,sr=sr)
 tempo,beats=librosa.beat.beat_track(onset_envelope=onset,sr=sr)
 chroma=librosa.feature.chroma_stft(y=h,sr=sr).mean(axis=1)
 scores=sorted([(float(np.corrcoef(chroma,np.roll(prof,k))[0,1]),librosa.midi_to_note(60+k)[:-1]+' '+mode) for mode,prof in [('major',major),('minor',minor)] for k in range(12)],reverse=True)
 r={'duration_s':len(y)/sr,'beat_tracker_bpm':float(np.asarray(tempo).flat[0]),'beat_times_s':librosa.frames_to_time(beats,sr=sr).tolist(),'key_profile_candidates':scores[:5],'warning':'Mixed-audio beat/key heuristics, not a verified meter, tonic, chord sequence or vocal melody.'}
 (out/(asset_stem(p.stem)+'.json')).write_text(json.dumps(r,indent=2));print(p.stem,r['beat_tracker_bpm'],scores[:3],flush=True)
