# /onboard — Initialize Comparative Inspector workspace

REQUIRED first run. Conducts an interview that personalizes the workspace to the user's research focus, taxonomic scope, specimen access, and output expectations.

## Goals

1. Populate `context/role.md` (user role, experience, taxonomic focus, nomenclatural preference, output voice).
2. Populate `context/project.md` (active investigation, specimens, hypotheses, character set if applicable).
3. Populate `context/constraints.md` only where the user wants to override defaults (defaults are research-grade strict).
4. Populate `context/for-agent/environment.md` (specimens, software, file conventions).

## Procedure

Conduct the interview in phases. Confirm each phase back to the user before writing.

### Phase 1: Role & focus

Ask the user (one or two questions per turn, not all at once):

1. What's your role here — PI / postdoc / grad student / undergraduate / curator / educator / paleontologist / independent? Years in field?
2. What taxonomic group is your primary focus? (vertebrates broadly / mammals / sauropsids / fishes / specific clade / specific invertebrate phylum)
3. Roughly how many specimens does this workspace need to handle in scope, and over what timeframe?

### Phase 2: Specimens & access

4. Specimen source: own collection, institutional collection, borrowed loans, digital-only (photos / CT / surface scans), fossil collection, classroom?
5. Holding institution(s) for any institutional material?
6. Imaging available: photography, micro-CT, surface scans, histological sections, none?

### Phase 3: Project & hypotheses

7. What's the project doing? (descriptive monograph / comparative survey / phylogenetic character coding / geometric morphometrics / curation audit / educational / paleontological)
8. What's the specific question or scope? Phrase it as a testable claim or operational question.
9. Are there pre-defined characters being coded, or will characters emerge from inspections?

### Phase 4: Conventions & output

10. Nomenclatural convention preference: Terminologia Anatomica (TA2) / NAV / NAA / taxon-specific atlas / your group's house style?
11. Output voice for `/report`: manuscript-ready / curation entry / classroom handout / field-notebook / cladistic-coding terse?
12. Any embargo or sensitive-locality flags on the project?

### Phase 5: Tooling

13. R / Python environment — installed? Key packages?
14. Mesquite, ImageJ, TPS series, geomorph — which are available?
15. Specimen-management software in use? (OpenSpecimen / Specify / spreadsheet / paper)

### Write & confirm

After the interview, write the populated files and read them back to the user as a unified summary. Ask: "Anything to correct before this is locked in?" Iterate until the user accepts.

Then offer next steps:
- "Want to run `/inspect` on a first specimen?"
- "Want to draft a character set in `context/project.md` first?"
- "Want me to scan an existing trait matrix or NEXUS file you can supply?"

## Outputs

- `context/role.md` — populated
- `context/project.md` — populated
- `context/constraints.md` — populated (or unchanged if defaults accepted)
- `context/for-agent/environment.md` — populated
- A confirmation summary in chat
