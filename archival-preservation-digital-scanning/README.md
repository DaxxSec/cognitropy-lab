# Archival Preservation Digital Scanning Workspace

> Run a cultural-heritage digitization program with operations-research rigor — preserve the most value per scarce capture-hour, without ever letting the schedule endanger a fragile original.

## What This Workspace Does

This workspace turns a digitization lab from a reactive scan-what-shows-up operation into a planned, standards-conformant, optimization-driven program. It covers the full lifecycle: deciding **what** to scan and in what order, **how** to capture it to a preservation standard, **whether** it passes QA, **how** to package it for long-term trust, and **how** to keep it readable for decades.

The distinguishing method is **resource optimization**. Capture-station hours, trained operators, storage, and budget are always scarce, and most archives hold a backlog measured in decades. So this workspace frames the core decisions as optimization problems: priority queues as a weighted-value **0/1 knapsack** under a capacity constraint; station assignment as **parallel-machine makespan minimization**; backlog drawdown as a **queueing** model with a real utilization discount; and the in-house-vs-vendor split as a **make-vs-buy** cost optimization with hard ethical gates. The math allocates effort — it never decides that a crumbling acetate negative can wait or that a unique manuscript is safe to ship.

The other half is **preservation craft**: capture profiles pinned to FADGI / Metamorfoze / ISO 19264, objective QA against target charts (ΔE, OECF, SFR/MTF), OAIS-conformant AIPs with METS/PREMIS/MIX metadata and SHA-256 fixity, and IIIF/OCR access deliverables. Optimization without that craft produces images fast that no future curator can trust; the craft without optimization produces a backlog that never clears. This workspace insists on both.

## Why This Workspace Exists

Cultural-heritage institutions hold vastly more material than they can digitize, on media that is actively decaying, under budgets that never match the backlog. The recurring failures are predictable: scanning whatever is convenient instead of what is most at-risk or most in demand; under-specifying capture and discovering years later that masters must be re-shot (often impossible once an original has degraded further); shipping irreplaceable originals to a vendor to "save money" and losing or damaging them; and storing TIFFs with no fixity or provenance, so a silent bit-flip a decade later goes undetected. This workspace codifies the decisions that prevent each of those — and keeps the reasoning explicit so program managers can defend their choices to funders and stakeholders.

## Getting Started

### Prerequisites

- A collection inventory (CSV/JSON/Markdown) with, per lot: extent, material type, condition, rights, and demand signal.
- Capture hardware appropriate to the material (overhead/planetary scanner for bound volumes, copy stand/flatbed for loose sheets, film/transparency scanner for negatives) and its throughput figures.
- A device-level imaging target chart and analysis software for objective QA (e.g. an open-source SFR/OECF analyzer).
- Storage with a known replication factor, and a checksum tool (SHA-256).

### Quick Start

1. Clone this workspace and drop your inventory into `outputs/` (or point a command at it).
2. Run `/triage-fragile-condition` to grade condition and flag anything actively decaying.
3. Run `/plan-digitization-queue` to produce an optimization-ranked queue under your lab's capacity.
4. Run `/spec-capture-profile` for each material class, then capture and run `/audit-image-quality` on the results.
5. Run `/assemble-aip-package` on QA-passed masters, then `/audit-fixity-integrity` to start the integrity regime.

## Command Reference

| Command | Description | When to Use |
|---------|-------------|-------------|
| `/plan-digitization-queue` | Weighted-value + knapsack priority queue under capacity | Start of a project or whenever capacity/inventory changes |
| `/optimize-scanner-schedule` | Assign lots to stations to minimize makespan | After the queue is set, to load the week across stations |
| `/forecast-backlog-drawdown` | Completion-date and steady-state queueing forecast | Budget/staffing planning; answering "when will we be done?" |
| `/model-project-cost` | Cost-per-image + in-house vs. vendor optimization | Scoping a project or deciding what to outsource |
| `/spec-capture-profile` | Standards-conformant imaging spec per material | Before capturing any new material class |
| `/audit-image-quality` | Objective QA vs. the capture profile | After each capture session/batch |
| `/triage-fragile-condition` | Condition grading and capture-path routing | At intake, before scheduling fragile material |
| `/assemble-aip-package` | Build an OAIS AIP with METS/PREMIS/MIX + fixity | Once masters pass QA |
| `/audit-fixity-integrity` | Generate/verify checksums over time | At packaging and on the recurring verification cadence |
| `/derive-access-deliverables` | Access copies, IIIF tiles, OCR, thumbnails | When publishing cleared material for use |

## Directory Structure

```
archival-preservation-digital-scanning/
├── CLAUDE.md                 # Agent role, context refs, command list
├── README.md                 # This file
├── .claude/commands/         # 10 bespoke digitization commands
├── context/
│   ├── concepts.md           # Standards, file/metadata models, condition, optimization framing
│   ├── workflows.md          # The prioritize → capture → QA → package → preserve pipeline
│   └── references.md         # Standard levels, throughput/handling figures, catalogues
├── prompts/                  # Reusable prompt templates
└── outputs/                  # Queues, schedules, cost models, QA + fixity reports, AIPs
```

## Example Use Cases

### Clearing a decade-long backlog with a fixed budget
Triage condition, build a knapsack-optimized queue, forecast the drawdown under current capacity, and model whether adding a station or outsourcing the overflow clears it faster per dollar.

### Specifying a grant-funded manuscript digitization to FADGI 4-star
Define a preservation capture profile pinned to FADGI 4★, run objective QA against the target chart on every session, and package masters as OAIS AIPs with full provenance for the funder's deliverable.

### Rescuing a collection of deteriorating acetate negatives
Flag active vinegar syndrome as an urgency override, pin those lots to the front of the queue, keep them in-house (no transit), and capture under a transmissive profile before further decay.

### Publishing a digitized collection for researchers
Generate IIIF-tiled deep-zoom derivatives plus OCR with confidence flags, gate on cleared rights, and let researchers explore at full resolution without ever touching the preservation masters.

## Recommended MCP Servers

- **Filesystem MCP** — walk inventories, batch-rename per the capture profile, and organize `outputs/` AIPs and derivative trees.
- **A spreadsheet/CSV MCP** — ingest collection inventories and emit queue/schedule/cost tables the lab can paste into its tracking sheet.

## Legal & Ethical Considerations

- **Rights gating before access.** Capture for preservation may be broad, but public dissemination must respect copyright, donor restrictions, and cultural-sensitivity agreements. Never publish a lot whose rights are unresolved.
- **Custody of irreplaceable originals.** The make-vs-buy model encodes a hard gate: unique or fragile material that cannot be safely transported stays in-house even when a vendor is cheaper.
- **Honest access metadata.** Surface OCR confidence and capture limitations rather than presenting derived text or images as authoritative.
- **Safety hazards.** Nitrate film, active mold, and off-gassing acetate are handling/safety issues — route to specialists, do not improvise.

## Technical References

- [FADGI — Technical Guidelines for Digitizing Cultural Heritage Materials](https://www.digitizationguidelines.gov/guidelines/digitize-technical.html) — the U.S. federal star-rating imaging guidelines.
- [Metamorfoze Preservation Imaging Guidelines](https://www.metamorfoze.nl/en/digitization/guidelines) — the Dutch national preservation imaging standard.
- [ISO 19264-1 — Image quality analysis for cultural heritage](https://www.iso.org/standard/79172.html) — the international conformance/measurement standard.
- [OAIS Reference Model (CCSDS 650.0 / ISO 14721)](https://public.ccsds.org/pubs/650x0m2.pdf) — the archival information package and preservation framework.
- [PREMIS Data Dictionary for Preservation Metadata](https://www.loc.gov/standards/premis/) and [METS](https://www.loc.gov/standards/mets/) — preservation/structural metadata schemas.
- [IIIF — International Image Interoperability Framework](https://iiif.io/) — the image and presentation APIs for access deliverables.
- [NDSA Levels of Digital Preservation](https://ndsa.org/publications/levels-of-digital-preservation/) — a tiered model for fixity, storage, and integrity practice.

## Optional plugin

If you have the [`workspace-foundational`](https://github.com/danielrosehill/Claude-Workspace-Foundational-Plugin) plugin installed, additional global commands (`/workspace-foundational:context-sweep`, `/workspace-foundational:find-template`) are available; the workspace works without it.
