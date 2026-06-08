# /tangent-ratio-adapt — Port a Design Across Refractive Indices

Rescale every angle of a published faceting design from the RI it was cut for to a new material, using the Strickland tangent-ratio method, so light performance and meet points carry over.

## Inputs

- The source design: its reference RI and the full list of (angle, index) facet steps (or at least the pavilion main, crown main, and break facets).
- The target material's RI, and its recommended pavilion main from `/optimize-pavilion-angle`.

## Steps

1. Get the **target pavilion main** for the new material (the design's anchor angle).
2. Solve the tangent ratio: `TR = tan(target_pavilion_main) / tan(source_pavilion_main)`.
3. Apply `θ_new = arctan( TR · tan(θ_old) )` to **every** angle in the design — pavilion mains, break facets, crown mains, stars, girdle facets. Index values do **not** change.
4. Verify meet points: confirm groups of facets that converged in the source still share a common point after rescaling (uniform TR preserves this; spot-check the steepest and shallowest).
5. Sanity-check against the new material's critical floor — no rescaled pavilion facet may fall below it.
6. Re-budget tolerance for the new angles (`/tolerance-budget`).

## Output

The adapted design table: original angle → new angle for each step, the TR used, source/target RI, and a meet-point verification note. Save to `outputs/<design>-adapted-<material>.md`.

## Notes

- TR > 1 steepens (porting from higher to lower RI); TR < 1 shallows (lower to higher RI).
- If a crown angle rescales to an impractically steep value, cap it and accept a small light-return trade rather than an uncuttable facet — note the deviation.
- GemCad/GemRay automate this; this command reproduces it transparently and documents the result.
