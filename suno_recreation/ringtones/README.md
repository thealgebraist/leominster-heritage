# Ringtones

There is one short ringtone derived from each source video's original audio, in two formats:

- **Apple:** AAC-LC audio in an `.m4r` file, no longer than 30 seconds.
- **Android:** mono 44.1 kHz MP3, suitable to select as a local ringtone.

These are edited source clips, not Suno-generated recordings. Each clip starts at the beginning of the extracted audio and uses its opening vocal hook or verse. Clips shorter than 30 seconds retain their full audible duration; longer clips are cut at 30 seconds. A short fade-in and fade-out reduce abrupt edges, and loudness is normalized to a common target. Exact source intervals, output hashes, codec details, and decode results are recorded in [manifest.json](manifest.json).

| Video / track | Apple `.m4r` | Android `.mp3` | Duration |
|---|---|---|---:|
| [Flaunching](../tracks/01_flaunching/analysis.md) | [Download](apple/flaunching.m4r) | [Download](android/flaunching.mp3) | 15.81 s |
| [Guttae / Good Day](../tracks/02_guttae/analysis.md) | [Download](apple/guttae-good-day.m4r) | [Download](android/guttae-good-day.mp3) | 22.32 s |
| [Corbel / Bargeboard](../tracks/03_corbel_bargeboard/analysis.md) | [Download](apple/bargeboard.m4r) | [Download](android/bargeboard.mp3) | 30.00 s |
| [Columns / Classical Orders](../tracks/04_columns/analysis.md) | [Download](apple/columns-classical-orders.m4r) | [Download](android/columns-classical-orders.mp3) | 30.00 s |
| [Doors](../tracks/05_doors/analysis.md) | [Download](apple/doors.m4r) | [Download](android/doors.mp3) | 30.00 s |
| [Windows](../tracks/06_windows/analysis.md) | [Download](apple/windows.m4r) | [Download](android/windows.mp3) | 30.00 s |
| [Echinus / Entasis](../tracks/07_echinus_entasis/analysis.md) | [Download](apple/echinus-entasis.m4r) | [Download](android/echinus-entasis.mp3) | 22.50 s |
| [Hall House](../tracks/08_hall_house/analysis.md) | [Download](apple/hall-house.m4r) | [Download](android/hall-house.mp3) | 30.00 s |
| [Door Knockers](../tracks/09_door_knockers/analysis.md) | [Download](apple/door-knockers.m4r) | [Download](android/door-knockers.mp3) | 30.00 s |

On iPhone, Apple documents importing an audio file into GarageBand, selecting a section of up to 30 seconds, and exporting it as a ringtone; the `.m4r` version is prepared for ringtone use. [Apple's instructions](https://support.apple.com/en-us/120692). On Android, copy the MP3 to the device, then choose it in **Settings → Sound & vibration → Phone ringtone**, or use Files by Google to set the audio file as the ringtone. [Google Android instructions](https://support.google.com/android/answer/9082609) · [Files by Google instructions](https://support.google.com/files/answer/10018943).

To rebuild or verify the exports from the local extracted source audio, run `python3 evidence/make_ringtones.py` from the `suno_recreation` directory. It requires FFmpeg and FFprobe and performs a full decode check on every output.
