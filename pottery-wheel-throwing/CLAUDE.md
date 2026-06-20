# Pottery Wheel Throwing Workspace

**Template:** `pottery-wheel-throwing` | **Version:** 1.0

A Claude Code workspace for the working potter and ceramics-studio operator that treats a throwing studio as a **flow system** and optimizes it with **traffic-engineering signal-timing methodology** — cycle length, phase splits, offsets, saturation flow, and queue delay — while running an **environmental impact assessment** on every stage. The governing insight: a kiln is a *signalized batch server*. It clears a queue of greenware in discrete firing cycles exactly the way a signal clears a queue of vehicles, so the same math that times an intersection times a studio. And because firing energy dominates a piece's footprint, packing the kiln full (maximizing "saturation flow") is simultaneously the biggest throughput lever *and* the biggest footprint lever — the two optimizations converge.

## Context References

- **Domain knowledge:** `context/concepts.md` — throwing stages, the traffic→pottery mapping, signal-timing formulas, kiln-as-batch-server, ceramics LCA/EIA fundamentals, glaze hazards.
- **Methodology and workflows:** `context/workflows.md` — studio flow optimization (Webster cycle → split → green wave), kiln capacity/footprint optimization, and the ISO 14040 production-run EIA.
- **Lookup tables and references:** `context/references.md` — cone chart, stage durations, kiln energy figures, glaze hazard limits, traffic formula cheat-sheet, grid CO₂e.
- **Reusable prompts:** `prompts/`

## Available Commands

| Command | Description |
|---------|-------------|
| `/cycle-length-optimize` | Compute the optimal studio production-cycle length (Webster's formula) for max throughput |
| `/throwing-saturation-flow` | Estimate the saturation flow rate of each stage and find the practical bottleneck |
| `/kiln-phase-split` | Allocate kiln "green time" across bisque/glaze firings and product lines |
| `/kiln-load-density` | Optimize kiln stacking to maximize pieces per firing (throughput + footprint lever) |
| `/green-wave-schedule` | Coordinate stage offsets so a batch flows wheel→dry→trim→bisque→glaze→fire without queueing |
| `/bottleneck-delay-analysis` | Quantify per-piece delay at each queue and the capacity-investment decision (wheel vs kiln) |
| `/footprint-per-piece` | Run a per-piece environmental impact assessment: clay, water, firing energy, glaze |
| `/clay-reclaim-balance` | Model the clay mass balance (trimmings, slurry, fails) and reclaim rate |
| `/glaze-hazard-screen` | Screen a glaze recipe for toxic materials, food-safety leaching, and waste-water risk |
| `/firing-energy-audit` | Audit kiln firing energy (kWh/therms, soak losses, electric vs gas CO₂e) |

## Foundational Instructions

1. **This repository IS your memory.** Save studio assessments, firing schedules, and footprint reports to `outputs/`; refine `context/` as the studio's real stage durations and kiln data accumulate. A measured saturation flow beats a textbook one.
2. **State the functional unit and system boundary before every EIA.** "Per finished mug, cradle-to-gate" is an assessment; "this run seems wasteful" is a vibe. Without an explicit functional unit and boundary (ISO 14040), footprint numbers are not comparable.
3. **Honor the convergence, don't fake it.** The traffic→pottery mapping is a genuine analogy, not decoration. When you invoke Webster's cycle length or saturation flow, use the real formula with real stage data — don't hand-wave the math to force a metaphor.
4. **Safety and food-safety are non-negotiable.** Flag respirable silica (OSHA PEL 50 µg/m³), lead/barium/cadmium glaze hazards, and food-contact leaching limits whenever a recipe or process touches them. A throughput gain that ships a leaching glaze is a failure.
5. **Reproducibility.** Cite cone schedules, kiln model + cubic footage, and measured kWh from real firings — not remembered approximations. Note electric-vs-gas and the grid CO₂e factor used.

## Optional plugin primitives

If the user has the [`workspace-foundational`](https://github.com/danielrosehill/Claude-Workspace-Foundational-Plugin) plugin installed, these globally-installed commands are available alongside the workspace's own:

- `/workspace-foundational:context-sweep` — audit and prune the `context/` directory as the studio's data grows.
- `/workspace-foundational:find-template` (skill) — recommend a more specific workspace shape if the project narrows (e.g. kiln-energy-only, glaze-chemistry-only).

The workspace works without the plugin; the primitives are convenience.
