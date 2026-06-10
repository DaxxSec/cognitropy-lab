# Coffee Roasting Temperature Profiling Workspace

> Design and reproduce coffee roast curves — charge, turning point, drying/Maillard/development phases, rate-of-rise, first crack, development-time ratio — and wire every profile into green-coffee inventory and supply-chain tracking, so each roasted bag traces back to a green lot and a versioned profile, and every batch is reconciled in roast-loss, yield, and FIFO terms.

## What This Workspace Does

This is a Claude Code agent workspace for the two halves of a production roastery that are usually run in separate tools: **roast-profile development** and **green-inventory / supply-chain management**. On the roasting side it covers target-curve design, rate-of-rise shaping, defect diagnosis (crash, flick, stall, baking, tipping, scorching), roaster calibration, and batch-to-golden reproducibility scoring. On the inventory side it covers green-lot traceability, roast-loss/yield accounting, blend recipes, par/reorder planning, and demand-driven roast scheduling with FIFO drawdown.

What makes it distinct is that those two halves are treated as **one traceable production line**. The technique woven through every command is *inventory and supply-chain tracking*: a roast profile is a versioned artifact, a batch is an instance of running it on a specific green lot, and the act of roasting converts green inventory into roasted inventory at a measured yield. So `/calc-roast-loss` is both a quality signal (development) and an inventory move; `/track-green-lot` links a lot forward to every batch it produced *and* backward from any roasted SKU; `/forecast-roast-schedule` and `/plan-green-reorder` make sure the lot you dialed a profile in on is still on the shelf — and still in-crop — when demand calls for it.

The agent reads its domain knowledge from `context/`, runs ten bespoke commands for the recurring calculations, and saves every profile, batch log, reconciliation, blend recipe, and traceback to `outputs/` so the workspace becomes the roastery's traceable production record.

## Why This Workspace Exists

Roasteries lose money and quality in the seam between the cupping table and the spreadsheet. A profile is dialed in perfectly on a sample lot, then drifts batch-to-batch because the probe was never calibrated. A blend is costed on green price while it is sold on roasted weight, quietly eroding margin by the roast-loss percentage. A beautiful microlot is bought, roasted twice, and then forgotten until it is two crops old and bakes flat. And when a customer complains, nobody can say which green lot or profile version produced the bag in their hand. Each of these is a *traceability and inventory* failure dressed up as a roasting problem. Framing the whole operation as "green lot → versioned profile → roasted SKU, accounted at yield and consumed FIFO" makes the right questions unavoidable: which lot, which profile version, what yield, how much is left, and how stale is it.

## Getting Started

### Prerequisites

- **Roast logging:** a temperature-logging setup — [Artisan](https://artisan-scope.org/) (free/open-source) or a commercial platform ([Cropster](https://www.cropster.com/), [RoastLog](https://roastlog.com/)) — with at least a bean-probe channel; an environmental/ET channel and RoR display strongly recommended.
- **A calibrated scale** for green charge weight and roasted drop weight (roast loss is computed from these).
- **Green-lot data:** origin chain (country → region → farm/washing station → exporter → importer), ICO marks where available, certifications, processing method, screen size, moisture %, and water activity from the supplier spec sheet or a moisture/aw meter.
- **A demand signal:** roasted-SKU sales history or a forecast, plus supplier lead times, to drive scheduling and reorder.
- **Optional tooling:** a moisture/water-activity meter; an Agtron / color meter or SCA roast-color tiles; a spreadsheet or DB for the inventory ledger.

### Quick Start

1. Clone this workspace and open it with Claude Code.
2. Read `context/concepts.md` for roast phases, RoR/DTR, roast-loss, and the green-inventory + supply-chain model that frames every command.
3. Run `/calibrate-roaster` once per machine so bean-probe temperatures are comparable, then `/track-green-lot` to register the lot you are about to roast.
4. Design a curve with `/design-roast-profile`, sample-roast it, and use `/diagnose-roast-curve` + `/tune-rate-of-rise` to clean up the RoR and lock a golden profile.
5. In production, `/match-profile-batch` scores each batch against the golden, `/calc-roast-loss` posts the green→roasted inventory move, and `/forecast-roast-schedule` + `/plan-green-reorder` keep green on the shelf and in-crop.

## Command Reference

| Command | Description | When to Use |
|---------|-------------|-------------|
| `/design-roast-profile` | Target curve: charge, turning point, phase splits, RoR shape, FC timing, DTR for a lot + roast level | Starting a new lot or roast-level target |
| `/diagnose-roast-curve` | Detect crash, flick, stall, baking, tipping, scorching; assess RoR smoothness and DTR | After any roast that tasted off or logged a ragged curve |
| `/tune-rate-of-rise` | Re-schedule gas/airflow/drum to get a smooth declining RoR without crash/flick | Iterating a profile toward reproducibility |
| `/match-profile-batch` | Score a batch vs its golden profile; flag out-of-tolerance markers | Every production batch (QC + reproducibility) |
| `/calibrate-roaster` | Calibrate bean-probe vs ET, probe lag, ice-point/boiling references | New machine, new probe, or before cross-machine comparison |
| `/track-green-lot` | Register a lot with full origin chain, certs, moisture/aw, crop year; link batches both ways | At green intake and whenever a batch consumes the lot |
| `/calc-roast-loss` | Weight-loss %, green→roasted yield, reconcile vs development and inventory | Every batch drop; monthly inventory reconciliation |
| `/build-blend-recipe` | Compose a blend from component lots; per-lot consumption, landed+loss cost, drawdown | Creating or re-balancing a blend SKU |
| `/plan-green-reorder` | Par levels, reorder points, lead-time demand; crop-year staleness flags | Weekly inventory review; before placing green orders |
| `/forecast-roast-schedule` | Demand → green-consumption + roast-batch schedule; FIFO drawdown | Planning the roast week/month against sales |

## Directory Structure

```
coffee-roasting-temperature-profiling/
├── CLAUDE.md                 # Agent role, context refs, command list
├── README.md                 # This file
├── .claude/commands/         # 10 bespoke roasting + inventory commands
├── context/
│   ├── concepts.md           # Roast phases, RoR/DTR, defects, green coffee, inventory model
│   ├── workflows.md          # New-lot→profile, production reconciliation, forecast→procure, recall traceback
│   └── references.md         # Roast levels/Agtron, RoR/DTR targets, moisture/aw, inventory formulas, standards
├── prompts/                  # 5 reusable prompt templates
└── outputs/                  # Profiles, batch logs, reconciliations, blend recipes, reorder + traceback reports
```

## Example Use Cases

### Dialing in and locking a new washed Ethiopian microlot
`/track-green-lot` registers the lot (origin chain, 10.8% moisture, aw 0.54, current crop). `/design-roast-profile` sets a light-medium target (DTR ~20%, FC ~9:30); `/diagnose-roast-curve` catches a crash right after first crack, `/tune-rate-of-rise` smooths the gas step, and `/calc-roast-loss` confirms a 13.5% loss. The approved curve becomes profile v1.2, golden for that SKU.

### Catching margin leakage on a house espresso blend
`/build-blend-recipe` composes 60/30/10 from three lots, costs each component on **roasted** weight after its measured roast loss, and shows the blend's true landed cost per roasted kg is 14% above the back-of-envelope green-price estimate — then draws the three lots down in inventory and flags which one hits its reorder point first.

### Tracing a quality complaint back to source
A wholesale account reports a baked, flat batch. The recall traceback prompt walks SKU → roast date/batch ID → profile version → green lot → importer, `/diagnose-roast-curve` confirms a development-phase stall on that batch, and `/match-profile-batch` shows it was the only batch that week outside DTR tolerance — scoping the recall to a single day's production instead of the whole lot.

## Recommended MCP Servers / Tools

- **Filesystem MCP** — read exported roast logs (Artisan `.alog` / CSV), supplier spec sheets, and sales CSVs; write profiles, reconciliations, and reports to `outputs/`.
- **Fetch / web MCP** — pull current ICE Coffee "C" futures context, ICO indicator prices, and supplier/importer offer sheets at procurement time.
- **SQLite / database MCP (optional)** — back the green-and-roasted inventory ledger and the lot↔batch genealogy so traceback queries are exact rather than reconstructed.
- **Artisan / Cropster / RoastLog (local tools, not MCP)** — authoritative roast logging and profile libraries; this workspace structures the targets and interprets the exported curves.

## Legal & Ethical Considerations

- **Food safety & labeling:** roasted coffee is a food product. Roast date, net weight, country/region of origin, and any decaf process should be labeled per the applicable jurisdiction (e.g. US FDA / FALCPA, EU FIC 1169/2011). Keep moisture/water-activity records — high green water activity is a mold/ochratoxin-A risk.
- **Certification chain-of-custody:** Organic, Fairtrade, and Rainforest Alliance claims require segregated lots and documented mass-balance; do not let a blend or a re-bag break the certified-lot trail. Only make a claim the lot genealogy can substantiate.
- **Origin and pricing honesty:** single-origin and "direct trade" claims must match the traceability record. Differentials and premiums paid to producers are part of the supply-chain record this workspace keeps — represent them accurately.
- **Analysis, not a final spec:** temperatures here are machine-relative and the cost models are planning aids. Validate against your own calibrated equipment, cupping table, and accounting before committing production or purchase decisions.

## Technical References

- [Specialty Coffee Association (SCA)](https://sca.coffee/research) — cupping protocol, roast-color/Agtron standards, green-grading and defect definitions, water-activity guidance.
- [Artisan Roasterscope](https://artisan-scope.org/) — free/open-source roast-logging software; RoR, phase markers, and profile comparison/overlay.
- [International Coffee Organization (ICO)](https://www.ico.org/) — composite and group indicator prices, country/ICO-mark conventions, trade statistics.
- [ICE Coffee "C" (KC) Futures](https://www.ice.com/products/15/Coffee-C-Futures) — the Arabica benchmark that anchors differentials and forward/spot green pricing.
- *The Coffee Roaster's Companion* and *Coffee Roasting: Best Practices*, Scott Rao — the standard practitioner references for RoR shaping and development-time ratio.

## Optional plugin

If you have the [`workspace-foundational`](https://github.com/danielrosehill/Claude-Workspace-Foundational-Plugin) plugin installed, additional global commands (`/workspace-foundational:context-sweep`, `/workspace-foundational:find-template`) are available; the workspace works without it.
