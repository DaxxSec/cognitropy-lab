# Repertoire Comparison Memo

## Purpose

Compare two repertoires — two individuals, two populations, or recording-vs-reference — and classify their relationship (same individual, shared population, distinct dialect, distinct taxon). Use after `/build-repertoire` has cataloged both.

## Prompt Template

```
You are an avian bioacoustician comparing two song-type repertoires. Classify their relationship by shared structure, and keep individual variation, dialect, and taxonomy distinct.

Repertoire A:
- **Song-types & exemplars:** [LIST WITH KEY CHARACTERS]
- **Source:** [INDIVIDUAL / POPULATION / REFERENCE], [LOCALITY, DATE]

Repertoire B:
- **Song-types & exemplars:** [LIST WITH KEY CHARACTERS]
- **Source:** [INDIVIDUAL / POPULATION / REFERENCE], [LOCALITY, DATE]

Please:
1. Quantify overlap: shared song-types, shared elements, and structural similarity.
2. Classify the relationship (same idiolect / song-sharing neighbors / same dialect / different dialect / different taxon) with the evidence for each.
3. State sampling sufficiency — could the differences be undersampling of a large repertoire?
4. Recommend whether the difference carries any taxonomic weight or is purely infraspecific.
```

## Expected Output

- An overlap quantification (shared types/elements, similarity score)
- A classified relationship with supporting characters
- A sampling-sufficiency caveat
- A taxonomic-weight verdict (infraspecific vs needs-corroboration)
