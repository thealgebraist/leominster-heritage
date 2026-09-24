#!/usr/bin/env python3
"""Build verified Apple (.m4r) and Android (.mp3) ringtones for every track."""
from __future__ import annotations

import hashlib
import json
import subprocess
from pathlib import Path

from track_data import TRACKS, asset_stem

ROOT = Path(__file__).resolve().parent.parent
EVIDENCE = ROOT / 'evidence'
OUT = ROOT / 'ringtones'
MAX_SECONDS = 30.0
FADE_IN = 0.06
FADE_OUT = 0.45
# Shorter tracks use the complete audible clip. Longer tracks use the opening
# musical hook/verse, which is the most recognizable and lyric-rich section.
STARTS = {t['id']: 0.0 for t in TRACKS}


def run(args: list[str]) -> str:
    return subprocess.run(args, check=True, capture_output=True, text=True).stdout


def probe(path: Path) -> dict:
    return json.loads(run([
        'ffprobe', '-v', 'error', '-show_entries',
        'format=duration,format_name:stream=codec_name,codec_type,sample_rate,channels',
        '-of', 'json', str(path),
    ]))


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open('rb') as f:
        for block in iter(lambda: f.read(1024 * 1024), b''):
            h.update(block)
    return h.hexdigest()


def main() -> None:
    (OUT / 'apple').mkdir(parents=True, exist_ok=True)
    (OUT / 'android').mkdir(parents=True, exist_ok=True)
    records = []
    for track in TRACKS:
        source = EVIDENCE / 'audio' / f"{track['id']}.wav"
        source_duration = float(probe(source)['format']['duration'])
        start = STARTS[track['id']]
        duration = min(MAX_SECONDS, max(0.0, source_duration - start))
        if duration < 1.0:
            raise RuntimeError(f'{source}: only {duration:.3f}s available')
        fade_out_start = max(0.0, duration - FADE_OUT)
        fade_out_len = min(FADE_OUT, duration)
        filters = (
            'loudnorm=I=-16:TP=-1.5:LRA=11,'
            f'afade=t=in:st=0:d={min(FADE_IN, duration / 4):.3f},'
            f'afade=t=out:st={fade_out_start:.3f}:d={fade_out_len:.3f}'
        )
        stem = asset_stem(track['id'])
        outputs = [
            (OUT / 'apple' / f'{stem}.m4r', [
                '-c:a', 'aac', '-profile:a', 'aac_low', '-b:a', '128k',
                '-ar', '44100', '-ac', '1', '-f', 'ipod',
            ]),
            (OUT / 'android' / f'{stem}.mp3', [
                '-c:a', 'libmp3lame', '-b:a', '128k', '-ar', '44100', '-ac', '1',
            ]),
        ]
        item = {
            'source_id': track['id'], 'title': track['title'], 'asset_stem': stem,
            'source': f'evidence/audio/{track["id"]}.wav',
            'start_s': start, 'duration_s': round(duration, 3),
            'fade_in_s': round(min(FADE_IN, duration / 4), 3),
            'fade_out_s': round(fade_out_len, 3),
            'loudness_target_i_lufs': -16, 'true_peak_limit_db': -1.5,
            'outputs': [],
        }
        for path, codec_args in outputs:
            cmd = [
                'ffmpeg', '-hide_banner', '-loglevel', 'error', '-y',
                '-ss', f'{start:.3f}', '-i', str(source), '-t', f'{duration:.3f}',
                '-vn', '-sn', '-dn', '-map_metadata', '-1', '-af', filters,
                *codec_args, str(path),
            ]
            run(cmd)
            info = probe(path)
            stream = next(s for s in info['streams'] if s['codec_type'] == 'audio')
            actual = float(info['format']['duration'])
            # MP3 encoder delay/padding can shorten the probed presentation by
            # roughly one frame even though the full stream decodes correctly.
            if actual > MAX_SECONDS + 0.03 or abs(actual - duration) > 0.15:
                raise RuntimeError(f'{path}: duration {actual:.3f}s, expected {duration:.3f}s')
            run(['ffmpeg', '-hide_banner', '-v', 'error', '-xerror', '-i', str(path), '-f', 'null', '-'])
            item['outputs'].append({
                'path': str(path.relative_to(ROOT)), 'codec': stream['codec_name'],
                'sample_rate': int(stream['sample_rate']), 'channels': int(stream['channels']),
                'duration_s': round(actual, 3), 'size_bytes': path.stat().st_size,
                'sha256': sha256(path), 'full_decode': 'passed',
            })
        records.append(item)
        print(f"{track['title']}: {duration:.2f}s, Apple AAC and Android MP3 verified", flush=True)
    manifest = {
        'description': 'Original source-video audio edited into short ringtone clips; not Suno-generated audio.',
        'apple_format': 'AAC-LC in .m4r / MPEG-4 container; <=30 seconds.',
        'android_format': 'MP3, 44.1 kHz mono; suitable as a local ringtone audio file.',
        'processing': 'Integrated loudness target -16 LUFS, true-peak limit -1.5 dBTP, 60 ms fade-in and 450 ms fade-out.',
        'tracks': records,
    }
    (OUT / 'manifest.json').write_text(json.dumps(manifest, indent=2) + '\n')
    print(f'Wrote {len(records) * 2} verified ringtone files and manifest.')

if __name__ == '__main__':
    main()
