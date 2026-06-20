# /barcode-id

Identify a specimen from its ITS (and/or secondary-marker) sequence against UNITE and GenBank, returning a threshold-aware provisional determination with explicit confidence.

## Inputs

- Sequence file(s): `.ab1` traces or `.fasta`, plus the marker(s) sequenced and primers used.
- Accession number and the candidate taxon from `/morphology-key` (if available).
- Reference-database version (UNITE SH release; GenBank query date).

## Steps

1. Read `context/concepts.md` "Molecular markers" and "Barcode pitfalls".
2. QC the read: trim primers/low-quality ends, confirm expected length, screen for chimeras and contamination, and check protein-coding markers for stop codons/frameshifts (pseudogene artifacts).
3. Query UNITE (assign to a **Species Hypothesis**) and GenBank/BLAST; capture top hits with % identity, coverage, and reference reliability (ex-type / curated vs unverified).
4. Apply the identity → confidence prior from `context/references.md`, **down-weighting matches to unverified GenBank records**.
5. Reconcile against morphology: agreement raises confidence; conflict triggers a recommendation to escalate to `/phylogenetic-placement`.
6. If the genus is a low-ITS-resolution group and no secondary marker was run, recommend one before finalising.

## Output

- `outputs/determinations/<accession>-barcode.md` — marker(s), primers, QC summary, UNITE SH, top hits table, confidence, morphology reconciliation, and next-step recommendation.

## Notes

- A 100% match to a *mislabelled* reference is still wrong — never report a name without judging reference reliability.
- Report the UNITE SH (DOI-citable) alongside any binomial; SH assignment is more defensible than a raw % identity.
- ITS under-resolves in *Fusarium*, *Trichoderma*, *Cladosporium*, *Penicillium*, *Aspergillus*, *Colletotrichum* — do not settle a species there on ITS alone.
