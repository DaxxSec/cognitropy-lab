# Single Specimen Inspection — Prompt Template

**Use case:** You have one specimen and want a complete, structured anatomical inspection driven by the standardized checklist.

## Prompt

I need to inspect specimen `[SPECIMEN_ID]`.

Provenance:
- Taxon: `[BINOMIAL + AUTHOR]`
- Sex: `[M / F / unknown]`
- Age class: `[neonate / juvenile / subadult / adult / unknown]`
- Preservation: `[fluid / dry / mount / fossil / imaged-only]`
- Locality (coarse): `[REGION]`
- Holding institution + accession: `[INSTITUTION + ACCESSION]`

Source material I can supply: `[photographs / dissection notes / micro-CT / paper reference]`. Available views/files: `[LIST]`.

Target system(s) for this pass: `[e.g. "skull osteology" or "all"]`.

Run `/inspect`. For each structure in the body-plan checklist (adapted for taxon as needed), record presence, count where applicable, measurements with units, and notes. Use Terminologia Anatomica nomenclature primarily; secondary citations in parens. Halt and ask if any provenance field is missing or any structure can't be assessed from the source material.

Output a complete `outputs/inspections/[SPECIMEN_ID]__[SYSTEM].md` (or `__full.md` for all-systems) following the format in `context/for-agent/domain-knowledge.md` §5. End with a system-summary paragraph noting any features that diverge from modal expectation for the taxon.
