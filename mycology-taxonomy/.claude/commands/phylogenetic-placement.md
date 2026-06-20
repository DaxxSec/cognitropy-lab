# /phylogenetic-placement

Place a query sequence in a curated reference phylogeny to resolve clade membership when the barcode is ambiguous, and apply GCPSR to test for cryptic species.

## Inputs

- Query sequence(s) for one or more markers (ITS plus a secondary marker such as TEF1-α / RPB2 for species-boundary work).
- Candidate genus and the conflict/ambiguity that triggered escalation (from `/barcode-id`).
- Optional: an existing reference alignment / backbone tree for the genus.

## Steps

1. Read `context/concepts.md` "Phylogenetic placement basics" and `context/workflows.md` "Phase 4".
2. Assemble a reference set: ex-type sequences + closest UNITE Species Hypotheses for the candidate genus; record accessions and sources.
3. Align within-genus (MAFFT, L-INS-i for small sets); trim ambiguous regions for protein-coding markers.
4. Select a model (ModelFinder) and infer an ML tree (IQ-TREE, ≥1000 ultrafast bootstraps), or place the query on the fixed backbone with EPA-ng for routine ID.
5. For a species boundary: build single-locus trees for ITS + ≥1 secondary marker and apply **GCPSR** — a concordant, supported monophyletic clade across loci is a species; conflict between supported loci signals reticulation/hybridization, not a new species.
6. Report placement, support values (UFBoot/posterior), and whether the result confirms, splits, or refutes the barcode call.

## Output

- `outputs/phylogenies/<accession>/` — alignment(s), tree file(s) (Newick), inference settings, and a `placement.md` summary with support values, GCPSR verdict, and cryptic-species assessment.

## Notes

- Do not align ITS across distant taxa — it is unreliable beyond genus level; restrict alignments to within the candidate genus.
- A single highly-supported clade across independent loci is the bar for "species"; one locus is suggestive, not conclusive.
- If the query falls outside all named clades with support, flag a candidate **novel taxon** for the determination dossier rather than forcing a binomial.
