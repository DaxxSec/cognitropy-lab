# qa-rescan-report

## Purpose

Turn raw QA measurements (target-chart metrics + per-image findings) into a clear pass/rescan report that names the failing metric, groups rejects by root cause, and produces an actionable rescan worklist. Use after `/audit-image-quality` measures a batch, when communicating results to operators or stakeholders.

## Prompt Template

```
You are the imaging-QA lead writing a rescan report for a captured batch.

Inputs:

- **Batch / session ID:** [ID, DATE, STATION, OPERATOR]
- **Target standard & tolerances:** [FADGI ?★ / METAMORFOZE / ISO 19264 — KEY AIM VALUES]
- **Target-chart results:** [SFR/MTF50, OECF DEVIATION, ΔE MEAN/MAX, UNIFORMITY, NOISE]
- **Per-image findings:** [LIST OR TABLE: IMAGE ID → ISSUE — FOCUS, COLOR, CROP, ARTEFACT, MISSING ITEM]
- **Agreed batch reject threshold:** [E.G. 5%]

Please:
1. State the **batch verdict** (pass / fail) and why — distinguish systemic chart failure (whole session suspect) from scattered per-image defects.
2. Produce a **per-image pass/rescan table** with the specific failing metric for each reject.
3. **Group rejects by root cause** (focus, color/profile, illumination, framing, handling) and recommend one corrective action per group for the capture chain.
4. Compute the **reject rate** and flag it for the backlog forecast.
5. Output the **rescan worklist** ordered so the chain is corrected once before re-shooting.
```

## Expected Output

- A batch verdict that separates systemic from sporadic failure.
- A per-image rescan table keyed to the failing metric (auditable, not hand-wavy).
- A root-cause-grouped corrective-action list and a reject rate to feed `/forecast-backlog-drawdown`.
