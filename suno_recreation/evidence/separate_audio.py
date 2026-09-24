import pathlib,subprocess,json,time
import torch,torchaudio,numpy as np,soundfile as sf
from track_data import asset_stem
from torchaudio.pipelines import HDEMUCS_HIGH_MUSDB_PLUS
torch.set_num_threads(4)
model=HDEMUCS_HIGH_MUSDB_PLUS.get_model().eval()
sr=44100
root=pathlib.Path('suno_recreation/evidence/stems');root.mkdir(exist_ok=True)
for p in sorted(pathlib.Path('account_mp4').glob('*.mp4')):
 if (root/(p.stem+'_vocals.wav')).exists():continue
 raw=subprocess.check_output(['ffmpeg','-v','error','-i',str(p),'-vn','-ac','2','-ar',str(sr),'-f','f32le','-'])
 y=np.frombuffer(raw,dtype='<f4').reshape(-1,2).T.copy();mix=torch.from_numpy(y)
 ref=mix.mean(0);mean=ref.mean();std=ref.std().clamp_min(1e-8);norm=(mix-mean)/std
 n=mix.shape[1];out=torch.zeros(4,2,n);weight=torch.zeros(n);chunk=sr*8;overlap=sr
 t=time.time()
 with torch.inference_mode():
  for a in range(0,n,chunk-overlap):
   b=min(a+chunk,n);x=norm[:,a:b];pred=model(x[None])[0]
   w=torch.ones(b-a)
   if a>0:w[:min(overlap,b-a)]=torch.linspace(0,1,min(overlap,b-a))
   if b<n:w[-overlap:]=torch.linspace(1,0,overlap)
   out[:,:,a:b]+=pred*w;weight[a:b]+=w
 out=out/weight.clamp_min(1e-8);out=out*std
 # Share the DC component so all source estimates sum consistently.
 out=out+mean/4
 vocal=out[3].numpy();back=out[:3].sum(0).numpy()
 for label,arr in [('vocals',vocal),('backing',back)]:sf.write(root/(p.stem+'_'+label+'.wav'),arr.T,sr,subtype='PCM_16')
 residual=mix-out.sum(0)
 meta={'source':str(p),'model':'torchaudio HDEMUCS_HIGH_MUSDB_PLUS','sources':model.sources,'seconds':n/sr,'runtime_s':time.time()-t,'residual_rms':float(residual.square().mean().sqrt()),'mix_rms':float(mix.square().mean().sqrt()),'warning':'Estimated stems may leak voice into backing and instruments into vocals; not original multitracks.'}
 (root/(asset_stem(p.stem)+'.json')).write_text(json.dumps(meta,indent=2));print(p.stem,meta,flush=True)
