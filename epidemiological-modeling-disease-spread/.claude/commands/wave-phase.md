# /wave-phase

Classify the current epidemic phase (introduction / growth / peak / decline / endemic) and detect wave change-points in a surveillance series.

## Inputs

- The cleaned, nowcast-corrected series (and, if available, the Rt series from `/estimate-rt` and a seasonal baseline from `/decompose-trend`).
- Pathogen seasonality context (epidemic vs endemic expectation).
- Sensitivity preference for change-point detection (penalty / number of segments).

## Steps

1. Read `context/workflows.md` "Methodology Phases — epidemic stage read".
2. Assemble the trend signal: de-seasonalised trend + nowcast-corrected recent window + Rt where available.
3. Run **change-point detection** on the trend (PELT / binary segmentation via `changepoint`/`ruptures`, or Bayesian online CPD) to locate wave inflections (onset, peak, trough).
4. Classify the current phase from the joint evidence:
   - **Introduction** — low, stochastic counts → defer to `/detect-aberration`.
   - **Growth** — r > 0, Rt > 1 (CI excludes 1).
   - **Peak/plateau** — Rt → 1, growth → 0, change-point near the inflection (verify it is nowcast-corrected, not a truncated-tail artifact).
   - **Decline** — Rt < 1, positive halving time; watch for resurgence.
   - **Endemic / inter-wave** — settled to seasonal baseline → switch to threshold methods.
5. Estimate peak timing/height with uncertainty where in/near peak.
6. Write the phase call + change-point timeline to `outputs/`.

## Output

`outputs/wave-phase-<stream>-<snapshot-date>.md` + figure: the series with annotated change-points and current-phase label, the supporting evidence (Rt, r, baseline), peak estimate if relevant, and a one-line situational-awareness statement with caveats.

## Notes

- The most common false call is "peak/decline" read off a right-truncated tail — only classify on nowcast-corrected data.
- Change-points are descriptive; corroborate a detected peak with Rt crossing 1, not the change-point alone.
- In endemic phase, "above/below normal" (threshold) is more meaningful than growth/decline — hand off to `/decompose-trend` baselines.
