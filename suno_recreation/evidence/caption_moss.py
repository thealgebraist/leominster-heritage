import sys,json,pathlib,gc,re,time
import numpy as np,soundfile as sf,mlx.core as mx
from huggingface_hub import snapshot_download
from mlx_lm import load
from mlx_lm.generate import generate_step
from mlx_lm.sample_utils import make_sampler,make_logits_processors
repo='RumiLabs/MOSS-Audio-4B-Thinking-MLX-4bit'
path=pathlib.Path(snapshot_download(repo,local_files_only=True,ignore_patterns=['.DS_Store']))
sys.path.insert(0,str(path/'scripts'))
from moss_audio_mlx_bridge_v3 import load_mlx_audio_path,run_mlx_audio_pipeline,install_deepstack_hooks
from moss_audio_mel_mlx import build_mel_and_input_ids
model,tok=load(str(path/'mlx_llm'),tokenizer_config={'fix_mistral_regex':True})
import moss_audio_mel_mlx as mel_module
# MLX's compressed-NPZ loader fails on this bundled asset; NumPy reads the same array.
mel_filters=mx.array(np.load(path/'scripts/assets/mel_filters.npz')['mel_128'])
mel_module._mel_filters=lambda:mel_filters
# The bundled processor inserts trained audio token IDs directly; its text tokenizer does not expose their names.
enc,adapter,mergers=load_mlx_audio_path(path/'mlx_audio',int4=True)
original_call=type(model.model).__call__
out=pathlib.Path('suno_recreation/evidence/audio_descriptions');out.mkdir(exist_ok=True)
prompt='Describe the audible music in this excerpt: voice characteristics and accent if identifiable, singing versus rhythmic speech, instruments and timbres, beat and groove, melodic contour, harmonic mood, production effects, and any non-musical sound effects. Do not invent exact notes, key, tempo, lyrics, or unseen context. State uncertainty. Give a concise but specific description.'
chat_prompt='<|im_start|>system\nYou are a helpful assistant.<|im_end|>\n<|im_start|>user\n<|audio_bos|><|AUDIO|><|audio_eos|>\n'+prompt+'<|im_end|>\n<|im_start|>assistant\n<think>\n\n</think>\n'
for p in sorted(pathlib.Path('suno_recreation/evidence/audio').glob('*.wav')):
 if p.stem=='DdZlT3TIx3q':continue
 y,sr=sf.read(p)
 for start in range(0,len(y),sr*24):
  target=out/f'{p.stem}_{start//sr:02d}.json'
  if target.exists() and not json.loads(target.read_text())['description'].startswith('INCOMPLETE'):continue
  clip=np.array(y[start:start+sr*24],dtype=np.float32)
  if len(clip)<sr*2:continue
  mx.random.seed(42)
  mel,lens,ids,aid=build_mel_and_input_ids(clip,tok,prompt=chat_prompt,enable_time_marker=True)
  primary,ds=run_mlx_audio_pipeline(enc,adapter,mergers,mel,lens)
  primary=primary.astype(mx.bfloat16);ds=[d.astype(mx.bfloat16) for d in ds];mx.eval(primary,*ds)
  positions=np.where(np.array(ids[0])==aid)[0]
  assert len(positions)==primary.shape[1], (len(positions),primary.shape)
  arr=np.array(model.model.embed_tokens(ids).astype(mx.float32));arr[0,positions,:]=np.array(primary.astype(mx.float32))[0]
  merged=mx.array(arr).astype(mx.bfloat16)
  type(model.model).__call__=original_call
  install_deepstack_hooks(model,[d[0] for d in ds],positions)
  generated=[];t=time.time()
  for token,_ in generate_step(prompt=ids[0],model=model,input_embeddings=merged[0],max_tokens=600,prefill_step_size=2048,sampler=make_sampler(temp=1.0,top_p=1.0,top_k=50),logits_processors=make_logits_processors(repetition_penalty=1.08,repetition_context_size=256)):
   generated.append(int(token))
   if int(token)==tok.eos_token_id:break
  raw=tok.decode(generated)
  desc=re.sub(r'<think>.*?</think>','',raw,flags=re.S).replace('<|im_end|>','').strip()
  if '</think>' not in raw and '<think>' in raw:desc='INCOMPLETE RESPONSE: no final answer before token limit.'
  data={'source':p.name,'start_s':start/sr,'end_s':min(len(y),start+sr*24)/sr,'model':repo,'prompt':prompt,'description':desc,'raw_output':raw,'status':'model inference, not direct listening by assistant','generation_s':time.time()-t}
  target.write_text(json.dumps(data,indent=2));print(target.name,desc,flush=True)
  type(model.model).__call__=original_call
  del mel,lens,ids,primary,ds,merged,arr;gc.collect();mx.clear_cache()
