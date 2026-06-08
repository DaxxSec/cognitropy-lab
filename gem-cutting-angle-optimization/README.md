# Gem Cutting Angle Optimization Workspace

> Optimize faceting angles for maximum light return — and keep the machine inside the tolerance band those angles demand with predictive maintenance scheduling.

## What This Workspace Does

Faceting a gemstone is an optics problem solved with a machine. The **angles** of the pavilion (bottom) and crown (top) facets decide whether light entering the table reflects back to the eye as brilliance or leaks out the bottom as a dull "window." Those angles are dictated by the material's **refractive index** through the **critical angle** for total internal reflection. This workspace computes the optimal angles for a given rough, adapts published cutting designs across materials, and grades finished proportions against the standards used in the trade.

But an optimal angle is only as good as the machine's ability to *hold* it. A faceting machine that has drifted — a spindle with excess runout, a master lap that has worn dished, an index gear with backlash — silently corrupts the angle at the lap, turning a calculated 40.8° pavilion into a windowing 39.9°. So the second half of this workspace treats the machine as a monitored asset: it trends spindle runout, lap flatness, and grit wear, allocates an **angle-error budget** across those sources, and schedules **predictive maintenance** to intervene *before* degradation crosses the budget — not after a stone is scrapped.

The two halves are one loop: optimization sets the tolerance the machine must meet; condition monitoring decides whether it still can.

## Why This Workspace Exists

Most faceting guidance treats optics and machine upkeep as separate disciplines — angle charts in one book, machine manuals in another. In practice they are coupled by a single quantity: the **angle-error budget**. Cutters lose stones not because they chose the wrong angle but because the bench could no longer deliver the angle they chose. This workspace codifies that coupling so the question "can I cut this design tonight?" is answered by both the optics *and* the current machine condition, together.

## Getting Started

### Prerequisites

- A faceting machine (Ultra Tec, Facetron, VJ, Graves, or similar) with a protractor/angle scale and index gear (96, 80, 64, or 32 splits)
- A dial test indicator (0.0001" or 1 µm resolution) and a small surface plate or reference flat for runout and lap-flatness checks
- The refractive index of the material you intend to cut (see `context/references.md`)
- Optional: [GemCad](http://www.gemcad.com/) / GemRay for design files and ray-trace previews, a refractometer for unknown rough

### Quick Start

1. Clone this workspace
2. Run `/critical-angle-calc` with your material's refractive index to get the critical angle and the minimum safe pavilion angle
3. Run `/optimize-pavilion-angle` to pick the pavilion main that maximizes light return for that material
4. Run `/tolerance-budget`, then `/spindle-runout-trend` and `/lap-wear-forecast`, to confirm the machine can currently hold that angle
5. Cut; afterward run `/cut-grade-check` on the finished proportions and `/pdm-schedule` to log condition and queue any maintenance

## Command Reference

| Command | Description | When to Use |
|---------|-------------|-------------|
| `/critical-angle-calc` | Critical angle + minimum pavilion from RI | First step for any new material |
| `/optimize-pavilion-angle` | Pavilion main that maximizes light return | Choosing the working pavilion angle |
| `/tangent-ratio-adapt` | Port a design across refractive indices | Cutting a published design in a different material |
| `/light-return-map` | Brilliance/fire/scintillation over an angle grid | Trading off fire vs brilliance; choosing crown angle |
| `/cut-grade-check` | Grade proportions vs GIA-style tolerances | After cutting, or before committing a design |
| `/tolerance-budget` | Allocate the angle-error budget | Before cutting fine work; after any machine change |
| `/spindle-runout-trend` | Trend spindle TIR, forecast breach | Periodic condition check; runout suspected |
| `/lap-wear-forecast` | Forecast lap dressing/replacement | Polish quality dropping; planning lap purchases |
| `/pdm-schedule` | Build the predictive-maintenance plan | Weekly/monthly; after logging condition data |

## Directory Structure

```
gem-cutting-angle-optimization/
├── CLAUDE.md                 # Agent role, context refs, command list
├── README.md                 # This file
├── .claude/commands/         # Bespoke faceting + maintenance commands
├── context/
│   ├── concepts.md           # Faceting optics, machine anatomy, PdM fundamentals
│   ├── workflows.md          # Optimize-and-cut, design adaptation, condition→schedule
│   └── references.md         # RI/critical-angle table, lap grits, condition thresholds
├── prompts/                  # Reusable prompt templates
└── outputs/                  # Optimization runs, grade reports, maintenance logs
```

## Example Use Cases

### New rough, no chart for it
You have a parcel of a less-common material (say spessartine garnet at RI 1.79). `/critical-angle-calc` and `/optimize-pavilion-angle` give you a pavilion angle from first principles instead of guessing from a quartz chart.

### Porting a favorite quartz design to topaz
A design you love was cut for quartz (RI 1.544). `/tangent-ratio-adapt` rescales every angle to topaz (RI 1.62) so the light performance carries over instead of windowing.

### The stones keep coming out with a faint center window
`/tolerance-budget` plus `/spindle-runout-trend` reveal the spindle has drifted to 18 µm TIR, eating most of your angle budget — the angle math was fine; the machine wasn't. `/pdm-schedule` queues the bearing service.

### Polish quality falling off on a 3,000-grit lap
`/lap-wear-forecast` shows the lap is glazed and past its forecasted dressing point; you dress or recharge it on schedule instead of fighting it for three more stones.

## Recommended MCP Servers

- **Filesystem MCP** — persist optimization runs, grade reports, and the machine condition log under `outputs/` so trends accumulate across sessions.
- **Fetch / web MCP** — pull refractive-index and design data from the IGS gem encyclopedia and Facetdiagrams.org when a material isn't in the local table.

## Legal & Ethical Considerations

- **Material disclosure.** If you optimize a cut for a synthetic, treated, or assembled stone, record the treatment — cut optimization does not change a disclosure obligation when the stone is later sold.
- **Provenance.** Note the source of rough where known; some material (certain corundum, garnet, and colored stones) carries origin-disclosure expectations in the trade.

## Technical References

- [International Gem Society — Gemstone Refractive Index List](https://www.gemsociety.org/article/table-refractive-index-double-refraction-gems/) — RI values and faceting fundamentals.
- [Facetdiagrams.org](https://facetdiagrams.org/) — large free catalogue of GemCad faceting designs with per-material angles.
- [United States Faceters Guild (USFG)](https://usfacetersguild.org/) — design library, tangent-ratio guidance, competition standards.
- [GIA — Diamond Cut Grading](https://www.gia.edu/diamond-cut) — proportion tolerances behind `/cut-grade-check`.
- [Reliabilityweb — P-F Curve & Predictive Maintenance](https://reliabilityweb.com/) — condition-based maintenance and RUL background.

## Optional plugin

If you have the [`workspace-foundational`](https://github.com/danielrosehill/Claude-Workspace-Foundational-Plugin) plugin installed, additional global commands (`/workspace-foundational:context-sweep`, `/workspace-foundational:find-template`) are available; the workspace works without it.
