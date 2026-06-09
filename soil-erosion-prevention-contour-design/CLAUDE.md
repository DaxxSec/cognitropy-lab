# Soil Erosion Prevention — Contour Design Workspace

**Template:** `soil-erosion-prevention-contour-design` | **Version:** 1.0

## Agent Role

A Claude Code workspace for designing contour-based water-erosion control on cultivated and graded slopes — contour cultivation, strip cropping, broadbase and bench terraces, grassed waterways, diversions, sediment basins, and gully check dams. The distinguishing lens is **capacity planning models**: every structure is treated as a capacity-constrained system where the *demand* is design-storm runoff and sediment, the *capacity* is hydraulic conveyance and storage volume, and the design target is to keep **utilization** below 1.0 with adequate **headroom** (freeboard / soil-loss-tolerance margin) across the planned service life. The agent sizes structures, finds the bottleneck reach, stress-tests against climate-intensified storms, and schedules maintenance as a capacity-refresh cadence driven by sediment fill and cover degradation.

## Context References

- **Domain knowledge:** `context/concepts.md` — RUSLE factors, soil-loss tolerance, runoff hydrology, the capacity-planning analogy, terrace/waterway/basin/check-dam fundamentals, permissible velocity, freeboard, failure modes.
- **Methodology and workflows:** `context/workflows.md` — the demand→budget→sizing→utilization→bottleneck→stress-test→maintenance phase sequence, with decision trees for practice selection.
- **Lookup tables and references:** `context/references.md` — K/C/P factors, permissible velocities, Manning's n, T-values, return-period guidance, runoff curve numbers, standards and handbooks.
- **Reusable prompts:** `prompts/` — field erosion assessment, capacity-plan narrative, practice selection, climate stress scenario, design-review audit.

## Available Commands

| Command | Description |
|---------|-------------|
| `/estimate-soil-loss` | Run RUSLE (A = R·K·LS·C·P) and compare predicted loss against the soil-loss tolerance T (the erosion capacity budget) |
| `/layout-contour-lines` | Lay out contour or key lines from a DEM/survey; decide on-contour vs graded and set the channel grade |
| `/design-terrace-interval` | Compute vertical/horizontal terrace spacing and channel grade for the slope, soil, and rainfall |
| `/size-grassed-waterway` | Size a vegetated waterway: peak runoff demand vs Manning conveyance capacity, permissible-velocity check, cross-section |
| `/forecast-runoff-capacity` | Capacity-planning core — design-storm demand vs conveyance/storage capacity across return periods; utilization, headroom, overtopping risk |
| `/plan-sediment-basin` | Size a sediment basin: trap efficiency, sediment-yield demand, storage drawdown → design life and cleanout cadence |
| `/space-check-dams` | Design a check-dam series in a gully: spacing by the head-to-toe rule, effective grade reduction, storage behind each |
| `/budget-infiltration` | Compare rainfall intensity (IDF) against soil infiltration capacity (Horton/Green-Ampt) to size the runoff the contour system must intercept |
| `/stress-test-design-storm` | Scenario stress test — scale storms for climate intensification / higher return periods, re-rank utilization, flag the first structure to fail |
| `/schedule-maintenance-capacity` | Build a capacity-refresh maintenance calendar tied to remaining structure capacity (sediment fill, cover loss, channel re-grading) |

## Foundational Instructions

1. **This repository IS your memory.** Save soil-loss runs, sizing calcs, capacity tables, stress-test results, and maintenance schedules to `outputs/`; refresh `context/` as field surveys, rainfall records, and as-built data accumulate.
2. **Design to a stated return period and write it down.** A structure sized to a 10-yr storm is a different artifact from one sized to a 25-yr storm. Every capacity number is meaningless without its design storm, and overtopping at a higher recurrence is a *known* residual risk, not a failure — record it.
3. **Predicted loss must stay at or below the soil-loss tolerance T.** RUSLE estimates an average annual rate; T is the capacity budget. A design that leaves A ≤ T is adequate, A > T is over-utilized. State both numbers and their units (t/ac/yr or t/ha/yr) explicitly.
4. **Reproducibility: log every factor and assumption.** R-factor source, K from survey vs estimated, LS slope length and steepness, the cover scenario behind C, the support practice behind P, the runoff curve number / rational C, and Manning's n. Erosion estimates are only comparable when their inputs are traceable.
5. **Engineering judgment over a single equation.** RUSLE is empirical and was not built for gully/ephemeral erosion, construction sites, or sub-field routing. Cross-check against site observation, name the equation's domain of validity, and recommend a stamped engineer's review before any structure is built.

## Optional plugin primitives

If the user has the [`workspace-foundational`](https://github.com/danielrosehill/Claude-Workspace-Foundational-Plugin) plugin installed, these globally-installed commands work alongside the workspace's own:

- `/workspace-foundational:context-sweep` — audit and prune the `context/` directory as surveys and as-builts accumulate.
- `/workspace-foundational:find-template` (skill) — recommend a different workspace shape if the project narrows (e.g. dedicated stormwater detention or stream-restoration work).

The workspace works without the plugin; the primitives are convenience.
