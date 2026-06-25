# Engine Block Metallurgy Analysis Workspace

> A forensic-metallurgy workspace for engine blocks, heads, and liners that reasons about composition, microstructure, and failure with explicit Bayesian probability assessment rather than gut-feel verdicts.

## What This Workspace Does

Cylinder blocks fail in ways that look alike on the bench: a cracked bore bridge could be a casting flaw, a thermal-fatigue crack from chronic overheating, or detonation damage from a tune problem. This workspace equips a Claude agent to act as the lab metallurgist who pulls those apart — classifying graphite morphology per **ASTM A247 / ISO 945**, checking spectrochemistry against grade specs (**ASTM A48, A536, ISO 16112 CGI, AA aluminium**), reading fracture surfaces, mapping porosity and inclusions, and planning hardness traverses.

What makes it different is the reasoning discipline. The engine's technique for today is **Bayesian probability assessment**, so the workspace treats every investigation as a hypothesis space. You start with prior odds over candidate root causes (informed by base rates for the material and service condition), then each lab result — a composition deviation, a graphite-degeneration zone, a fatigue striation field — enters as a **likelihood ratio** that multiplies the odds. The agent reports a **posterior distribution over causes**, not a single answer, and tells you which next test buys the most information.

The result is a failure-analysis dossier you can defend: priors stated, evidence weighted transparently, and a confidence number attached to the conclusion that a warranty board, OEM supplier-quality engineer, or expert-witness review can audit.

## Why This Workspace Exists

Root-cause analysis on castings is notorious for confirmation bias — the first plausible cause becomes the conclusion, and contradicting evidence gets explained away. The standard texts (ASM Handbook Vol. 11, *Failure Analysis and Prevention*) warn about this but offer no calculus for it. Bayesian assessment supplies one: it forces priors into the open, makes "this evidence is only weakly diagnostic" a number instead of a hedge, and keeps every hypothesis alive until the data actually discriminates. This workspace codifies that calculus into repeatable commands so the metallurgist's judgment is *augmented and recorded*, not replaced.

## Getting Started

### Prerequisites

- Lab data for the part under analysis: OES/XRF composition, metallographic micrographs (etched + as-polished), hardness readings, fracture photos
- The grade the part was *supposed* to be (e.g. ASTM A48 Class 35B, A536 65-45-12, ISO 16112 GJV-450, or an AA aluminium designation)
- Service history if available: mileage/hours, coolant-loss or overheat events, fuel/tune notes
- Optional: a spreadsheet or notebook for the likelihood-ratio worksheet (`outputs/`)

### Quick Start

1. Clone this workspace and drop the case data into a working folder under `outputs/<case-id>/`.
2. Run `/composition-cross-check` to confirm the material identity and conformance — this anchors the prior (a part already off-spec shifts base rates toward material cause).
3. Run `/failure-hypothesis-rank` to enumerate candidate root causes and set prior odds for this material + service condition.
4. Work the evidence with `/graphite-morphology-classify`, `/fracture-surface-read`, `/porosity-defect-map`, and `/hardness-traverse-plan`, feeding each result into `/bayes-evidence-update`.
5. Close with the posterior: the dossier names the leading cause, its probability, the runner-up, and the single highest-value confirmatory test still outstanding.

## Command Reference

| Command | Description | When to Use |
|---------|-------------|-------------|
| `/failure-hypothesis-rank` | Enumerate root-cause hypotheses; assign prior odds by material + duty | Start of any failure case, before weighing evidence |
| `/bayes-evidence-update` | Multiply the current odds by a new finding's likelihood ratio | Each time a lab result lands |
| `/graphite-morphology-classify` | Type graphite (A247 I–VII, nodularity %), classify the matrix | Reading any etched cast-iron micrograph |
| `/composition-cross-check` | Compare OES/XRF to spec; carbon equivalent; conformance probability | Confirming material identity and grade compliance |
| `/fracture-surface-read` | Identify fracture mode, initiation site, and propagation history | A cracked or separated part with an exposed fracture |
| `/porosity-defect-map` | Quantify voids/inclusions; classify gas vs shrinkage vs slag | Suspected casting-quality defect |
| `/hardness-traverse-plan` | Lay out and interpret a hardness traverse; flag chill and gradients | Checking chill, decarb, or section-property variation |
| `/thermal-fatigue-assess` | Score thermal-fatigue/HCF risk; fit life with a Bayesian prior | Cracks in valve bridges, bore bridges, or hot zones |
| `/sample-prep-protocol` | Plan sectioning, mounting, grinding, polishing, etching | Before destructively sampling a part |
| `/batch-accept-decision` | Decision-theoretic accept/reject from sampled lot results | QC disposition of a casting lot, not a single failure |

## Directory Structure

```
engine-block-metallurgy-analysis/
├── CLAUDE.md                 # Agent role, context refs, command list
├── README.md                 # This file
├── .claude/commands/         # Bespoke domain commands
├── context/
│   ├── concepts.md           # Materials, graphite taxonomy, defects, Bayes fundamentals
│   ├── workflows.md          # The Bayesian FA loop, metallography & spectro procedures
│   └── references.md         # Grade tables, standards, etchants, likelihood-ratio scales
├── prompts/                  # Reusable prompt templates
└── outputs/                  # Dossiers, posteriors, micrograph reads, decision logs
```

## Example Use Cases

### Cracked diesel block, warranty dispute
A 6.7 L CGI block cracks between the bore and water jacket at 40k miles. `/failure-hypothesis-rank` opens with casting-defect, thermal-fatigue, and overheat-event hypotheses; metallography (`/graphite-morphology-classify`) reveals low nodularity (degenerate vermicular → flake transition), `/bayes-evidence-update` swings the posterior toward a CGI process escape, and the dossier supports a supplier-side finding.

### Aluminium block bore scuffing in the field
A hypereutectic Al-Si block scuffs cylinders early. `/composition-cross-check` confirms primary-silicon content is below spec; `/hardness-traverse-plan` shows a soft as-cast surface; the posterior favors inadequate silicon refinement over lubrication failure.

### Incoming-lot disposition under cost pressure
Twelve of 200 gray-iron blocks show borderline tensile bars. `/batch-accept-decision` weighs the cost of a field escape against scrap, given the posterior probability the lot is out of spec, and recommends 100% screen vs. accept vs. reject.

## Recommended MCP Servers

- **Filesystem / repo access** — read micrograph metadata, composition CSVs, and write dossiers to `outputs/`.
- **Python / data-analysis sandbox** — run the odds-form Bayes worksheet, Weibull fits, and point-count statistics (ASTM E562) reproducibly.

## Legal & Ethical Considerations

- **Warranty and litigation neutrality.** Failure-analysis conclusions feed money and liability decisions. State the posterior honestly, including the probability the *opposing* hypothesis is correct; do not tune priors to a desired outcome.
- **Chain of custody.** Photograph and log the part before any destructive step; preserve fracture surfaces and retain archive specimens. A finding that cannot be reproduced is not evidence.
- **Scope honesty.** Metallurgy answers "what the material was and how it broke," not "who is at fault." Keep that boundary explicit in reports.

## Technical References

- [ASM Handbook Vol. 11 — Failure Analysis and Prevention](https://dl.asminternational.org/handbooks) — the canonical FA methodology and case studies.
- [ASTM A247 — Evaluating the Microstructure of Graphite in Iron Castings](https://www.astm.org/a0247-19.html) — graphite type/size/distribution classification.
- [ISO 945-1 — Microstructure of cast irons](https://www.iso.org/standard/72100.html) — international graphite classification.
- [ISO 16112 — Compacted (vermicular) graphite cast irons, classification](https://www.iso.org/standard/70509.html) — CGI grade spec.
- [ASTM A48 / A536 — Gray iron & ductile iron castings](https://www.astm.org/a0048_a0048m-22.html) — grade specifications.
- [MatWeb material property database](https://www.matweb.com/) — reference compositions and mechanical properties.

## Optional plugin

If you have the [`workspace-foundational`](https://github.com/danielrosehill/Claude-Workspace-Foundational-Plugin) plugin installed, additional global commands (`/workspace-foundational:context-sweep`, `/workspace-foundational:find-template`) are available; the workspace works without it.
