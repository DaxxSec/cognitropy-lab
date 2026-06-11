# /clausius-clapeyron-fit

Fit the stress–temperature transformation slope (dσ/dT) that governs stress-induced martensite, linking the thermal transformation to the mechanical one.

## Inputs

- A set of (temperature, critical transformation stress) pairs — e.g. plateau onset stress from isothermal tensile tests at several temperatures above Af, or shift of Ms under applied load.
- The zero-load transformation temperatures (Ms, Af) from `/dsc-transformation-map`.
- Transformation strain ε_tr (recoverable plateau strain) and ΔH if a Maxwell-relation cross-check is wanted.

## Steps

1. Read `context/concepts.md` for the Clausius–Clapeyron analogue: `dσ/dT = −ΔH / (T·ε_tr·ρ)` (equivalently ΔS per unit volume), and why SMAs follow a near-linear σ–T transformation line.
2. Plot critical stress vs. test temperature; fit a straight line over the superelastic regime (T > Af).
3. Report the slope **dσ/dT** (MPa/°C) with its confidence interval and R²; typical binary NiTi is ~5–8 MPa/°C.
4. Cross-check the fitted slope against the thermodynamic estimate from ΔH and ε_tr — a large mismatch flags inconsistent ε_tr, friction/hysteresis effects, or non-isothermal heating during loading.
5. Use the slope to predict the **stress to induce martensite** at any service temperature, and the temperature ceiling above which the alloy plastically yields before transforming (loss of superelasticity).
6. Note loading-rate effects: fast loading is adiabatic (self-heating raises the apparent slope).

## Output

`outputs/clausius-clapeyron-<alloy>-YYYY-MM-DD.md`: the σ–T plot description, fitted slope ± CI, thermodynamic cross-check, predicted SIM stress at the target service temperature, and the superelastic temperature window upper bound.

## Notes

- The line is only piecewise-linear; near Ms it curves and below Mf the alloy is fully martensitic (detwinning, not transformation).
- Self-heating from the latent heat makes high strain-rate tests deviate — quote the strain rate.
- Cu-based SMAs show steeper, more scattered slopes; do not transfer a NiTi slope to a CuAlNi part.
