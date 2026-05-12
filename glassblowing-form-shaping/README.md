# Glassblowing Form Shaping Workspace

> An agent workspace for hot-glass artists who want to plan forms with simulation and scenario testing instead of intuition alone — and who want every gather, color rod, and lehr run logged with the same rigor a soil-microbiome research plot gets.

## What This Workspace Does

This workspace turns your studio into a half-lab, half-bench environment. Before you fire the glory hole, the agent helps you simulate a planned form: how many gathers, how much mass, how much working time you actually have before the gather drops below 850 °C, how the piece will sag under its own weight at each step, whether the proposed annealing schedule will hold given wall thickness and mass, and whether the colors you're planning to combine share a coefficient of expansion.

After (and during) the session, every working day becomes a **batch record** — a structured log inspired by how soil-microbiome researchers track plot interventions: glass batch IDs, color rod lots and suppliers, ambient studio temperature/humidity, glory hole soak temperature, lehr program, observed outcome, and any deviations. Months later, when a piece cracks unexpectedly, `/lineage-trace` and `/post-mortem` walk back through the batch records to find the root cause instead of guessing.

## Why This Workspace Exists

Most studios run on intuition and a tattered notebook. That works for the artist who's been making the same vase for fifteen years. It does not work for someone learning a new form, switching color suppliers, working a glass family they don't know well (Bullseye 90 vs. Effetre 104 vs. System 96 vs. borosilicate 33), or trying to reproduce a successful piece six months later. The two failure modes that this workspace is built to kill:

1. **Form failures the artist could have predicted.** A 1.4 kg gather with a planned 220 mm reach will sag asymmetrically once viscosity drops below 10⁵ poise — that's a calculation, not a surprise. `/form-sim` runs that calculation before you commit hot glass.
2. **Cracks no one can explain.** Six pieces from the same week cracked in the lehr, four months later, in storage. Was it a single bad rod lot? A subtle cool-curve change after the lehr controller firmware update? Without lineage, no one knows. With `/batch-log` and `/lineage-trace`, you can answer in minutes.

The microbiome metaphor isn't decoration. Soil microbiomes shift in non-obvious ways from upstream interventions; so do glass pieces. The discipline of tracking *every* input is what makes either field tractable.

## Getting Started

### Prerequisites
- A working studio with at least: glory hole, lehr (annealing oven) with programmable controller, marver, blowpipe(s) and punties, jacks/blocks/paddles
- Documented glass family in use (Bullseye COE 90, Effetre/Moretti COE 104, System 96, Schott Borosilicate 33, etc.)
- Access to the lehr's programmable schedule (segments + ramp rates) — needed for `/cool-curve`
- A way to record studio ambient temperature and humidity (a $20 hygrometer is enough)
- Optional but recommended: pyrometer or thermocouple in the glory hole, kitchen scale for gather mass estimates

### Quick Start
1. Clone this workspace into your studio's repo.
2. Run `/onboard` to capture your studio profile, glass families, lehr specs, and the form vocabulary you work in.
3. For the next piece, run `/form-sim` with a description (or sketch) of the target form before you light the glory hole.
4. Run `/scenario-test` against the result — at minimum a "gather drops 100 °C between heats" scenario.
5. After the session, `/batch-log` walks you through capturing the day as a tracked batch.
6. When something fails, `/post-mortem` plus `/lineage-trace` close the loop.

## Command Reference

| Command | Description | When to Use |
|---------|-------------|-------------|
| `/onboard` | Initialize studio profile, glass families, equipment, target form vocabulary | First time setup, or after a major studio change |
| `/form-sim` | End-to-end form simulation: gathers, mass, working time, viscosity per step, gravity sag | Before any new or unfamiliar form |
| `/scenario-test` | Apply perturbation scenarios (color rod break, punty failure, crash cool, devit onset, COE mismatch, gather over-mass) | After `/form-sim` passes — stress-test the plan |
| `/batch-log` | Open a session batch record with glass batch IDs, color lineage, environmental envelope, lehr program, outcome | At the start of every studio session |
| `/cool-curve` | Design or critique an annealing schedule given piece mass and max wall thickness | When piece geometry changes meaningfully, or after lehr-stage cracks |
| `/lineage-trace` | Walk material provenance from color rod lot to finished piece; flag repeated failure-by-input correlations | After two or more failures that may share an upstream cause |
| `/post-mortem` | Diagnose a failed piece against the failure-mode taxonomy; append finding to the originating batch record | After any unexpected crack, devit, color shift, or lehr-stage failure |

## Directory Structure

```
glassblowing-form-shaping/
├── CLAUDE.md                          # Agent role, command index, foundational rules
├── README.md                          # This file
├── CREATION_REPORT.md                 # Workspace creation provenance
├── context/
│   ├── project.md                     # Studio scope, target forms, project goals
│   ├── role.md                        # Artist's experience and operating context
│   ├── constraints.md                 # Studio constraints (glass families, lehr capacity, time)
│   └── for-agent/
│       ├── domain-knowledge.md        # Viscosity curves, COE families, failure taxonomy, microbiome documentation patterns
│       ├── workflows.md               # 4 core workflows: pre-session sim, in-session log, post-session closeout, post-mortem
│       ├── environment.md             # Studio equipment specs, lehr controller details
│       └── tools.md                   # Sim formulas, lehr program syntax, batch record schema
├── .claude/commands/
│   ├── onboard.md                     # Studio onboarding interview
│   ├── form-sim.md                    # Form simulation walkthrough
│   ├── scenario-test.md               # Perturbation scenarios
│   ├── batch-log.md                   # Session batch record open/close
│   ├── cool-curve.md                  # Annealing schedule design
│   ├── lineage-trace.md               # Material provenance trace
│   └── post-mortem.md                 # Failure diagnosis
├── prompts/
│   ├── new-form-design.md             # Template for a new form, sim-first
│   ├── color-incompatibility-check.md # Template for vetting a proposed color combo
│   └── studio-environment-envelope.md # Template for capturing studio ambient before a session
├── resources/
│   ├── glass-viscosity-reference.md   # Working/softening/annealing/strain temps for major COE families
│   ├── failure-mode-taxonomy.md       # Diagnostic decision tree for cracks/devit/color failures
│   └── batch-record-card.md           # Canonical batch record schema (microbiome-inspired)
├── planning/
│   └── plan.md                        # Active form plans
├── outputs/
│   └── .gitkeep                       # Generated form specs, post-mortems, lineage reports
├── user-docs/
│   ├── getting-started.md             # Studio-friendly walkthrough
│   └── microbiome-method-explained.md # Why a glass studio borrows from soil-research record-keeping
└── work-log/
    └── session-log.md                 # Session batch records, dated
```

## The Simulation Model in Brief

The simulator is intentionally simple — it has to run in your head, on paper, or in a markdown file, not in COMSOL.

### 1. Working Time Budget
Each gather has a thermal mass. Once it leaves the glory hole, it cools. Working time is the interval between leaving the glory hole and the surface dropping below the glass's *working point* (viscosity 10⁴ poise; ~1050 °C for soda-lime, ~1250 °C for borosilicate). The simulator estimates this from gather mass, ambient temperature, and the operations planned (marver, jack, block — each cools the surface by a known approximate ΔT).

### 2. Gravity Sag Risk
At a working temperature, glass behaves like a high-viscosity fluid. A horizontal extension of length L with cross-section A and density ρ ≈ 2.5 g/cm³ at viscosity η will sag at a rate proportional to ρgL²/η. The simulator flags any planned operation that exceeds an empirical threshold (different per form type — a goblet stem tolerates more sag than a flat plate's foot).

### 3. Cool Curve Risk
The lehr (annealing oven) holds the piece above its strain point (~480 °C for soda-lime), then ramps down slowly enough that the thermal gradient between surface and core never builds compressive stress that exceeds the glass's tensile strength. Empirical rule: ramp rate (°C/h) ≤ K / (max wall thickness in mm)² where K ≈ 1500 for soda-lime. The simulator computes K and flags any program that violates it.

### 4. COE Compatibility Check
Mixing glasses with COE differing by more than ~0.5 (× 10⁻⁷ K⁻¹) creates differential contraction during anneal. The check is binary: same family or no go. The agent enforces this hard.

## The Microbiome-Inspired Batch Record

Every session opens a record that mirrors a soil-microbiome plot intervention card:

| Field | Microbiome equivalent | Glassblowing meaning |
|-------|----------------------|----------------------|
| **Batch ID** | Plot ID | Date + session sequence (e.g., `2026-05-03-B`) |
| **Inputs (lineage)** | Seed lot, inoculant, amendment | Glass cullet/billet melt ID, color rod lots with supplier + lot # |
| **Environmental envelope** | Air temp, soil moisture, pH | Studio ambient °C/RH, glory hole soak temp, lehr starting temp |
| **Intervention sequence** | Tilling, watering, amending | Gathers, marvering, jacks, blocks, optic mold, transfer |
| **Observed outcome** | Yield, biomass, microbiome assay | Form achieved (yes/partial/no), surface defects, mass |
| **Successional follow-up** | 7d, 30d, 90d observations | Post-anneal inspection, 24h shelf check, 30d crack survey |
| **Diagnostic notes** | Plot blight observation | Devit, cord, color shift, anneal crack, cold check |

Six months in, you have a queryable history. That's the deliverable.

## Example Use Cases

### A New Form You've Never Made
You want to try a 320 mm reach blown plate with a folded rim. `/form-sim` says: requires three gathers totaling ~900 g, working window per heat is ~75 s before sag risk exceeds threshold for a flat form, and the proposed lehr program crashes too fast for the planned 12 mm rim thickness. Adjust the lehr first, then approach the bench.

### Switching Color Suppliers
You're moving from Effetre to Reichenbach for a specific color family. `/lineage-trace` plus `/scenario-test` build a small test piece checklist: same form, three pieces with new color, three pieces with old, all logged under one batch ID, 30-day shelf check on both sets. Now incompatibility shows up as data, not as a mystery crack months later.

### A Mystery Crack Cluster
Three pieces from the past month all cracked at the punty mark within 48 hours of removal from the lehr. `/lineage-trace` pulls every batch record from that month, filters to pieces with that punty technique, and surfaces a common factor: the lehr's hold-at-anneal segment was 30 minutes too short on those days due to a controller schedule edit.

### Apprentice Onboarding
A new studio assistant needs to learn the studio's failure modes. `/post-mortem` walked over the last quarter's failures becomes a structured curriculum — the failure-mode taxonomy plus the actual studio history.

### Reproducing a Successful Piece
You made something good in March. `/lineage-trace` on the finished piece pulls the exact gather count, color rod lots, lehr program, and even the studio ambient that day. You can now reproduce it instead of approximating it.

## Recommended MCP Servers

- **filesystem** — Read/write batch records, form specs, lehr programs, and post-mortems on disk
- **shell** — Run any auxiliary scripts (lehr log parsers, mass estimators, hygrometer log ingest)
- **python** — Useful for running the viscosity / sag / cool-curve calculations as actual code; the agent can produce a small Python module under `outputs/sim/` if the user wants reproducibility

## Legal & Ethical Considerations

- **Studio safety** — This workspace is for planning and documentation. Hot glass work involves >1000 °C surfaces, IR exposure, and silica dust. The agent never substitutes for proper PPE (didymium glasses, leather/Kevlar, ventilation), studio safety training, or supervision of beginners.
- **Lehr controller modifications** — If `/cool-curve` recommends a program change, the user, not the agent, must enter and verify the program on the controller. Confirm in person before unattended runs.
- **Material data sheets** — Manufacturer SDS/COE data takes precedence over the reference tables in this workspace. If they conflict, trust the SDS.
- **Apprentice supervision** — Outputs of `/form-sim` and `/scenario-test` are planning aids, not supervision. A new artist must still work under direct supervision of someone qualified, regardless of what the simulator says.

## Technical References

- [Bullseye Glass: TipSheets — Annealing for Sculptural Castings](https://www.bullseyeglass.com/tipsheets/) — Authoritative annealing tables for COE 90 with mass-based ramp rates
- [Frantz Art Glass: COE Reference Chart](https://www.frantzartglass.com/) — Cross-supplier compatibility table for soft-glass color rods
- [Corning Museum of Glass: Studio Education Resources](https://www.cmog.org/article/studio-education) — Form vocabulary, technique nomenclature, hot-shop methodology
- [Schott Technical Glass: Borosilicate Properties](https://www.schott.com/en-us/products/borosilicate-glass) — Datasheets for borosilicate working/strain points
- [J. Reichenbach Glass: Color Compatibility Notes](https://www.glasreichenbach.de/) — Manufacturer guidance for color rod compatibility
- [Glass on Web: Annealing of Glass](https://www.glassonweb.com/) — Industry articles on annealing physics and stress measurement
- [GAS — Glass Art Society Resource Library](https://www.glassart.org/resources/) — Studio practice references, technique videos, safety guidance
