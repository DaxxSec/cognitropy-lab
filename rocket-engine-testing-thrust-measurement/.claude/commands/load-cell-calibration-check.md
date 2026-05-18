# /load-cell-calibration-check

Validate the load-cell calibration chain per ASTM E74. Walk the `C-*` tree (`context/workflows.md` §6) and emit a PASS / REJECT with a per-cell risk-cell mapping. This is a hard gate for `/thrust-uncertainty-budget` and a contributing term to `/test-readiness-risk`.

## Inputs

- `cell_serial` — load-cell serial number.
- `cell_model` — model (e.g. `Interface 1010ACK-20K`, `Lebow 3173-200K`).
- `fs_rating` — full-scale rating in lbf or N.
- `manufacturer_cal_interval_months` — manufacturer's stated maximum calibration interval (typically 12, sometimes 6 for mission-critical).
- `cal_cert_path` — most recent calibration certificate per ASTM E74 (PDF or markdown).
- `service_history_path` — log of overload events, environmental exposures, mechanical alterations since last cal.
- `intended_fire_thermal_env` — expected ambient temperature range during the test.

## Steps

1. Run `C-0` intake. All inputs required; reject if any missing.
2. At `C-1`, compare cal date + interval to today. If overdue, REJECT — no thrust report possible until re-cal.
3. At `C-2`, verify NIST (or accredited NMI) traceability is named on the cert. If the cert names a transfer standard, that transfer standard's traceability must also be on file.
4. At `C-3`, evaluate ASTM E74 fit residuals. Class AA (0.025%) or A (0.05%) is preferred for qualification. Class B (0.25%) is acceptable for development testing only with explicit flag.
5. At `C-4`, walk the service history for overload events. Any reading > 100% FS requires post-event recalibration; > 150% FS (safe-overload) renders the cell suspect; preferable replacement.
6. At `C-5`, check that the calibration ambient temperature is within ±10 °C of the intended fire stand environment. If not, propagate the thermal coefficient correction into the uncertainty budget (`U-*` term).
7. At `C-6`, emit PASS / REJECT with the cited terminal node and a risk-matrix cell. Calibration-drift hazard is typically severity II (data integrity loss, not safety) and likelihood is administration-dependent (A if cal admin is sloppy, E if rigorous).
8. Write the result to `outputs/calibration/<cell_serial>-check-<YYYYMMDD>.md`.

## Output

Markdown file containing:
- Cell serial, model, FS rating, cal cert hash, cert date, cal interval, NIST traceability path.
- Per-node verdict (C-1 through C-5) with cited values.
- ASTM E74 class achieved with residuals.
- Service-history summary: overload events, environmental excursions, alterations.
- PASS / REJECT decision with the terminal node id.
- Risk-matrix cell for "calibration-drift" hazard (severity, likelihood, band).
- Recommended next action if REJECT: re-calibrate / replace / reduce FS rating / restrict to development-class measurements.
- Reproducibility footer.

## Notes

- A "we re-zeroed it" tare adjustment is not a substitute for an ASTM E74 calibration. Tare correction is for thermal expansion of the stand, not for cell drift.
- An overload event > 150% FS may leave no visible damage but shift the span. Post-event re-cal is mandatory; assuming the cell is fine because the trace "looked normal" is a frequent mode for `2A` HIGH cells.
- For a multi-cell stand, run `/load-cell-calibration-check` per cell. The aggregate stand uncertainty depends on *every* cell passing C-1..C-5.
- The Class B (0.25%) acceptance for development is not a license to lower a qualification-class calibration. Development data tagged with Class B residuals is not portable to a flight-qual report.
- If the cell sees cryogenic boil-off plume reflection during fire, the thermal environment delta is large; either thermally compensate the cell in-situ (heated jacket) or move the cal point much closer to the fire-time temperature.
