# /measure-acoustic-features

Extract the standardized character set that classification keys are built from. Measurement turns a picture into characters; characters are what you can key on and defend.

## Inputs

- Accession ID and its element inventory from `/segment-syllables`
- Spectrogram parameters (so measurements are reproducible)
- The measurement target: per-element-type, or whole-song summary, or both

## Steps

1. For each element type, measure **frequency** characters: peak frequency, low/high band edges (at a stated −dB threshold), bandwidth.
2. Measure **temporal** characters: element duration, inter-onset interval, syllable rate, and any pace trend (accelerating/decelerating).
3. Measure **modulation/structural** characters: FM slope and contour shape (rising/falling/V/flat/modulated), tonal vs broadband, harmonic presence.
4. Record **ranges**, not just point values, when multiple instances exist — keys built on means alone fail on the tails.
5. Flag any character likely biased by recording quality (e.g. high-frequency edge under low SNR) so the key can down-weight it.

## Output

`outputs/specimens/<accession-id>/measurements.md` — a character table per element type with values, ranges, units, and the −dB threshold and spectrogram settings used.

## Notes

- Prefer relative/structural characters (ratios, contour shapes, rhythm) over absolute frequency when SNR is poor — they travel better.
- Use the character names in `references.md` verbatim so measurements line up with the key.
