from pathlib import Path
import json,hashlib
r=Path(__file__).resolve().parent
m=json.loads((r/'manifest.json').read_text())
for e in m:
 if e['file']=='account_mp4/DcRZB_PBFkr.mp4':
  current=r.parents[1]/'account_mp4/bargeboard.mp4'
  assert hashlib.file_digest(current.open('rb'),'sha256').hexdigest()==e['sha256']
  e['current_file']='account_mp4/bargeboard.mp4'
(r/'manifest.json').write_text(json.dumps(m,indent=2))
jobs=[]
for p in sorted((r/'stems').glob('*_backing.wav')):
 jobs.append(dict(audio=str(p),start=0,end=15,normalize=True,prompt='Describe only the audible backing music: rhythm, bass, pitched instruments, timbre and sound effects. Is the sound mainly electronic synthesizers, acoustic instruments, vocal noises, or a mixture? Do not invent lyrics or where the audio came from. State uncertainty when the instrument is unclear.',output=str(r/'second_pass'/(p.stem+'.json'))))
for id,a,b,question in [
 ('Dc1uBZahhts',0,12,'Transcribe the words, preserving repetitions. In particular, what is the phrase before "nicely keeping it dry"?'),
 ('Dc8axxYIC3k',0,20,'Transcribe the repeated words and any interjections. Describe how the main repeated word is pronounced.'),
 ('DcbYsWLhhdZ',23,29,'Transcribe any audible words in this short vocal passage. If the sound is a nonverbal vocalization rather than a clear word, say so.'),
 ('DcqWhZtBIEI',37,44,'Transcribe the words exactly, especially the word after "oriel".'),
 ('DcvxvGDhSeb',0,12,'Transcribe the words exactly, including specialist architectural terms if recognizable. Describe the pronunciation and stress of the repeated terms.')]:
 jobs.append(dict(audio=str(r/'stems'/(id+'_vocals.wav')),start=a,end=b,normalize=True,prompt=question+' Do not guess if unclear.',output=str(r/'second_pass'/(id+'_vocals.json'))))
(r/'second_pass_jobs.json').write_text(json.dumps(jobs,indent=2))
print('Verified renamed source by original SHA256. Prepared',len(jobs),'jobs.')
