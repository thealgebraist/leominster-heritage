import pathlib,json,html,re
from track_data import TRACKS
ROOT=pathlib.Path(__file__).resolve().parents[1]
MUSIC=json.loads((ROOT/'evidence/music_notes.json').read_text())
MANIFEST=json.loads((ROOT/'evidence/manifest.json').read_text())
SECTION_CHROMA=json.loads((ROOT/'evidence/section_tonality.json').read_text())
ROLLING_CHROMA=json.loads((ROOT/'evidence/rolling_tonality.json').read_text())
SOURCE={pathlib.Path(x['file']).stem:x.get('current_file',x['file']) for x in MANIFEST}
source_links=[];combined=['# Architectural music — complete recreation guide\n\nRead [README.md](README.md) for evidence limits and Suno instructions.\n']
for t in TRACKS:
 p=ROOT/'tracks'/t['slug'];p.mkdir(parents=True,exist_ok=True)
 m=MUSIC[t['id']]
 signal=json.loads((ROOT/'evidence/signal'/(t['id']+'.json')).read_text())
 tempo_data=next(x for x in json.loads((ROOT/'evidence/tempo_crosscheck.json').read_text()) if x['source']==t['id']+'.wav')
 tempo_candidates=tempo_data['candidates'][:3]
 tempo_line='Autocorrelation candidates: '+', '.join(f"{x['bpm']:.1f} BPM (peak score {x['correlation']:.2f})" for x in tempo_candidates)+'. These are relative peak scores, not probabilities; both tempo estimates use the same audio and cannot confirm one another independently.'
 keys=signal['key_profile_candidates'][:3]
 def spell(k):return k.replace('A♯','B♭').replace('D♯','E♭').replace('G♯','A♭').replace('C♯','D♭')
 keytext=', '.join(f'{spell(k)} ({s:.2f})' for s,k in keys)
 section_chroma=next(x for x in SECTION_CHROMA['tracks'] if x['id']==t['id'])
 chroma_rows='\n'.join(f"| {x['start_s']:.0f}–{x['end_s']:.0f}s | {x['original_mix_harmonic'][0]['label']} ({x['original_mix_harmonic'][0]['correlation']:.2f}) | {x['separated_backing_harmonic'][0]['label']} ({x['separated_backing_harmonic'][0]['correlation']:.2f}) |" for x in section_chroma['sections'])
 chroma_block=f"**Section-level chroma comparison:** {section_chroma['interpretation']} The table gives only each signal's top profile candidate; the full ranked candidates, method and caveats are in [section_tonality.json](../../evidence/section_tonality.json) and [section_tonality.py](../../evidence/section_tonality.py). Scores are correlations, not probabilities.\n\n| Time window | Original mix harmonic | Estimated backing harmonic |\n|---|---|---|\n{chroma_rows}"
 rolling_track=next((x for x in ROLLING_CHROMA['tracks'] if x['id']==t['id']),None)
 rolling_block=(f"**Overlapping-window sensitivity check:** {rolling_track['interpretation']} The check uses 4-second windows at 2-second hops, so it tests whether the 8-second result depends on one fixed cut; these overlapping windows are still not musical phrase boundaries. Full rankings and caveats: [rolling_tonality.json](../../evidence/rolling_tonality.json) and [rolling_tonality.py](../../evidence/rolling_tonality.py)." if rolling_track else '')
 descs=[json.loads(x.read_text()) for x in sorted((ROOT/'evidence/audio_descriptions').glob(t['id']+'_*.json'))]
 (p/'lyrics.txt').write_text(t['lyrics']+'\n')
 (p/'source_transcript.txt').write_text(t['title']+' — source transcript\nApproximate timings; uncertainty markers are not sung words.\n\n'+'\n'.join(a+'  '+b for a,b in t['transcript'])+'\n')
 substitutions={'flaunching':'flawn-ching','guttae':'guh-tay','bargeboard':'barj-board','mullion':'mul-yun','quatrefoil':'kat-er-foyl','quoin':'coin','finial':'fin-ee-ul','pilaster':'pih-las-tuh','Corinthian':'kuh-rin-thee-un','Ionic':'eye-on-ik','Palladio':'puh-lah-dee-oh','composite':'kum-poz-it','echinus':'eh-kye-nuhs','entasis':'en-tuh-sis','oriel':'or-ee-ul','Dumbledore':'Dum-buhl-daw'}
 phonetic=t['lyrics']
 for word,sound in substitutions.items():phonetic=re.sub(r'\b'+re.escape(word)+r'\b',sound,phonetic,flags=re.I)
 (p/'lyrics_phonetic.txt').write_text(phonetic+'\n')
 (p/'style.txt').write_text(m['style']+'\n')
 pron_note=('Cambridge lists UK echinus /ekˈaɪ.nəs/ and US /ɪˈkaɪ.nəs/; [Wiktionary records entasis /ˈɛntəsɪs/](https://en.wiktionary.org/wiki/entasis). These standard pronunciations are helpful targets, not proof of the recorded vowels.' if t['id']=='DcvxvGDhSeb' else 'Broad respellings are performance targets; they do not establish every vowel of the recorded accent.')
 pron='| Word / phrase | Broad sound / stress guide | Delivery and evidence |\n|---|---|---|\n'+'\n'.join('| '+' | '.join(x)+' |' for x in t['pronunciation'])
 (p/'pronunciation.md').write_text('# '+t['title']+' — pronunciation\n\nFor dictionary IPA targets for specialist terms (standard pronunciations, not claims about this singer), see [PRONUNCIATION_SOURCES.md](../../PRONUNCIATION_SOURCES.md).\n\nCAPITALS indicate stress; respellings are broad performance targets, not narrow IPA. “uh” is a weak vowel; “aw” is a long rounded vowel.\n\n'+('Cambridge lists UK echinus /ekˈaɪ.nəs/ and US /ɪˈkaɪ.nəs/; [Wiktionary records entasis /ˈɛntəsɪs/](https://en.wiktionary.org/wiki/entasis). These are dictionary targets, not proof of the recorded singer’s vowels.\n\n' if t['id']=='DcvxvGDhSeb' else '')+pron+'\n')
 transcript='| Approx. source time | Best-supported words / event |\n|---|---|\n'+'\n'.join('| '+a+' | '+b+' |' for a,b in t['transcript'])
 body=f'''# {t['title']}

Source: [{pathlib.Path(SOURCE[t['id']]).name}](../../../{SOURCE[t['id']]}) · **{t['duration']:.2f} seconds** · [extracted audio](../../evidence/audio/{t['id']}.wav)

## Listening/navigation aids

- [Waveform and onset-strength overview (navigation aid, not a score)](../../evidence/listen_cues/{t['id']}/waveform_onsets.png)
- [8-second source-audio excerpts with relative time ranges](../../evidence/listen_cues/{t['id']}/)

The excerpts are PCM slices from the existing mono analysis WAV. The plot shows amplitude and spectral onset strength; it does not establish notes, instrumentation, meter, or a transcription. Use the original stereo/video for final listening checks.

## Transcript and timing

{transcript}

Punctuation is editorial. Caption timing and sung-word timing can differ. Bracketed uncertainty notes above are not sung text.

## Pronunciation and vocal phrasing

{pron}

{pron_note} Capital letters indicate stress, not a request to shout.

## Music, tone, rhythm, and effects

**Voice and delivery — model interpretation:** {m['voice']}

**Melody and phrase shape:** {m['melody']}

**Rhythm:** {m['rhythm']} {tempo_line}

**Tonality and harmony:** {m['harmony']} Mixed-audio pitch-class profile candidates: {keytext}. These numbers are correlation scores, not probabilities. They are retained for experimentation, not stated as verified keys. An exact chord sequence and note-by-note melody have not been established.

{chroma_block}

{rolling_block}

**Instrumentation and timbre — model interpretation:** {m['instruments']}

**Production, sound effects, and edits:** {m['effects']}

**Arrangement recipe:** {t['recipe']}

## Source uncertainties and reconstruction choices

'''+ '\n'.join('- '+s for s in t['issues']) + f'''

The musical recipe adds explicit directions where the source analysis is incomplete. “Suggested” features are prompt-design choices, not recovered measurements. The copy-ready lyric file expands some repeated motifs to a practical arrangement and omits unresolved nonverbal passages; use the timed transcript as the evidence record.

## Paste into Suno: Styles

```text
{m['style']}
```

## Paste into Suno: Lyrics

```text
{t['lyrics']}
```

## Optional phonetic lyric variant

`lyrics_phonetic.txt` replaces specialist words with broad sound-based spellings. Use it only if ordinary spelling is mispronounced. These respellings are suggested generator inputs, not a certified transcription of the recorded phonemes.

## First comparison after generating

{m['check']}

## Audio-model evidence

Raw excerpt interpretations are preserved below as evidence links. They are not independent listening verification, and their incidental lyric guesses are not the corrected transcript. The recipe above prefers broad timbral descriptions when instrument identifications conflict.

'''
 stem=pathlib.Path(SOURCE[t['id']]).stem
 body+=f"- [Separated-backing interpretation](../../evidence/second_pass/{stem}_backing.json)\n"
 ocr=ROOT/'evidence/ocr_results'/(t['id']+'.json')
 frames=ROOT/'evidence/frames'/(t['id']+'.jpg')
 if ocr.exists():body+=f"- [Sampled-frame OCR results (automated and noisy)](../../evidence/ocr_results/{t['id']}.json)\n"
 if frames.exists():body+=f"- [Sampled source-frame contact sheet](../../evidence/frames/{t['id']}.jpg)\n"
 if (ROOT/'evidence/second_pass'/(t['id']+'_vocals.json')).exists():body+=f"- [Targeted vocal interpretation](../../evidence/second_pass/{t['id']}_vocals.json)\n"
 pitch=json.loads((ROOT/'evidence/pitch'/(t['id']+'.json')).read_text())
 body+=f"- [Pitch tracking diagnostic](../../evidence/pitch/{t['id']}.json): {pitch['retained_fraction']:.1%} of frames passed the strict voicing filter; too sparse to establish a complete melody.\n"
 vosk=ROOT/'evidence/asr_vosk'/(t['id']+'.json')
 if vosk.exists():body+=f"- [Independent small-model Vosk ASR output (raw; noisy)](../../evidence/asr_vosk/{t['id']}.json)\n"
 large_vosk=ROOT/'evidence/asr_vosk_large'/(t['id']+'.json')
 if large_vosk.exists():body+=f"- [Higher-capacity Vosk ASR output (raw; noisy)](../../evidence/asr_vosk_large/{t['id']}.json)\n"
 mix_pitch=ROOT/'evidence/pitch'/(t['id']+'_mix_check.json')
 if mix_pitch.exists():body+=f"- [Original-mix and harmonic pitch tracking diagnostic](../../evidence/pitch/{t['id']}_mix_check.json)\n"
 for d in descs:
  evidence_name=t["id"]+"_"+f"{int(d['start_s']):02d}"+".json"
  body+=f"- [{d['start_s']:.1f}–{d['end_s']:.1f}s model interpretation](../../evidence/audio_descriptions/{evidence_name})\n"
 (p/'analysis.md').write_text(body)
 source_links.append(f"| [{t['title']}](tracks/{t['slug']}/analysis.md) | `{t['id']}` | {t['duration']:.2f}s | [Styles](tracks/{t['slug']}/style.txt) · [Lyrics](tracks/{t['slug']}/lyrics.txt) · [Pronunciation](tracks/{t['slug']}/pronunciation.md) |")
 # Relative links in the combined guide need a different base.
 combined.append(body.replace('../../../account_mp4/','../account_mp4/').replace('../../evidence/','evidence/'))
(ROOT/'COMPLETE_GUIDE.md').write_text('\n\n---\n\n'.join(combined))
readme=(ROOT/'README.md').read_text().split('\n## Tracks\n')[0]
readme+='\n## Tracks\n\n| Track | Original file ID | Duration | Copy-ready files |\n|---|---|---:|---|\n'+'\n'.join(source_links)+'\n\n[Read the complete guide](COMPLETE_GUIDE.md) · [Open the listening and copying page](index.html)\n'
(ROOT/'README.md').write_text(readme)
# Offline HTML companion: source playback, evidence transcript, and copy-ready prompts.
def esc(s):return html.escape(s,quote=True)
parts=['''<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Architectural music — Suno recreation</title><style>
:root{color-scheme:light;--ink:#233135;--muted:#526267;--line:#d3dcdd;--accent:#1b6460}*{box-sizing:border-box}body{margin:0;background:#f5f5ef;color:var(--ink);font:16px/1.6 system-ui,sans-serif}main{max-width:1160px;margin:auto;padding:40px 28px}h1{font-size:clamp(28px,4vw,44px);line-height:1.15;margin:12px 0}h2{font-size:26px;margin:0 0 12px}h3{font-size:18px}p{max-width:850px}a{color:var(--accent)}nav{display:flex;flex-wrap:wrap;gap:8px;margin:24px 0}nav a{padding:7px 12px;background:white;border:1px solid var(--line);border-radius:6px;text-decoration:none}article{margin:32px 0;padding:26px;background:white;border:1px solid var(--line);border-radius:12px;scroll-margin-top:20px}.meta,.note{color:var(--muted);font-size:14px}.grid{display:grid;grid-template-columns:1fr 1fr;gap:24px}audio{width:100%;margin:12px 0}pre{white-space:pre-wrap;font:14px/1.6 ui-monospace,monospace;background:#f2f5f4;border:1px solid var(--line);padding:16px;border-radius:6px}button{background:var(--accent);color:white;border:0;border-radius:5px;padding:9px 13px;cursor:pointer}table{width:100%;border-collapse:collapse;font-size:14px}th,td{text-align:left;vertical-align:top;padding:10px 8px;border-bottom:1px solid var(--line)}td:first-child{white-space:nowrap}details{margin:16px 0}summary{cursor:pointer;font-weight:650}.flag{border-left:3px solid #b17825;padding:10px 16px;background:#fcf8ef}textarea{position:fixed;left:-9999px}@media(max-width:760px){main{padding:24px 14px}.grid{grid-template-columns:1fr}article{padding:18px}table{font-size:13px}td:first-child{white-space:normal}}
</style><main><div class="meta">8 CLIPS · SOURCE LYRICS + PRONUNCIATION + SUNO PROMPTS</div><h1>Architectural music</h1><p>Recreation recipes for the eight included videos. The door-knocker clip is excluded. Use the transcript to inspect the evidence and the separate prompt boxes to generate an approximation.</p><p class="flag">Audio descriptions and pronunciation details are model-assisted estimates, not a verified score. Exact repeated-word counts and a few phrases remain unresolved. Suno output has not been generated or tested. <a href="README.md">Read the evidence limits.</a></p><nav>''']
for t in TRACKS:parts.append(f'<a href="#{t["slug"]}">{esc(t["title"])}</a>')
parts.append('</nav>')
for t in TRACKS:
 m=MUSIC[t['id']];sid=t['slug'];parts.append(f'<article id="{sid}"><h2>{esc(t["title"])}</h2><div class="meta">{pathlib.Path(SOURCE[t["id"]]).name} · {t["duration"]:.2f}s · <a href="../{SOURCE[t["id"]]}">Original video</a> · <a href="tracks/{sid}/analysis.md">Full analysis</a></div><audio controls preload="none" src="evidence/audio/{t["id"]}.wav"></audio>')
 parts.append('<details><summary>Timed transcript and uncertainties</summary><table><thead><tr><th>Source time</th><th>Words / event</th></tr></thead><tbody>')
 for a,b in t['transcript']:parts.append(f'<tr><td>{esc(a)}</td><td>{esc(b)}</td></tr>')
 parts.append('</tbody></table><ul>'+''.join('<li>'+esc(x)+'</li>' for x in t['issues'])+'</ul></details>')
 parts.append('<details><summary>Pronunciation and delivery</summary><p class="note">CAPITALS mark stress. Broad respellings are performance targets, not narrow phonetic transcription.</p><table>')
 for a,b,c in t['pronunciation']:parts.append(f'<tr><td>{esc(a)}</td><td><strong>{esc(b)}</strong><br>{esc(c)}</td></tr>')
 parts.append('</table></details><details><summary>Music and effects</summary>')
 for k,label in [('voice','Voice'),('melody','Melody'),('rhythm','Rhythm'),('harmony','Tonality'),('instruments','Timbres'),('effects','Effects')]:parts.append(f'<p><strong>{label}:</strong> {esc(m[k])}</p>')
 parts.append('</details><div class="grid">')
 for key,title,text in [('style','Styles',m['style']),('lyrics','Lyrics',t['lyrics'])]:
  bid=sid+'-'+key;parts.append(f'<section><h3>{title}</h3><button type="button" data-copy="{bid}">Copy {title.lower()}</button><pre id="{bid}">{esc(text)}</pre></section>')
 parts.append('</div><p class="note">First comparison: '+esc(m['check'])+'</p></article>')
parts.append('''<p class="note">Prepared from the local source videos. <a href="COMPLETE_GUIDE.md">Complete Markdown guide</a> · <a href="evidence/manifest.json">Source manifest</a></p></main><script>
for(const button of document.querySelectorAll('[data-copy]')){button.addEventListener('click',async()=>{const text=document.getElementById(button.dataset.copy).textContent;try{await navigator.clipboard.writeText(text)}catch(e){const t=document.createElement('textarea');t.value=text;document.body.append(t);t.select();document.execCommand('copy');t.remove()}const old=button.textContent;button.textContent='Copied';setTimeout(()=>button.textContent=old,1500)})}
</script></html>''')
(ROOT/'index.html').write_text(''.join(parts))
print('Built',len(TRACKS),'track packets, complete guide and offline companion.')
