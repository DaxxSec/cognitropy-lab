# HAZMAT Transportation Regulations Workspace

> Read a dangerous goods shipment like ciphertext — the codebook is the regulation, the redundancy is the security, and a cryptanalyst's toolkit catches the misdeclaration before it catches fire.

## What This Workspace Does

A dangerous goods declaration is not prose — it is a cipher. The UN number is the cipher key; the Dangerous Goods List (49 CFR 172.101 in the US, Chapter 3.2 of the UN Model Regulations internationally) is the codebook; and the Proper Shipping Name, hazard class, subsidiary risks, packing group, labels, placards, ERG guide number, and special provisions are the deterministic *plaintext* that the key unlocks. Because every shipment encodes the same facts several times over (the UN number on the paper, the class on the label, the hazard on the placard, the Kemler code on the orange plate), the message carries enormous built-in redundancy — and redundancy is precisely what a codebreaker uses to detect tampering and error.

This workspace applies the **cryptanalyst's toolkit** to hazmat documentation review: **known-plaintext cribs** (expand a UN number to everything it must imply), **cross-field consistency checks** (the regulation's redundancy is a checksum — break it and you've found an error), **frequency analysis** (a frozen-food importer suddenly shipping Class 1 explosives is a frequency outlier), **entropy / anomaly detection** (copy-pasted fields, round-number quantities, and missing 24-hour emergency contacts are the tells of fabricated paperwork), **transposition-error detection** (UN 1203 → 1230 turns gasoline into something else entirely), and **traffic analysis** (a co-loaded set that is individually legal but collectively prohibited by the segregation table).

The engine technique for this build is **standardized inspection checklists**, and it shapes the whole workspace. Every decode is expressed as a numbered, repeatable, CVSA-style checklist item with an explicit pass/fail verdict — never a freeform opinion. A finding produced here can be handed to a second inspector who re-runs the same checklist against the same codebook edition and reaches the same result. The cryptanalysis supplies the *what to check*; the standardized checklist supplies the *auditable how*.

## Why This Workspace Exists

Undeclared and misdeclared dangerous goods are a leading cause of transport incidents — lithium batteries declared as "electronics," oxidizers shipped as "cleaning supplies," water-reactive solids loaded next to acids. The information needed to catch most of these is already on the paperwork; it is just not *read systematically*. Human reviewers skim, trust the shipper, and miss the single transposed digit or the one segregation conflict in a 40-line manifest. By reframing documentation review as a decode-and-verify problem with a fixed codebook and a fixed checklist, this workspace makes the review **exhaustive** (every field cross-checked), **reproducible** (codebook edition and checklist version recorded), and **prioritised** (statistical screening points the human inspector at the shipments most likely to be wrong).

## Getting Started

### Prerequisites

- A dangerous goods declaration / shipping paper, manifest, air waybill, or bill of lading — text, PDF, or a clear photo.
- The transport **mode** (road, rail, sea, air) and jurisdiction, so the right regulation applies (HMR / ADR / RID / IMDG / IATA-ICAO).
- A current edition of the codebook: the [Hazardous Materials Table (49 CFR 172.101)](https://www.ecfr.gov/current/title-49/part-172) or the UN Model Regulations / modal regulation Dangerous Goods List. The agent works from the edition you cite.
- For placard work: a photo or careful description of placards, labels, marks, and the orange Kemler plate.
- Optional: a batch of historical manifests for a lane/shipper to build a frequency baseline.

### Quick Start

1. Clone this workspace and skim `context/concepts.md` for the codebook↔cipher mapping and the hazard-class table.
2. Run `/decode-manifest` on a shipping paper to decode every line against the codebook and flag cross-field inconsistencies.
3. Run `/codebook-crossref` on any suspect UN number to see its full expected plaintext beside what the paper actually says.
4. Run `/segregation-conflict` on the full co-loaded set to catch prohibited combinations the line-by-line check can't see.
5. Run `/inspection-checklist` to assemble the mode-specific standardized checklist and record a pass/fail result into `outputs/`.

## Command Reference

| Command | Description | When to Use |
|---------|-------------|-------------|
| `/decode-manifest` | Decode a full DG declaration against the codebook and run cross-field consistency validation. | First pass on any shipping paper or manifest. |
| `/codebook-crossref` | Crib-expand one UN number into its complete expected plaintext; diff against the paper. | When a single entry looks off and you need ground truth. |
| `/placard-decipher` | Decode placards, orange-plate Kemler/HIN codes, and labels from a photo; reconcile with the paper. | At the dock or roadside with eyes on the vehicle. |
| `/transposition-check` | Find digit-transposition / substitution errors in UN and container numbers via edit distance + check digits. | When a UN number or ISO 6346 container number may be mistyped. |
| `/frequency-profile` | Frequency-analyse codes across a shipper/lane/fleet; surface statistical outliers. | Targeting inspections across a corpus of manifests. |
| `/anomaly-entropy` | Entropy/anomaly scan over a batch for fabrication tells. | Screening a stack of declarations for the suspicious few. |
| `/segregation-conflict` | Traffic-analyse co-loaded UN numbers against the segregation table. | Before consolidating a mixed load or stuffing a container. |
| `/undeclared-crib` | Crib-drag a commodity description for the DG it implies but the paper omits. | When the goods description hints at undeclared hazards. |
| `/inspection-checklist` | Assemble the standardized mode-specific documentation checklist; record pass/fail. | To produce the auditable inspection record. |

## Directory Structure

```
hazmat-transportation-regulations/
├── CLAUDE.md                 # Agent role, context refs, command list
├── README.md                 # This file
├── .claude/commands/         # Bespoke domain commands
├── context/
│   ├── concepts.md           # Regulatory codebook + cryptanalysis mapping
│   ├── workflows.md          # Inspection pipeline + decision trees
│   └── references.md         # Hazard classes, UN numbers, Kemler codes, links
├── prompts/                  # Reusable decode/audit prompt templates
└── outputs/                  # Decoded manifests, checklists, findings
```

## Example Use Cases

### Catching a transposed UN number on a fuel shipment
A tanker paper reads "UN 1230, Gasoline." `/transposition-check` flags that UN 1230 is *methanol* while the named substance is gasoline (UN 1203) — a single-digit transposition that changes the subsidiary toxicity hazard and the ERG guide. `/inspection-checklist` records the discrepancy as a fail with the corrective entry.

### Finding undeclared lithium batteries
An air waybill describes "portable power banks, 200 units" with no dangerous goods declaration. `/undeclared-crib` drags the description to UN 3480 (lithium ion batteries) / UN 3481 (packed with equipment), shows that air transport requires DG handling, and escalates the shipment for physical verification.

### Screening a week of ocean manifests
`/frequency-profile` builds the class/UN distribution for a shipper's normal traffic; `/anomaly-entropy` flags three declarations with copy-pasted emergency-contact fields and round-thousand net quantities; the human inspector reviews those three instead of all 400.

### Catching a segregation conflict in a mixed container
Each of eight line items is individually compliant, but `/segregation-conflict` shows a Class 5.1 oxidizer co-loaded with a Class 3 flammable liquid in violation of the segregation table — a collective hazard invisible to a line-by-line read.

## Recommended MCP Servers

- **Filesystem** — read shipping papers, manifests, and placard photos; write decoded manifests and checklists into `outputs/`.
- **Web fetch (read-only)** — pull the current eCFR text of 49 CFR 172.101, ERG guide pages, and modal regulation updates when the local codebook excerpt is incomplete.
- **PDF / document extraction** — parse multi-page air waybills, bills of lading, and dangerous goods declarations into structured fields for decoding.
- **Time / scheduling** — timestamp inspection records for the audit trail.

## Legal & Ethical Considerations

- **Safety-critical, advisory only.** This workspace screens paperwork; it does not certify compliance. A passed checklist is not a regulatory clearance. Defer to a certified DG advisor / Dangerous Goods Safety Adviser (DGSA), the carrier's hazmat program, and the **current** regulation text. Regulations change continually — always cite the codebook edition/year used.
- **Jurisdiction and mode matter.** HMR (US 49 CFR), ADR (road, Europe), RID (rail), IMDG (sea), and IATA-DGR/ICAO-TI (air) differ in placarding, quantities, segregation, and documentation. Decode against the regulation that actually governs the shipment.
- **Anomalies are leads, not verdicts.** A statistical flag justifies a closer look, not an accusation or a hold. Escalate to documentary or physical inspection; do not penalise a shipper on a frequency outlier alone.
- **Do not use this to evade detection.** The decode logic is for *finding* misdeclaration, not crafting paperwork that hides it. This workspace serves inspectors, shippers improving their own compliance, and trainers — not concealment.

## Technical References

- [49 CFR Parts 100–185 — Hazardous Materials Regulations (eCFR)](https://www.ecfr.gov/current/title-49) — the US codebook; §172.101 is the Hazardous Materials Table.
- [PHMSA — Hazardous Materials Safety](https://www.phmsa.dot.gov/hazmat) — US regulator, guidance, and special permits.
- [Emergency Response Guidebook (ERG)](https://www.phmsa.dot.gov/hazmat/erg/emergency-response-guidebook-erg) — UN-number → guide-number mapping and initial response.
- [UN Recommendations on the Transport of Dangerous Goods — Model Regulations (UNECE)](https://unece.org/transport/dangerous-goods/about-recommendations-transport-dangerous-goods-model-regulations) — the "Orange Book," source of UN numbers and the Dangerous Goods List.
- [ADR — European Agreement on road transport of dangerous goods (UNECE)](https://unece.org/about-adr) — road regulation and the Kemler/Hazard Identification Number system.
- [IMDG Code (IMO)](https://www.imo.org/en/OurWork/Safety/Pages/DangerousGoods-default.aspx) — sea transport, including the segregation table.
- [IATA Dangerous Goods Regulations](https://www.iata.org/en/programs/cargo/dgr/) — air transport, lithium battery and quantity rules.
- [CVSA — North American Standard Inspection Program](https://www.cvsa.org/inspections/inspections/) — the standardized inspection levels this workspace's checklists emulate.
- [Frequency analysis (cryptanalysis)](https://en.wikipedia.org/wiki/Frequency_analysis) and [Known-plaintext attack](https://en.wikipedia.org/wiki/Known-plaintext_attack) — the cryptanalytic techniques mapped onto documentation review.
- [ISO 6346 container check digit](https://en.wikipedia.org/wiki/ISO_6346) — the real check-digit algorithm used by `/transposition-check` for container numbers.

## Optional plugin

If you have the [`workspace-foundational`](https://github.com/danielrosehill/Claude-Workspace-Foundational-Plugin) plugin installed, additional global commands (`/workspace-foundational:context-sweep`, `/workspace-foundational:find-template`) are available; the workspace works without it.
