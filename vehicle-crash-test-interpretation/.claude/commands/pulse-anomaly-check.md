# /pulse-anomaly-check — Bayesian Crash-Pulse Anomaly Screening

Before any injury analysis, screen the vehicle accelerometer pulse against the **expected pulse family** for the test mode. Outputs a posterior probability that the pulse is in-family; if low, all downstream analyses (`/injury-posterior`, `/restraint-likelihood`) are suspect and must be flagged.

## Inputs

- Test ID and test mode (frontal rigid barrier 35 mph, ODB 40 mph, MPDB 50 km/h, IIHS small-overlap 40 mph, EuroNCAP side pole 32 km/h, etc.).
- Vehicle accelerometer time history at the floor-pan or rocker location (CFC 60 for crash pulse).
- Optional: B-pillar acceleration channels for side-impact modes.

## Steps

1. **Resample and filter.** Confirm CFC 60 anti-alias / low-pass per SAE J211. Resample to 10 kHz if needed.
2. **Extract pulse features.** Peak acceleration, time to peak, pulse duration (10%-90%), velocity change (integral), area under pulse (mean acceleration). For side impacts, add B-pillar peak and door intrusion timing.
3. **Load the expected-family prior.** Per test mode, the in-family pulse distribution is a multivariate Gaussian over the features above, with parameters in `context/references.md` fit from public NHTSA / Euro NCAP test databases.
4. **Compute Mahalanobis distance** of this pulse from the family mean in feature space; convert to a chi-squared p-value across feature degrees of freedom.
5. **Posterior P(in-family).** Use the chi-squared statistic as the likelihood; combine with a 95/5 prior favouring in-family (most test labs run within spec the vast majority of the time). Output posterior probability the pulse is in-family.
6. **Diagnose if anomalous.** If P(in-family) < 0.5, attribute by feature: shifted-time-to-peak → barrier offset or initial vehicle velocity error; elevated peak → stiffer-than-expected vehicle structure or barrier failure; truncated duration → channel saturation or sensor failure.
7. **Gate downstream analysis.** If P(in-family) < 0.2, refuse to run `/injury-posterior` without explicit analyst override; if < 0.5, run but flag prominently in output.

## Output

`outputs/<test-id>/pulse-check/`:
- `features.json` — extracted pulse features.
- `posterior.json` — P(in-family) with credibility interval.
- `attribution.md` — diagnosed cause if anomalous.
- `pulse-overlay.png` — pulse plotted against family mean ± 2σ envelope.

## Notes

- Public NHTSA database has thousands of frontal rigid pulses; small-overlap and oblique modes have fewer — priors are correspondingly broader, so don't over-interpret a P(in-family) = 0.6 in a rare mode.
- A pulse that's anomalous because the **vehicle structure** is genuinely novel is the most interesting case — it's a finding, not a fault. Don't silently reject; flag for analyst review.
- This check is mandatory before any other command. Skipping it is the single most common analytic mistake.
