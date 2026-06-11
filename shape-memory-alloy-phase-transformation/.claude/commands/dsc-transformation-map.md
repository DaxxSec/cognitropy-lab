# /dsc-transformation-map

Extract the four transformation temperatures, thermal hysteresis, and latent heat from a differential scanning calorimetry (DSC) thermogram — the foundational fingerprint of an SMA's phase transformation.

## Inputs

- DSC data file (heat flow vs. temperature, both cooling and heating segments) — CSV, or a description of peak positions if no raw file.
- Sample mass (mg) and the heating/cooling rate (°C/min) used — both affect peak shape and apparent temperatures.
- Alloy nominal composition if known (e.g. Ni-50.8 at% Ti), and prior thermal/mechanical history if available.

## Steps

1. Read `context/concepts.md` for the martensite ↔ austenite convention and the ASTM F2004 tangent (onset) construction.
2. Identify the **exothermic** peak on cooling (austenite → martensite, and any intermediate R-phase) and the **endothermic** peak on heating (martensite → austenite).
3. Apply the tangent/baseline-intercept method to read **Ms, Mf** (cooling) and **As, Af** (heating). Flag any shoulder or twin-peak as a possible R-phase or multistage transformation.
4. Compute **thermal hysteresis** as `Af − Ms` (or peak-to-peak Ap − Mp) and the **transformation enthalpy** ΔH by integrating each peak area (J/g).
5. Sanity-check against the alloy family in `context/references.md` (e.g. binary NiTi hysteresis ~20–40 °C, ΔH ~20–32 J/g); note deviations that suggest oxidation, off-stoichiometry, or aging precipitates.
6. Record rate and mass so the result is reproducible — apparent Ms/Mf shift with scan rate.

## Output

`outputs/dsc-map-<alloy>-YYYY-MM-DD.md`: a table of Ms/Mf/As/Af (+R-phase Rs/Rf if present), hysteresis, ΔH (cooling and heating), the construction method used, scan parameters, and a one-line interpretation of the transformation signature.

## Notes

- Onset (tangent) vs. peak temperatures differ by several degrees — state which convention you used; ASTM F2004 specifies the tangent method.
- A widened or suppressed peak after thermal cycling is a functional-fatigue signature — cross-link to `/functional-fatigue-budget`.
- Multistage (B2 → R → B19′) transformations are common in aged Ni-rich NiTi; do not force a single Ms/Mf onto a twin-peak curve.
