# /socket-fit-control-chart

Build I-MR or X-bar-R control charts on socket-pressure-mapping data across follow-up visits — detects fit drift early, before it shows up as a clinical complaint.

## Inputs

- **Pressure-mapping data** — F-Scan (Tekscan), pedar-X (Novel), or FSA (Vista Medical) exports across follow-up visits. Minimum 8 visits post-baseline-lock for meaningful chart sensitivity.
- **Regions of interest** — typically: patellar tendon bar (PTB), tibial crest, fibular head, distal end-bearing area, popliteal fossa for TT; ischial tuberosity, lateral wall, distal end for TF. List all regions of interest before charting.
- **Per-region statistic to chart** — peak pressure (kPa), peak pressure-time integral (kPa·s), contact area (cm²), pressure gradient (kPa/cm). Pick one primary plus 1-2 secondary per ROI.
- **Baseline** — output of `/gait-lab-spc-baseline` if available, OR the first 8-10 visits used as embedded baseline (calling out the increased uncertainty).
- **Activity context per visit** — was the pressure-map session a representative session (typical activity day), or a problem-focused session (patient came in complaining)? Mix differently — problem visits aren't process samples.

## Steps

1. Read `context/workflows.md` "Socket fit SPC workflow" + `context/references.md` "Cp/Cpk interpretation".
2. Filter to representative-session visits only (exclude problem-focused unless explicitly compared separately).
3. Per ROI per statistic, compute control limits from baseline (or first-N if no separate baseline).
4. Build I-MR chart (or X-bar-R if you have repeated trials per visit — typical 3 trials).
5. Apply Shewhart rules 1-4 (Western Electric): (1) single point beyond 3σ, (2) 2/3 consecutive beyond 2σ same side, (3) 4/5 consecutive beyond 1σ same side, (4) 8 consecutive same side of mean.
6. Flag any out-of-control signals with: visit ID, rule triggered, magnitude (σ-units), candidate assignable causes (recent doffing pattern change, sleeve switch, prosthetic-component swap, limb-volume change, footwear change).
7. Write chart data + signals to `outputs/spc-charts/<patient-id>/<YYYY-MM-DD>-<ROI>-<statistic>.json`.
8. Render visualisation (matplotlib / R `qcc`) and save PNG alongside the JSON.
9. Generate an investigation memo for each flagged signal — what changed, what was tried, what the recommendation is.

## Output

- **JSON chart data** per ROI × statistic: control limits, per-visit point, MR-bar, signal flags.
- **PNG chart visualisation** ready for CPO review.
- **Markdown investigation memo** for each signal: `outputs/spc-charts/<patient-id>/<YYYY-MM-DD>-signal-<n>.md` — visit ID, rule, assignable-cause hypothesis, action recommendation.

## Decision points

- **If the patient had a known intervention (component change, limb volume shift) since baseline** → either re-baseline (re-run `/gait-lab-spc-baseline`) before charting OR mark a documented step-change on the chart.
- **If multiple ROIs trigger simultaneously** → suspect a system-level cause (full re-cast needed) rather than localised drift.
- **If the chart is consistently in-control but the patient reports discomfort** → the chart is measuring the wrong variable. Add a secondary variable or revisit ROI selection.

## Notes

- Pressure-mapping repeatability has substantial measurement noise; a Gauge R&R study (`/fitting-gauge-rr`) on your specific mat / pad should be in place before treating I-MR variation as process-only.
- Common assignable-cause patterns: (a) summer/winter limb-volume seasonal swing; (b) gel-liner break-in over first 60 days post-fit; (c) component wear (foot bumpers, knee dampers) on a 6-12 month cadence.
- Watch for "operator-induced" pattern: same fitter consistently produces tighter control limits than another fitter on the same patient — that's a measurement-system signal, not a process signal.
