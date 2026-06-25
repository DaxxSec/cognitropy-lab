# /confusion-audit

Build and interrogate a confusion matrix between acoustically similar taxa. Where a key can't cleanly split a pair, the honest output is a *quantified confusion*, not a forced ID.

## Inputs

- A set of taxa that recur as confusables (cryptic pairs, convergent calls, mimic/model)
- Vouchered recordings for each, with measurements
- The key path that led to the confusion (from `/key-out-species`)

## Steps

1. Assemble the confusable set and tabulate every classification character side by side, with ranges.
2. Identify which characters overlap (non-diagnostic) and which (if any) separate the taxa.
3. Build a confusion matrix: classify each held-out reference and tally where determinations land vs truth.
4. For each off-diagonal confusion, record the character that *should* split the pair and why it failed here (quality, overlap, individual variation).
5. Recommend: a stronger discriminating character, a higher-rank stopping point, or "voice-indistinguishable — corroborate by other means."

## Output

`outputs/confusion/<taxon-set>/matrix.md` — the confusion matrix, the per-pair diagnostic-vs-overlapping character table, and the recommended stopping rank or new character.

## Notes

- A clean off-diagonal of zero across many recordings is the evidence that justifies a species-limit (split) argument; persistent confusion is evidence for lumping or for "voice not diagnostic."
- Keep this matrix versioned — it is the workspace's institutional memory of what voice can and cannot resolve.
