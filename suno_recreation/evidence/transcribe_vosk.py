from pathlib import Path
import json,time,sys
import numpy as np,soundfile as sf
from vosk import Model, KaldiRecognizer, SetLogLevel
SetLogLevel(-1)
root=Path(__file__).resolve().parent
model_dir=Path(sys.argv[1]) if len(sys.argv)>1 else root/'vosk_model/vosk-model-small-en-us-0.15'
output_dir=root/(sys.argv[2] if len(sys.argv)>2 else 'asr_vosk')
model=Model(str(model_dir))
for p in sorted((root/'audio').glob('*.wav')):
 if p.stem=='DdZlT3TIx3q':continue
 target=output_dir/(p.stem+'.json');target.parent.mkdir(exist_ok=True)
 if target.exists():continue
 y,sr=sf.read(p)
 if y.ndim>1:y=y.mean(axis=1)
 assert sr==16000,(p,sr)
 pcm=np.clip(y*32768,-32768,32767).astype('<i2').tobytes()
 rec=KaldiRecognizer(model,sr);rec.SetWords(True)
 parts=[];t=time.time()
 for start in range(0,len(pcm),sr*2*2):
  if rec.AcceptWaveform(pcm[start:start+sr*2*2]):
   obj=json.loads(rec.Result());
   if obj.get('text'):parts.append(obj)
 obj=json.loads(rec.FinalResult())
 if obj.get('text'):parts.append(obj)
 result={'model':model_dir.name,'sample_rate':sr,'chunks':parts,'transcript':' '.join(x.get('text','') for x in parts),'runtime_s':round(time.time()-t,3),'provenance':'Offline recognizer, unconstrained vocabulary; raw hypothesis, not corrected.'}
 target.write_text(json.dumps(result,indent=2));print(p.stem,repr(result['transcript']),flush=True)
