# /dummy-bias-prior — Per-Dummy Calibration Prior

Elicit and update a per-dummy-serial-number prior over channel-level systematic bias, from the lab's certification history. This prior feeds `/injury-posterior` so that a dummy with a chronically-hot chest deflection channel doesn't drag down a vehicle's posterior unfairly.

## Inputs

- Dummy serial number (e.g. `HIII-5M-SN-001234`, `THOR-50M-SN-2024-07`).
- Path to the lab's certification log (CSV or JSON) — one row per certification cycle, containing channel-by-channel residuals against the certification reference.
- Number of historical cycles to weight (default: last 12; deeper history is downweighted with an exponential kernel τ = 6 cycles).
- Optional: a prior from the dummy manufacturer's spec sheet for new dummies with thin history.

## Steps

1. **Load history.** Filter the certification log to this serial. Build a per-channel matrix of residuals (rows = cycles, columns = channels: head accel X/Y/Z, neck Fx/Fy/Fz/Mx/My/Mz, chest accel + deflection, pelvis accel, femur force L/R).
2. **Detect drift.** For each channel, fit a linear trend in residual vs. cycle index. Channels with significant slope (p < 0.05) are flagged as drifting; their prior uses the projected residual at the test date, not the historical mean.
3. **Compute per-channel prior.** For stable channels, the bias prior is Normal(mean = residual mean, sigma = residual std × √(1 + 1/N)). For drifting channels, mean is the projected residual; sigma is the regression residual std.
4. **Cross-channel correlation.** Compute the correlation matrix of residuals across channels — head accel X and Y often drift together due to the same accelerometer pack. Encode as a joint Gaussian prior.
5. **Persist.** Write the prior to `outputs/_priors/<dummy-serial>/<YYYY-MM-DD>.json`; downstream commands read this file. Bump a manifest so `/injury-posterior` knows which prior to load for which test.
6. **Re-elicit on certification.** Whenever a fresh certification cycle lands, re-run this command before the next test campaign.

## Output

`outputs/_priors/<dummy-serial>/<YYYY-MM-DD>.json` — per-channel mean, sigma, drift flag; joint correlation matrix.
`outputs/_priors/<dummy-serial>/<YYYY-MM-DD>-summary.md` — human-readable: which channels are drifting, which are stable, how confident the prior is.

## Notes

- A dummy with fewer than 4 certification cycles cannot have a meaningful empirical prior — fall back to manufacturer spec and report the prior as "weak."
- THOR-50M and Hybrid III have different channel sets; keep separate priors per dummy type.
- If two dummies (one per occupant position) are used in the same test, each gets its own prior; do not pool unless certification residuals are demonstrably exchangeable.
- This command updates the prior; it does **not** re-analyse past tests. Past test posteriors are frozen with the prior in force at the time of analysis. Re-analysis with a refreshed prior is a deliberate decision, not a side effect.
