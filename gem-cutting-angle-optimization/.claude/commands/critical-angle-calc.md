# /critical-angle-calc — Critical Angle & Minimum Pavilion

Compute the total-internal-reflection critical angle from a material's refractive index and translate it into the minimum safe pavilion main angle below which the stone will window.

## Inputs

- Refractive index (RI) of the material — measured (refractometer) or from `context/references.md`. For doubly-refractive stones, use the average or the relevant ray's RI.
- (Optional) intended table % and outline (round, oval, emerald) — affects how much margin to add.

## Steps

1. Compute `θ_critical = arcsin(1 / RI)` in degrees.
2. State the windowing principle: pavilion rays must strike the facet at more than `θ_critical` from the normal to reflect; shallower pavilions leak.
3. Derive the **minimum pavilion main** as `θ_critical + 2°` (conservative floor) and a **recommended starting pavilion** as `θ_critical + 3–4°`, clamped to known good values in `references.md`.
4. Flag low-RI risk: if RI < 1.50, warn that the windowing margin is narrow and brilliance falls off fast above optimum.
5. Note how table size interacts — large tables on shallow pavilions invite fish-eye even above the floor.

## Output

A short report: RI, critical angle, minimum pavilion main, recommended starting pavilion, and a windowing-risk note. Save to `outputs/<material>-critical-angle.md` so later commands can read it.

## Notes

- Critical angle is the *floor*, not the optimum — feed the recommended starting pavilion into `/optimize-pavilion-angle`.
- Synthetic equivalents share the natural RI (synthetic sapphire = corundum 1.762); treatments rarely move RI enough to matter for the floor.
