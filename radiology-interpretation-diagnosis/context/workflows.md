# Radiology Interpretation Diagnosis — Workflows and Methodology

Step-by-step procedures the agent runs, tied to today's technique: **Failure Mode and Effects Analysis (FMEA)**. `concepts.md` is *what things are*; this file is *what the agent does with them*.

## Workflow 1: The systematic read (per batch)

**Goal:** Convert a batch of spheres into a structured, action-bearing report without satisficing.

### Steps

1. **Adequacy gate** (`/study-quality`). Confirm: alginate rested/degassed; concentrations in range; base pH ≥ 3.6 (buffered if not); bath salt + % correct; bath fresh/calibrated. If non-diagnostic → **stop and remake**; do not "read" a prep error as a defect.
2. **Search pattern** (`/read-batch`). Sweep the fixed path in order, logging a *finding* at each station even if "normal":
   - **Shape** — round / tailed / teardrop / dimpled / collapsed.
   - **Membrane** — thickness, uniformity, thin spots, full-gel (rubbery) zones.
   - **Surface** — smooth / wrinkled / cloudy / grainy / weeping (syneresis).
   - **Buoyancy** — sinks (good) / floats (air entrapment).
   - **Burst** — squeeze/bite test: clean liquid release / no burst / premature leak.
   - **Flavor** — true to base / bitter-metallic (CaCl₂ carry-over) / dilute.
3. **Differential** (`/differential`). For each non-normal finding, pull its **gamut** from `references.md` and rank candidate process causes by likelihood given the recipe.
4. **Categorize** (`/sphere-rads`). Assign the worst-applicable Sphere-RADS 0–5 and read off its management action.
5. **Report** (`/structured-report`). Emit Technique → Findings → Impression → Category → Corrective action → Re-test interval. Save to `outputs/`.

### Decision Points

- If the adequacy gate fails: remake; the read is invalid.
- If two findings co-occur (e.g. float + thin membrane): record **both** differentials — beware satisfaction of search.
- If the category is RADS-3+ : route the dominant cause into the FMEA (Workflow 2) so it is tracked, not just fixed once.

## Workflow 2: Build/maintain the process FMEA (the technique)

**Goal:** Rank spherification failure modes by risk so corrective effort goes where RPN is highest.

### Steps

1. **Scope** the process steps (hydrate alginate → rest/degas → buffer base → dose calcium → form droplets → bath → rinse → hold/plate).
2. For each step, **enumerate failure modes** (under-rested, under-buffered, over-bathed, under-dosed Ca, hard-water bath, poor rinse…) and their **effects** on the plate/guest.
3. **Score** each on 1–10: **Severity** (effect), **Occurrence** (frequency, informed by `/read-batch` history), **Detection** (10 = nearly impossible to catch pre-service).
4. Compute **RPN = S × O × D**; optionally add **AIAG-VDA Action Priority (H/M/L)**.
5. **Rank descending**; assign a corrective action + owner to every High-AP / top-RPN item. Detection improvements (a float test, a pH check) lower D even when S and O are fixed.
6. **Re-score** after actions land; track the RPN trend in `outputs/`.

### Decision Points

- If Severity = 9–10 (e.g. allergen mislabel, choking-size sphere): act regardless of RPN.
- If RPN is high but driven by **Detection**: add an inspection step rather than re-engineering the recipe.
- If a defect recurs after action: the cause was misdiagnosed — re-run the differential, don't just re-score.

## Workflow 3: Method-selection decision tree (`/select-method`)

**Goal:** Choose the appropriate spherification method for a given liquid — the "appropriateness criteria" consult.

```
Is the base acidic (pH < 3.6)?
  └─ yes → buffer with sodium citrate. Still acidic/alcoholic? → REVERSE.
Is the base high-calcium or dairy/alcoholic?
  └─ yes → REVERSE (calcium already present / alginate won't behave in the base).
Do you need large, perfectly round spheres or make-ahead storage?
  └─ yes → FROZEN REVERSE.
Is the base thin/watery (tails when dropped)?
  └─ yes → add xanthan to ~0.2% first, then choose by the rules above.
Otherwise (neutral, low-Ca, serve-immediately caviar) → BASIC.
```

Output a method + a starting recipe (alginate %, calcium salt + %, bath time band, buffer/viscosity adds) and the *reason*, then hand off to `/membrane-titration` to lock the bath window.

## Workflow 4: Double-read & discordance (`/double-read`)

**Goal:** Quantify and reconcile inter-taster disagreement on subjective findings (burst, texture).

### Steps

1. Two tasters independently score the same N spheres on the agreed scale (blind to each other).
2. Compute agreement: % concordance and **Cohen's κ** (κ<0.4 poor, 0.4–0.6 moderate, 0.6–0.8 good, >0.8 excellent).
3. For discordant spheres, surface them together; identify whether the disagreement is **definition drift** (what counts as "burst"?) or **real variability** in the batch.
4. Tighten the scale definition or re-baseline; record the κ trend so the QA scale itself improves.

## Methodology Phases (the read, as a pipeline)

### Phase 1 — Acquisition
Make the batch under a pinned recipe; this is the "scan." Garbage acquisition → non-diagnostic study.

### Phase 2 — Quality assurance
The adequacy gate. Equivalent to a radiographer rejecting an under-exposed film before it reaches the reading room.

### Phase 3 — Interpretation
Search pattern + differential. Findings are described, then explained.

### Phase 4 — Reporting & categorization
Sphere-RADS + structured report — the standardized, actionable deliverable.

### Phase 5 — Quality governance
Double-read, FMEA, and error-rounds close the loop so the *process* improves, not just the single batch.
