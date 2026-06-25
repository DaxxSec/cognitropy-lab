# /build-repertoire

Assemble an individual's or species' song-type repertoire as a classified, deduplicated catalog. The repertoire is a taxon's vocal phenotype — the reference future recordings are matched against.

## Inputs

- A set of recordings of one individual (or one taxon), each with element inventories
- A song-type similarity threshold (when two songs count as the same type)
- Scope: individual repertoire vs population/species repertoire

## Steps

1. Compute pairwise similarity between songs (spectrographic cross-correlation or shared-element-sequence overlap).
2. Cluster songs into candidate **song-types**; pick the cut that matches the species' known variety pattern (immediate vs eventual variety).
3. For each song-type, designate a clean exemplar and record its element sequence and key characters.
4. Estimate repertoire size and note sampling sufficiency (a short recording undersamples large repertoires — state the floor).
5. Catalog each type with an ID, exemplar spectrogram, and the characters distinguishing it from its nearest type.

## Output

`outputs/repertoires/<taxon-or-individual>/catalog.md` — the enumerated song-types with exemplars, characters, repertoire-size estimate, and sampling caveat.

## Notes

- Repertoire size is a biased estimator under short recordings — report it as a minimum, with recording duration.
- Distinguish *individual* repertoire (idiolect) from *species* repertoire (the union across individuals); they answer different questions.
