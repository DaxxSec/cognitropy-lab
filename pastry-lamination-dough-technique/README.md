# Pastry Lamination Dough Technique Workspace

> Read a laminated dough like a medieval codex — codicology, collation, and diplomatic transcription applied to butter and flour, delivered as stakeholder-ready communications.

## What This Workspace Does

Laminated dough — croissant, pain au chocolat, Danish, classic puff (*pâte feuilletée*) — is a folded, layered, stratified artifact. So is a medieval manuscript. This workspace borrows the methods scholars use to read codices and turns them on the lamination block: it counts and notates layers with a **collation formula**, records a build as a reproducible **lamination codex**, **transcribes** what actually happened on a production run, **reads the baked crumb** like a page of script to diagnose faults, and traces **provenance** of every ingredient batch.

The engine technique for this build is **stakeholder communication templates**, and it shapes everything. The analysis is never the deliverable on its own — it is always converted into a communication tuned to whoever needs it: a one-page spec sheet for the production line, a defect/incident report for the head pastry chef, a yield-and-waste memo for the F&B cost controller, a training brief for junior bakers, and accurate menu copy for front-of-house. The paleographer's habit of *exact, layered, audience-aware description* is exactly what makes a bakery's communications trustworthy.

## Why This Workspace Exists

Lamination knowledge is notoriously tacit — it lives in a head baker's hands and rarely survives staff turnover. When a batch fails, the "why" is argued over rather than read off the evidence, and the fix is communicated as a hallway remark that the next shift never receives. By treating each dough as a document to be collated, transcribed, and provenanced, this workspace makes lamination **reproducible** (the codex), **diagnosable** (stratigraphic crumb reading), and **communicable** (templated stakeholder briefs) — so a fault found on the morning shift reaches the evening shift as a written, evidenced corrective action instead of folklore.

## Getting Started

### Prerequisites

- A target product and its house formula (flour weight, hydration %, butter %, fold regimen).
- Butter and flour spec sheets (fat %, water %, protein %) — or batch labels to look them up.
- For diagnosis: a clear photo of a baked cross-section, or a careful written description of the crumb.
- Optional: a kitchen probe thermometer and a hygrometer for ambient/dough/butter temperatures.

### Quick Start

1. Clone this workspace and skim `context/concepts.md` for the codex↔dough mapping.
2. Run `/collation-formula` with your fold regimen to confirm the target layer count and notation.
3. Run `/codify-lamination` to capture the full reproducible build as a lamination codex in `outputs/`.
4. After a production run, run `/transcribe-bake`, then `/diagnose-crumb` on the cross-section if anything is off.
5. Run `/stakeholder-brief` to convert the result into the right communication for the line, the chef, or cost control.

## Command Reference

| Command | Description | When to Use |
|---------|-------------|-------------|
| `/collation-formula` | Compute and notate the fat/dough layer count for a fold regimen. | Designing or verifying a build before mixing. |
| `/codify-lamination` | Produce the reproducible "lamination codex" spec record. | Locking a product's recipe for the house archive. |
| `/transcribe-bake` | Diplomatically transcribe an actual run vs the codex. | Immediately after a production bake. |
| `/diagnose-crumb` | Read the baked cross-section to identify faults. | When lift, layering, or honeycomb looks wrong. |
| `/defect-stratigraphy` | Trace a fault to the build stage that caused it. | After `/diagnose-crumb`, to find root cause. |
| `/butter-temper-window` | Match butter plasticity to dough; compute temper window. | Before lock-in, or when butter keeps cracking/bleeding. |
| `/provenance-trace` | Record ingredient batch provenance and chain of custody. | Onboarding a new flour/butter lot, or for audits. |
| `/stakeholder-brief` | Turn any analysis into an audience-tuned communication. | Whenever a finding needs to reach a person/team. |

## Directory Structure

```
pastry-lamination-dough-technique/
├── CLAUDE.md                 # Agent role, context refs, command list
├── README.md                 # This file
├── .claude/commands/         # Bespoke domain commands
├── context/
│   ├── concepts.md           # Lamination science + codicology mapping
│   ├── workflows.md          # Methodology and decision trees
│   └── references.md         # Layer math, spec targets, glossary, links
├── prompts/                  # Stakeholder communication templates
└── outputs/                  # Codices, transcriptions, diagnoses, briefs
```

## Example Use Cases

### Standardizing a croissant across two shifts
Codify the build once, hand the line a `/stakeholder-brief` spec sheet, and the morning and evening teams produce the same 27-layer croissant — with the collation formula on the sheet so anyone can verify the fold count.

### Diagnosing a "bready," un-flaky batch
`/diagnose-crumb` reads the welded layers and grey crumb; `/defect-stratigraphy` traces it to a too-warm lock-in; `/stakeholder-brief` issues a defect report with the corrective temper window to the head chef.

### Onboarding a new laminating butter
A new *beurre de tourage* lot arrives at a different fat %. `/butter-temper-window` recomputes the working range and `/provenance-trace` logs the lot so the change is auditable if quality shifts.

## Recommended MCP Servers

- **Filesystem** — read cross-section photos and batch spec PDFs, write codices and reports into `outputs/`.
- **Time / scheduling** — stamp transcriptions and proof timers with accurate timestamps for the diplomatic record.
- **Web fetch (read-only)** — pull butter/flour manufacturer spec sheets and AOP butter data when a batch label is incomplete.

## Legal & Ethical Considerations

- **Allergens:** laminated products contain gluten (wheat) and milk; some include egg wash, nuts, or chocolate. Any spec sheet or menu copy this workspace produces must declare allergens accurately — this is a legal labelling requirement in most jurisdictions (e.g. EU FIC 1169/2011, US FALCPA/FASTER Act).
- **Food safety:** keep dough out of the 4–60 °C danger zone beyond safe limits; proof below butter's melt point; follow local HACCP practice. Diagnostic convenience never overrides safety.
- **Provenance honesty:** "artisan," "AOP butter," or origin claims in menu copy must match the traced provenance record. Do not generate marketing claims the batch data cannot support.

## Technical References

- [Codicology — physical description of manuscripts (British Library glossary)](https://www.bl.uk/catalogues/illuminatedmanuscripts/glossary.asp) — the source discipline for the codex↔dough mapping.
- [Quire & collation formula conventions (Wikipedia: Quire / Collation)](https://en.wikipedia.org/wiki/Quire_(bookbinding)) — how folded gatherings are notated.
- [Lamination & viennoiserie technique (King Arthur Baking — laminated dough)](https://www.kingarthurbaking.com/blog/2020/05/13/how-to-laminate-dough) — fold types, lock-in, layer counts.
- [Butter for lamination — *beurre de tourage* and fat content (Wikipedia: Beurre AOP / butterfat)](https://en.wikipedia.org/wiki/Butter) — why ≥82–84% fat butter laminates cleanly.

## Optional plugin

If you have the [`workspace-foundational`](https://github.com/danielrosehill/Claude-Workspace-Foundational-Plugin) plugin installed, additional global commands (`/workspace-foundational:context-sweep`, `/workspace-foundational:find-template`) are available; the workspace works without it.
