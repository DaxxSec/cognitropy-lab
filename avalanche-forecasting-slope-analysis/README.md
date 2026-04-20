# Avalanche Forecasting & Slope Analysis Workspace

> A Claude agent workspace for snow-science forecasters, ski-patrol leads, and backcountry guides that transforms raw weather + snowpack observations into defensible avalanche hazard ratings — built on a **predictive-maintenance scheduling** cadence so that pack checks, instrument calibration, and mitigation asset readiness never drift out of the operational loop.

---

## Why This Workspace Exists

Avalanche forecasting is a classic "small data, high consequence" decision problem. A regional forecaster may have two to six snow study plots, a dozen remote weather stations, and a flood of public observations — all feeding into a single daily bulletin that thousands of recreationists and highway managers will act on.

What goes wrong in real operations is almost never "we didn't know how to interpret the column test." It's:

1. **Drift** — a persistent weak layer (PWL) that stopped propagating in ECT tests two weeks ago is mentally filed as "healing" when in fact you just stopped touching it.
2. **Scheduling gaps** — the Ravelli tower's anemometer has been reading 0.0 m/s for 11 days but nobody has the calibration on their radar.
3. **Bulletin language drift** — the avalanche problem type quietly shifts from "Persistent Slab" to "Storm Slab" in the text without an explicit decision being documented.
4. **Asset readiness** — when the storm finally arrives, a DaisyBell pre-check or explosive inventory hadn't been re-verified since December.

This agent is a **forecasting co-pilot**, not a black box. It enforces the *predictive-maintenance cadence* — scheduled recurring checks for snowpack observations, instruments, and mitigation assets — and it builds forecast bulletins from structured observation data while keeping a clean audit trail.

---

## Who This Is For

- Avalanche Center forecasters (CAIC, SAC, NWAC, AAC, Avalanche Canada, etc.)
- Ski-patrol forecast leads at ski resorts
- Department of Transportation highway avalanche programs
- Backcountry guide services and heli/cat operations
- Snow safety managers at industrial sites (mines, pipelines, transmission line crews in avalanche terrain)
- Educators teaching AIARE / CAA-level snow science courses

> **Not** a replacement for AIARE Level 1/2/3 or Professional Avalanche Operations training. You still own the call.

---

## Getting Started

```bash
git clone https://github.com/DaxxSec/cognitropy-lab.git
cd cognitropy-lab/avalanche-forecasting-slope-analysis
claude
```

First command in-session should always be:

```
/onboard
```

That establishes your forecast zone, operational authority, data sources, and reporting cadence.

---

## Command Reference

| Command | Purpose |
|---|---|
| `/onboard` | One-time setup: zone, role, data sources, reporting cadence |
| `/daily-forecast` | Build today's hazard bulletin from observations and weather |
| `/snowpack-analysis` | Walk through ECT/PST/CT/stratigraphy data and update weak-layer tracking |
| `/slope-check` | Terrain-scale go/no-go for a specific aspect / elevation / slope angle |
| `/mitigation-plan` | Schedule control work + predictive-maintenance actions for instruments + assets |
| `/incident-review` | Post-incident accident analysis in the FACETS framework |

---

## Directory Structure

```
avalanche-forecasting-slope-analysis/
├── CLAUDE.md                       # Lightweight agent stub (loaded every prompt)
├── README.md                       # This file
├── CREATION_REPORT.md              # Why this workspace was built + domain notes
├── context/
│   ├── project.md                  # Populated by /onboard
│   ├── role.md                     # Populated by /onboard
│   ├── constraints.md              # Populated by /onboard
│   └── for-agent/
│       ├── domain-knowledge.md     # Snow-science fundamentals, problem types, tests
│       ├── workflows.md            # Step-by-step forecast build process
│       ├── environment.md          # Forecaster tooling (InfoEx, SNOTEL, etc.)
│       └── tools.md                # External data sources, APIs, formats
├── .claude/
│   └── commands/
│       ├── onboard.md
│       ├── daily-forecast.md
│       ├── snowpack-analysis.md
│       ├── slope-check.md
│       ├── mitigation-plan.md
│       └── incident-review.md
├── prompts/                        # Reusable prompt templates
├── planning/                       # Active plan.md + pivots/
├── resources/
│   ├── problem-type-matrix.md      # Nine avalanche problem types + decision criteria
│   ├── hazard-scale-reference.md   # NA Public Avalanche Danger Scale
│   ├── stability-test-reference.md # ECT/PST/CT scoring + ECTP quality
│   ├── pm-schedule-template.md     # Predictive-maintenance calendar template
│   └── bulletin-template.md        # Forecast bulletin skeleton
├── user-docs/                      # Agent-produced references for the user
├── work-log/                       # Dated session logs
└── outputs/                        # Generated bulletins, advisory text, plans
```

---

## The Nine Avalanche Problem Types

This agent uses the standardized avalanche problem types adopted by CAIC, AAC, Avalanche Canada, and the USFS National Avalanche Center:

1. **Dry Loose** — sluffing of unconsolidated dry snow
2. **Wet Loose** — point-release wet snow avalanches
3. **Storm Slab** — soft slab of recent storm snow
4. **Wind Slab** — slab formed by wind-transported snow
5. **Persistent Slab** — slab sitting on a PWL (buried surface hoar, facets, depth hoar)
6. **Deep Persistent Slab** — PWL near the ground, often basal facets/depth hoar
7. **Wet Slab** — slab weakened by meltwater or rain
8. **Cornice Fall** — cornice failure initiating slabs below
9. **Glide** — full-depth release on smooth ground surfaces

Each `/daily-forecast` run asks the agent to classify which problem(s) are active by aspect and elevation and stay consistent across the bulletin's text, icons, and travel advice.

---

## The Predictive-Maintenance Cadence

The workspace tracks recurring obligations — not just "what happened today" but "what am I due for?"

| Action | Typical Cadence |
|---|---|
| Full snow profile at study plot | 1-2 times per week per plot |
| ECT / PST at representative sites | Daily during active build periods |
| Weather station data sanity check (T, RH, wind, snow depth) | Daily automated + weekly manual |
| Precip gauge orifice clearing | After every storm, weekly minimum |
| Wind instrument calibration | Seasonal + after wind events > 40 m/s |
| Explosive inventory audit | Weekly during operations |
| Hand charge & throwable system function test | Per AST-30 / manufacturer schedule |
| DaisyBell / Gazex / Avalauncher pre-check | Before each control mission |
| Remote Avalanche Control System (RACS) battery + comms check | Weekly |
| InfoEx and bulletin publication QA | Daily |
| Bulletin language audit against problem-type definitions | Weekly |

The `/mitigation-plan` command reads + updates the schedule in `resources/pm-schedule-template.md`.

---

## Data Sources the Agent Knows

- **Weather**: NOAA, SNOTEL, local RAWS, mountain weather forecast products, radar/satellite
- **Observations**: InfoEx (professional exchange), MIN (Mountain Information Network), CAIC Observations, agency field ops
- **Snow & terrain**: ATES (Avalanche Terrain Exposure Scale) ratings, slope angle shading, aspect/elevation bands
- **Stability tests**: ECT (Extended Column), PST (Propagation Saw Test), CT (Compression), RB (Rutschblock), Hand/Shear

See `context/for-agent/tools.md` for ingestion formats.

---

## Example Session

```
> /onboard
Agent: What forecast zone are you responsible for, and at what authority level
       (public forecaster, ski patrol, guide, or DOT highway program)?

User: CAIC Front Range, public forecaster.

Agent: Got it. I'll populate context/*.md. Any seasonal operational focus beyond
       the public bulletin — highway 34 advisory support, for example?

...

> /snowpack-analysis
I have an ECT from a 4200 m study plot, NE aspect, 35deg:
- ECTP 14 @ 75 cm on buried surface hoar (BSH), sudden planar
- HS 145 cm, slab density ~210 kg/m3
- Snow temp -8 C at weak layer, -2 C at surface

Agent: This is the classic PWL signature that kills professionals. Adding to
       tracker with HIGH concern. Triggering would be possible by single skier
       loading. Recommend UPGRADING persistent-slab problem to CONSIDERABLE
       above treeline on N-E-SE aspects. Drafting forecast discussion...
```

---

## Ethical & Operational Considerations

- **Do not publish bulletins without human sign-off.** This agent drafts. A certified forecaster publishes.
- **Private obs under InfoEx professional exchange stay private.** The agent will flag if a proposed public-facing output contains protected information.
- **This is not a replacement for field presence.** Weather station data can be stale or wrong; a snowpit under your skis is still ground truth.
- **Absolute statements about safety are forbidden.** "Safe slope" does not appear in bulletin language.
- **Backcountry decision-making is the user's.** The agent assists with analysis, never with absolving consequence.

---

## Recommended MCP Servers / External Tools

- Web fetch / search MCP for NOAA, CAIC, Avalanche Canada public products
- File-based MCP pointing at InfoEx exports (if licensed) or local observation CSV
- Optional: weather-station telemetry MCP (MADIS, SNOTEL, RAWS)
- Optional: GIS MCP for slope-angle/aspect/ATES rasters

---

## Built By

The Cognitropy Lab — daily agent workspace experimentation.
Model: danielrosehill/Claude-Agent-Workspace-Model

