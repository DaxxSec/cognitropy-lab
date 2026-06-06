# /characterize-historic-mortar

Run the full two-track identification of an original mortar — petrographic "morphology" plus chemical "barcode" — and assign it a binomial name.

## Inputs

- Sample provenance: building, elevation, height, date sampled, drawing reference (one record per fragment).
- Petrographic data if available: thin-section images / report (binder character, aggregate mineralogy, grading, voids, point-counted binder:aggregate).
- Chemical data if available: acid-digestion binder:aggregate + insoluble-residue grading; oxide analysis (SEM-EDS/XRF); XRD phases; TGA steps.
- The provisional binder class from `/mortar-key` (optional but recommended).

## Steps

1. Read `context/workflows.md` "Two-track identification" and `context/concepts.md` "Mortar characters".
2. **Morphology track:** record binder character, hydraulic phases, lime lumps, aggregate mineralogy/provenance/roundness, grading curve, voids; note point-counted binder:aggregate (by volume).
3. **Barcode track:** record acid-digestion binder:aggregate (by mass) + residue grading; compute **Hydraulic Index** `(SiO₂+Al₂O₃+Fe₂O₃)/(CaO+MgO)` from oxides; list XRD phases and TGA mass-loss steps.
4. Cross-check the tracks for calcareous-aggregate confounding (petrography vs digestion disagreement) and contamination (gypsum, salts vs original binder).
5. Score concordance; set a determination confidence (high/medium/provisional) and the characters that drove it.
6. Assign the binomial name per the naming convention (`<binder class> <ratio> (<aggregate descriptor>)`) with author + date.

## Output

A markdown identification report `outputs/idreport-<slug>-YYYY-MM-DD.md` with: provenance, both character tracks, HI, binder:aggregate, aggregate grading, phases, concordance note, assigned binomial name, and determination confidence. Hand off to `/specimen-accession`.

## Notes

- Never trust acid-digestion binder:aggregate alone when aggregate may be calcareous — pair with petrography.
- One track only → mark the name *provisional* and name the missing confirmatory character.
- Separate decay products (efflorescence salts, ettringite, gypsum) from the original binder before naming.
