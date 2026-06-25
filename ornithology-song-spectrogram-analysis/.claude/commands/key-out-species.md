# /key-out-species

Run a dichotomous acoustic key on a measured recording, descending the biological hierarchy rank-by-rank and naming the diagnostic character at every split. This is the determination — the systematist keying a specimen.

## Inputs

- Accession ID with measurements from `/measure-acoustic-features`
- The applicable key (regional/family key from `outputs/keys/`, or build one with Workflow 2)
- A candidate shortlist (optional; e.g. a BirdNET suggestion to test, never to accept)

## Steps

1. **Coarse placement:** use robust structure (song vs call, trill/warble/whistle, element-type count) to enter the correct branch of the key.
2. At each node, read the **stated character**, compare the recording's measured value, and take the branch — recording which character and value decided it.
3. Continue until you reach a terminal taxon **or** a node where the recording's characters don't cleanly fall on one side.
4. If terminal: state the determination, the full key path (character at each split), and a confidence level.
5. If stuck: stop at the lowest confident rank (genus, species-pair, superspecies) and hand off to `/confusion-audit`; never force a species.

## Output

`outputs/specimens/<accession-id>/determination.md` — the taxon (or higher rank), the key path with the character cited at each branch, confidence, and the nearest confusable noted for the confusion check.

## Notes

- A determination is only as strong as its weakest cited character; if a split rested on a quality-biased character, say so and down-rank confidence.
- Suboscine/non-passerine voices are more reliably diagnostic (innate) than learned oscine song — weight accordingly.
