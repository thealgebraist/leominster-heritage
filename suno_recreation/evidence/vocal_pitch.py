from pathlib import Path
import json,re,time
import numpy as np,librosa,soundfile as sf
from track_data import TRACKS
r=Path(__file__).resolve().parent
out=r/'pitch';out.mkdir(exist_ok=True)
for tr in TRACKS:
 target=out/(tr['id']+'.json')
 if target.exists():continue
 stem='bargeboard' if tr['id']=='DcRZB_PBFkr' else tr['id']
 y,sr=sf.read(r/'stems'/(stem+'_vocals.wav'));y=y.mean(axis=1)
 y=librosa.resample(y,orig_sr=sr,target_sr=8000);sr=8000
 tic=time.time()
 f0,voiced,prob=librosa.pyin(y,sr=sr,fmin=65,fmax=700,frame_length=1024,hop_length=128,fill_na=np.nan)
 ts=librosa.times_like(f0,sr=sr,hop_length=128)
 rms=librosa.feature.rms(y=y,frame_length=1024,hop_length=128)[0]
 keep=voiced&(prob>=.7)&(rms>max(.004,np.quantile(rms,.2)))
 mid=librosa.hz_to_midi(f0)
 np.savetxt(out/(tr['id']+'.csv'),np.column_stack([ts,f0,prob,keep]),delimiter=',',header='seconds,estimated_hz,voiced_probability,retained',comments='')
 phrases=[]
 for interval,words in tr['transcript']:
  a,b=map(float,interval.split('–'));s=(ts>=a)&(ts<b);k=s&keep
  rec={'time':interval,'words':words,'retained_seconds':round(float(k.sum()*.016),2),'retained_fraction':round(float(k.sum()/max(1,s.sum())),2)}
  if k.sum()>=10:
   q=np.quantile(mid[k],[.1,.5,.9]);rec['midi_p10_median_p90']=np.round(q,2).tolist();rec['nearest_notes_p10_median_p90']=librosa.midi_to_note(q).tolist()
  phrases.append(rec)
 result={'method':'pYIN on estimated vocal stem, 8kHz, 1024 frame, 128 hop, f0 65-700 Hz; retain voiced probability >=0.7 and audible RMS','warning':'Model-separated vocal may contain instruments; pYIN may choose octave errors and excludes unvoiced/uncertain frames. Quantiles describe retained frames, not scored melody or true vocal range.','retained_fraction':float(keep.mean()),'phrases':phrases,'runtime_s':time.time()-tic}
 target.write_text(json.dumps(result,indent=2));print(tr['id'],round(float(keep.mean()),3),round(time.time()-tic,1),flush=True)
