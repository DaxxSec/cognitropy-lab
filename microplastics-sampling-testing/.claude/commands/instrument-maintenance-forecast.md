# /instrument-maintenance-forecast

Forecast the next required service for every "checkpoint" in the network — field samplers and benchtop instruments — before drift or failure quietly corrupts the data. This is the predictive-maintenance spine that keeps the screen from going blind mid-program.

## Inputs

- Asset register: each sampler and instrument with usage counters and condition signals, e.g.
  - **Net / sieve:** tow distance or sample count since last mesh inspection; aperture wear.
  - **Pump / autosampler:** run hours, flow-calibration drift, diaphragm/tubing age.
  - **FTIR:** IR source hours, ATR-crystal condition, desiccant state, detector (MCT/LN₂) checks.
  - **Raman:** laser diode hours, grating/CCD calibration, fluorescence baseline creep.
  - **Py-GC/MS:** column injections, liner/septum cycles, MS source cleaning interval.
- Calibration-verification history (control-chart points; Westgard/Shewhart flags).
- QA trend feeds: blank-load trend (`/blank-audit`) and recovery trend (`/qa-recovery-spike`).

## Steps

1. **Condition + usage model.** For each asset, compare cumulative usage to the service interval (`context/references.md`) and overlay condition signals. Estimate remaining useful life (RUL) from whichever is nearer: usage budget or drift trajectory.
2. **Fold in QA early-warnings.** A creeping blank fiber load or a declining recovery is often the *first* sign a filter/sieve/medium is failing — treat these as condition signals, not just QA outcomes. This is what makes the schedule predictive rather than calendar-blind.
3. **Calibration-verification check.** If control charts show drift approaching limits (consecutive points one side of the mean, trend, or a Westgard violation), schedule service before the next batch, not after the failure.
4. **Prioritize by data-risk.** Rank pending services by how much data they jeopardize: an FTIR drifting before a high-value source-attribution batch outranks a routine pump-tubing swap. (Risk-based, like everything else here.)
5. **Emit the schedule** with due-by dates/usage and the consequence of deferral (e.g. "ATR crystal at 95% — HQI degradation likely → false denials").
6. **Quarantine rule.** Any asset past a hard limit or with an open calibration failure is *out of service* for reportable work until serviced and re-verified — analogous to closing a checkpoint that can't screen reliably.

## Output

A maintenance forecast under `outputs/maintenance/<date>.md`: per-asset RUL, due-by service list ranked by data-risk, the QA early-warning signals folded in, calibration-verification status, and any out-of-service quarantines. Re-run on a standing cadence.
