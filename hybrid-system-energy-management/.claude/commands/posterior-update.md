# /posterior-update

Update battery SOH/capacity or driver-intention posteriors from new telemetry.

## Inputs

- Telemetry log: timestamp, current, voltage, temperature, vehicle speed, pedal positions, brake state.
- Sample rate (ideally ≥10 Hz for current/voltage; 100 Hz for pedals).
- Existing posterior(s) to update (most recent SOH; current driver-class belief).
- Choice of estimator (UKF, particle filter, moving-horizon).

## Steps

1. Read `context/workflows.md` "Bayesian SOC + SOH Estimation Pipeline" for the canonical procedure.
2. Validate telemetry sanity: monotonic timestamps, no current spikes outside cell limits, no temperature dropouts.
3. Run the estimator forward across the log, carrying the prior posterior as initial state.
4. Track innovation covariance — log when it grows beyond 3× expected (model mismatch flag).
5. At end of log, update SOH posterior: compare modelled vs. measured terminal voltage trajectory; joint coulomb-counting + voltage-fit.
6. Update driver-class posterior: hierarchical Bayes with pedal/brake-pattern likelihood per class.
7. Write the new posteriors to `outputs/posteriors/YYYY-MM-DD.md` with mean, 5th/95th percentiles, and the residual diagnostics.

## Output

Two artifacts in `outputs/posteriors/YYYY-MM-DD/`:
- `battery-soh.md` — updated SOH posterior + innovation diagnostics + flagged anomalies.
- `driver-class.md` — updated categorical posterior over driver classes + likelihood evidence per class.

## Notes

- Don't update SOH from a single short cycle — coulomb counting accumulates error; require ≥30 min of varied operation.
- Particle filter resampling kills diversity if not done carefully (use systematic resampling, monitor effective sample size).
- A bias in the innovation series ≥ 2σ for two consecutive segments = recalibrate model parameters before continuing.
