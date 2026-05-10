# /clr-transform

CLR/ILR-normalise a relative-abundance table; flag low-prevalence taxa.

## Inputs

- Path to a count table (samples × taxa, with sample metadata in a separate file or columns).
- Choice of CLR (general-purpose) vs. ILR (when balances between known taxonomic groups matter).
- Prevalence-filter threshold (default: present in ≥10% of samples at ≥0.01% relative abundance).
- Pseudo-count strategy (default: 0.5; alternative: `zCompositions` imputation).

## Steps

1. Read `context/workflows.md` "Compositional Normalisation".
2. Read the count table; report dimensions and zero count.
3. Apply the prevalence filter; record what was dropped (count + which taxa).
4. Add the pseudo-count or impute zeros via `zCompositions::cmultRepl`.
5. Apply the chosen transform: CLR (subtract row geometric-mean log) or ILR (build a sequential binary partition or a taxonomy-aware partition).
6. Report the resulting matrix dimensions, the row-sum sanity check (should equal log(n_taxa) for CLR), and any warnings about sparse rows.
7. Write the transformed table to `outputs/normalisation/clr-YYYY-MM-DD.csv` or `.tsv`.

## Output

Two artifacts:
- `outputs/normalisation/clr-YYYY-MM-DD.csv` — the transformed table.
- `outputs/normalisation/log-YYYY-MM-DD.md` — record of: input dimensions, prevalence filter applied, taxa dropped, pseudo-count strategy, transform used, output dimensions, and any anomalies flagged.

## Notes

- Never run linear models, distance calculations, or Mann-Kendall on raw relative abundances — the compositionality bias will fool every test.
- If absolute counts (qPCR total 16S, flow cytometry, spike-ins) are available, run `/clr-transform` AND a parallel absolute-anchored analysis; flag disagreements.
- Rarefaction is a robustness check, not a primary fix — apply it after CLR analysis to confirm trends survive.
- For taxonomic-group-balance questions (e.g. "did the bacteria-to-fungi ratio shift?"), prefer ILR with a deliberate partition over CLR.
