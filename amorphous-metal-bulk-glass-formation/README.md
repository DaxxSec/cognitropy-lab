# Amorphous Metal Bulk Glass Formation Workspace

> Planning an amorphous-alloy foundry where the crystallization nose — not the machine — is the binding capacity constraint.

## What This Workspace Does

Bulk metallic glasses (BMGs) are metallic alloys frozen into a non-crystalline, glassy atomic structure by cooling faster than crystals can nucleate and grow. "Bulk" means thick enough to be a real part — millimetres to centimetres — rather than the micron-thick melt-spun ribbons of the 1960s. They reach ~2 GPa strength, ~2% elastic strain, and net-shape castability, but a single missed quench turns the whole part into ordinary brittle crystalline metal. This workspace is for the engineer who has to *produce* them at volume.

The organising idea is **capacity planning under a thermodynamic-kinetic constraint**. A conventional manufacturing planner sizes a line around machine cycle times, yield, and demand. Here the binding constraint sits one level deeper: the alloy's **glass-forming ability (GFA)** sets a maximum castable thickness, the **time–temperature–transformation (TTT) nose** sets how long the melt can linger before it crystallizes, and the **supercooled-liquid processing window** sets how long you can thermoplastically form a part per heating cycle. Every command in this workspace reads one of those kinetic limits and converts it into a capacity figure — castable product mix, parts-per-heat throughput, yield-adjusted good-part rate, and the QA sampling load that hangs off it.

The technique lens for this build is **capacity planning models** (Theory of Constraints, Little's Law, OEE, yield-adjusted capacity, demand forecasting). The fusion is literal, not decorative: the crystallization clock *is* the bottleneck resource, the TPF window *is* a per-cycle time budget, and GFA-limited castability *is* a product-mix feasibility constraint.

## Why This Workspace Exists

BMG production fails in ways that ordinary casting does not. An alloy that glass-forms beautifully at 2 mm crystallizes at the centre at 6 mm; a 50-ppm jump in dissolved oxygen seeds heterogeneous nucleation and collapses the yield; a thermoplastic-forming step that runs thirty seconds too long at temperature partially crystallizes the part and nobody sees it until the XRD halo turns into Bragg peaks. The planning question — *how many good parts can this line make this quarter?* — cannot be answered without the kinetics. This workspace codifies the alloy thermal data, the GFA-to-thickness translation, the JMAK yield model, and the line-throughput math so the capacity answer is grounded in the crystallization clock rather than wishful machine arithmetic.

## Getting Started

### Prerequisites

- DSC thermal data (Tg, Tx, Tm, Tl) for your candidate alloy(s), ideally at ≥3 heating rates for kinetics.
- Casting-route parameters: method (copper-mold suction/injection, melt spin, water quench), mold material, achievable cooling rate or section thickness.
- XRD and/or DSC capability for amorphicity verification.
- A demand forecast and per-station cycle times if you are sizing a line (optional for single-alloy screening).
- Claude Code with this workspace as the working directory.

### Quick Start

1. Clone this workspace and open it in Claude Code.
2. Drop your DSC scan (or peak temperatures) in and run `/dsc-landmarks` to extract Tg, Tx, Tm, Tl and ΔTx.
3. Run `/gfa-assess` to score glass-forming ability and get the max castable thickness — your capacity feasibility envelope.
4. Run `/cooling-budget` for your mold + part geometry to confirm the achievable cooling rate beats Rc with margin.
5. Run `/product-mix-plan` and `/line-throughput` to turn castability and cycle times into a capacity-constrained production plan.

## Command Reference

| Command | Description | When to Use |
|---------|-------------|-------------|
| `/gfa-assess` | Score GFA (Trg, ΔTx, γ, …), estimate Rc and max castable thickness | First-pass screening of any candidate alloy/composition |
| `/dsc-landmarks` | Read Tg, Tx, Tp, Tm, Tl, ΔTx, supercooled-liquid width from a DSC trace | Whenever a new DSC scan arrives |
| `/kissinger-kinetics` | Crystallization Ea + Avrami n from multi-heating-rate DSC | Before any yield or TPF-window modelling that needs kinetics |
| `/cooling-budget` | Achievable cooling rate vs Rc for a mold+geometry; max castable section | Sizing a mold or qualifying a part geometry |
| `/tpf-window` | Time–temperature thermoplastic-forming window; parts-per-heat | Planning a thermoplastic forming / embossing / blow-molding step |
| `/crystallization-yield` | JMAK crystallized fraction along a real thermal path → yield | Estimating scrap rate / yield-adjusted capacity for a process |
| `/melt-flux-spec` | Charge purity, atmosphere, fluxing to suppress heterogeneous nucleation | Setting up or troubleshooting melt prep; protecting GFA |
| `/line-throughput` | Bottleneck (TOC), Little's-Law WIP, OEE of the casting line | Sizing or debugging the production line's capacity |
| `/product-mix-plan` | Castability × demand forecast → capacity-constrained product mix | Quarterly/run planning; deciding what to make vs defer |
| `/amorphicity-qa` | Amorphicity verdict + capacity-aware sampling plan | Qualifying a lot; keeping QA off the critical path |

## Directory Structure

```
amorphous-metal-bulk-glass-formation/
├── CLAUDE.md                 # Agent role, context refs, command list
├── README.md                 # This file
├── .claude/commands/         # 10 bespoke BMG + capacity-planning commands
├── context/
│   ├── concepts.md           # GFA, kinetics, DSC, alloy families, capacity vocabulary
│   ├── workflows.md          # Production-run planning loop, GFA screen, bottleneck loop
│   └── references.md         # Alloy thermal data, GFA & capacity formulas, standards
├── prompts/                  # Reusable prompt templates
└── outputs/                  # Generated scorecards, run readouts, capacity plans
```

## Example Use Cases

### Qualifying a thicker part
Marketing wants a 5 mm case in Vitreloy 1. Run `/gfa-assess` (Dmax ~ 10 mm in Vit1, so feasible) then `/cooling-budget` for the proposed copper mold — confirm the centre still beats Rc ≈ 1 K/s before quoting the geometry.

### Sizing a thermoplastic-forming cell
A Zr-based net-shape part needs micro-features embossed in the supercooled-liquid region. `/kissinger-kinetics` + `/tpf-window` give the safe forming temperature and the seconds-per-heat budget; `/line-throughput` turns that into parts/hour and finds whether the press or the cooling step is the bottleneck.

### Diagnosing a yield collapse
Yield dropped from 92% to 60% after a feedstock change. `/melt-flux-spec` flags an oxygen-control regression; `/crystallization-yield` quantifies how much the higher nucleation density shrinks the amorphous core; `/amorphicity-qa` tightens the sampling plan until the cause is contained.

## Recommended MCP Servers

- **Filesystem MCP** — keep DSC CSVs, XRD patterns, and capacity plans versioned under `outputs/`.
- **Fetch / web MCP** — pull thermal data and GFA parameters from open BMG literature and reviews when an alloy isn't in `context/references.md`.
- **Code-execution / Jupyter MCP** — run the JMAK, Kissinger, and Newtonian-cooling fits numerically rather than by hand for production-grade numbers.

## Safety, Legal & Ethical Considerations

- **Beryllium.** The most famous BMG family (Vitreloy: Zr-Ti-Cu-Ni-**Be**) contains beryllium. Be dust, fume, and fines cause chronic beryllium disease (CBD), an irreversible lung condition; OSHA PEL is 0.2 µg/m³ (8-hr TWA). Any grinding, machining, or powder handling of Be-bearing BMG requires engineered controls. This workspace flags Be alloys explicitly and will recommend Be-free alternatives where GFA allows.
- **Molten metal & reactive elements.** Zr and Ti melts are oxygen- and moisture-sensitive and pyrophoric as fines; melting is done under vacuum or inert atmosphere. Treat all melt-handling as a high-temperature hazard.
- **HF etchants.** Metallographic preparation of BMGs often uses HF-bearing etchants — hydrofluoric acid causes deep, delayed burns and systemic fluoride toxicity. Follow institutional HF protocols and keep calcium gluconate available.
- **Honest reporting.** GFA parameters and Rc estimates are correlations with scatter, not guarantees. Report ranges and the data behind them; "this won't glass-form at the thickness you need" is a valid, non-negotiable answer.

## Technical References

- [Inoue, *Stabilization of metallic supercooled liquid and bulk amorphous alloys*, Acta Mater. 48 (2000) 279](https://doi.org/10.1016/S1359-6454(99)00300-6) — the canonical three empirical rules for GFA.
- [Wang, Dong & Shek, *Bulk metallic glasses*, Mater. Sci. Eng. R 44 (2004) 45](https://doi.org/10.1016/j.mser.2004.03.001) — comprehensive BMG review.
- [Lu & Liu, *A new glass-forming ability criterion for bulk metallic glasses*, Acta Mater. 50 (2002) 3501](https://doi.org/10.1016/S1359-6454(02)00166-0) — the γ = Tx/(Tg+Tl) parameter.
- [Schroers, *Processing of bulk metallic glass*, Adv. Mater. 22 (2010) 1566](https://doi.org/10.1002/adma.200902776) — thermoplastic forming in the supercooled-liquid region.
- [Goldratt, *The Goal* / Theory of Constraints](https://en.wikipedia.org/wiki/Theory_of_constraints) — the bottleneck-focusing method this workspace borrows for line capacity.

## Optional plugin

If you have the [`workspace-foundational`](https://github.com/danielrosehill/Claude-Workspace-Foundational-Plugin) plugin installed, additional global commands (`/workspace-foundational:context-sweep`, `/workspace-foundational:find-template`) are available; the workspace works without it.
