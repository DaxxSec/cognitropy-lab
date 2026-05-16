# /restraint-likelihood — Restraint System Performance Likelihood

Estimate the posterior likelihood ratio that observed occupant kinematics reflect **normal** vs. **degraded** restraint-system performance (belt slip, pretensioner non-fire, airbag mis-timing, load-limiter saturation, head-form A-pillar contact).

## Inputs

- Test ID and occupant position.
- High-speed kinematics markers (head CG, T1, hip, knee) — at minimum X, Z displacement vs. time.
- Restraint system log: pretensioner fire time, airbag deploy time + stages, seatbelt load cell trace, load limiter spec.
- Test mode (frontal rigid, ODB, MPDB, small-overlap, oblique, side pole) — selects the expected kinematic envelope.

## Steps

1. **Compute kinematic features.** Head excursion peak (X, Z), forward displacement at peak chest acceleration, head-to-airbag contact timing, peak belt force, time to peak belt force.
2. **Build the "normal" likelihood family.** Use the prior distribution of kinematic features from prior-art tests of healthy restraint systems (parametrised in `context/references.md` per test mode and occupant size). Treat as a multivariate normal in feature space.
3. **Build the "degraded" likelihood family.** Library of degradation modes (belt slip = forward excursion outlier; non-fire pretensioner = late peak belt force; mis-timed airbag = head-form contact spike at non-canonical timing).
4. **Compute the Bayes factor.** P(features | degraded) / P(features | normal). Convert to posterior probability of degradation under a flat 50/50 prior (or an asymmetric prior if the lab has reason to suspect a specific failure — pretensioner recall in progress, etc.).
5. **Localise the degradation.** If posterior probability of degradation > 0.3, attribute to the single most likely failure mode by per-feature contribution to the Bayes factor.
6. **Cross-check with `/injury-posterior`.** A degraded restraint should manifest in elevated body-region posteriors; if it does not, surface the inconsistency for analyst review (channels may have been mis-mapped).

## Output

`outputs/<test-id>/restraint/<occupant>/`:
- `bayes-factor.json` — log10 Bayes factor by feature.
- `posterior-degraded.png` — posterior probability distribution.
- `attribution.md` — single most likely degradation mode with evidence chain, or "consistent with normal performance" if Bayes factor favours normal.

## Notes

- A high Bayes factor for "degraded" does not by itself mean the restraint **failed regulation** — it means the kinematics are anomalous relative to the prior. Translate to compliance via `/regulation-compare`.
- Marker dropouts behind airbag deployment are common; treat any feature derived from a marker that disappears as missing data, not as a zero.
- Side-impact tests have different feature sets (head-to-pillar, head-to-window, pelvis-to-door) — use the per-mode feature library.
