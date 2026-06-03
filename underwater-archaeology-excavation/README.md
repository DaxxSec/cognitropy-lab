# Underwater Archaeology Excavation Workspace

> Decide what to dig, what to leave, and what it will really cost — submerged-heritage excavation run as an explicit cost-benefit analysis.

## What This Workspace Does

Underwater archaeology is dominated by a single, recurring decision: **should a submerged site be excavated, or preserved where it lies?** This workspace treats that question — and the budgeting, method, and prioritisation questions that follow it — as a structured **cost-benefit analysis (CBA)**. It pairs real maritime-archaeology methodology (site-formation theory, geophysical survey, controlled stratigraphic excavation, waterlogged-organics conservation) with the discipline of putting costs and benefits on the same ledger so that recommendations survive scrutiny from a funder, a regulator, or a peer reviewer.

The CBA lens is not decoration. It is the framing the field itself uses, because underwater excavation is uniquely expensive: bottom time is rationed by decompression physiology, survey and dive vessels cost thousands per day, and every object raised commits the project to conservation and curation costs that run for decades. The workspace forces the full lifecycle cost into view, expresses archaeological significance as the benefit currency, prices the *cost of inaction* through threat-driven loss, and stress-tests every recommendation against the assumptions that drive it.

## Why This Workspace Exists

The single most common failure in submerged-heritage projects is excavating something that could not be afforded once it was out of the water. The conservation backlog — tanks of waterlogged timber waiting years for treatment, iron artefacts spalling in store — is a field-wide symptom of recovery decisions made without the lifecycle cost on the table. UNESCO's 2001 Convention codified the inverse default: in situ preservation as the *first* option, excavation only where justified. This workspace operationalises that doctrine. It refuses to let "we found something interesting" stand in for "the benefit of recovering this exceeds its full cost, and exceeds the value of leaving it protected in place."

## Getting Started

### Prerequisites

- Site documentation: position/depth, environment (sediment, currents, salinity, biology), and any prior survey or desk-based assessment.
- Cost inputs: vessel and dive day-rates, conservation-lab rates or estimates, and a working discount rate for lifecycle costs.
- A regulatory context: jurisdiction, whether UNESCO 2001 applies, and any national heritage designation or permit requirement.
- Optional: geophysical data (side-scan, magnetometer, multibeam, sub-bottom), photogrammetry imagery, and a preliminary finds inventory.

### Quick Start

1. Clone this workspace and drop site documentation and cost inputs into `context/` (or `outputs/raw/`).
2. Run `/site-significance-score` to establish the benefit currency, then `/threat-decay-model` to price the cost of leaving the site untouched.
3. Run `/dive-budget-model` and `/conservation-cost-forecast` to build the full lifecycle cost of an excavation option.
4. Run `/insitu-vs-excavate` to combine them into the core decision, then `/cba-sensitivity-sweep` to test how robust that decision is.
5. Before any disturbance, run `/permit-compliance-check`. Save every model and memo to `outputs/`.

## Command Reference

| Command | Description | When to Use |
|---------|-------------|-------------|
| `/insitu-vs-excavate` | Core CBA comparing in-situ preservation vs. full excavation. | The pivotal go/no-go decision for a site. |
| `/dive-budget-model` | Diver-days, bottom time, decompression overhead, vessel time → cost. | Estimating fieldwork cost for any in-water option. |
| `/conservation-cost-forecast` | Lifetime conservation + perpetual curation cost of an assemblage. | Whenever recovery of material is on the table. |
| `/site-significance-score` | Structured significance rubric → the benefit side of the ledger. | First pass on any new site; benefit input to CBA. |
| `/threat-decay-model` | In-situ degradation, trawling, looting risk over time. | Valuing the "do nothing" branch and rescue urgency. |
| `/survey-method-tradeoff` | Remote-sensing package selection on cost/coverage/resolution. | Planning the geophysical/evaluation phase. |
| `/excavation-method-select` | Sediment-removal method by cost, disturbance, recovery quality. | Once excavation is justified and being scoped. |
| `/recovery-prioritization` | Rank artefacts/areas by benefit-per-cost under a fixed budget. | When the budget cannot recover everything. |
| `/permit-compliance-check` | UNESCO 2001 Annex Rules + national-law compliance gate. | Mandatory before any seabed disturbance. |
| `/cba-sensitivity-sweep` | Stress-test the CBA against its key assumptions. | Before presenting any recommendation to a funder/regulator. |

## Directory Structure

```
underwater-archaeology-excavation/
├── CLAUDE.md                 # Agent role, context refs, command list
├── README.md                 # This file
├── .claude/commands/         # 10 bespoke CBA + excavation commands
├── context/
│   ├── concepts.md           # Domain knowledge: site formation, in-situ doctrine, methods, conservation, CBA mapping
│   ├── workflows.md          # Methodology: the project CBA pipeline + decision trees
│   └── references.md         # Cost ballparks, UNESCO Annex Rules, conservation lookups, catalogues
├── prompts/                  # Reusable prompt templates
└── outputs/                  # Cost models, decision memos, significance scores
```

## Example Use Cases

### A trawl-damaged wreck on a development corridor
A pipeline route crosses a partially-exposed wooden wreck. `/threat-decay-model` shows active scour plus trawl impact; `/site-significance-score` rates it regionally significant. `/insitu-vs-excavate` weighs a funded rescue excavation against a (cheaper but riskier) in-situ protection-and-monitoring option.

### A fixed-grant research excavation
A museum has a fixed grant and a rich cargo site. `/recovery-prioritization` ranks cargo lots by benefit-per-cost so the grant recovers the highest-value, lowest-conservation-burden material first, rather than the most photogenic.

### A deep-water site beyond diver reach
At 400 m, SCUBA is impossible. `/survey-method-tradeoff` and `/dive-budget-model` (in ROV mode) compare an AUV photogrammetry survey against a targeted ROV recovery, pricing the technology premium against the significance gain.

### Defending a conservation line item
A funder questions why conservation costs more than the diving. `/conservation-cost-forecast` produces the decades-long, discounted treatment-and-curation projection that justifies the figure.

## Recommended MCP Servers

- **Filesystem** — read site documentation, geophysical exports, and finds inventories from `context/` and write cost models to `outputs/`.
- **Fetch / web** — pull UNESCO 2001 text, national heritage-law summaries, and published conservation-treatment cost data for citation.
- **Spreadsheet / data** — drive the lifecycle cost and sensitivity tables that the CBA commands produce.

## Legal & Ethical Considerations

- **UNESCO 2001 Convention** establishes in-situ preservation as the first option, prohibits commercial exploitation of underwater cultural heritage, and binds excavation to the Annex Rules. Treat it as the baseline even outside ratifying states.
- **Salvage and "treasure hunting" are not archaeology.** This workspace serves research and heritage management, not commercial recovery for sale; commercial dispersal of an assemblage destroys its research value.
- **Human remains and war graves** (e.g. sunken warships, aircraft) carry sovereign-immunity and ethical obligations independent of age. Flag them; do not model them as ordinary finds.
- **Jurisdiction is layered** — territorial sea, contiguous zone, EEZ, and the Area each carry different obligations. Confirm before any fieldwork.

## Technical References

- [UNESCO 2001 Convention on the Protection of the Underwater Cultural Heritage](https://www.unesco.org/en/legal-affairs/convention-protection-underwater-cultural-heritage) — the governing instrument and its Annex Rules.
- [Nautical Archaeology Society (NAS)](https://www.nauticalarchaeologysociety.org/) — training scheme and field methods standards.
- [Honor Frost Foundation](https://honorfrostfoundation.org/) — maritime-archaeology research and grants, Eastern Mediterranean focus.
- [International Journal of Nautical Archaeology (IJNA)](https://onlinelibrary.wiley.com/journal/10959270) — the field's primary peer-reviewed journal.

## Optional plugin

If you have the [`workspace-foundational`](https://github.com/danielrosehill/Claude-Workspace-Foundational-Plugin) plugin installed, additional global commands (`/workspace-foundational:context-sweep`, `/workspace-foundational:find-template`) are available; the workspace works without it.
