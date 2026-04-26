# Getting Started With This Workspace

Welcome — this is a Comparative Anatomy workspace specialized for **standardized-checklist-driven inspection** of zoological specimens.

## What it does

The workspace gives you a structured way to examine specimens (your own, museum loans, or published descriptions), record findings consistently, compare across taxa with explicit homology reasoning, and produce reports in your preferred voice (manuscript / curation entry / classroom handout / cladistic coding).

## What you do first

1. **Run `/onboard`.** Claude will interview you through ~15 questions covering your role, taxonomic focus, specimen access, project goals, nomenclatural preference, and tooling. It then populates `context/role.md`, `context/project.md`, `context/constraints.md`, and `context/for-agent/environment.md`. You can change your answers later — it's not locked.

## Then for each working session

After `/onboard`, you have five workflow commands:

| Command | What it does |
|---|---|
| `/inspect` | Apply the standardized inspection checklist to one specimen. Outputs a structured per-system or full-specimen record. |
| `/compare` | Compare homologous structures across two or more taxa with explicit topology + ontogeny + phylogenetic justification. |
| `/landmark` | Catalog anatomical landmarks for a body region (foundation for geometric morphometrics). |
| `/trait-matrix` | Build or update a comparative trait matrix with explicit homology and per-cell citations. |
| `/report` | Synthesize prior inspections + comparisons into a manuscript / curation / classroom / cladistic / field-notebook output. |

Each command is documented in `.claude/commands/<command>.md`. Each one has a pre-flight checklist, a procedure, output specification, and validation criteria.

## Key principle: the repo IS your memory

Every inspection, comparison, landmark catalog, matrix, and report lives in `outputs/`. Every project decision in `planning/plan.md` (with pivots in `planning/pivots/`). Every session in `work-log/<YYYY-MM-DD>.md`. Don't rely on conversational memory — reload context from these files.

## What to put under your hands first

- Specimen photos / dissection notes / paper references in a stable location (recommended: outside this workspace, referenced by absolute path).
- A nomenclatural reference: TA2, NAV, NAA, or a taxon-specific atlas. Cite which one when you onboard.
- A phylogenetic tree for your taxa of interest if you'll do comparative work — published references or a Newick / NEXUS file.

## Things to know up front

- The agent will refuse to invent measurements, ranges, or character states. If you don't have data, it'll tell you what it would need.
- Provenance is a hard requirement: specimen ID, taxon, sex, age class, preservation, locality, and holding institution. Specimens without provenance produce records flagged as preliminary.
- Live-animal procedures are out of scope unless you supply IACUC (or equivalent) approval.
- Indigenous / culturally significant material requires explicit consultation evidence before descriptive work proceeds.

## Where to push deeper

- Read `context/for-agent/domain-knowledge.md` for the conceptual foundation (homology theory, body plans, methodology principles).
- Read `context/for-agent/workflows.md` for full procedural detail of each workflow.
- Read `resources/vertebrate-body-plan-checklist.md` to see the actual standardized checklist.

## When this workspace doesn't help

- Phylogenetic tree inference (use IQ-TREE / RAxML / MrBayes / BEAST).
- Multivariate morphometric analysis beyond descriptives (use geomorph / Morpho / MorphoJ).
- Histological interpretation requiring specialized stain expertise (defer to a histologist).
- Identifications beyond your claimed taxonomic competence.

## When you find a bug or want to extend

- The skeleton this workspace was built from lives in the `cognitropy-library` repository at `skills/cognitropy-daily-build/templates/workspace-base/`. Improvements there propagate to all future daily builds.
- The body-plan checklist (`resources/vertebrate-body-plan-checklist.md`) is the single most important resource — improvements to it improve every future inspection.
- If you adapt the checklist for an invertebrate phylum, save the adaptation as `resources/<phylum>-body-plan-checklist.md` and reference it from your inspections.
