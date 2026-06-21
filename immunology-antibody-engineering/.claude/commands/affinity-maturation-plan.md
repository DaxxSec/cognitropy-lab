# /affinity-maturation-plan

Design an affinity-maturation campaign to improve a lead antibody's KD — choose the diversification strategy, library design, and selection pressure, with a developability guardrail so gains in affinity don't cost manufacturability.

## Inputs

- Lead VH/VL and current KD / kon / koff (from `/binding-kinetics`).
- Affinity target and the limiting kinetic parameter (off-rate-limited vs on-rate-limited campaigns differ).
- Display platform available (phage, yeast, mammalian) and library-size ceiling.
- Hard constraints: epitope to preserve, format, and a developability floor (no new Red liabilities).

## Steps

1. Read `context/concepts.md` "Affinity maturation" and `context/workflows.md` "Loop B — engineering".
2. Pick the diversification strategy: targeted CDR libraries (NNK/NNS or trinucleotide soft-randomization of CDR-H3 + hotspots), chain shuffling, error-prone PCR, or in-silico/DMS-guided design — justify against the KD target and library ceiling.
3. Define the library: which positions, what codon scheme, theoretical vs practically-sampled diversity, and the oversampling factor needed to cover it.
4. Set the selection pressure: decreasing antigen concentration across rounds, off-rate (kinetic) selection with competitor for koff-limited campaigns, and counter-selection against off-target/poly-reactivity.
5. Specify the per-round readout (titer, pool KD by BLI, NGS of enriched clones) and the stop criterion; plan a deep-mutational-scanning arm if epistasis mapping is in scope.
6. Add the developability guardrail: every advancing clone re-runs `/sequence-liability-scan`; reject affinity wins that introduce CDR liabilities or aggregation risk.

## Output

- `outputs/maturation/<lead>-maturation-plan-<date>.md` — strategy rationale, library design table (positions, codons, diversity), round-by-round selection scheme, readouts, stop criterion, and the developability guardrail.
- Demonstrates competency: **affinity-maturation design**.

## Notes

- Affinity is often off-rate-limited; below ~100 pM, KD measurement itself becomes the bottleneck — plan the assay before the library.
- Maximizing affinity can hurt specificity and developability (the "affinity ceiling" beyond which gains are clinically meaningless and risks rise); set a *target*, not "as tight as possible".
- Epistasis means good single mutations don't always combine — plan a combinatorial confirmation round rather than stacking winners blindly.
