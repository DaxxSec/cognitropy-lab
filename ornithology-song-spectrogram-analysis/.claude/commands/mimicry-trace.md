# /mimicry-trace

For oscine mimics, attribute borrowed elements back to their model species. This is a cross-taxon classification problem: the singer is one taxon, but its phrases belong to many — and mis-attributing them invents species that aren't there.

## Inputs

- Accession ID of a known/suspected mimic (mockingbird, starling, marsh warbler, lyrebird, etc.)
- The element inventory (mimics recombine discrete borrowed units)
- A regional reference set of candidate model species' vocalizations

## Steps

1. Segment the song into discrete borrowed phrases (mimics typically repeat each a few times before switching — a useful diagnostic of mimicry itself).
2. For each phrase, match against the reference set by spectrographic cross-correlation and character comparison.
3. Attribute each phrase to its **model species** with a confidence, or mark it as the mimic's own / unattributable.
4. Distinguish *mimicry* from genuine presence: a faithfully reproduced but isolated, repeated phrase embedded in a mimic's stream is the singer, not the model bird being present.
5. Summarize the borrowed inventory and explicitly list species **not** to be logged as present despite appearing in the spectrogram.

## Output

`outputs/specimens/<accession-id>/mimicry-trace.md` — phrase-by-phrase attribution table, the "do not log as present" list, and the evidence the recording is a mimic.

## Notes

- The repeat-then-switch pattern is itself diagnostic of mimicry in several taxa — use it to flag mimic recordings before attribution errors propagate into survey data.
- Mimics can copy mechanical and other-animal sounds too; not every borrowed phrase has an avian model.
