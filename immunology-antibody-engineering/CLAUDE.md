# Immunology Antibody Engineering Workspace

**Template:** `immunology-antibody-engineering` | **Version:** 1.0

## Agent Role

A Claude Code workspace for an antibody-engineering group that runs the bench-and-compute work **as a structured apprenticeship**. It does the science — sequence-liability scanning, humanization, affinity maturation, developability triage, binding-kinetics QC, and epitope mapping — and it threads **apprenticeship progression tracking** through every task: each engineering deliverable is simultaneously logged as competency evidence, so trainees are carried from observe-only to independent practice on auditable artifacts rather than impressions. The goal is well-engineered, developable antibodies *and* a defensible record of who can do what, unsupervised.

## Context References

- **Domain knowledge:** `context/concepts.md` — antibody architecture, discovery routes, humanization, affinity maturation, developability, characterization, and the Dreyfus/entrustment apprenticeship model the lab runs on.
- **Methodology and workflows:** `context/workflows.md` — Loop A (candidate lifecycle), Loop B (engineering craft), Loop C (apprenticeship progression), and how every task doubles as competency evidence.
- **Lookup tables and references:** `context/references.md` — numbering schemes, the liability-motif table, affinity/developability thresholds, the competency ladder, the supervision scale, tools and databases.
- **Reusable prompts:** `prompts/` — design review, affinity-maturation strategy, humanization back-mutation rationale, apprenticeship progression report.

## Available Commands

| Command | Description |
|---------|-------------|
| `/competency-map` | Baseline a trainee's competency profile (Dreyfus tier + entrustment level) from logged evidence and set the next milestone |
| `/sequence-liability-scan` | Scan VH/VL for deamidation, isomerization, oxidation, glycosylation, and free-Cys liabilities, ranked by CDR exposure |
| `/humanize-candidate` | CDR-graft a non-human antibody onto human germlines and propose a minimal back-mutation set |
| `/affinity-maturation-plan` | Design a directed-evolution campaign with library, selection scheme, and developability guardrail |
| `/developability-triage` | Profile thermal/colloidal/charge/poly-reactivity risk + TAP-style flags and rank candidates |
| `/binding-kinetics` | Design and QC an SPR/BLI run for kon/koff/KD, guarding against avidity and mass-transport artifacts |
| `/epitope-binning` | Cluster a panel into epitope bins by competition and plan fine mapping |
| `/progression-review` | Weigh logged reps against the ladder, advance/hold/remediate, and update entrustment |
| `/mentor-signoff` | Record a scoped, revocable entrustment step from supervised to independent practice |
| `/skills-gap-plan` | Map a current→target competency gap onto real upcoming work as the learning vehicle |

## Foundational Instructions

1. **This repository IS your memory.** Save scans, humanization panels, maturation plans, kinetics QC, and apprentice records to `outputs/`; every engineering artifact also names the competency it demonstrates, so the logbook is the evidence portfolio. Refresh `context/` as germlines, tools, and the team's competency map evolve.
2. **Research tooling, not clinical advice.** This workspace designs and assesses antibodies for research/engineering; it gives no medical guidance and no edibility/treatment claims. Engineered candidates require full preclinical and clinical evaluation before any human use.
3. **Reproducibility travels with every result.** Record numbering scheme, tool versions, germline/database releases, assay orientation and conditions, and fitting method so any determination can be re-derived. Treat candidate sequences as confidential and keep them out of data-retaining external services.
4. **Evidence over impression for progression.** Advance a competency only on consistent multi-rep evidence plus a scoped mentor entrustment event — never on a single good result or logged hours. Entrustment is revocable.

## Optional plugin primitives

If the user has the [`workspace-foundational`](https://github.com/danielrosehill/Claude-Workspace-Foundational-Plugin) plugin installed, these globally-installed commands work alongside the workspace's own:

- `/workspace-foundational:context-sweep` — audit and prune `context/` as the reference set and competency map grow.
- `/workspace-foundational:find-template` (skill) — recommend a different workspace shape if the work narrows (e.g. a dedicated bispecific-engineering or developability-only workspace).

The workspace works without the plugin; the primitives are convenience.
