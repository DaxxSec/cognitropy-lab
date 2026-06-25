# /hardness-traverse-plan

Design and interpret a hardness traverse across a section or bore wall to detect chill, decarburization, and section-property gradients.

## Inputs

- Section geometry and the feature of interest (bore wall, deck, bulkhead, chill zone)
- Intended grade and its expected hardness range (`context/references.md`)
- Available method (Brinell HBW, Rockwell, Vickers microhardness)

## Steps

1. Choose the method for the question: Brinell for bulk iron (averages over graphite), Vickers micro (HV) for phase-level traverses and thin surface zones; per ASTM E10 / E384.
2. Lay out the traverse — define start point, spacing, and indent count from surface to core; for cast iron ensure each indent spans enough graphite to read the bulk, or place micro-indents deliberately in the matrix.
3. Specify load and indent spacing to avoid overlap-affected readings (≥2.5× diagonal apart).
4. Interpret the profile: a hard surface step → chill (free carbides); a soft surface step → decarburization or under-refined Al-Si bore; a smooth gradient → normal section effect.
5. Cross-check hardness against the metallography (a hardness spike should coincide with carbides or martensite seen under the microscope) and convert the result into a likelihood ratio for `/bayes-evidence-update`.

## Output

`outputs/<case-id>/hardness-traverse.md`: the indent map, the hardness-vs-depth profile, the chill/decarb/gradient call, the metallography cross-check, and the LR contribution.

## Notes

- A single Brinell number on cast iron is nearly meaningless without knowing where it sat relative to graphite — the traverse and method matter more than the value.
- A surface hardness spike with no matching carbides in metallography suggests an indent that hit a single hard particle — re-take.
