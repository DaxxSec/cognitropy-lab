# Cryptic Complex Investigation

## Purpose

Use this prompt when a morphospecies keeps returning ambiguous or split barcode results and you suspect a cryptic species complex — to design and interpret a multi-locus, GCPSR-based investigation that decides "one variable species" vs "several cryptic ones."

## Prompt Template

```
You are a fungal systematist. Investigate whether this is a cryptic species complex.

The situation:

- **Candidate genus / morphospecies:** [VALUE]
- **Symptom:** [e.g. ITS returns 99% to two named species; morphology is uniform but barcode splits]
- **Specimens available:** [count, accessions, geographic/host spread]
- **Markers in hand / obtainable:** [ITS, TEF1-α, RPB2, BenA, ...]
- **Known references:** [ex-type sequences, prior revisions, UNITE SHs]

Please:
1. Choose the marker set that best resolves this genus and justify each locus.
2. Specify the alignment and tree-inference plan (within-genus alignment, model selection, ML + support).
3. Apply GCPSR: build single-locus genealogies and test for concordant, supported monophyly across loci.
4. Interpret the result: one variable species, multiple cryptic species, or reticulation/hybridization (locus conflict).
5. Map any cryptic lineages onto morphology, ecology, and geography for an integrative verdict.
6. State what would be needed to formally describe a new species, if warranted (type, epitype/ex-type sequence, registration).
```

## Expected Output

- A marker-set rationale and a concrete phylogenetic analysis plan.
- Single-locus genealogies and a GCPSR concordance verdict with support values.
- An integrative interpretation tying lineages to morphology/ecology/geography.
- A clear call: lump, split (with provisional lineage labels), or "reticulate — not resolvable as discrete species," plus the path to formal description if applicable.
