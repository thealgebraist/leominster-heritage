import pathlib,json,mlx_whisper,soundfile as sf,numpy as np
from track_data import asset_stem
out=pathlib.Path('suno_recreation/evidence/asr_chunks');out.mkdir(exist_ok=True)
for name in ['Dc1uBZahhts','Dc8axxYIC3k','DcRZB_PBFkr','DcYTYvMBSMn','DcbYsWLhhdZ','DcqWhZtBIEI','DcvxvGDhSeb','DdLxzBIoJ8F','DdZlT3TIx3q']:
 y,sr=sf.read(f'suno_recreation/evidence/audio/{name}.wav');rows=[]
 for start in range(0,len(y),sr*8):
  if len(y)-start<sr:continue
  r=mlx_whisper.transcribe(np.array(y[max(0,start-sr//2):min(len(y),start+sr*8+sr//2)],dtype=np.float32),path_or_hf_repo='mlx-community/whisper-large-v3-turbo',language='en',word_timestamps=True,temperature=0,condition_on_previous_text=False)
  rows.append({'offset':max(0,start-sr//2)/sr,'result':r});print(name,start/sr,r['text'],flush=True)
 (out/(asset_stem(name)+'.json')).write_text(json.dumps(rows,indent=2))
