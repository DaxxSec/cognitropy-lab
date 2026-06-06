# /delimit-mix

Decide whether variation across sampled mortars represents one mortar taxon or several distinct mixes / build phases — the species-delimitation analog.

## Inputs

- Character sets for multiple samples (HI, binder:aggregate, aggregate grading, colour) with their provenance/elevation.
- Documentary or archaeological phasing if available (build campaigns, known repairs).
- The "same mix" tolerance rule from `context/references.md`.

## Steps

1. Read `context/workflows.md` "Delimiting mixes".
2. Plot each sample's characters against its location on the elevation map.
3. Look for **discontinuities, not gradients**: clustered character sets separated by clear gaps = distinct taxa; a continuum = one mortar with natural variation.
4. Cross-check clusters against documentary phasing; align each cluster with a likely campaign (original, later repair, modern patch).
5. Apply the tolerance rule per cluster; within tolerance → one taxon, beyond → delimit and accession a new mix (`/specimen-accession`).
6. Watch for **cryptic** cases — visually identical but chemically distinct (different HI) → trust the chemical barcode.
7. Map each delimited mix to its own repair recipe and conservation decision (retain / repair / plan careful removal of damaging cement).

## Output

A delimitation report `outputs/delimit-<building>-YYYY-MM-DD.md`: the character plot/table, the delimited taxa with their locations and likely phases, cryptic-case flags, and the recipe/decision per taxon.

## Notes

- Resist over-splitting on gradients — one recipe with stated tolerances is more conservable than many bespoke patches.
- A cluster that maps exactly to a known repair date is strong corroboration; absence of records is not evidence of one mortar.
