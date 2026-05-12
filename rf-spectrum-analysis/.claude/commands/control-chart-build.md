# /control-chart-build

Build one or more SPC control charts on a chosen spectrum metric and apply Western Electric run rules to detect special-cause variation. This is the workspace's diagnostic instrument — it converts a noisy spectrum into a yes/no signal about whether the process has shifted.

## Inputs

- **Baseline manifest** — `outputs/baseline-<site>-<date>/manifest.md` plus the `limits.json` and `subgroups.parquet` it ships with.
- **Metric** — one of: noise-floor median (dBm), channel occupancy (%), peak power (dBm), peak-count (# bins above threshold), inter-burst interval (ms), packet-loss rate (%).
- **Chart type** — `xbar-r` (continuous, normally distributed), `ewma` (small-shift detection, λ default 0.2), `cusum` (small persistent shifts), `p-chart` (proportion non-conforming), or `c-chart` (defect count per fixed area).
- **Window** — most-recent-N subgroups (default 50) or an absolute date range.
- *(Optional)* **Annotations** — symptom IDs from `/symptom-assess` and intervention IDs from `/intervention-ladder` to overlay as event markers.

## Steps

1. **Load and align data.** Read `subgroups.parquet`, filter to the requested window and channel, confirm subgroup size matches the limits in `limits.json`. Refuse the run if subgroup size has changed (limits aren't comparable).
2. **Build the chart.**
   - `xbar-r`: plot subgroup means with the precomputed UCL/CL/LCL; plot ranges with R-bar and D4·R-bar.
   - `ewma`: smooth with λ and plot ±L·σ_EWMA bands (L=3 default).
   - `cusum`: tabular CUSUM with reference value k=0.5σ and decision interval h=4σ unless overridden.
   - `p-chart` / `c-chart`: appropriate attribute-data limits.
3. **Apply Western Electric rules.** Flag points violating any of:
   1. Single point beyond 3σ.
   2. 2 of 3 consecutive points beyond 2σ on the same side.
   3. 4 of 5 consecutive points beyond 1σ on the same side.
   4. 8 consecutive points on the same side of the centre line.
   5. 6 consecutive trending up or down.
   6. 14 consecutive alternating up/down.
   7. 15 consecutive within 1σ (over-control / re-baseline candidate).
   8. 8 consecutive outside 1σ either side.
4. **Overlay annotations.** Plot symptom-assessment markers and intervention markers as vertical lines with hover-text. Without this overlay the chart is a graph; with it, it's a clinical record.
5. **Diagnose.** Write 3–5 sentences interpreting the chart: in-control vs out-of-control, which rule fired, candidate special cause (correlate with recent symptoms / interventions / known site events).
6. **Persist.** Save chart PNG, chart JSON (for diff), and the diagnosis to `outputs/charts/<metric>-<chart-type>-<window>.{png,json,md}`.

## Output

- `outputs/charts/<id>.png` — the chart with WE-rule violations highlighted.
- `outputs/charts/<id>.json` — machine-readable points, limits, and triggered rules.
- `outputs/charts/<id>.md` — the diagnosis. Includes a recommendation: continue monitoring, escalate to `/symptom-assess`, or re-baseline.

## Notes

- A chart is only as valid as the baseline. If the noise floor has materially shifted *and you know why*, re-run `/spectrum-baseline-survey` rather than chasing false alarms.
- EWMA and CUSUM are more sensitive than X-bar/R to small persistent shifts; use them when the symptom is "creeping" not "spiking".
- A `p-chart` is the right choice when measuring packet-loss percentage; an `xbar-r` is wrong because the data is binomial.
- Save the chart JSON not just the PNG — the JSON is what `/longitudinal-track` reads.
