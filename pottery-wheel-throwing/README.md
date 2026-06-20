# Pottery Wheel Throwing Workspace

> Run a throwing studio like a signalized intersection — time the kiln like a traffic light, and let the throughput optimization double as the environmental one.

## What This Workspace Does

This is an operations workspace for potters who throw at scale: production potters filling wholesale orders, teaching studios juggling shared wheels and a single kiln, and small ceramics businesses trying to fire more pots without burning more kilowatt-hours. It borrows its entire toolkit from **traffic-engineering signal timing** — the discipline that decides how long each light stays green at a busy intersection — and applies it to the studio's real bottlenecks: the wheel, the drying rack, the trimming bench, and above all the kiln.

The mapping is exact enough to be useful. A signal serves a *queue* of vehicles in repeating *cycles*, splitting *green time* between competing movements, and an engineer tunes the *cycle length* and *offsets* to maximize throughput and minimize delay. A studio serves a queue of greenware: the kiln fires a batch every cycle, the potter splits time between forms, and pieces wait at leather-hard and bone-dry stages exactly like cars at a red. **Webster's optimal cycle-length formula, saturation flow rate, and queue-delay models are not metaphors here — they are run with the studio's measured stage times.**

On top of the flow analysis sits an **environmental impact assessment** lens (the engine's technique for this build). Every command accounts for clay, water, firing energy, and glaze chemistry. The payoff is a genuine convergence rather than a tradeoff: because a kiln firing costs roughly the same energy whether it is half full or packed, the single move that most increases throughput — **maximizing kiln load density** — is also the single move that most cuts per-piece carbon. Optimizing the studio as a flow system and optimizing it as an environmental system turn out to be the same project.

## Why This Workspace Exists

Most studio "efficiency" advice is folk wisdom: throw faster, dry on a rack, don't open the kiln early. None of it tells a studio *where its actual bottleneck is* or *what a marginal wheel versus a marginal kiln would buy*. Traffic engineering answers exactly those questions for road networks, with a century of validated math. This workspace ports that math so a studio can stop guessing — identify the controlling constraint, quantify the delay it imposes, and price the fix — while keeping the environmental cost of every choice in view, since for ceramics that cost is dominated by the kiln and hidden in the glaze.

## Getting Started

### Prerequisites

- A studio you can measure: number of wheels, drying capacity, and **kiln model + interior cubic footage**.
- A stopwatch or a few logged sessions: real per-stage durations (centering, pulling, trimming) for your typical forms.
- Your kiln's energy data: rated kW, a measured kWh per firing if you have a meter, and your electric tariff or gas price.
- Glaze recipes (by material, in percent) for anything food-contact or sprayed.

### Quick Start

1. Clone this workspace and drop your studio's stage-time log and kiln spec into `context/` (or `outputs/raw-logs/`).
2. Run `/throwing-saturation-flow` to estimate each stage's capacity and surface the bottleneck — it is almost always the kiln.
3. Run `/kiln-load-density` then `/kiln-phase-split` to set how the kiln's "green time" is allocated across bisque and glaze firings.
4. Run `/cycle-length-optimize` and `/green-wave-schedule` to set the studio's batch cadence and stage handoffs.
5. Run `/footprint-per-piece` on a representative form to get a cradle-to-gate footprint and confirm the throughput plan also lowered the per-piece impact.

## Command Reference

| Command | Description | When to Use |
|---------|-------------|-------------|
| `/cycle-length-optimize` | Webster optimal cycle length for the studio's production batch | Setting the master cadence for a production week |
| `/throwing-saturation-flow` | Saturation flow rate + practical capacity per stage | First diagnostic; finds the bottleneck stage |
| `/kiln-phase-split` | Allocate firing capacity across bisque/glaze and product lines | Planning the firing calendar for a mixed product mix |
| `/kiln-load-density` | Maximize pieces per firing via stacking/shelf optimization | Before any firing; the core throughput+footprint lever |
| `/green-wave-schedule` | Offset-coordinate stages so a batch flows without waiting | Scheduling a specific order through the pipeline |
| `/bottleneck-delay-analysis` | Per-piece delay per queue + wheel-vs-kiln investment math | Deciding what equipment to buy next |
| `/footprint-per-piece` | Cradle-to-gate EIA per finished piece | Quoting eco-claims; comparing forms or processes |
| `/clay-reclaim-balance` | Clay mass balance and reclaim-rate model | Cutting clay/water waste; sizing a reclaim workflow |
| `/glaze-hazard-screen` | Toxicity, food-safety leaching, waste-water screen of a recipe | Before selling or food-using any new glaze |
| `/firing-energy-audit` | kWh/therm audit, soak losses, electric-vs-gas CO₂e | Lowering the firing footprint or the energy bill |

## Directory Structure

```
pottery-wheel-throwing/
├── CLAUDE.md                 # Agent role, context refs, command list
├── README.md                 # This file
├── .claude/commands/         # 10 bespoke studio-flow + EIA commands
├── context/
│   ├── concepts.md           # Throwing stages, traffic→pottery mapping, signal-timing math, ceramics LCA
│   ├── workflows.md          # Flow optimization, kiln optimization, ISO 14040 production-run EIA
│   └── references.md         # Cone chart, stage times, kiln energy, glaze hazards, formula cheat-sheet
├── prompts/                  # 5 reusable prompt templates
└── outputs/                  # Generated schedules, footprint reports, audits
```

## Example Use Cases

### A teaching studio with 8 wheels and one kiln is "always backed up"
`/throwing-saturation-flow` shows the wheels can produce far more greenware than the single kiln can fire — the kiln is oversaturated. `/bottleneck-delay-analysis` prices a second kiln against a drying cabinet and shows the kiln pays back; the wheels were never the problem.

### A production potter wants to fire fewer times per month without cutting output
`/kiln-load-density` re-stacks the kiln to fit 38 mugs instead of 26 per firing; `/firing-energy-audit` confirms the kWh-per-mug drops by a third and one firing per week disappears. The footprint and the electric bill fall together.

### A maker is about to sell a bright-yellow dinnerware glaze
`/glaze-hazard-screen` flags the colorant as a cadmium-bearing stain with food-contact leaching risk, recommends an ASTM C738 leach test, and proposes a liner-glaze strategy for the food surface before anything ships.

### A studio wants to put a credible "low-carbon" claim on its packaging
`/footprint-per-piece` runs a cradle-to-gate EIA on the flagship bowl with an explicit functional unit and boundary, attributing the dominant share to firing energy and giving a defensible number instead of a marketing guess.

## Recommended MCP Servers

- **Filesystem / repo MCP** — read stage-time logs and kiln meter exports from `context/` and write reports to `outputs/`.
- **Spreadsheet / CSV MCP** — ingest firing logs, energy-meter CSVs, and glaze-recipe sheets for the saturation-flow and footprint math.
- **Web/fetch MCP** — pull current grid CO₂e intensity (e.g. from a national grid carbon API) and glaze-material safety data at assessment time.

## Legal & Ethical Considerations

- **Respirable crystalline silica** is a confirmed carcinogen. Dry clay, glaze materials, and kiln-wash all contain it; the OSHA PEL is 50 µg/m³ (8-hr TWA), action level 25 µg/m³. Any workflow recommendation must keep dust-control (wet methods, HEPA, no dry sweeping) in scope.
- **Food-safety leaching.** Glazes on food-contact surfaces must not leach lead or cadmium above FDA limits. Treat `/glaze-hazard-screen` output as advisory, not a substitute for a lab leach test (ASTM C738 / C895).
- **Hazardous glaze materials** — lead, barium carbonate, cadmium, lithium carbonate, and many colorant oxides are toxic in raw form and in studio waste water. Follow local hazardous-waste rules; do not pour glaze slurry down a domestic drain.
- This workspace gives engineering and operations analysis. It does not replace a certified ceramics-materials lab, an occupational-hygiene assessment, or a registered traffic engineer's judgment for any actual roadway.

## Technical References

- [Orton Cone Chart](https://www.ortonceramic.com/files/2785/File/cone-chart-2016.pdf) — cone numbers to temperature at standard heat-rise.
- [Highway Capacity Manual (TRB)](https://www.trb.org/Main/Blurbs/175169.aspx) — saturation flow rate and signalized-intersection delay reference.
- [Webster, F.V. (1958) *Traffic Signal Settings*, Road Research Technical Paper No. 39](https://trid.trb.org/view/112216) — the optimal cycle-length formula.
- [ISO 14040 / 14044 — Life Cycle Assessment](https://www.iso.org/standard/37456.html) — functional unit, boundary, LCI/LCIA framework for the EIA.
- [Digitalfire Reference Database](https://digitalfire.com/) — glaze materials, oxides, food-safety, and firing chemistry.
- [OSHA Respirable Crystalline Silica standard (29 CFR 1910.1053)](https://www.osha.gov/silica-crystalline) — exposure limits and controls.

## Optional plugin

If you have the [`workspace-foundational`](https://github.com/danielrosehill/Claude-Workspace-Foundational-Plugin) plugin installed, additional global commands (`/workspace-foundational:context-sweep`, `/workspace-foundational:find-template`) are available; the workspace works without it.
