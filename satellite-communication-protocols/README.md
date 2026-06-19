# Satellite Communication Protocols Workspace

> Design satellite links the way an optician designs a lens — as a budgeted cascade bounded by a conservation law, with every dB justified by cost-benefit.

## What This Workspace Does

This is a Claude Agent Workspace for **designing and adjudicating satellite communication links** — Earth-to-space, space-to-Earth, and inter-satellite. It equips the agent to build a full link budget, measure how close the link runs to the information-theoretic ceiling, diagnose what is degrading it, and recommend a configuration where every design choice carries a price tag.

Its distinctive lens is a fusion: it treats a **radio link as an optical system**. An optical designer traces light through a cascade of surfaces, each with a gain or loss, bounded by *étendue* (the optical invariant), degraded by *aberrations*, and judged against the *diffraction limit* via the *Strehl ratio*. A link engineer does the identical thing with signal power — bounded by **Shannon capacity**, degraded by **impairments**, judged by distance-from-capacity. The workspace makes that mapping explicit so intuition transfers both ways: phase noise *is* spherical aberration; antenna beamwidth *is* the diffraction limit; climbing the MODCOD table *is* opening the aperture.

The whole exercise is run through today's technique — **cost-benefit analysis frameworks**. Aperture, power, receiver noise, coding rate, ground stations, optical crosslinks, rain margin: each is a curve of benefit (dB, bits/s, availability) against cost ($, watts, kilograms, latency, regulation). The agent operates at the **knee of every curve**, exposes the **Pareto frontier**, and refuses to spend a decibel that buys less than it costs.

## Why This Workspace Exists

Link budgets are usually built as one-off spreadsheets and over-margined "to be safe," which quietly wastes the most expensive resource on a satellite — dB, which translate directly to mass, power, and money. By codifying the optical-systems analogy and forcing a cost-benefit number onto every lever, this workspace turns link design from spreadsheet folklore into a defensible, reproducible argument: *here is the budget, here is the capacity gap, here is why each dB was bought where it was, and here is what would break it.*

## Getting Started

### Prerequisites

- Claude Code (or any agent runtime that reads `CLAUDE.md` + `.claude/commands/`)
- Mission inputs: orbit/geometry, frequency band, target data rate, and target availability
- Optional: a link-budget calculator or Python (NumPy) for the arithmetic; ITU-R rain data for the site
- Optional: the [`workspace-foundational`](https://github.com/danielrosehill/Claude-Workspace-Foundational-Plugin) plugin for `/workspace-foundational:*` primitives

### Quick Start

1. Clone this workspace and open it in your agent runtime.
2. Run `/open-link-budget` with your mission (orbit, band, rate & availability targets) to lay out the budget cascade.
3. Run `/cascade-budget` to fill the EIRP → FSPL → atmosphere → G/T → Eb/N₀ train and read the margin.
4. Run `/shannon-gap` to see how close you are to capacity, then `/aberration-audit` to find what is costing the most.
5. Run `/aperture-tradeoff`, `/modcod-pareto`, and `/rain-margin-economics` to close any gap at minimum cost, then `/commit-design` to lock and justify the result.

## Command Reference

| Command | Description | When to Use |
|---------|-------------|-------------|
| `/open-link-budget` | Open a case; lay out the cascade "optical train" | First, per link direction |
| `/cascade-budget` | Trace the full gain/loss budget to a margin | After inputs are gathered |
| `/shannon-gap` | Strehl ratio: achieved vs Shannon spectral efficiency | To find the capacity gap and regime |
| `/aberration-audit` | Map impairments to optical aberrations; price correctors | When implementation loss is high |
| `/aperture-tradeoff` | dB-per-dollar on aperture, power, G/T, ground stations | To close a margin gap cheaply |
| `/modcod-pareto` | Pareto frontier over DVB-S2X MODCOD/ACM points | To pick the operating point / CCM vs ACM |
| `/rain-margin-economics` | Cost-benefit of availability (dB per nine) | On rain-dominated Ku/Ka/Q/V bands |
| `/optical-crosslink-eval` | RF vs free-space optical for a hop | Sizing inter-satellite / feeder links |
| `/commit-design` | Lock the design with provenance + sensitivity | Final, once the budget closes |

## Directory Structure

```
satellite-communication-protocols/
├── CLAUDE.md                 # Agent role, context refs, command list
├── README.md                 # This file
├── .claude/commands/         # 9 bespoke link-design commands
├── context/
│   ├── concepts.md           # Link-as-optical-system, budgets, Shannon↔étendue, aberrations
│   ├── workflows.md          # Define→Budget→Bound→Audit→Optimize→Allocate→Commit
│   └── references.md         # Band table, DVB-S2X MODCODs, aberration crosswalk, equations
├── prompts/                  # 4 reusable design-decision prompts
└── outputs/                  # Link cases, budget ledgers, committed designs
```

## Example Use Cases

### Sizing a Ka-band HTS downlink
Build the budget, find it bandwidth-limited near Shannon, and use `/modcod-pareto` + ACM to deliver more average throughput than a conservative fixed MODCOD — at lower $/bit.

### Diagnosing a degraded VSAT return link
A measured EVM is worse than the budget predicts. `/aberration-audit` maps the loss to phase noise (spherical) and IQ imbalance (astigmatism); the cheapest dB turns out to be a software carrier-loop fix, not a bigger dish.

### Justifying an availability spec
Marketing asks for "five nines." `/rain-margin-economics` shows the marginal $ per nine exceeds the outage cost above 99.9% — the memo recommends 99.9% with ACM and documents the saving.

### Deciding an inter-satellite link
`/optical-crosslink-eval` shows a 1550 nm laser crosslink delivers ~100 dB more antenna gain than RF in vacuum with no spectrum filing — optical wins, gated only by the pointing budget.

## Recommended MCP Servers

- **Filesystem MCP** — persist budget ledgers and committed designs under `outputs/`.
- **Python / code-execution MCP** — run the dB arithmetic, ITU-R rain models, and Pareto sweeps reproducibly.
- **Fetch / web MCP** — pull current ITU-R recommendation tables, DVB-S2X MODCOD data, and satellite frequency records (e.g. SatNOGS DB).

## Legal & Ethical Considerations

- **Spectrum is regulated.** EIRP and power-flux-density limits, frequency coordination, and orbital filings are set by the ITU Radio Regulations and national administrations. A budget that needs more EIRP than the filing allows is non-compliant, not merely costly — flag it.
- **Coordinate, don't interfere.** Designs must respect adjacent-satellite and terrestrial-service coordination; this workspace assumes licensed, coordinated operation.
- **Be honest about margin.** Undocumented "safety" dB are how budgets mislead reviewers; every term carries its source.

## Technical References

- [ITU-R P.618 — Earth-space propagation & rain attenuation](https://www.itu.int/rec/R-REC-P.618) — the availability/margin model
- [ITU-R P.838 — rain specific-attenuation coefficients](https://www.itu.int/rec/R-REC-P.838) — `γ_R = k·R^α`
- [DVB-S2X (ETSI EN 302 307-2)](https://www.dvb.org/standards/dvb-s2x) — MODCOD/ACM standard
- [CCSDS standards](https://public.ccsds.org) — RF & modulation (401.0-B), channel coding (131.0-B), optical comms (141/142)
- [SatNOGS DB](https://db.satnogs.org) — open satellite frequency & telemetry catalogue
- *Smith, Modern Optical Engineering* — étendue, Strehl ratio, Seidel aberrations, f-number (the optics half of the bridge)

## Optional plugin

If you have the [`workspace-foundational`](https://github.com/danielrosehill/Claude-Workspace-Foundational-Plugin) plugin installed, additional global commands (`/workspace-foundational:context-sweep`, `/workspace-foundational:find-template`) are available; the workspace works without it.
