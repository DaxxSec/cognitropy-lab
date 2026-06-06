# /match-compatible-mortar

Design or select a repair mortar that is compatible with a characterised original — softer, more porous and more vapour-open than the substrate.

## Inputs

- The characterised original (name, HI, binder:aggregate, aggregate grading/mineralogy/colour) from the accession record.
- Substrate data: unit type and strength (soft brick / soft stone / hard stone), porosity if known.
- Exposure: orientation, driving-rain severity, parapet/chimney/below-DPC flags, frost exposure.
- Any salt loading and known moisture sources.

## Steps

1. Read `context/workflows.md` "Designing the compatible repair mortar" and `context/concepts.md` "The cardinal selection rule".
2. **Match aggregate first** — replicate grading, mineralogy and colour of the original; this controls porosity, shrinkage and appearance.
3. Choose a binder **no harder** than the original (one notch softer is safe; harder is never): air lime → air lime / pozzolan-gauge only if exposure demands; NHL → match or undershoot the class.
4. Validate the proposed mix on `/binder-phylogeny` — it must sit in or below the original's clade; reject anything landing in the cement clade.
5. Set proportions by volume (voids-ratio rule), water demand, pozzolan/gauge, batching, knock-up, application and joint profile.
6. Define performance acceptance vs the substrate: strength **below** the unit (EN 1015-11); capillarity **above** a dense substrate (EN 1015-18); vapour resistance μ **≤** the unit (EN 1015-19); frost/salt resistance for the exposure (EN 12371/12370).
7. Specify curing (frost/rain/rapid-dry protection, damp curing, carbonation time) — this feeds the maintenance calendar.

## Output

A repair-mortar specification `outputs/mixspec-<slug>-YYYY-MM-DD.md`: target original, aggregate spec + grading, binder + proportions, pozzolan/gauge, water, application, acceptance criteria with target values and standards, and curing/weather constraints.

## Notes

- Severe exposure tempts a harder mix — prefer better detailing/sheltering or a sacrificial render over an incompatible mortar.
- If the "original" is a damaging later cement repair, design for the *units and surviving original*, not the cement.
- Test panels and 28/90-day acceptance testing precede full-scale work.
