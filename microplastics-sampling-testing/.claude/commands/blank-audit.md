# /blank-audit

Audit the contamination-control blanks and gate the batch. In microplastics work this is the single most important QA step — your own lab's airborne fibers are the most common "detection." The batch does not proceed to reported numbers until blanks pass.

## Inputs

- Blank set for the batch: procedural blanks (full method, no sample), field blanks (open container exposed in the field), and air/deposition blanks (wet filter exposed at the bench).
- Per-blank particle counts by polymer/morphology/size.
- Sample counts the blanks will correct.

## Steps

1. **Tally each blank tier** separately by morphology and polymer. Fibers are usually the dominant blank contaminant; track them apart from fragments.
2. **Compute the contamination limit of detection (LOD).** A common convention: LOD = mean blank + 3·SD of blanks (per particle category). Particles below LOD in samples are not distinguishable from background.
3. **Gate the batch.** If any blank tier's load exceeds the program threshold (e.g. blank fibers > X% of the lowest sample count, or > the method's stated acceptance), the batch is **quarantined** — flag it, do not report, and raise a maintenance/process check (often a degraded air filter, synthetic clothing at the bench, or contaminated reagents). See `/contamination-anomaly` and `prompts/contamination-incident-writeup.md`.
4. **Set the blank-correction vector** for batches that pass: per-category subtraction to apply in `/concentration-report`, plus the LOD floor below which counts are reported as "< LOD".
5. **Trend the blanks.** Append to the rolling blank history; a creeping blank load is an early predictive-maintenance signal (filter nearing end of life) — hand it to `/instrument-maintenance-forecast`.

## Output

A blank-audit record under `outputs/qa/blanks/<batch>.md`: per-tier blank tallies, computed LOD per category, the pass/quarantine verdict with reason, the blank-correction vector for passing batches, and the blank-trend update. A failed audit blocks `/screen-sample` and `/concentration-report` for the batch.
