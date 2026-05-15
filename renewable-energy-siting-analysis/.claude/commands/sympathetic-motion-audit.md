# /sympathetic-motion-audit

Flag siting choices that produce **unwanted correlated ramping** across joints — two wind farms in one resource shed, two solar sites under one cloud cell — and quantify the resulting penalty to portfolio Effective Load Carrying Capability (ELCC). In puppet terminology: when one articulator moves and another moves *with it* unintentionally, the rig is sympathetically wired and the choreography breaks down.

## Inputs

- `project_id` — articulation graph identifier.
- `shed_groups` — joint-to-shed mapping from `/articulate-portfolio` (joints sharing a MERRA-2 cell or proximity radius).
- `centerlines` — hourly resource series for each joint (output of `/centerline-resource-walk`).
- `correlation_window` — `hourly | 10min | 5min`. Hourly is sufficient for ELCC purposes; sub-hourly matters for ancillary services.
- `external_portfolio` — *other developers' assets in the same shed* if data is available (queue cluster public information, FERC EQR data, EIA Form 860). Counted as "shadow joints" for cumulative-shed analysis.

## Steps

1. **Audit intake (`Y-0`).** Verify centerlines exist for every joint, sheds are assigned, and hourly resolution is available. Abort with REWORK at Y-0 on missing inputs.
2. **Walk `Y-1` — within-portfolio correlation.** For each shed with ≥2 portfolio joints, compute the Pearson and Spearman correlation of *normalised* hourly output over a full year. Normalised = `output / nameplate`, so the correlation reflects shape, not scale. Flag pairs with ρ > 0.6.
3. **Walk `Y-2` — capacity-coincident correlation.** Restrict to the top-100 net-load hours of the year (the ELCC-relevant hours). Recompute ρ. This is the correlation that matters for capacity credit; high annual-ρ but low capacity-coincident-ρ is *acceptable* (the joints diversify when it counts).
4. **Walk `Y-3` — drought-year correlation.** Repeat Y-1 and Y-2 over the worst resource year in the record. Sympathetic motion is worst when resources are scarce — joints drop together precisely when the system needs them.
5. **Walk `Y-4` — cumulative shed analysis.** Add the external portfolio's "shadow joints" to the correlation. The marginal ELCC of your project's joints in a shed is a function of *all* the nameplate in that shed, not just yours.
6. **ELCC penalty quantification.** For each high-ρ pair, compute the ELCC penalty:
   - Conservative (most defensible): use the ISO's published shed-saturation curve (Table R-4 in `context/references.md`) — the marginal ELCC class rating declines as installed shed nameplate rises.
   - Higher-fidelity: rerun the production-cost model with the joints decorrelated (shuffle their hours) and recompute ELCC; the delta is the sympathetic-motion penalty.
7. **Walk `Y-5` — site-shift candidates.** For each pair flagged at REWORK or REJECT, identify alternative siting that breaks the shed (a different MERRA-2 cell, a different cloud-cover band, a different river basin). The shift target is `ρ_target < 0.3` at capacity-coincident hours.
8. **Aggregate `Y-6`.** Emit a pair correlation table, per-pair ELCC penalty, and portfolio-level adjusted capacity credit.
9. Save to `outputs/<project_id>/sympathetic-motion-<YYYYMMDD>.md`.

## Output

Markdown audit containing:

- Within-portfolio correlation matrix (annual and capacity-coincident).
- Cumulative-shed correlation including external developers' shadow joints.
- ELCC penalty table per pair (`pair, ρ_annual, ρ_capcoin, ELCC_solo, ELCC_paired, penalty_pct`).
- Drought-year correlation deltas.
- Site-shift suggestions where applicable.
- Aggregate portfolio capacity-credit adjustment (the number that flows into `/lead-follow-pairing` step 6).
- Reproducibility footer.

## Notes

- Sympathetic motion is the *silent* ELCC killer. A developer who sites three wind farms 18 km apart in flat terrain and signs three identical PPAs at the same capacity-credit assumption is going to find the third farm earning a third of the credit of the first by year 3 of the capacity market.
- Solar sympathetic motion is worse than wind sympathetic motion at the shed scale — solar joints under a single cloud system can drop to 5% output simultaneously, while wind joints across 30 km usually retain >30% diversity.
- The "shadow joints" (other developers' assets) cannot be fully known — the FERC EQR and Form 860 lag, queue cluster public data is partial. Use the queue cluster snapshot as the lower bound and assume an additional 30-50% "phantom shadow" capacity.
- Sympathetic motion can also be *desired* — pair-correlated solar and lithium storage joints in the same shed produce a clean diurnal choreography. The audit flags unwanted correlation; deliberate co-location with paired storage is a feature, not a bug.
