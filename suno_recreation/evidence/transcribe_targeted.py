import mlx_whisper,soundfile as sf,numpy as np,json,pathlib
from track_data import asset_stem
jobs={'Dc1uBZahhts':[(0,8),(8,13)],'Dc8axxYIC3k':[(0,6),(6,12),(12,19)],'DcRZB_PBFkr':[(7,11),(10.5,15),(14.5,20),(19.5,25)],'DcbYsWLhhdZ':[(0,7.5),(7.5,13),(13,18),(18,24),(23,29),(28.5,35),(39,45),(44,50),(49,55),(55,63)],'DcqWhZtBIEI':[(38,43),(12,15)],'DcvxvGDhSeb':[(3.5,7),(9,12)],'DdLxzBIoJ8F':[(34,41)],'DdZlT3TIx3q':[(0,8),(7.5,16),(15.5,24),(23.5,32)]}
prompt='Architectural terms: flaunching, guttae, corbel, bargeboard, mullion, brace, quatrefoil, quoin, string course, buttress, finial, pilaster, Doric, Tuscan, Corinthian, Ionic, Palladio, entasis, echinus, glazing, fastener, sash cord, oriel, hall house, solar, cellar door.'
out=pathlib.Path('suno_recreation/evidence/asr_targeted');out.mkdir(exist_ok=True)
for name,ranges in jobs.items():
 y,sr=sf.read(f'suno_recreation/evidence/audio/{name}.wav');rows=[]
 for a,b in ranges:
  r=mlx_whisper.transcribe(np.array(y[int(a*sr):int(b*sr)],dtype=np.float32),path_or_hf_repo='mlx-community/whisper-large-v3-turbo',language='en',initial_prompt=prompt,word_timestamps=False,temperature=(0,.2,.4),condition_on_previous_text=False,compression_ratio_threshold=1.8)
  rows.append({'start':a,'end':b,'result':r});print(name,a,b,r['text'],flush=True)
 (out/(asset_stem(name)+'.json')).write_text(json.dumps(rows,indent=2))
