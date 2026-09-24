import sys,json,pathlib,gc,re,time
import numpy as np,soundfile as sf,mlx.core as mx
from scipy.signal import resample_poly
from huggingface_hub import snapshot_download
from mlx_lm import load
from mlx_lm.generate import generate_step
from mlx_lm.sample_utils import make_sampler,make_logits_processors
repo='RumiLabs/MOSS-Audio-4B-Thinking-MLX-4bit';path=pathlib.Path(snapshot_download(repo,local_files_only=True,ignore_patterns=['.DS_Store']))
sys.path.insert(0,str(path/'scripts'))
from moss_audio_mlx_bridge_v3 import load_mlx_audio_path,run_mlx_audio_pipeline,install_deepstack_hooks
from moss_audio_mel_mlx import build_mel_and_input_ids
import moss_audio_mel_mlx as mel_module
filters=mx.array(np.load(path/'scripts/assets/mel_filters.npz')['mel_128']);mel_module._mel_filters=lambda:filters
model,tok=load(str(path/'mlx_llm'),tokenizer_config={'fix_mistral_regex':True})
enc,adapter,mergers=load_mlx_audio_path(path/'mlx_audio',int4=True);original_call=type(model.model).__call__
for job in json.load(open(sys.argv[1])):
 target=pathlib.Path(job['output']);target.parent.mkdir(exist_ok=True,parents=True)
 if target.exists():continue
 y,sr=sf.read(job['audio']);y=y.mean(axis=1) if y.ndim==2 else y
 a=job.get('start',0);b=job.get('end',len(y)/sr);clip=y[int(a*sr):int(b*sr)]
 if sr!=16000:
  import math
  g=math.gcd(sr,16000);clip=resample_poly(clip,16000//g,sr//g)
 clip=clip.astype(np.float32)
 if job.get('normalize',False):clip=clip/max(np.max(np.abs(clip)),.00001)*.85
 prompt=job['prompt']
 chat='<|im_start|>system\nYou are a helpful assistant.<|im_end|>\n<|im_start|>user\n<|audio_bos|><|AUDIO|><|audio_eos|>\n'+prompt+'<|im_end|>\n<|im_start|>assistant\n<think>\n\n</think>\n'
 mx.random.seed(42);mel,lens,ids,aid=build_mel_and_input_ids(clip,tok,prompt=chat,enable_time_marker=True)
 primary,ds=run_mlx_audio_pipeline(enc,adapter,mergers,mel,lens);primary=primary.astype(mx.bfloat16);ds=[d.astype(mx.bfloat16) for d in ds];mx.eval(primary,*ds)
 pos=np.where(np.array(ids[0])==aid)[0];assert len(pos)==primary.shape[1]
 arr=np.array(model.model.embed_tokens(ids).astype(mx.float32));arr[0,pos,:]=np.array(primary.astype(mx.float32))[0];merged=mx.array(arr).astype(mx.bfloat16)
 type(model.model).__call__=original_call;install_deepstack_hooks(model,[d[0] for d in ds],pos)
 gen=[];t=time.time()
 for token,_ in generate_step(prompt=ids[0],model=model,input_embeddings=merged[0],max_tokens=600,prefill_step_size=2048,sampler=make_sampler(temp=.8,top_p=.95,top_k=50),logits_processors=make_logits_processors(repetition_penalty=1.05,repetition_context_size=128)):
  gen.append(int(token))
  if int(token)==tok.eos_token_id:break
 text=re.sub(r'<think>.*?</think>','',tok.decode(gen),flags=re.S).replace('<|im_end|>','').strip()
 target.write_text(json.dumps({'job':job,'model':repo,'response':text,'generation_s':time.time()-t,'status':'machine interpretation; separated stems may contain artifacts'},indent=2))
 print(target.name,text,flush=True)
 type(model.model).__call__=original_call;del mel,lens,ids,primary,ds,merged,arr;gc.collect();mx.clear_cache()
