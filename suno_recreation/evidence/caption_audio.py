import pathlib,json,soundfile as sf,numpy as np,gc,mlx.core as mx
from mlx_audio.stt.utils import load_model
model=load_model('mlx-community/Qwen2-Audio-7B-Instruct-4bit')
out=pathlib.Path('suno_recreation/evidence/audio_descriptions');out.mkdir(exist_ok=True)
prompt='Describe only what is audible in this music excerpt: singing voice and vocal delivery, instruments and timbres, rhythmic groove, melody movement, harmony or mood, production and any non-musical sound effects. Be specific and acknowledge uncertainty. Do not invent lyrics, instrument brands, precise BPM or key. Write one concise paragraph.'
for p in sorted(pathlib.Path('suno_recreation/evidence/audio').glob('*.wav')):
 if p.stem=='DdZlT3TIx3q':continue
 y,sr=sf.read(p); results=[]
 for start in range(0,len(y),sr*25):
  target=out/f'{p.stem}_{start//sr:02d}.json'
  if target.exists():continue
  clip=np.array(y[start:start+sr*25],dtype=np.float32)
  if len(clip)<sr*2:continue
  r=model.generate(clip,prompt=prompt,max_tokens=240,temperature=0)
  data={'source':p.name,'start_s':start/sr,'end_s':min(len(y),start+sr*25)/sr,'model':'mlx-community/Qwen2-Audio-7B-Instruct-4bit','prompt':prompt,'description':r.text,'status':'model inference, not direct human listening'}
  target.write_text(json.dumps(data,indent=2));print(target.name,r.text,flush=True)
  mx.clear_cache();gc.collect()
