from pathlib import Path
import json,time
import numpy as np,librosa,soundfile as sf
from track_data import TRACKS,asset_stem
r=Path(__file__).resolve().parent
for tr in TRACKS:
 y,sr=sf.read(r/'audio'/(tr['id']+'.wav'));y=y.mean(axis=1) if y.ndim>1 else y
 y=librosa.resample(y,orig_sr=sr,target_sr=8000);sr=8000
 tic=time.time();h,p=librosa.effects.hpss(y,margin=3.0)
 for label,z in [('mix',y),('harmonic',h)]:
  f0,voiced,prob=librosa.pyin(z,sr=sr,fmin=70,fmax=650,frame_length=1024,hop_length=128,fill_na=np.nan)
  ts=librosa.times_like(f0,sr=sr,hop_length=128)
  rms=librosa.feature.rms(y=z,frame_length=1024,hop_length=128)[0]
  keep=voiced&(prob>=.8)&(rms>max(.003,np.quantile(rms,.3)))
  pitches=librosa.hz_to_midi(f0)
  print(tr['id'],label,'kept',round(float(keep.mean()),3),'note',np.round(np.quantile(pitches[keep],[.1,.5,.9]),1).tolist() if keep.any() else None,flush=True)
  np.savetxt(r/'pitch'/(asset_stem(tr['id'])+'_'+label+'.csv'),np.column_stack([ts,f0,prob,keep]),delimiter=',',header='seconds,estimated_hz,voiced_probability,retained',comments='')
 (r/'pitch'/(asset_stem(tr['id'])+'_mix_check.json')).write_text(json.dumps({'method':'librosa pYIN, 8 kHz source mixture and HPSS harmonic component; f0 70-650 Hz; probability >=.8; RMS above 30th percentile/floor .003','warning':'Includes backing, which can dominate detected pitch; quantiles are candidate periodicities, not an established sung line.'},indent=2))
 print('elapsed',round(time.time()-tic,1),flush=True)
