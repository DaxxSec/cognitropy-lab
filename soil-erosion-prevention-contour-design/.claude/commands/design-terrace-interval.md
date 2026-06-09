# /design-terrace-interval

Compute terrace spacing (vertical and horizontal interval) and channel grade for a slope, then express the result as the slope-length capacity it restores.

## Inputs

- Slope steepness (%) and total slope length.
- Soil erodibility/infiltration class and rainfall region (drive the spacing coefficients).
- Terrace type: broadbase (graded/level), channel (Nichols), or bench.
- For graded terraces: target channel grade (0.1–0.6%) and outlet location.

## Steps

1. Read `context/concepts.md` "Contour-based support practices" (terraces) and "RUSLE" (LS factor).
2. Compute the **vertical interval** VI = X·s + Y (s = slope %; X, Y from the regional rainfall/soil pair — state the source). Convert to horizontal interval HI = VI / (s/100).
3. Choose level vs graded: level (store + infiltrate) for permeable soils in humid–subhumid zones; graded (carry to outlet) otherwise. For graded, set the channel grade and confirm a stable outlet.
4. Express the erosion benefit as LS reduction: each terrace shortens the effective slope length to ~HI, lowering LS and therefore RUSLE A — recompute A/T with the new effective length via `/estimate-soil-loss`.
5. Size the terrace channel cross-section to carry the inter-terrace runoff (hand off Qₚ to `/forecast-runoff-capacity`); set freeboard.
6. Count terraces over the slope length and note construction earthwork order of magnitude.

## Output

`outputs/terraces/interval-<field>-YYYY-MM-DD.md` — VI/HI, terrace count, type and grade, the effective-slope-length reduction and resulting A/T, channel sizing hand-off, and outlet assignment.

## Notes

- A graded terrace with no designed outlet is a breach waiting to happen — the outlet (waterway/diversion) is part of this design, not separate.
- Bench terraces suit steep land (>15–20%) but are earthwork-intensive; verify cost vs strip cropping at moderate slopes.
- Wider HI eases farm machinery but raises inter-terrace soil loss — balance farmability against A/T.
