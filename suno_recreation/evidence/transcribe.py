import pathlib,json,mlx_whisper
from track_data import asset_stem
for p in sorted(pathlib.Path('suno_recreation/evidence/audio').glob('*.wav')):
 out=pathlib.Path('suno_recreation/evidence/asr')/(asset_stem(p.stem)+'.json');out.parent.mkdir(exist_ok=True)
 if out.exists():continue
 r=mlx_whisper.transcribe(str(p),path_or_hf_repo='mlx-community/whisper-large-v3-turbo',language='en',word_timestamps=True,temperature=0,condition_on_previous_text=False)
 out.write_text(json.dumps(r,indent=2));print(p.stem,r['text'],flush=True)
