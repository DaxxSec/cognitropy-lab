# /segment-syllables

Decompose a continuous vocalization into the acoustic taxonomy's lower ranks — elements, syllables, phrases — and emit a labeled inventory. This is the morphology step: you are dissecting the specimen before classifying it.

## Inputs

- Accession ID from `/ingest-recording`
- The wideband spectrogram (short window — sharp onsets segment cleanly)
- Optional: a prior element-label scheme to stay consistent with a reference

## Steps

1. Mark element boundaries at onset/offset on the wideband view; an element is one unbroken trace.
2. Group co-occurring elements into **syllables** (the smallest repeated unit) and runs of syllables into **phrases/trills**.
3. Assign provisional element-type labels (a, b, c…), merging visually identical traces under one label.
4. Record the **sequence** (e.g. `intro-a a a b-trill c`) and the repetition rule (immediate vs eventual variety).
5. Tabulate counts: number of element types, syllables per song, phrases, and total duration.

## Output

`outputs/specimens/<accession-id>/element-inventory.md` — the labeled element list, the song's element-type sequence, and structural counts.

## Notes

- Beware over-segmentation: a single frequency-modulated element can look like several short ones at too-short a window, and a harmonic stack is one element, not many.
- Keep labels stable across recordings of the same taxon so repertoires and keys stay comparable.
