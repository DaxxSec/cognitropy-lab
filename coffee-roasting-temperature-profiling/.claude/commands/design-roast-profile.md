# /design-roast-profile

Design a target roast curve — charge, turning point, drying/Maillard/development phase splits, RoR shape, first-crack timing, and development-time ratio — for a specific green lot and target roast level, anchored to the lot's inventory record.

## Inputs

- Green lot ID (from `/track-green-lot`) including processing, density/screen, **moisture % and water activity**, crop year.
- Roaster + last calibration date (BT probe); roaster capacity and batch (charge) weight.
- Target roast level (e.g. light / City / Full City) and intent (filter, espresso, single-origin clarity, blend component).
- Ambient conditions (helpful for repeatability) and target total roast time, if constrained.

## Steps

1. Read `context/concepts.md` ("three phases", "RoR, crash & flick") and `context/references.md` (phase markers, RoR/DTR targets).
2. Confirm the lot is in spec (aw < ~0.65, sane moisture). Denser / higher-grown / washed greens want more energy and tolerate a longer Maillard; flag if green needs profile adjustment.
3. Set charge temp and batch weight for the machine; predict the turning point.
4. Lay out phase targets: drying-end time, FC start time, and drop — and the **DTR** target (~15–25%, level-dependent). Sketch the intended RoR curve (peak after TP, smooth decline).
5. Translate to a gas/airflow plan: initial energy, the Maillard-phase glide, and the pre-FC heat reduction that *anticipates* the exothermic crash.
6. Tag the design with the lot ID and a profile version (e.g. v0.1 — candidate); note expected weight-loss band for the target level so `/calc-roast-loss` can check it.

## Output

`outputs/profiles/<sku-or-lot>-vX.Y-YYYY-MM-DD.md` — the target curve (markers + times + RoR shape), gas/airflow plan, machine + calibration reference, target level + DTR, expected weight-loss band, and the linked green lot ID. Marked "candidate" until cup-approved via Workflow A.

## Notes

- Temperatures are machine-relative; the design is a *target relative to your calibrated probe*, not absolute °C.
- Don't over-specify second crack for a light/medium target — design the drop by BT + time-in-development, not by chasing a temperature.
- A profile is only "golden" after it is sample-roasted, cupped, and versioned (Workflow A). This command produces a candidate.
