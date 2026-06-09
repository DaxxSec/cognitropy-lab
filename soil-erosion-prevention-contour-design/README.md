# Soil Erosion Prevention — Contour Design Workspace

> Design contour-based water-erosion control — terraces, waterways, diversions, sediment basins, check dams — by treating every structure as a capacity-constrained system: storms are demand, conveyance and storage are capacity, and good design keeps utilization below 1.0 with headroom across its service life.

## What This Workspace Does

This is a Claude Code agent workspace for planning and sizing contour-based erosion control on cultivated and graded land. It covers the full toolkit — contour cultivation and strip cropping, broadbase/bench terraces, grassed waterways, diversions, sediment basins, and gully check dams — and grounds each decision in the (Revised) Universal Soil Loss Equation, runoff hydrology (rational and Curve-Number methods), and open-channel hydraulics (Manning, permissible velocity).

What makes it distinct is the **capacity-planning model** running through every command. Instead of just asking "how big is the channel," it asks "what is the *demand* (design-storm runoff, storm sediment yield, annual soil loss), what is the *capacity* (conveyance, storage volume, soil-loss tolerance), what is the *utilization* (demand ÷ capacity), how much *headroom* (freeboard, the T−A margin) is left, and where is the *bottleneck* that fails first?" Sediment that fills a basin over years is treated as **capacity drawdown**, and the cleanout/re-grading calendar is a **capacity-refresh cadence** — part of the design, not an afterthought.

The agent reads its domain knowledge from `context/`, runs ten bespoke commands for the recurring calculations, and saves every soil-loss run, sizing calc, capacity table, and maintenance schedule to `outputs/` so the workspace accumulates a traceable design record.

## Why This Workspace Exists

Erosion control fails in two predictable ways: a structure that meets a flow target but scours because nobody checked velocity, and a structure that was sized correctly on day one but silted to zero because nobody scheduled the cleanout. Both are capacity-management failures. Framing the whole problem as demand-vs-capacity-over-time makes the right questions unavoidable — what return period, what utilization, what headroom, which bottleneck, what refresh cadence — and forces the residual (above-design) risk to be written down instead of discovered during the next big storm.

## Getting Started

### Prerequisites

- **Site data:** slope (%), slope length, drainage area, and concentrated-flow paths (from a DEM, contour survey, or field walk).
- **Soil data:** soil mapping unit → erodibility K, soil-loss tolerance T, hydrologic soil group (e.g. from USDA Web Soil Survey or local equivalent).
- **Climate data:** R-factor and IDF / return-period rainfall depths (e.g. NOAA Atlas 14 in the US, or a local IDF source).
- **Optional tooling:** RUSLE2 for authoritative soil-loss runs; a DEM/GIS tool (QGIS) for contour and flow-path extraction; a spreadsheet for the capacity tables.

### Quick Start

1. Clone this workspace and open it with Claude Code.
2. Read `context/concepts.md` for the RUSLE factors, runoff methods, and the capacity-planning analogy that frames every command.
3. Run `/estimate-soil-loss` with your slope, soil, cover, and practice to get the do-nothing soil loss A and its utilization A/T.
4. Walk the practice-selection decision tree in `context/workflows.md`, then size structures with `/design-terrace-interval`, `/size-grassed-waterway`, or `/space-check-dams`.
5. Run `/forecast-runoff-capacity`, build the utilization/headroom table, then `/stress-test-design-storm` to find the bottleneck and residual risk.

## Command Reference

| Command | Description | When to Use |
|---------|-------------|-------------|
| `/estimate-soil-loss` | RUSLE A = R·K·LS·C·P vs soil-loss tolerance T | First pass on any field; before/after practice comparison |
| `/layout-contour-lines` | Contour/key-line layout from DEM/survey; on-contour vs graded + channel grade | Setting alignments before terrace/waterway sizing |
| `/design-terrace-interval` | Terrace vertical/horizontal spacing and channel grade | Long-slope fields where LS is the dominant driver |
| `/size-grassed-waterway` | Peak runoff vs Manning conveyance, permissible-velocity check, cross-section | Concentrated flow in a natural drainageway |
| `/forecast-runoff-capacity` | Demand vs capacity across return periods; utilization, headroom, overtopping risk | Core capacity check for any conveyance/storage structure |
| `/plan-sediment-basin` | Trap efficiency, sediment-yield demand, storage drawdown → design life + cleanout | Where settling/detention is needed and silting governs |
| `/space-check-dams` | Check-dam series spacing (head-to-toe), effective grade, storage | Active or ephemeral gullies |
| `/budget-infiltration` | Rainfall intensity vs infiltration capacity → excess runoff to intercept | Establishing the runoff demand the contour system must handle |
| `/stress-test-design-storm` | Scale storms for climate/return-period; re-rank utilization; find first failure | After sizing, to quantify residual risk and the bottleneck |
| `/schedule-maintenance-capacity` | Capacity-refresh calendar from sediment fill / cover loss / re-grading | Turning a sized design into an operable, maintained system |

## Directory Structure

```
soil-erosion-prevention-contour-design/
├── CLAUDE.md                 # Agent role, context refs, command list
├── README.md                 # This file
├── .claude/commands/         # 10 bespoke erosion/capacity commands
├── context/
│   ├── concepts.md           # RUSLE, runoff, hydraulics, the capacity analogy
│   ├── workflows.md          # Demand→budget→sizing→utilization→bottleneck→stress→refresh
│   └── references.md         # K/C/P, permissible velocity, Manning n, T, CN, IDF
├── prompts/                  # 5 reusable prompt templates
└── outputs/                  # Generated soil-loss runs, sizing calcs, capacity tables
```

## Example Use Cases

### Bringing a row-crop field within tolerance
A 6%, 250 m slope under conventional-till row crop runs RUSLE A well above T. `/estimate-soil-loss` quantifies the gap, the decision tree recommends no-till + contour strip cropping, and a re-run shows A back under T with the margin documented.

### Sizing a grassed waterway for a swale that gullies every spring
`/budget-infiltration` and `/forecast-runoff-capacity` set the 10-yr peak demand; `/size-grassed-waterway` returns a parabolic cross-section whose conveyance carries it with freeboard *and* keeps mean velocity under the grass-cover permissible limit.

### Planning a sediment basin's whole life, not just day one
`/plan-sediment-basin` sizes live storage from MUSLE sediment yield and Brune trap efficiency, then projects storage drawdown to a design life and a cleanout cadence that `/schedule-maintenance-capacity` folds into an operable calendar.

## Recommended MCP Servers / Tools

- **Filesystem MCP** — read DEM exports, soil-survey CSVs, and IDF tables; write capacity tables and reports to `outputs/`.
- **Fetch / web MCP** — pull NOAA Atlas 14 rainfall-frequency values and NRCS practice standards at design time.
- **RUSLE2 / QGIS (local tools, not MCP)** — authoritative soil-loss modeling and DEM-based contour/flow-path extraction; the workspace structures the inputs and interprets the outputs.

## Legal & Ethical Considerations

- Structures that impound or discharge water may trigger local stormwater, dam-safety, and wetland/clean-water permitting — flag for jurisdictional review before construction.
- Designs that condition cost-share funding (e.g. NRCS conservation practice standards) must be built to the applicable standard.
- This workspace produces analysis and preliminary sizing. Constructed water-control structures should carry a licensed engineer's review/stamp where the jurisdiction requires it; do not treat its output as a final stamped design.

## Technical References

- [USDA-ARS RUSLE2](https://www.ars.usda.gov/southeast-area/oxford-ms/national-sedimentation-laboratory/watershed-physical-processes-research/research/rusle2/) — current process-based soil-loss model and factor databases.
- [NRCS National Engineering Handbook](https://directives.sc.egov.usda.gov/) — hydrology (Part 630, CN method) and the Engineering Field Handbook (Part 650: terraces, waterways, diversions).
- [NOAA Atlas 14 Precipitation Frequency](https://hdsc.nws.noaa.gov/pfds/) — IDF and return-period rainfall depths for design storms.
- [USDA Web Soil Survey](https://websoilsurvey.nrcs.usda.gov/) — site-specific erodibility K, soil-loss tolerance T, and hydrologic soil group.

## Optional plugin

If you have the [`workspace-foundational`](https://github.com/danielrosehill/Claude-Workspace-Foundational-Plugin) plugin installed, additional global commands (`/workspace-foundational:context-sweep`, `/workspace-foundational:find-template`) are available; the workspace works without it.
