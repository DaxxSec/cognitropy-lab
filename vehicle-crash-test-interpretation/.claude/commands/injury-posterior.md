# /injury-posterior — Posterior Injury-Risk Distribution

Compute a posterior probability distribution over AIS-coded injury severity per body region from validated ATD channels, using canonical injury-risk curves as likelihoods and the lab's prior over dummy / vehicle population as the prior.

## Inputs

- Test ID and occupant position (driver, front passenger, rear left, rear right, second-row centre).
- Validated ATD channels (after `/pulse-anomaly-check` passes): head accel (CFC 1000), upper-neck force/moment (CFC 1000), chest accel + deflection (CFC 180 / 600), pelvis accel (CFC 1000), femur force (CFC 600).
- Dummy serial number and last-certification date (consumed via `/dummy-bias-prior`).
- Body regions of interest: `head`, `neck`, `chest`, `pelvis`, `femur` (default all).
- Posterior sample count (default 10,000).

## Steps

1. **Channel hygiene.** Verify each requested channel is in SAE J211 polarity, low-pass filtered to the appropriate CFC class, and free of clipping. If any channel fails, abort and refer to `/pulse-anomaly-check`.
2. **Compute scalar criteria from time histories.** HIC15 from head resultant acceleration; Nij from upper-neck Fz and My; chest deflection peak from sternum displacement; femur peak axial force. Persist intermediate scalars to `outputs/<test-id>/criteria.json`.
3. **Load priors.** Pull the dummy-calibration prior produced by `/dummy-bias-prior` for the active dummy serial; pull the fleet-level injury prior from `context/references.md` (Mertz / Eppinger / Kuppa risk curves parametrised by AIS level).
4. **Bayesian update.** For each body region, run an MCMC update (PyMC, `target_accept=0.9`) with the canonical risk curve as the likelihood and the elicited prior. Sample the requested posterior count for AIS 1+, 2+, 3+, 4+, 5+ probabilities.
5. **Compute credibility intervals.** Report posterior median, 5th and 95th percentiles for each AIS level per body region. Flag any region where the 5–95 interval crosses the regulatory threshold.
6. **Write outputs.** Posterior trace + summary JSON, posterior-density plots (one per body region) to `outputs/<test-id>/posteriors/`, and a one-page summary markdown.

## Output

`outputs/<test-id>/posteriors/<occupant>/` containing:
- `summary.md` — posterior medians + 5/95 percentiles per body region.
- `criteria.json` — point-estimate criteria for traceability.
- `posterior-<region>.png` — density plot for each body region.
- `trace.nc` — full NetCDF trace for downstream reuse.

## Notes

- Use Mertz 2003 risk curves for Hybrid III; switch to Eppinger/Kuppa for THOR-50M. The dummy serial selects which family.
- Never report a body region in isolation when chest and abdomen criteria conflict — interpret in `/restraint-likelihood` instead.
- The 5–95 credibility interval is the deliverable; do not collapse to median in any consumer-facing artefact.
