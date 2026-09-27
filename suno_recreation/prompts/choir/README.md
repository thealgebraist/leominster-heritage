# Choir prompts

Suno-ready choir arrangements recovered from this project’s user-visible prompt history and saved Hall House track files. Each prompt has a separate `lyrics.txt` and `styles.txt`. These are recovered prompts, not newly generated music.

| Folder | Arrangement | Lyrics chars | Styles chars | Provenance |
|---|---|---:|---:|---|
| [`01_door-knockers/`](./01_door-knockers/) | Door Knockers | 2,889 | 981 | Recovered from 2026-09-26 no-organ revision; one undoubled boy soprano until final choir. |
| [`02_echinus-entasis/`](./02_echinus-entasis/) | Echinus / Entasis | 2,906 | 984 | Recovered from 2026-09-26 no-organ revision; one undoubled boy soprano until final choir. |
| [`03_corbel-bargeboard/`](./03_corbel-bargeboard/) | Corbel / Bargeboard | 2,922 | 969 | Recovered from 2026-09-26 no-organ revision; one undoubled boy soprano until final choir. |
| [`04_hall-house-five-minute/`](./04_hall-house-five-minute/) | Hall House — five-minute church choir | 4,597 | 993 | Copied byte-for-byte from saved track-level prompt files; follows the separate hand-drawn curve. |
| [`05_den-anden-vej/`](./05_den-anden-vej/) | Den anden vej (Danish church song) | 2,552 | 695 | Recovered from 2026-09-26 Danish church-choir response. |

## Use in Suno

Paste `lyrics.txt` into Lyrics and `styles.txt` into Styles. Counts include spaces, punctuation and line breaks, but exclude an extra trailing newline. The three boy-soprano Styles fields are below 1,000 characters; Hall House is 993 characters. Timing and vocal behavior remain generation targets, not guarantees.

The Door Knockers, Echinus / Entasis, and Corbel / Bargeboard prompts reflect the later no-organ revision. “Den anden vej” is the Danish choir song requested after the Silent Spring work.
