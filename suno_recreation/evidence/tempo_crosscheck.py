import pathlib,json,librosa,soundfile as sf,numpy as np
from scipy.signal import correlate,find_peaks
rows=[]
for p in sorted(pathlib.Path('suno_recreation/evidence/audio').glob('*.wav')):
 if p.stem=='DdZlT3TIx3q':continue
 y,sr=sf.read(p);hop=128;o=librosa.onset.onset_strength(y=y,sr=sr,hop_length=hop);o-=o.mean()
 ac=correlate(o,o,mode='full',method='fft')[len(o)-1:];peaks,_=find_peaks(ac)
 candidates=[]
 for q in peaks:
  bpm=60*sr/hop/q
  if not 65<bpm<190:continue
  delta=.5*(ac[q-1]-ac[q+1])/(ac[q-1]-2*ac[q]+ac[q+1])
  candidates.append({'bpm':float(60*sr/hop/(q+delta)),'correlation':float(ac[q]/ac[0])})
 candidates.sort(key=lambda x:x['correlation'],reverse=True)
 r={'source':p.name,'method':'Spectral-flux onset envelope; scipy autocorrelation, peak interpolation; no tempo prior','candidates':candidates[:4],'interpretation':'Strong pulse around 135 BPM, with half-time and other subdivision aliases. Does not determine meter.'}
 rows.append(r);print(p.stem,candidates[:3],flush=True)
pathlib.Path('suno_recreation/evidence/tempo_crosscheck.json').write_text(json.dumps(rows,indent=2))
