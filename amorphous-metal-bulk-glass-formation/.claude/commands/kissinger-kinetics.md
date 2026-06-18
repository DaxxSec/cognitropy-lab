# /kissinger-kinetics

Derive the crystallization activation energy and Avrami parameters from multi-heating-rate DSC — the kinetic constants that turn "it will eventually crystallize" into a clock the yield and TPF-window models can read.

## Inputs

- Crystallization peak (or onset) temperatures Tp at **three or more** heating rates β (e.g. 5, 10, 20, 40 K/min).
- Optional: isothermal DSC crystallized-fraction-vs-time curves at one or more hold temperatures (for a direct Avrami n).
- Alloy composition and the DSC convention used (from `/dsc-landmarks`).

## Steps

1. Read `context/references.md` for the Kissinger, Ozawa, and JMAK working equations.
2. Build the **Kissinger plot**: ln(β/Tp²) vs 1/Tp. Linear-fit; slope = −Ea/R → activation energy Ea. Report R².
3. Cross-check with **Ozawa/Flynn-Wall-Ozawa** (ln β vs 1/Tp, slope −1.052·Ea/R) — agreement within ~10% builds confidence.
4. Determine the **Avrami exponent n**: from isothermal data via ln[−ln(1−X)] vs ln t (slope = n), or estimate from the non-isothermal peak shape (Augis–Bennett / Ozawa) if only scans exist. State which method.
5. Back out **K₀** (pre-exponential) so K(T) = K₀·exp(−Ea/RT) is fully specified for the supercooled-liquid range.
6. Report uncertainty: fit scatter, n method, and the temperature range over which the kinetics are valid (don't extrapolate far past the data).

## Output

`outputs/kinetics-<alloy>-YYYY-MM-DD.md`: Ea (Kissinger + Ozawa), pre-exponential K₀, Avrami n with method, the Kissinger plot fit quality, and the validity temperature range. This is the kinetic model consumed by `/crystallization-yield` and `/tpf-window`.

## Notes

- Kissinger assumes a single dominant, thermally-activated crystallization process — for **multistage** (twin-peak) transformations, fit each peak separately and say so.
- n encodes nucleation + growth dimensionality (1–4); a non-integer n usually means overlapping mechanisms, not a measurement error.
- ASTM E698 standardizes Arrhenius-type kinetics by thermal analysis — follow it for reportable numbers.
