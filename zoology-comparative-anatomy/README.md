# zoology-comparative-anatomy

> A Claude Agent Workspace for **comparative anatomy fieldwork driven by standardized inspection checklists.**
>
> Part of the [Cognitropy Lab](https://github.com/DaxxSec/cognitropy-lab) — Day 31, Life Sciences.

## What This Workspace Is

A standalone working environment that turns Claude into a **Comparative Inspector** — a specialist collaborator for examining specimens, photos, and published descriptions through structured, reproducible checklists, then translating those observations into homology hypotheses, trait matrices, and comparative reports usable for research, teaching, or curation.

The technique pairing for this build is intentional: comparative anatomy without a checklist is anecdote; with one, it becomes a survey. Every inspection in this workspace runs the same body-plan checklist (`resources/vertebrate-body-plan-checklist.md`), adapted per taxon. Every comparison cross-references the resulting structured records. Every claim of homology cites topology, ontogeny, and (when available) molecular phylogenetic evidence.

## Why a Checklist-Driven Workflow

Field experience and published reviews repeatedly surface the same failure modes in comparative descriptions:

1. **Missed structures.** A muscle, foramen, or sutural junction goes unrecorded because nobody asked about it. Three years later the question can't be answered without re-examining specimens.
2. **Inconsistent vocabulary.** Two papers describe the same structure with different names, and a third invents its own. A trait matrix built from them is silently corrupted.
3. **Implicit homology assertions.** "The X of taxon A is like the X of taxon B" — no topology check, no ontogenetic check. Cladistic analyses inherit unverified character codings.
4. **Lost provenance.** Specimens become "AMNH M-31420" in field notes and "the New York male" in the manuscript. Re-identification is impossible.

A standardized checklist does four things: it forces completeness, anchors vocabulary, requires explicit homology justification, and makes provenance a structured field rather than a footnote.

## Getting Started

1. From the `cognitropy-lab` repo:

   ```bash
   git clone https://github.com/DaxxSec/cognitropy-lab.git
   cd cognitropy-lab/zoology-comparative-anatomy
   claude
   ```

2. On the first session, run `/onboard`. Claude will interview you about:
   - Your role (PI, postdoc, grad student, undergrad, museum curator, educator, paleontologist)
   - Taxonomic focus (vertebrates broadly, mammals, sauropsids, fishes, invertebrate phylum X)
   - Specimen access (live observation, museum specimens, photos, published figures, micro-CT data)
   - Project goal (descriptive monograph, phylogenetic character coding, geometric morphometrics, teaching exercise, curation audit)
   - Nomenclatural convention preference (Terminologia Anatomica, NAV, NAA, taxon-specific atlas)
   - Output format expected (manuscript-ready, NEXUS character matrix, classroom handout, museum catalog entry)

3. After onboarding, invoke any domain command below.

## Command Reference

| Command | Purpose | Inputs | Outputs |
|---------|---------|--------|---------|
| `/onboard` | Initial workspace personalization | Interview-style answers | Populated `context/role.md`, `context/project.md`, `context/constraints.md`, `context/for-agent/environment.md` |
| `/inspect` | Apply the standardized inspection checklist to ONE specimen | Specimen ID + photos / dissection notes / paper reference; target body system or "all" | `outputs/inspections/<specimen-id>__<system>.md` — structured per-system findings with measurements + coded character states |
| `/compare` | Structured comparison of homologous structures across 2+ taxa | List of specimen IDs + structure(s) of interest | `outputs/comparisons/<structure>__<taxa>.md` — homology assertions with topology/ontogeny justification, character-state differences, candidate apomorphies |
| `/landmark` | Identify and catalog anatomical landmarks for one body region | Specimen ID + body region (e.g. "skull lateral view", "humerus proximal end") | `outputs/landmarks/<specimen-id>__<region>.md` — landmark list with definitions + Type I/II/III classification (Bookstein), coordinates if image-derived |
| `/trait-matrix` | Build or update a comparative trait matrix | Taxa list + character set (or "derive from prior inspections") | `outputs/matrix/<project-slug>.tsv` + `<project-slug>.notes.md` — rows × columns with explicit state definitions, citations per cell |
| `/report` | Synthesize inspections into a comparative anatomy report | Project slug or specimen list | `outputs/reports/<title>.md` — manuscript-style or curation-style depending on `context/project.md` settings |

## Directory Structure

```
zoology-comparative-anatomy/
├── CLAUDE.md                           # Lightweight agent identity & rules
├── README.md                           # This file
├── CREATION_REPORT.md                  # Build provenance
├── context/
│   ├── project.md                      # Active investigation
│   ├── role.md                         # User profile
│   ├── constraints.md                  # Data/ethics/publishing constraints
│   └── for-agent/
│       ├── domain-knowledge.md         # Comparative anatomy concepts, homology theory
│       ├── workflows.md                # Step-by-step inspection/comparison workflows
│       ├── environment.md              # User's specimens & tools
│       └── tools.md                    # Recommended digital tools
├── .claude/commands/                   # Slash commands
├── prompts/                            # Reusable prompt templates
├── resources/                          # Checklists, glossary, protocols
├── planning/                           # plan.md + pivots/
├── work-log/                           # Dated session logs
├── user-docs/                          # Polished deliverables for the user
└── outputs/                            # inspections/, comparisons/, landmarks/, matrix/, reports/
```

## Example Use Cases

**1. Vertebrate paleontology — fossil description.**
You have a partial postcranial skeleton of an extinct mammal. Run `/inspect` system-by-system on the holotype with photos. Run `/landmark` on each preserved element. Run `/compare` against three closely related extant taxa. Run `/trait-matrix` to position the new specimen in an existing cladistic dataset. Run `/report` to produce a description manuscript draft conforming to journal style.

**2. Museum curation — re-identification audit.**
You inherited a drawer of "ratfish" specimens with sparse labeling. Run `/inspect` on each specimen using the chondrichthyan-specific checklist. The structured outputs feed a trait matrix that lets you re-key specimens against the latest taxonomy and surface mislabeled or undetermined material.

**3. Undergraduate comparative anatomy course.**
Students dissect a frog and a rat. Run `/inspect` on each, side-by-side. Run `/compare` on the cardiovascular and respiratory systems. The structured comparison shows homology vs. analogy in pulmonary circulation, the four-chambered vs. three-chambered heart distinction, and the embryological origin of the diaphragm. Output is a classroom handout.

## Recommended Tools / MCP Servers

- **ImageJ / Fiji** — measurements from digital images, calibration via scale bars.
- **Mesquite** — phylogenetic character coding, NEXUS file management.
- **geomorph** (R package) — geometric morphometrics from landmark data.
- **TPS series** (tpsDig, tpsRelw, tpsSplin) — landmark digitization workflow.
- **OpenSpecimen / Specify** — specimen metadata management.
- **iDigBio API** — query specimen metadata across U.S. natural history collections.
- **VertNet** — vertebrate specimen records search.
- **MorphoSource** — 3D media (CT scans, surface scans) repository.

If MCP servers exist for any of the above, register them in `.mcp.json` after `/onboard`.

## Standards & References

- **Terminologia Anatomica (TA2, 2019)** — international standard for human anatomy nomenclature; baseline for vertebrate cross-reference.
- **Nomina Anatomica Veterinaria (NAV, 6th ed., 2017)** — domestic mammal nomenclature; widely applied to wild vertebrates.
- **Nomina Anatomica Avium (NAA, 2nd ed., 1993)** — bird-specific nomenclature.
- **Romer, A.S. & Parsons, T.S.** *The Vertebrate Body* (6th ed., 1986) — classic comparative reference.
- **Kardong, K.V.** *Vertebrates: Comparative Anatomy, Function, Evolution* (8th ed., 2018) — modern comprehensive textbook.
- **Liem, K.F., Bemis, W.E., Walker, W.F., Grande, L.** *Functional Anatomy of the Vertebrates* (3rd ed., 2001).
- **Hall, B.K.** *Homology: The Hierarchical Basis of Comparative Biology* (1994) — homology theory.
- **Bookstein, F.L.** *Morphometric Tools for Landmark Data* (1991) — landmark classification (Type I/II/III).

For invertebrate phyla, defer to the taxon-specific reference (e.g. Brusca & Brusca *Invertebrates* 3rd ed.; Ruppert et al.; phylum-specific monographs).

## Ethical & Legal Considerations

- **Specimen sourcing.** Only work with legally collected/accessioned material. Wildlife specimens require collection permits (US: ESA, MBTA, state permits; international: CITES). Museum specimens carry institutional accession terms — respect them.
- **Publishing photos of specimens.** Get permission from the holding institution; cite the museum number; respect any embargo.
- **Live animals.** Any methodology involving live animals requires IACUC (US) or equivalent ethical review. This workspace assumes specimens are dead, preserved, fossilized, or imaged-only.
- **Indigenous & culturally significant material.** Some collections (especially bioarchaeological / culturally significant) require consultation with descendant communities (NAGPRA, equivalent). Flag and decline analysis if provenance is unclear.
- **Endangered/threatened taxa.** Be aware of species status. Even descriptive work can have policy implications for poaching pressure (avoid publishing precise locality for sensitive taxa).

## Memory Rule

Use this repository as primary memory. Log each session in `work-log/<YYYY-MM-DD>.md`. Keep `context/project.md` current with the active investigation. Treat user-supplied specimen data as sensitive by default — see `context/constraints.md`.
