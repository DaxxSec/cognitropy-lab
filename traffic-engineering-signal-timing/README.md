# Traffic Engineering Signal Timing — with Environmental Impact Assessment

> An agent workspace for designing, retiming, and evaluating signalized-intersection control plans on the **delay × emissions × fuel × noise** Pareto frontier rather than as a single-objective level-of-service exercise.

## What This Workspace Does

Most signal retiming projects optimize for delay, queue length, or LOS and then bolt on an emissions estimate at the end of the report. This workspace inverts the workflow: every cycle-length, split, and offset recommendation is generated with an embedded emissions and fuel-consumption model so that the engineer can show the trade-off curve to decision-makers (council, MPO, FHWA reviewer) instead of a single "optimum."

The agent guides you end-to-end: pull baseline performance from controller logs and ATSPM, build an HCM 7-compliant capacity model, tune Webster/Akcelik/HCS cycle lengths, design coordination bandwidth across a corridor, run an EPA MOVES4 / CMEM-style emissions inventory on each candidate plan, and produce a NEPA/CEQA-style environmental impact assessment narrative.

## Why This Workspace Exists

Signal retiming is one of the cheapest and highest-benefit interventions in surface transportation — FHWA's Every Day Counts program puts the ROI between 40:1 and 100:1 — yet most agencies still treat it as a delay-minimization exercise and miss the air-quality co-benefits that unlock CMAQ funding, satisfy SIP commitments, and qualify the project as a TCM (Transportation Control Measure) under the Clean Air Act. This workspace codifies the multi-objective methodology so a single analyst can produce both the engineering retiming report and the environmental finding from the same dataset.

## Getting Started

### Prerequisites
- Signal controller make/model and access to event logs (ATSPM-compatible: Econolite, McCain, Siemens, Trafficware, Intelight)
- Turning-movement counts, peak-hour data, or 15-minute volume bins
- Saturation flow rate measurements (or HCM defaults if unavailable)
- Fleet-mix estimate (LDV / LDT / SU truck / combination truck / bus / motorcycle %), typically from local MPO or HPMS
- One of: Synchro 11+, Vissim 2024, AIMSUN Next, SUMO 1.20+, HCS, or TRANSYT-7F (for capacity modeling)
- Python 3.10+ with `pandas`, `numpy`, `pulp` (LP for offset optimization), and `matplotlib`
- For emissions: an EPA MOVES4 install OR the CMEM-style modal-emission lookup tables seeded in `resources/`

### Quick Start
1. Clone this workspace into the corridor's project folder.
2. Run `/onboard` to register the corridor, intersections, controllers, fleet-mix assumptions, and air-quality basin.
3. Run `/timing-baseline` to ingest existing controller logs (or hand-entered timing) and compute today's delay, queue, and LOS.
4. Run `/emissions-model` to convert the baseline to per-pollutant inventories (CO, NOx, VOC, PM2.5, PM10, CO2-eq, fuel gal/hr).
5. Run `/eco-optimize` for each peak (AM, midday, PM, off-peak) — produces the Pareto frontier of delay vs. CO2.
6. Run `/coordination-design` if there are 3+ adjacent signals on the corridor.
7. Run `/scenario-compare` to pin a recommended plan against baseline.
8. Run `/report-eia` to draft the NEPA/CEQA finding and the CMAQ benefit-cost narrative.

## Command Reference

| Command | Description | When to Use |
|---------|-------------|-------------|
| `/onboard` | Register corridor, controllers, fleet, air-quality basin | First time setup |
| `/timing-baseline` | Pull current splits/offsets, compute baseline performance | Before any optimization |
| `/eco-optimize` | Multi-objective cycle/split/offset tuning | Each peak period |
| `/emissions-model` | MOVES- or CMEM-style emissions estimate | After every timing candidate |
| `/coordination-design` | Green-wave bandwidth design with emissions weighting | 3+ signal corridors |
| `/scenario-compare` | Side-by-side delta on delay, fuel, CO2, NOx, PM | Before plan selection |
| `/report-eia` | NEPA/CEQA-style environmental impact assessment write-up | Stakeholder/funding submittal |

## Directory Structure

```
traffic-engineering-signal-timing/
├── CLAUDE.md                          # Agent role, commands, foundational instructions
├── README.md                          # This file
├── CREATION_REPORT.md                 # Workspace creation summary
├── context/
│   ├── project.md                     # Corridor scope, intersections, study period
│   ├── role.md                        # User experience and agency context
│   ├── constraints.md                 # Funding, MUTCD, agency policy boundaries
│   └── for-agent/
│       ├── domain-knowledge.md        # HCM methodology, Webster, MOVES, CMEM, NEMA phasing
│       ├── workflows.md               # 5 core workflows (baseline → EIA report)
│       ├── environment.md             # Controller make/model, data sources, tool versions
│       └── tools.md                   # Synchro/Vissim/SUMO/MOVES configuration
├── .claude/commands/
│   ├── onboard.md                     # Corridor & fleet & air-basin registration
│   ├── timing-baseline.md             # Controller log ingestion + baseline metrics
│   ├── eco-optimize.md                # Multi-objective Pareto cycle tuning
│   ├── emissions-model.md             # MOVES/CMEM emissions estimation
│   ├── coordination-design.md         # Green-wave with emissions-weighted bandwidth
│   ├── scenario-compare.md            # Plan-vs-plan delta with all impact dimensions
│   └── report-eia.md                  # NEPA/CEQA-style environmental impact write-up
├── prompts/
│   ├── corridor-quick-screen.md       # Triage prompt for "is this corridor a retiming candidate?"
│   ├── webster-cycle-bootstrap.md     # Volume-only first-cut cycle estimate
│   └── eco-driving-feasibility.md     # GLOSA / eco-approach signaling potential
├── resources/
│   ├── hcm7-saturation-defaults.md    # HCM 7 base saturation flow + adjustment factors
│   ├── moves4-emission-rates.md       # Aggregated CO, NOx, VOC, PM, CO2 lookup tables
│   ├── cmem-modal-fuel-rates.md       # CMEM idle/cruise/accel modal fuel & CO2 coefficients
│   └── nema-phasing-reference.md      # NEMA TS-2 ring-and-barrier reference + dual-ring diagrams
├── planning/                          # Active retiming plans, scenario notes, pivots
├── outputs/                           # Optimized timing plans, EIA reports, CMAQ narratives
├── user-docs/
│   ├── getting-started.md             # 30-minute walkthrough for new corridor
│   └── how-emissions-are-modeled.md   # Plain-language MOVES vs CMEM explainer
└── work-log/                          # Dated session logs
```

## Core Methodology

### 1. HCM 7 Capacity Foundation
Every analysis begins with HCM 7th Edition Chapter 19 (Signalized Intersections). Saturation flow rate, lane-group volumes, v/c ratios, and control-delay estimates are computed before any optimization, with adjustment factors documented per movement.

### 2. Webster + Akcelik Cycle Bootstrap
Initial cycle length is computed from Webster's formula `C = (1.5L + 5) / (1 - sum(y_i))` and refined with Akcelik's overflow-delay correction for v/c > 0.85. This is a **starting point only**, never the final answer.

### 3. Multi-Objective Optimization
Pareto-frontier search over cycle length (60–180 s), split allocation, and corridor offsets, with the objective vector `[control_delay, CO2, NOx, PM2.5, fuel_gal_hr, noise_Leq]`. The user picks a point on the frontier informed by their corridor's binding constraint (NAAQS exceedance, transit OTP, ped LOS, etc.).

### 4. Emissions Modeling
Two interchangeable estimators:
- **MOVES4** (project-level run): authoritative for SIP/CMAQ submittals; requires the EPA tool.
- **CMEM modal lookup** (offline): per-second engine load translated to CO/NOx/HC/CO2/fuel via fleet-weighted modal coefficients seeded in `resources/`.
The agent always runs CMEM for the on-the-fly Pareto search and re-runs MOVES4 only on the finalist plans.

### 5. Coordination Bandwidth with Eco-Weighting
TRANSYT-7F-style multi-band optimization with the objective augmented by a CO2-per-stop term so the green wave is sized to platoon-friendly speeds (typically 5–7 mph below the posted limit on suburban arterials, where eco-driving studies show the largest fuel benefit).

### 6. NEPA/CEQA Reporting
The output report follows FHWA Categorical Exclusion (CE) language for retiming projects (23 CFR 771.117(c)(28)) plus the air-quality conformity narrative for non-attainment basins, citing the calculated emission deltas with the methodology appendix.

## Example Use Cases

### Suburban Arterial Retiming (CMAQ Application)
Corridor with 8 coordinated signals, 25,000 ADT, in an ozone non-attainment basin. Workspace produces the Pareto frontier, picks a plan with 12% delay reduction and 9% NOx reduction, packages the CMAQ application narrative with the air-quality conformity finding.

### Downtown Grid During Peak
4×4 grid of signals with mixed AM/PM directional demand. Workspace solves AM and PM as separate optimization problems, designs a time-of-day plan with 6 plans/day, evaluates whether adaptive control (SCATS/SCOOT/ACS-Lite) is cost-justified.

### Transit Signal Priority Retrofit
Bus rapid transit corridor where TSP is being added. Workspace evaluates the emissions impact of TSP green extensions/early-greens on cross-street vehicles vs. the bus fleet's recovered runtime, ensuring net CO2 stays negative.

### School Zone Adjacent to Highway Ramp
Pedestrian-heavy intersection where MUTCD walk minimums collide with ramp queue spillback. Workspace finds the cycle that respects walk constraints while keeping the ramp queue below the gore.

### Connected/Automated Vehicle (CV/AV) Pilot
Intersection equipped with SPaT broadcast for GLOSA. Workspace evaluates whether eco-approach speed advice yields measurable fuel savings given current CV market penetration (~1–3% as of 2026).

## Recommended MCP Servers

- **filesystem** — Read controller exports (.csv, .vsd, .syn) and write timing plan files
- **shell** — Invoke MOVES4, SUMO, or local TRANSYT-7F batch runs
- **python** — Run the multi-objective optimizer, plot Pareto frontiers, render time-space diagrams
- **postgres** (optional) — Query an ATSPM database directly (UDOT/FDOT/UTA-style schema)
- **sqlite** — Local cache of detector event logs

## Legal & Regulatory Considerations

- **MUTCD compliance:** Pedestrian walk and clearance intervals (MUTCD §4E.06), yellow change interval (ITE Recommended Practice), all-red clearance — these are statutory minimums and may not be reduced to chase emissions or delay savings.
- **ADA / PROWAG:** Pedestrian accessible signals (APS), curb-ramp timing, and crossing distances govern minimum walk timing for elderly and accessible pedestrians (3.0 ft/s walk speed per MUTCD 2009; verify local agency override).
- **CAA conformity:** In ozone, CO, or PM non-attainment/maintenance areas, project-level conformity demonstration is required for any retiming receiving federal funds (40 CFR Part 93 Subpart B).
- **NEPA:** Most signal retiming qualifies for a Categorical Exclusion under 23 CFR 771.117(c)(28); a Documented CE may be required if emissions or pedestrian access changes are non-trivial.
- **State/local CEQA equivalents:** California CEQA, Washington SEPA, New York SEQRA may require their own air-quality finding even when the federal CE applies.

## Technical References

- [Highway Capacity Manual 7th Edition (TRB)](https://www.trb.org/Main/Blurbs/180048.aspx) — Chapter 19 Signalized Intersections
- [Manual on Uniform Traffic Control Devices (FHWA, 2023 Edition)](https://mutcd.fhwa.dot.gov/) — Chapter 4 Signals
- [FHWA Signal Timing Manual, 2nd Edition (2015)](https://ops.fhwa.dot.gov/publications/fhwahop08024/) — comprehensive practitioner reference
- [EPA MOVES4 (2024)](https://www.epa.gov/moves) — official mobile-source emissions model
- [CMEM (UC Riverside)](https://www.cert.ucr.edu/cmem/) — Comprehensive Modal Emissions Model
- [NEMA TS-2 Standard](https://www.nema.org/standards/view/Traffic-Controller-Assemblies-with-NTCIP-Requirements) — controller hardware/software spec
- [NTCIP 1202 v03A (2019)](https://www.ntcip.org/) — actuated signal controller object definitions
- [Utah ATSPM Open Source](https://github.com/udot-atspm) — reference ATSPM implementation
- [SUMO (Eclipse)](https://www.eclipse.org/sumo/) — open-source traffic microsimulation
- [TRANSYT-7F](https://mctrans.ce.ufl.edu/featured/transyt7f/) — McTrans signal coordination tool
- [ITE Trip Generation, 11th Edition](https://www.ite.org/) — for new-development demand forecasting
