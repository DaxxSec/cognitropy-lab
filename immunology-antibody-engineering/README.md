# Immunology Antibody Engineering Workspace

> Engineer developable antibodies — humanize, mature, and de-risk them — while running the lab as a structured apprenticeship where every task is also a logged competency.

## What This Workspace Does

This workspace equips a Claude Code agent to act as the working core of an antibody-engineering group. On the **science** side it carries the engineering chain end to end: scanning a VH/VL pair for sequence liabilities, humanizing a non-human antibody by CDR grafting and minimal back-mutation, designing affinity-maturation campaigns, triaging developability (thermal, colloidal, charge, poly-reactivity, plus TAP-style structural flags), QC-ing binding kinetics on SPR/BLI, and binning epitopes across a panel.

On the **people** side it treats that chain as an **apprenticeship**. Antibody engineering is a craft learned by supervised practice, so this workspace folds **apprenticeship progression tracking** into the work: a Dreyfus competency ladder (Novice → Expert) across eight core competencies, an entrustment/supervision scale, scoped mentor sign-offs, and evidence-based progression reviews. The trick is that the two halves share artifacts — every engineering command tags the competency its output demonstrates, so the `outputs/` logbook *is* the trainee's evidence portfolio.

The combination is the whole idea: a candidate is only as good as the engineer who can produce it unsupervised. Building antibodies and building the people who build antibodies are the same job here — and both are tracked on auditable evidence rather than impressions.

## Why This Workspace Exists

Antibody engineering has two failure modes that look unrelated but aren't. The first is technical: leads that win on affinity but fail late on developability, or "20 pM" kinetics that are really avidity artifacts. The second is organizational: skill lives in a few experts' heads, "they're experienced" stands in for evidence, and trainees get advanced (or stuck) on impressions. Both are problems of *missing, auditable evidence*.

This workspace codifies both halves of the fix: rigorous, reproducible engineering practice **and** the competency-based progression discipline to record who can do each task unsupervised — anchored to the same real deliverables. It encodes the numbering schemes, liability motifs, developability thresholds, and assay QC an engineer relies on, alongside the Dreyfus/entrustment vocabulary a mentor needs, so the agent can move a candidate from sequence to de-risked lead — and tell you, with cited evidence, which trainee is ready to do that alone.

## Getting Started

### Prerequisites

- VH/VL sequences (FASTA/plain text) for the candidates you're engineering.
- Python 3 with antibody tooling for the in-silico arm: `ANARCI` (numbering), `ImmuneBuilder`/`ABodyBuilder2` (Fv models), optionally `BioPhi`/`Hu-mAb` (humanness) and `NetMHCIIpan` (immunogenicity).
- Access to SPR (Biacore) or BLI (Octet) data for the kinetics commands, or existing sensorgrams.
- Internet access to IMGT, OAS, SAbDab/Thera-SAbDab and the SAbPred tools (or local mirrors).
- A trainee roster and logbook convention for the apprenticeship commands.

### Quick Start

1. Clone this workspace and skim `context/concepts.md` (antibody architecture + the apprenticeship model) and `context/workflows.md` (Loops A/B/C).
2. Run `/sequence-liability-scan` on a candidate — annotated liabilities land in `outputs/liabilities/`.
3. Humanize if it's non-human (`/humanize-candidate`), then characterize with `/binding-kinetics` and `/epitope-binning`.
4. Triage with `/developability-triage`; if affinity misses target, plan a campaign with `/affinity-maturation-plan`.
5. For the people side: `/competency-map` to baseline a trainee, `/skills-gap-plan` to assign the next real task, and `/progression-review` + `/mentor-signoff` at review checkpoints.

## Command Reference

| Command | Description | When to Use |
|---------|-------------|-------------|
| `/competency-map` | Baseline a trainee's Dreyfus tier + entrustment level per competency from evidence | When a trainee starts, or to refresh their profile |
| `/sequence-liability-scan` | Flag deamidation/isomerization/oxidation/glycosylation/free-Cys liabilities by CDR exposure | First pass on any new sequence |
| `/humanize-candidate` | CDR-graft onto human germlines + minimal back-mutations | When the parent is non-human |
| `/affinity-maturation-plan` | Design library + selection scheme with a developability guardrail | When affinity misses target |
| `/developability-triage` | Profile thermal/colloidal/charge/poly-reactivity + TAP flags; rank candidates | Before the lead/backup decision |
| `/binding-kinetics` | Design/QC an SPR/BLI run for kon/koff/KD; guard against avidity & mass transport | Whenever an affinity number is reported |
| `/epitope-binning` | Cluster a panel into epitope bins; plan fine mapping | For lead diversity or bispecific pairing |
| `/progression-review` | Weigh logged reps, advance/hold/remediate, update entrustment | Periodic (e.g. quarterly) review |
| `/mentor-signoff` | Record a scoped, revocable supervised→independent entrustment step | When evidence supports independence |
| `/skills-gap-plan` | Map current→target competency gap onto real upcoming work | When planning a trainee's next assignments |

## Directory Structure

```
immunology-antibody-engineering/
├── CLAUDE.md                 # Agent role, context refs, command list
├── README.md                 # This file
├── .claude/commands/         # Bespoke domain + apprenticeship commands
├── context/
│   ├── concepts.md           # Antibody science + Dreyfus/entrustment model
│   ├── workflows.md          # Loop A lifecycle, Loop B craft, Loop C progression
│   └── references.md         # Numbering, liability motifs, thresholds, competency ladder, tools
├── prompts/                  # Design review, maturation strategy, humanization rationale, progression report
└── outputs/                  # Scans, humanization panels, kinetics QC, apprentice records
```

## Example Use Cases

### De-risk a hybridoma lead before committing it
A murine hybridoma antibody needs to become a developable human IgG. `/sequence-liability-scan` flags an NG in CDR-H2; `/humanize-candidate` grafts it onto matched germlines with three Vernier back-mutations; `/binding-kinetics` confirms the intrinsic KD (not avidity); `/developability-triage` clears it on TAP flags. The whole chain is logged against the trainee who ran it.

### Plan an affinity-maturation campaign that won't wreck developability
A lead sits at 8 nM and needs sub-nanomolar. `/affinity-maturation-plan` diagnoses it as off-rate-limited, designs a focused CDR-H3 + hotspot library with kinetic (off-rate) selection, and sets the guardrail that every advancing clone re-runs `/sequence-liability-scan`.

### Advance a trainee from supervised to independent humanization
A trainee has co-led three humanizations. `/progression-review` counts the independent reps, confirms consistent evidence, and `/mentor-signoff` records a *scoped* entrustment — independent for standard IgG humanization, still supervised for unusual scaffolds.

### Resolve a kinetics dispute
Two groups report wildly different affinities for the same antibody. `/binding-kinetics` shows one was bivalent over a dense antigen surface (avidity), the other a clean 1:1 monomeric fit — and writes up which number to trust and why.

## Recommended MCP Servers

- **Filesystem** — read/write sequences, models, sensorgrams, and apprentice records in `outputs/`.
- **Fetch / HTTP** — query IMGT, OAS, SAbDab/Thera-SAbDab, and the SAbPred tools for germlines, humanness baselines, and developability scoring.
- **SQLite / database** — back the trainee logbook and competency-evidence tables for the apprenticeship commands.

## Legal & Ethical Considerations

- **Not medical advice.** This is research/engineering tooling. Engineered antibodies require full preclinical and clinical evaluation; nothing here is a treatment, diagnostic, or edibility claim.
- **Biosafety & animal ethics.** Recombinant antibody work falls under institutional biosafety oversight; immunization-based discovery requires IACUC/animal-ethics approval. Record provenance and approvals.
- **IP & freedom-to-operate.** Antibody sequences and formats are heavily patented. Check FTO before advancing an engineered candidate; this workspace does not clear IP.
- **Confidentiality.** Candidate sequences are proprietary — keep them out of external services that retain data.
- **Fair assessment.** Competency progression must be evidence-based and auditable; do not inflate tiers, and record entrustment decisions so they can be challenged.

## Technical References

- [Jones et al. 1986, *Replacing the CDRs of a human antibody* (Nature)](https://doi.org/10.1038/321522a0) — the original CDR-grafting humanization.
- [Raybould et al. 2019, *Five computational developability guidelines (TAP)* (PNAS)](https://doi.org/10.1073/pnas.1810576116) — the Therapeutic Antibody Profiler metrics.
- [IMGT — the international ImMunoGeneTics information system](https://www.imgt.org/) — numbering, germlines, nomenclature.
- [Observed Antibody Space (OAS)](https://opig.stats.ox.ac.uk/webapps/oas/) and [SAbDab/Thera-SAbDab + SAbPred tools](https://opig.stats.ox.ac.uk/webapps/sabdab-sabpred/) — repertoire data, structures, TAP.
- [BioPhi — humanization & humanness (OASis/Sapiens)](https://biophi.dichlab.org/) — humanness scoring and back-mutation design.
- [ten Cate 2005, *Entrustability of professional activities and competency-based training* (Med Educ)](https://doi.org/10.1111/j.1365-2929.2005.02341.x) — the entrustment model the progression loop uses.
- [Collins, Brown & Newman 1989, *Cognitive Apprenticeship*](https://en.wikipedia.org/wiki/Cognitive_apprenticeship) — the modeling/coaching/scaffolding scheme behind the tier-by-tier mentoring.

## Optional plugin

If you have the [`workspace-foundational`](https://github.com/danielrosehill/Claude-Workspace-Foundational-Plugin) plugin installed, additional global commands (`/workspace-foundational:context-sweep`, `/workspace-foundational:find-template`) are available; the workspace works without it.
