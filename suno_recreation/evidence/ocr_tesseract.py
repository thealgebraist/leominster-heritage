import pathlib,subprocess,json,concurrent.futures
root=pathlib.Path('suno_recreation/evidence')
def ocr(p):
 r=subprocess.run(['tesseract',str(p),'stdout','--psm','11'],capture_output=True,text=True)
 return {'time':(int(p.stem)-1)*.5,'text':r.stdout.strip()}
for p in sorted(pathlib.Path('account_mp4').glob('*.mp4')):
 if p.stem=='DdZlT3TIx3q':continue
 frames=root/'frames'/p.stem;frames.mkdir(exist_ok=True)
 subprocess.run(['ffmpeg','-v','error','-y','-i',str(p),'-vf','fps=2,scale=720:-2','-q:v','3',str(frames/'%04d.jpg')],check=True)
 with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:rows=list(pool.map(ocr,sorted(frames.glob('*.jpg'))))
 (root/'ocr_results'/(p.stem+'.json')).write_text(json.dumps(rows,indent=2))
 print(p.stem,flush=True)
