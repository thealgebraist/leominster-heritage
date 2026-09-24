"""Section-level chroma comparison on each source mix and separated backing.

This reports Krumhansl-style key-profile correlations over HPSS harmonic
chroma-CQT. It is exploratory: correlations are not probabilities and a key
profile is not a chord transcription or verified tonal center.
"""
from pathlib import Path
import json
import numpy as np
import librosa
import soundfile as sf
from track_data import TRACKS

ROOT = Path(__file__).resolve().parent
OUT = ROOT / 'section_tonality.json'
MAJOR = np.array([6.35,2.23,3.48,2.33,4.38,4.09,2.52,5.19,2.39,3.66,2.29,2.88])
MINOR = np.array([6.33,2.68,3.52,5.38,2.60,3.53,2.54,4.75,3.98,2.69,3.34,3.17])
ENHARMONIC_FLATS = {'C#':'D♭','D#':'E♭','F#':'G♭','G#':'A♭','A#':'B♭'}

def candidates(y, sr):
    chroma = librosa.feature.chroma_cqt(y=y, sr=sr).mean(axis=1)
    result = []
    for mode, profile in [('major', MAJOR), ('minor', MINOR)]:
        for shift in range(12):
            corr = np.corrcoef(chroma, np.roll(profile, shift))[0, 1]
            tonic = librosa.midi_to_note(60 + shift)[:-1]
            tonic = ENHARMONIC_FLATS.get(tonic, tonic)
            result.append({'label': f'{tonic} {mode}', 'correlation': float(corr)})
    return sorted(result, key=lambda x: x['correlation'], reverse=True)[:3]

interpretations = {
    'Dc1uBZahhts': 'The two 8-second windows disagree across the original mix and separated backing; no stable center is supported.',
    'Dc8axxYIC3k': 'G major ranks first in both signals through 0–16 s; the short ending window disagrees (C major in the mix, F major in the backing). Treat G as an early-section experiment, not a whole-track key.',
    'DcRZB_PBFkr': 'The leading profiles shift from G major to C major in the mix, and the final short window disagrees sharply between mix and backing. No single track-wide key is supported.',
    'DcYTYvMBSMn': 'E-flat/B-flat profile labels recur across most sections in both signals, while major/minor mode and the strongest member of that family vary. An E-flat/B-flat tonal palette is a more cautious prompt test than a single asserted key.',
    'DcbYsWLhhdZ': 'Both signals rank F minor first in 0–16 s, C minor in 16–32 s, then F minor through most of 32–64 s. This repeated section pattern supports testing an F-minor / C-minor contrast, but does not prove a chord progression or tonal function.',
    'DcqWhZtBIEI': 'G is the leading tonic label throughout nearly all lyric sections in both signals, but major/minor rankings switch. A G-centered backing with mode left flexible is a testable recreation choice.',
    'DcvxvGDhSeb': 'The opening favors G major; later windows are weaker and the original mix and separated backing disagree. No stable whole-track key is supported.',
    'DdLxzBIoJ8F': 'C minor ranks first in most windows, but scores are modest and the 8–16 s and ending windows vary. C-minor-leaning backing is an experiment, not a verified key.',
    'DdZlT3TIx3q': 'The mix and estimated backing have weak, closely ranked and changing candidates. No stable tonic or mode is supported; use the brisk speech-rhythm as the reconstruction anchor and leave key and chords flexible.'
}
tracks = []
for track in TRACKS:
    source_id = track['id']
    stem = 'bargeboard' if source_id == 'DcRZB_PBFkr' else source_id
    mix, mix_sr = sf.read(ROOT / 'audio' / f'{source_id}.wav')
    backing, backing_sr = sf.read(ROOT / 'stems' / f'{stem}_backing.wav')
    if mix.ndim > 1: mix = mix.mean(axis=1)
    if backing.ndim > 1: backing = backing.mean(axis=1)
    if mix_sr != 22050: mix = librosa.resample(mix, orig_sr=mix_sr, target_sr=22050)
    if backing_sr != 22050: backing = librosa.resample(backing, orig_sr=backing_sr, target_sr=22050)
    sr = 22050
    mix_harmonic, _ = librosa.effects.hpss(mix, margin=3.0)
    backing_harmonic, _ = librosa.effects.hpss(backing, margin=3.0)
    duration = min(len(mix), len(backing)) / sr
    sections = []
    for start in np.arange(0, duration, 8.0):
        end = min(start + 8.0, duration)
        if end - start < 2.0: continue
        lo, hi = int(start * sr), int(end * sr)
        sections.append({
            'start_s': round(float(start), 2), 'end_s': round(float(end), 2),
            'original_mix_harmonic': candidates(mix_harmonic[lo:hi], sr),
            'separated_backing_harmonic': candidates(backing_harmonic[lo:hi], sr),
        })
    tracks.append({'id': source_id, 'title': track['title'], 'interpretation': interpretations[source_id], 'sections': sections})

result = {
    'method': '8-second non-overlapping sections, mono 22.05 kHz; librosa HPSS harmonic component; mean chroma-CQT; Pearson correlation against rotated Krumhansl major/minor profiles.',
    'warnings': [
        'Key-profile correlation scores are relative correlations, not probabilities.',
        'The original mix includes vocals and effects; the backing stem is a Demucs estimate and may contain vocal leakage or separation artifacts.',
        'Short, repetitive or weakly pitched excerpts can yield unstable or relative-major/minor-confused candidates.',
        'Section boundaries are fixed analysis windows, not necessarily musical phrase boundaries.',
        'No candidate establishes exact chords, a tonic, mode, or sung melody.'
    ],
    'tracks': tracks,
}
OUT.write_text(json.dumps(result, indent=2))
for track in tracks:
    print(track['id'], track['title'])
    for section in track['sections']:
        mix_top = section['original_mix_harmonic'][0]
        backing_top = section['separated_backing_harmonic'][0]
        print(f"  {section['start_s']:.0f}-{section['end_s']:.0f}s mix={mix_top['label']} {mix_top['correlation']:.2f}; backing={backing_top['label']} {backing_top['correlation']:.2f}")
