# Shape Memory Alloy Phase Transformation Workspace

> A Claude Code workspace for engineering the martensite ↔ austenite transformation in shape memory alloys — and weighing every transformation decision against its full environmental life cycle.

## What This Workspace Does

Shape memory alloys (NiTi / Nitinol and its kin) owe their shape memory and superelasticity to a reversible, diffusionless **martensitic phase transformation**. Engineering an SMA part means landing the transformation temperatures (Ms, Mf, As, Af) on the service window, mapping the superelastic regime, designing for functional fatigue, and sometimes training a two-way effect. This workspace gives an agent the domain knowledge and the bespoke commands to do all of that.

What makes it distinct is the **environmental-impact lens** woven through every command. Nickel and titanium are energy-intensive to extract (titanium especially, via the Kroll process); NiTi machining generates large scrap fractions; SMA actuators are latent-heat-driven and only a few percent efficient; and NiTi is notoriously hard to recycle back to functional grade. So here the transformation decision and the **life-cycle ledger** are made together — composition, processing, application, and end-of-life are each scored for performance *and* embodied energy, use-phase energy, recyclability, and nickel-release risk.

The integrating frame: **a phase-transformation engineer who carries the life-cycle ledger into the lab.** Performance and environmental cost are two axes of one decision, never sequential gates.

## Why This Workspace Exists

SMA engineering and sustainability assessment usually live in different rooms — a metallurgist tunes the alloy, and an LCA practitioner audits it much later, if at all. That sequence hides the cheapest wins (reducing the scrap ratio often beats any material substitution) and lets greenwashing slip through (an SMA actuator can be marketed as "smart and efficient" while never beating an electric motor on lifetime energy). This workspace codifies the *integrated* discipline: characterize and tune the transformation, then immediately carry the choice into a cradle-to-gate inventory, a use-phase break-even, and an end-of-life assessment — and put it all on one explicit Pareto frontier.

## Getting Started

### Prerequisites

- Claude Code (this workspace is a self-contained Claude Code workspace).
- DSC, tensile, or resistivity data for characterization commands (or described peak positions if no raw data).
- For life-cycle work: access to an LCA database (ecoinvent, GaBi/Sphera, or GREET) to reconcile the inventory against.
- Basic familiarity with SMA terminology (austenite, martensite, Af) — see `context/concepts.md` for a primer.

### Quick Start

1. Clone this workspace.
2. Drop characterization data (DSC traces, stress–strain loops, cycling logs) into `context/` or `outputs/raw/`.
3. Run `/dsc-transformation-map` to fingerprint the transformation (Ms/Mf/As/Af, hysteresis, enthalpy).
4. Tune to a target with `/composition-temperature-tune`, then check limits with `/superelasticity-window` and `/functional-fatigue-budget`.
5. Carry the design into the life-cycle ledger with `/lca-cradle-to-gate`, `/use-phase-energy-balance`, and `/recyclability-eol-assessment`, then integrate with `/eco-performance-frontier`.

## Command Reference

| Command | Description | When to Use |
|---------|-------------|-------------|
| `/dsc-transformation-map` | Extract Ms/Mf/As/Af, hysteresis, enthalpy from a DSC curve | Start of any characterization |
| `/clausius-clapeyron-fit` | Fit dσ/dT for stress-induced martensite | Relating thermal and mechanical transformation |
| `/composition-temperature-tune` | Hit a target Af + build the Ni-tolerance budget | Specifying or correcting an alloy |
| `/superelasticity-window` | Map the Af–Md pseudoelastic window | Designing a superelastic part (e.g. a stent) |
| `/functional-fatigue-budget` | Project cycling degradation into a life budget | Setting cycle life and strain amplitude |
| `/training-protocol` | Design a two-way shape memory training schedule | When spontaneous cooling-driven motion is needed |
| `/lca-cradle-to-gate` | Cradle-to-gate life-cycle inventory (ISO 14040/44) | Quantifying embodied energy / GWP |
| `/use-phase-energy-balance` | In-service energy vs. conventional alternative | Justifying SMA against a motor/solenoid |
| `/recyclability-eol-assessment` | End-of-life recyclability + Ni-release risk | Design-for-recycling and biocompatibility |
| `/eco-performance-frontier` | Pareto frontier: performance vs. environmental cost | Final integrated design decision |

## Directory Structure

```
shape-memory-alloy-phase-transformation/
├── CLAUDE.md                 # Agent role, context refs, command list
├── README.md                 # This file
├── .claude/commands/         # 10 bespoke domain commands
├── context/
│   ├── concepts.md           # Martensitic transformation + LCA fundamentals
│   ├── workflows.md          # Integrated design loop + assessment methodology
│   └── references.md         # NiTi property tables, embodied-energy ranges, standards
├── prompts/                  # 5 reusable prompt templates
└── outputs/                  # Generated maps, budgets, inventories, frontiers
```

## Example Use Cases

### Specifying a Nitinol stent alloy
Body temperature (37 °C) must sit just above Af for superelastic behavior. Use `/composition-temperature-tune` to land Af with a tolerance budget, `/superelasticity-window` to confirm the recovery margin, and `/recyclability-eol-assessment` to check Ni-release against REACH and ISO 10993.

### Justifying an SMA actuator over a motor
A designer wants to replace a solenoid with a NiTi wire actuator. `/use-phase-energy-balance` computes the lifetime energy comparison and the break-even cycle count — and honestly reports when there is *no* break-even.

### Diagnosing a degraded actuator
A wire actuator has lost stroke after thousands of cycles. The `shape-memory-failure-diagnosis` prompt and `/functional-fatigue-budget` separate functional fatigue from overheating, composition drift, and structural cracking.

### Choosing a high-temperature SMA without greenwashing
NiTiPd buys a higher Af but carries heavy embodied carbon and supply risk. `/lca-cradle-to-gate` quantifies the penalty and `/eco-performance-frontier` shows whether the temperature gain is worth it — with the weighting made explicit.

## Recommended MCP Servers

- **Filesystem** — read DSC/tensile data files and write analyses to `outputs/`.
- **Fetch / web** — pull current ASTM/ISO standard scopes and supplier datasheets when reconciling figures.
- **A reference-management or notes MCP** (optional) — to track LCA database versions and assumptions across sessions.

## Legal & Ethical Considerations

- **Biocompatibility.** SMA medical-device work touches ISO 10993 and ASTM F2063; nickel release is a regulated, allergen-relevant concern. This workspace supports engineering analysis, not regulatory certification — treat its output as input to a qualified process, not a substitute for it.
- **Honest assessment.** LCA figures here are illustrative ranges; never present a single sourced-from-nowhere number as settled. Surface uncertainty and data-quality, and let "no environmental advantage" be a publishable conclusion.

## Technical References

- [ASTM F2004 — DSC transformation-temperature measurement](https://www.astm.org) — the tangent-construction standard for Ms/Mf/As/Af.
- [ASTM F2063 — Wrought NiTi for medical implants](https://www.astm.org) — composition and property requirements.
- [ISO 14040 / 14044 — Life-cycle assessment](https://www.iso.org) — principles, framework, and requirements.
- [EU REACH Annex XVII (entry 27)](https://echa.europa.eu) — nickel-release limits for prolonged skin contact.
- [ecoinvent LCI database](https://ecoinvent.org) and [GREET model](https://greet.es.anl.gov) — for embodied-energy and GWP reconciliation.

## Optional plugin

If you have the [`workspace-foundational`](https://github.com/danielrosehill/Claude-Workspace-Foundational-Plugin) plugin installed, additional global commands (`/workspace-foundational:context-sweep`, `/workspace-foundational:find-template`) are available; the workspace works without it.
