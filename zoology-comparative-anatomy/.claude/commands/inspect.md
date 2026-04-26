# /inspect — Apply standardized inspection checklist to ONE specimen

The core operation. Drives a systematic, reproducible examination of a specimen against the vertebrate body-plan checklist (`resources/vertebrate-body-plan-checklist.md`), recording structured findings.

## Inputs

Required:
- **Specimen ID** — institutional accession or unambiguous field number.
- **Provenance fields** if not already on file in `context/project.md` for this ID: taxon (binomial + author), sex, age class, preservation, locality (coarse), holding institution.
- **Source material** — at least one of: photographs (note views), dissection notes, micro-CT volume reference, published description with citation.
- **Target system(s)** — e.g. "skull osteology", "all", "cardiovascular + respiratory".

Optional:
- Project's pre-defined character set (auto-loaded from `context/project.md` if present).

## Pre-flight

1. Halt and ask user to fill in any missing provenance.
2. Confirm nomenclatural convention from `context/role.md`.
3. Adapt the body-plan checklist for the target taxon — note adaptations in the output, do not silently drop checklist items.

## Procedure

Walk the checklist for the requested system(s), structure-by-structure:

For each structure:
1. State the structure name in the chosen convention. Secondary citations in parens.
2. Record presence: `present` / `absent` / `damaged-uncertain` / `not-evaluable`.
3. Record count if countable.
4. Record measurement(s) with unit + instrument. Photo-derived measurements flagged `est-from-image` and dependent on calibration.
5. Record character state (state ID) if a character set is defined.
6. Notes — anything noteworthy or unusual.
7. Citations / cross-refs.

Per-system: write a brief summary noting features that diverge from the modal expectation for the taxon.

## Output

Files in `outputs/inspections/`:
- `<specimen-id>__<system>.md` — one per system (e.g. `AMNH-M-31420__skull-osteology.md`)
- `<specimen-id>__full.md` — aggregate across all systems if "all" was requested

Format per `context/for-agent/domain-knowledge.md` §5.

## Validation

- Every checklist item appears in the record (or is flagged not-applicable for the taxon, with reason).
- Every measurement has a unit.
- Every character-state coding has a state ID matching the project's character set.
- Provenance block is complete.
- Damaged / not-evaluable structures are explicitly recorded, not silently omitted.

## Common pitfalls — agent must guard against

- "Large skull" instead of CBL = X mm. Always prefer measurement.
- Skipping a system because "the question doesn't need it" — run the full checklist; the unused systems are valuable for future reuse.
- Naming a structure with one convention then drifting into another mid-document.
- Missing provenance because the user said "you know which one I mean."
