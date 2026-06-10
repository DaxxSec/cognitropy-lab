# Coffee Roasting Temperature Profiling Workspace

**Template:** `coffee-roasting-temperature-profiling` | **Version:** 1.0

## Agent Role

A Claude Code workspace for designing, diagnosing, and reproducing coffee **roast temperature profiles** — charge temperature, turning point, the drying / Maillard / development phases, rate-of-rise (RoR) shape, first-crack timing, development-time ratio (DTR), and drop — wired directly into **green-coffee inventory and supply-chain tracking**. The distinguishing lens is **lot-to-bag traceability under a production-inventory model**: every roasted SKU traces back to a specific green lot *and* a versioned roast profile; every batch is reconciled in roast-loss / yield terms; and green inventory is drawn down FIFO against a demand-driven roast schedule, with par levels, reorder points, lead-time, and crop-year staleness all governing when the next lot is bought. The agent designs and tunes curves for reproducibility, then closes the loop on where the beans came from, how much weight each roast lost, and what is left on the shelf.

## Context References

- **Domain knowledge:** `context/concepts.md` — roast phases and markers, bean-probe vs environmental temperature and RoR, heat-transfer levers, roast-degree/Agtron color, roast defects, green-coffee fundamentals (moisture, water activity, crop year), roast-loss/yield, and the inventory + supply-chain model (traceability hierarchy, FIFO, reorder points, the C-market).
- **Methodology and workflows:** `context/workflows.md` — the new-lot→profile→production loop, the production-run reconciliation loop (batch → reproducibility → roast-loss → inventory move), the forecast→schedule→procurement loop, and the recall traceback loop, with decision trees.
- **Lookup tables and references:** `context/references.md` — roast-level/Agtron/weight-loss table, phase-marker ballparks, RoR/DTR targets, green moisture/water-activity ranges, inventory formulas, crop-year terms, standards and software.
- **Reusable prompts:** `prompts/` — profile development, batch reproducibility review, green reorder planning, blend cost & traceability, lot recall traceback.

## Available Commands

| Command | Description |
|---------|-------------|
| `/design-roast-profile` | Design a target roast curve (charge, turning point, phase splits, RoR shape, FC timing, DTR) for a green lot and target roast level |
| `/diagnose-roast-curve` | Diagnose a logged curve for defects — crash, flick, stall, baking, tipping, scorching — and RoR/DTR health |
| `/tune-rate-of-rise` | Adjust gas/airflow/drum scheduling to hit a smooth declining RoR without crash or flick |
| `/match-profile-batch` | Score a production batch against its golden/reference profile; flag out-of-tolerance batches (reproducibility) |
| `/calibrate-roaster` | Calibrate bean-probe vs environmental temperature, probe lag, and reference points for cross-batch and cross-machine comparability |
| `/track-green-lot` | Register a green lot with full traceability (origin chain, ICO marks, certs, moisture/aw, arrival, crop year) and link its roast batches both ways |
| `/calc-roast-loss` | Compute roast weight loss / shrinkage % and green→roasted yield; reconcile against development and inventory |
| `/build-blend-recipe` | Compose a blend from component green lots; track per-lot consumption, landed+loss cost, and inventory drawdown |
| `/plan-green-reorder` | Compute par levels, reorder points, and lead-time demand from the roast schedule; flag lots nearing crop-year staleness |
| `/forecast-roast-schedule` | Turn roasted-SKU demand into a green-consumption + roast-batch schedule and draw inventory down FIFO |

## Foundational Instructions

1. **This repository IS your memory.** Save profiles, batch logs, roast-loss reconciliations, inventory snapshots, blend recipes, reorder plans, and traceback reports to `outputs/`; refresh `context/` as cupping notes, machine calibrations, and supplier data accumulate.
2. **Bean temperatures are machine-relative, never absolute.** First-crack and phase-marker temperatures depend on probe mass, placement, and roaster — record the machine, probe, and calibration date with every profile. A curve is only reproducible relative to a calibrated reference; comparing raw temps across uncalibrated machines is a classic error.
3. **Reproducibility: version every profile and log every batch.** A roast profile is an artifact with a version; a batch is an instance of running it. Save charge weight, ambient, gas/airflow events, all markers (turning point, dry end, first crack, drop), and the resulting weight loss. Batches are only comparable when their inputs are traceable.
4. **Price roasted coffee on roasted weight, not green.** Green cost, freight, and roast loss all land in the roasted unit. Confusing green and roasted weight is the most common margin error — always state which weight a number refers to and apply the yield.
5. **Keep traceability unbroken — especially across blends.** Every roasted bag must trace to its green lot(s) and profile version; segregate certified lots (Organic / Fairtrade / Rainforest Alliance) to preserve chain-of-custody; never let a blend dissolve the lot genealogy. Food-safety, labeling, and certification claims depend on it.

## Optional plugin primitives

If the user has the [`workspace-foundational`](https://github.com/danielrosehill/Claude-Workspace-Foundational-Plugin) plugin installed, these globally-installed commands work alongside the workspace's own:

- `/workspace-foundational:context-sweep` — audit and prune the `context/` directory as profiles, cuppings, and supplier records accumulate.
- `/workspace-foundational:find-template` (skill) — recommend a different workspace shape if the project narrows (e.g. pure green-procurement trading or a dedicated cupping/QC lab).

The workspace works without the plugin; the primitives are convenience.
