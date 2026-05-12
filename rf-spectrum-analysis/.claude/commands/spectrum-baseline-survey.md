# /spectrum-baseline-survey

Establish a multi-day baseline of the local RF environment and derive the SPC control limits that all subsequent symptom assessments and control charts will reference. The first sample of any SPC programme: without a stable baseline, nothing else is interpretable.

## Inputs

- **Site identifier** (e.g. `bldg-2-server-room`, `vehicle-A-roof`) and a one-line description.
- **Frequency plan** — start MHz, stop MHz, and either a uniform step or an explicit list of sub-bands (e.g. `433.05-434.79 ISM-EU`, `868-868.6 SRD-1`).
- **Capture window** — wall-clock duration. Minimum 24 hours; 168 hours (one week) is the recommended default for sites with weekly cycles.
- **SDR configuration** — device, antenna, gain, sample rate, FFT length, window function. Record these verbatim.
- **Subgroup size** `n` (typically 4–6 contiguous sweeps per subgroup) and subgroup cadence (e.g. one subgroup every 10 minutes).

## Steps

1. **Lock measurement conditions.** Confirm the antenna and SDR will not move during the capture. Note ambient temperature, building occupancy, weather (if outdoor). Drift in any of these invalidates control limits later.
2. **Plan sweep coverage.** Divide the requested range into segments sized to the SDR's instantaneous bandwidth. Compute the time budget per segment so the subgroup cadence holds across the full range.
3. **Generate capture commands.** Emit `hackrf_sweep`, `rtl_power`, `gnuradio` or `RsaToolbox` invocations parameterised with the chosen FFT length, gain, and dwell. Save the exact command lines to `outputs/baseline-<site>-<date>/commands.txt`.
4. **Run the capture.** Either invoke the tools (when authorised) or hand off the command file to the operator. Stream output to `outputs/baseline-<site>-<date>/sweeps/`.
5. **Compute subgroup statistics.** For each subgroup and each frequency bin/channel, compute mean, range, standard deviation, and 95th-percentile power. Persist as `subgroups.parquet`.
6. **Derive control limits.** For each channel, compute X-bar centre line and UCL/LCL using `X-bar ± A2·R-bar`, and the R-chart UCL using `D4·R-bar`. Use the constants table in `context/references.md`.
7. **Identify persistent emitters.** Flag any bin with subgroup-mean ≥ noise floor + 6 dB and duty cycle ≥ 50%. Catalogue with frequency, level, bandwidth, modulation guess.
8. **Emit baseline manifest.** Write `outputs/baseline-<site>-<date>/manifest.md` with measurement config, subgroup statistics summary, control limits per channel, and the persistent-emitter inventory.

## Output

A directory `outputs/baseline-<site>-<date>/` containing:
- `manifest.md` — human-readable summary with limits and emitter inventory.
- `subgroups.parquet` — the structured subgroup statistics (input for `/control-chart-build`).
- `limits.json` — channel → {UCL, CL, LCL, R-UCL} (machine-readable; consumed by every later command).
- `sweeps/` — raw sweep CSVs preserved for reproducibility.
- `commands.txt` — the exact SDR invocations used.

## Notes

- The baseline window must be **representative** of how the environment is normally used. Avoid surveying during a known anomaly (construction, an event); reschedule or document the contamination in the manifest.
- 25 subgroups is the rule-of-thumb minimum for control-limit estimation (per AIAG SPC manual). Below that, limits are wide and unreliable.
- Re-baseline after any deliberate environmental change (new equipment, antenna move, neighbour change). Don't paper over a real shift with old limits.
