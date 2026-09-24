"""Overlapping chroma sensitivity check for Doors, Windows, and Columns.

Four-second windows at two-second hops reduce dependence on the fixed 8-second
bins used by section_tonality.py. They still are not musical phrase boundaries.
"""
from pathlib import Path
import json
import numpy as np
import librosa
import soundfile as sf
from track_data import TRACKS

ROOT = Path(__file__).resolve().parent
OUT = ROOT / 'rolling_tonality.json'
MAJOR = np.array([6.35,2.23,3.48,2.33,4.38,4.09,2.52,5.19,2.39,3.66,2.29,2.88])
MINOR = np.array([6.33,2.68,3.52,5.38,2.60,3.53,2.54,4.75,3.98,2.69,3.34,3.17])
FLATS = {'C#':'D♭','D#':'E♭','F#':'G♭','G#':'A♭','A#':'B♭'}
SELECT = {'DcYTYvMBSMn','DcbYsWLhhdZ','DcqWhZtBIEI'}
NOTES = {
 'DcYTYvMBSMn':'Overlapping windows repeatedly favor E-flat major, with B-flat major profiles recurring in the mix and in some backing windows. This strengthens an E-flat/B-flat major-leaning prompt experiment, but does not establish chords or harmonic function.',
 'DcbYsWLhhdZ':'Overlapping windows soften the exact change: both signals favor F minor in the opening, show a transition around 14–18 s, favor C-centered profiles around 18–28 s (minor/major labels vary), and return to F-minor-like profiles near 28–32 s. Later windows contain weaker local variations. This supports testing a tonal contrast, not a proven chord progression.',
 'DcqWhZtBIEI':'G minor ranks first for most overlapping windows in both signals; a brief G-major profile appears around 32–38 s in both signals, with another near 56–60 s. A G-minor-leaning prompt with brighter passages is a testable approximation; the outro is less stable.'
}

def top(chroma):
    rows=[]
    for mode,profile in [('major',MAJOR),('minor',MINOR)]:
        for shift in range(12):
            score=float(np.corrcoef(chroma,np.roll(profile,shift))[0,1])
            tonic=librosa.midi_to_note(60+shift)[:-1]
            tonic=FLATS.get(tonic,tonic)
            rows.append({'label':f'{tonic} {mode}','correlation':score})
    return sorted(rows,key=lambda x:x['correlation'],reverse=True)[:3]

tracks=[]
for track in TRACKS:
    if track['id'] not in SELECT: continue
    tid=track['id'];stem='bargeboard' if tid=='DcRZB_PBFkr' else tid
    signals={}
    for label,path in [('original_mix',ROOT/'audio'/f'{tid}.wav'),('estimated_backing',ROOT/'stems'/f'{stem}_backing.wav')]:
        y,sr=sf.read(path)
        if y.ndim>1:y=y.mean(axis=1)
        if sr!=22050:y=librosa.resample(y,orig_sr=sr,target_sr=22050)
        harmonic,_=librosa.effects.hpss(y,margin=3.0)
        hop=1024
        chroma=librosa.feature.chroma_cqt(y=harmonic,sr=22050,hop_length=hop)
        windows=[]
        for start in np.arange(0,max(0,len(y)/22050-4)+1e-9,2.0):
            lo=int(start*22050/hop);hi=min(chroma.shape[1],int((start+4)*22050/hop))
            if hi-lo<10:continue
            windows.append({'start_s':round(float(start),2),'end_s':round(float(start+4),2),'top':top(chroma[:,lo:hi].mean(axis=1))})
        signals[label]=windows
    tracks.append({'id':tid,'title':track['title'],'interpretation':NOTES[tid],'signals':signals})
result={'method':'HPSS harmonic component; 4-second windows, 2-second hop; mono 22.05 kHz; chroma-CQT mean compared by Pearson correlation with rotated Krumhansl major/minor profiles.','warnings':['Correlations are not probabilities.','These overlapping fixed windows are not phrase boundaries.','The estimated backing may contain leakage or separation artifacts; original mix includes vocals/effects.','This check reduces dependence on 8-second boundaries but does not establish keys, chords, harmonic function, or melody.'],'tracks':tracks}
OUT.write_text(json.dumps(result,indent=2))
for t in tracks:
 print(t['id'],t['title'])
 for i,(m,b) in enumerate(zip(t['signals']['original_mix'],t['signals']['estimated_backing'])):
  if m['start_s'] % 4 == 0:
   print(f" {m['start_s']:.0f}-{m['end_s']:.0f}: mix {m['top'][0]['label']} {m['top'][0]['correlation']:.2f}; backing {b['top'][0]['label']} {b['top'][0]['correlation']:.2f}")
