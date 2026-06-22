# /control-chart — Build or Update an I-MR / DNOM Control Chart

Build or extend a control chart for a tracked restoration characteristic and flag out-of-control signals, so the shop reacts to assignable causes and ignores common-cause craft variation.

## Inputs

- Characteristic name and unit (e.g. "front-rail joint gap, mm"; "seat-box squareness Δd, mm").
- The ordered series of individual measurements (one per frame/job), each with its date, operator, and MC/RH metadata.
- Chart mode: **I-MR** (single homogeneous characteristic) or **DNOM** (mixed frame types sharing a chart via measured − nominal).
- Whether limits are being **established** (baseline) or the chart is in **monitoring** mode (limits frozen).

## Steps

1. If establishing: require ≥ 20–25 baseline points; compute moving ranges, M̄R, and X̄ (or D̄ for DNOM).
2. Compute limits — I chart `X̄ ± 2.66·M̄R`; MR chart `UCL = 3.267·M̄R`, `LCL = 0`. (For DNOM, center on 0.)
3. Plot the series against center line and limits (text/ASCII or table; save the data so the chart persists in `outputs/`).
4. Apply the **Western Electric / Nelson rules** (`context/references.md`); list every rule violation with its point index.
5. If establishing: purge points with a *documented* assignable cause, recompute, then **freeze** limits and switch to monitoring. If monitoring: do **not** recompute limits — compare new points to the frozen limits.
6. On any signal, recommend launching the OCAP (`context/workflows.md` Workflow 4); do not "adjust" the process on an in-control point.

## Output

Chart artifact: the plotted series, center line, UCL/LCL, M̄R, σ̂ = M̄R/1.128, and a list of rule violations with interpretation. Save to `outputs/<characteristic>-imr-chart.md` plus the persisted data series.

## Notes

- Restoration is usually n = 1 per job → **I-MR is the default**, not X̄-R. Don't force subgroups that weren't produced under identical conditions.
- σ̂ from this chart feeds `/process-capability` — capability is only valid when this chart is in control.
- Six points trending or 8–9 on one side is a *shift*, often a new restorer, glue lot, or humidity regime — a quieter but realer signal than a single 3σ spike.
