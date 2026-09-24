import pathlib,subprocess,json,concurrent.futures
from PIL import Image,ImageOps,ImageFilter
import numpy as np
from track_data import asset_stem
root=pathlib.Path('suno_recreation/evidence')
def ocr(p):
 a=np.array(Image.open(p).convert('RGB'));r,g,b=[a[:,:,i].astype(float) for i in range(3)]
 mask=(r>155)&(g>80)&(g<235)&(b<110)&(r>g*1.06)&(g>b*1.25)
 im=Image.fromarray(np.where(mask,0,255).astype('uint8')).filter(ImageFilter.MinFilter(3))
 import io
 f=io.BytesIO();im.save(f,format='PNG')
 result=subprocess.run(['tesseract','stdin','stdout','--psm','11'],input=f.getvalue(),capture_output=True)
 return {'time':(int(p.stem)-1)*.5,'text':result.stdout.decode().strip()}
for frames in sorted((root/'frames').iterdir()):
 if not frames.is_dir():continue
 with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:rows=list(pool.map(ocr,sorted(frames.glob('*.jpg'))))
 (root/'ocr_results'/(asset_stem(frames.name)+'_yellow.json')).write_text(json.dumps(rows,indent=2));print(frames.name,flush=True)
