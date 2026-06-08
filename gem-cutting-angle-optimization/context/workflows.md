# Gem Cutting Angle Optimization — Workflows and Methodology

How the agent actually runs the bench. Every workflow ties the optical optimization to the machine's measured condition through **predictive maintenance scheduling** — the engine technique for today's build. Concepts (what things are) live in `concepts.md`; this file is what the agent *does*.

## Workflow 1: Optimize-and-cut pipeline

**Goal:** Take a piece of rough from unknown geometry to a window-free finished stone the machine can actually hold.

### Steps

1. **Identify the material and RI.** Measure with a refractometer or look up in `references.md`. Record RI (and dispersion if fire matters).
2. **Compute the optical floor.** `/critical-angle-calc` → critical angle and minimum safe pavilion main.
3. **Optimize the pavilion.** `/optimize-pavilion-angle` → pavilion main that maximizes light return for this RI, sitting a few degrees above the floor.
4. **Pick a crown for the fire/brilliance balance.** `/light-return-map` over a crown × pavilion grid; choose crown angle per how much fire the material's dispersion can deliver.
5. **Budget the tolerance.** `/tolerance-budget` → required hold tolerance (e.g. ±0.15°) vs current machine error sources.
6. **Gate on machine condition.** `/spindle-runout-trend` + `/lap-wear-forecast`. If the budget is blown, schedule maintenance (`/pdm-schedule`) *before* cutting — do not cut fine work on an out-of-budget machine.
7. **Cut** the pavilion, transfer the dop, cut the crown, polish — recording angle, index, and lap grit per facet.
8. **Grade.** `/cut-grade-check` on the finished proportions; log the result and any defect to `outputs/`.

### Decision Points

- If RI < 1.50: warn — narrow windowing margin; steepen pavilion and re-check brilliance.
- If tolerance budget exceeded: stop, schedule maintenance, re-validate; do not "cut carefully around it."
- If `/cut-grade-check` flags a window but angles were correct: the defect is the *machine*, not the design → run condition trends.

## Workflow 2: Porting a published design across materials

**Goal:** Re-use a GemCad design cut for one RI in a different material without windowing.

### Steps

1. Note the design's reference RI and its pavilion main / crown main angles.
2. Get the target material's recommended pavilion main (`/optimize-pavilion-angle`).
3. `/tangent-ratio-adapt` → solve TR so the pavilion main maps to the target, then apply `θ_new = arctan(TR · tan(θ_old))` to *every* angle.
4. Verify meet points still close (all converging facets share a common point in the rescaled design).
5. Re-budget tolerance for the new angles and re-gate on machine condition.

### Decision Points

- If TR pushes any crown angle past polishing practicality (very steep): cap it and accept a small light-return trade, or pick a different base design.
- If the target RI is *higher* than the source: TR < 1, angles shallow — confirm you haven't gone below the new critical floor anywhere.

## Workflow 3: Condition-monitoring → predictive-maintenance schedule

**Goal:** Keep every machine error source under its share of the angle budget by acting at the P-point.

### Steps

1. **Establish baselines.** On a known-good day, record spindle TIR, lap flatness deviation, vibration RMS, and cut rate. Store as the machine's reference in `outputs/machine-baseline.md`.
2. **Sample on a cadence.** Log the same indicators every N machine-hours or every M stones (`/spindle-runout-trend`, `/lap-wear-forecast`).
3. **Trend, don't snapshot.** Fit each indicator's trajectory; a single reading is noise, a slope is a forecast.
4. **Locate the P-point.** Where the trend will cross the indicator's threshold (from `references.md`).
5. **Estimate RUL and the P-F interval.** Schedule the intervention inside the P-F interval — early enough to act, late enough not to waste life.
6. **`/pdm-schedule`** consolidates all indicators into one dated work queue (dress lap, service spindle, replace bearings).
7. **Close the loop.** After maintenance, re-baseline and confirm the indicator reset below threshold.

### Decision Points

- If an indicator is already past threshold: it is a *functional failure* now — stop cutting fine work, service immediately, mark any stones cut since the last good reading for re-grade.
- If two indicators will cross within one P-F interval of each other: batch the maintenance to avoid two teardowns.
- If trend is flat and well under threshold: extend the sampling interval (don't over-maintain — that is just time-based PM wearing a PdM costume).

## Workflow 4: Diagnosing a window on a "correctly cut" stone

**Goal:** Decide whether a defect is a design error or a machine error.

### Steps

1. Reproduce the proportions actually achieved (`/cut-grade-check`) vs the proportions intended.
2. If achieved pavilion is shallower than intended by more than the tolerance budget → machine, not design.
3. Check spindle runout and lap flatness as of the cut date (`/spindle-runout-trend`). A dished lap shifts delivered angle radially; runout tilts facets.
4. If machine is in budget and angles match intent but it still windows → the *design* was below the optical floor for this RI; re-optimize.
5. Record the verdict and corrective action in `outputs/`.

## Methodology Phases — predictive maintenance, applied to faceting

### Phase 1 — Baseline
Characterize the machine when it is known-good. Without a baseline there is no trend, and without a trend there is no prediction — only guessing.

### Phase 2 — Surveillance
Sample condition indicators on a usage-based cadence. The faceting-specific indicators are spindle TIR, lap flatness, vibration RMS, and cut-rate decay — each mapped to a slice of the angle-error budget.

### Phase 3 — Diagnosis & prognosis
Fit trends, identify which component is degrading, estimate RUL, and find the P-point. Translate "the spindle is at 14 µm and climbing 1 µm per 20 hours" into "it crosses the 20 µm budget limit in ~120 hours."

### Phase 4 — Scheduling & action
Place the intervention inside the P-F interval, batch where sensible, execute, and re-baseline. The output is a dated maintenance queue that keeps the machine permanently inside the tolerance the optimization assumed.
