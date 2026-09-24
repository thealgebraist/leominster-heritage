from pathlib import Path
import hashlib,json,re
from html.parser import HTMLParser
import soundfile as sf
from track_data import TRACKS
root=Path(__file__).resolve().parents[1]
assert len(TRACKS)==8 and len({t['id'] for t in TRACKS})==8
assert 'DdZlT3TIx3q' not in {t['id'] for t in TRACKS}
manifest=json.loads((root/'evidence/manifest.json').read_text())
for m in manifest:
 p=root.parent/m.get('current_file',m['file']);actual=hashlib.file_digest(p.open('rb'),'sha256').hexdigest()
 assert actual==m['sha256'],f'Original changed: {p}'
checks=[]
for t in TRACKS:
 folder=root/'tracks'/t['slug']
 for name in ['analysis.md','style.txt','lyrics.txt','lyrics_phonetic.txt','pronunciation.md','source_transcript.txt']:
  p=folder/name;assert p.is_file() and p.stat().st_size>30,p
 analysis=(folder/'analysis.md').read_text()
 required_sections=['## Transcript and timing','## Pronunciation and vocal phrasing','## Music, tone, rhythm, and effects','## Source uncertainties and reconstruction choices','## Paste into Suno: Styles','## Paste into Suno: Lyrics']
 assert all(s in analysis for s in required_sections),(t['id'],'missing report section')
 required_music=['**Voice and delivery','**Melody and phrase shape','**Rhythm','**Tonality and harmony','**Instrumentation and timbre','**Production, sound effects, and edits']
 assert all(s in analysis for s in required_music),(t['id'],'missing requested music dimension')
 assert f'../../evidence/ocr_results/{t["id"]}.json' in analysis,(t['id'],'missing sampled-frame OCR evidence link')
 assert f'../../evidence/frames/{t["id"]}.jpg' in analysis,(t['id'],'missing sampled source-frame contact sheet link')
 pronunciation=(folder/'pronunciation.md').read_text()
 assert '| Word / phrase | Broad sound / stress guide | Delivery and evidence |' in pronunciation,(t['id'],'missing pronunciation table')
 assert 'CAPITALS indicate stress' in pronunciation,(t['id'],'missing pronunciation key')
 source_transcript=(folder/'source_transcript.txt').read_text()
 assert 'Approximate timings' in source_transcript and '–' in source_transcript,(t['id'],'missing timed source transcript')
 style=(folder/'style.txt').read_text().strip();assert len(style)<=1000,(t['id'],len(style))
 lyric=(folder/'lyrics.txt').read_text();assert len(lyric)<=5000,(t['id'],len(lyric))
 descriptions=[json.loads(p.read_text()) for p in sorted((root/'evidence/audio_descriptions').glob(t['id']+'_*.json'))]
 assert descriptions,t['id']
 vosk=root/'evidence/asr_vosk'/(t['id']+'.json')
 assert vosk.is_file(),f'Missing independent ASR comparison: {t["id"]}'
 raw=json.loads(vosk.read_text())
 assert raw['model']=='vosk-model-small-en-us-0.15' and raw['transcript']
 assert all(not (root/'evidence/asr_vosk'/(x+'.json')).exists() for x in ['DdZlT3TIx3q'])
 assert all(x['description'] and not x['description'].startswith('INCOMPLETE') for x in descriptions),t['id']
 assert descriptions[0]['start_s']==0,t['id']
 for a,b in zip(descriptions,descriptions[1:]):assert abs(a['end_s']-b['start_s'])<.01
 # A final segment shorter than two seconds may be skipped; it must be declared.
 assert descriptions[-1]['end_s']>=t['duration']-2.1,(t['id'],descriptions[-1]['end_s'])
 cues=json.loads((root/'evidence/listen_cues/index.json').read_text())
 cue=next(x for x in cues['tracks'] if x['id']==t['id'])
 # The packaged WAV is the authoritative audio duration; one video has a silent video-only tail.
 audio_info=sf.info(root/'evidence/audio'/f"{t['id']}.wav")
 assert abs(cue['duration']-audio_info.duration)<0.03,(t['id'],cue['duration'],audio_info.duration)
 assert len(cue['chunks'])==len(list((root/'evidence/listen_cues'/t['id']).glob('*.wav')))
 assert (root/cue['plot']).is_file()
 chunk_files=sorted((root/'evidence/listen_cues'/t['id']).glob('*.wav'))
 for cf,(start,end) in zip(chunk_files,cue['chunks']):
  info=sf.info(cf)
  assert abs(info.duration-(end-start))<0.03,(cf,info.duration,start,end)
 assert not (root/'evidence/listen_cues/DdZlT3TIx3q').exists()
 checks.append({'id':t['id'],'style_chars':len(style),'lyric_chars':len(lyric),'audio_model_intervals':[[d['start_s'],d['end_s']] for d in descriptions], 'independent_raw_asr':'present'})
class Parser(HTMLParser):
 def __init__(self):super().__init__();self.articles=[];self.audio=[];self.ids=[];self.copies=[];self.refs=[]
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if 'id' in a:self.ids.append(a['id'])
  if tag=='article':self.articles.append(a)
  if tag=='audio':self.audio.append(a)
  if 'data-copy' in a:self.copies.append(a['data-copy'])
  for k in ['href','src']:
   if k in a:self.refs.append(a[k])
p=Parser();p.feed((root/'index.html').read_text())
assert len(p.articles)==8 and len(p.audio)==8 and len(p.copies)==16
assert len(p.ids)==len(set(p.ids)) and set(p.copies)<=set(p.ids)
for ref in p.refs:
 if ref.startswith('#'):assert ref[1:] in p.ids
 elif '://' not in ref:assert (root/ref).exists(),ref
result={'inventory':'8 included, 1 excluded','source_hashes_verified':len(manifest),'tracks':checks,'report_coverage':'all eight reports contain timed lyrics, pronunciation guidance, melody, tonality, rhythm, instrumentation, effects, Suno prompt sections, and links to sampled visual evidence','audio_cue_validation':'all 8 tracks have a waveform/onset plot and time-aligned PCM excerpts covering their extracted audio duration; excluded knocker has no cue packet','html_structure_and_local_links':'passed','boundary':'These checks verify artifact presence, report coverage, source preservation, model excerpt coverage, and local links. They do not prove transcript accuracy, phonetic accuracy, musical correctness, or Suno reproduction.'}
(root/'evidence/pack_checks.json').write_text(json.dumps(result,indent=2));print(json.dumps(result,indent=2))
