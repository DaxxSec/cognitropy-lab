---
name: thermal-vibration-review
description: Athermalization and modal failure check — bond-line, CTE, mount stiffness.
---

# /thermal-vibration-review

## Inputs
- Prescription with glass choices and housing material
- Environmental spec from `context/project.md`

## Steps
1. **Athermalization**:
   - Compute dEFL/dT from dn/dT and thermal expansion of each element.
   - Compute barrel expansion dL/dT.
   - Net focal shift vs temperature — does it fit within depth of focus?
2. **Bond-line stress**:
   - For each cemented doublet and each adhesive bond: σ ≈ E_adh · (CTE_glass1 − CTE_glass2 or CTE_housing − CTE_glass) · ΔT
   - Flag σ > 1 MPa as high risk (AIAG-typical glass bond allowable).
3. **Mount compliance**:
   - Three-point vs six-point mount tradeoffs.
   - Preload required for expected shock (F = m·a).
4. **Modal analysis (first-cut)**:
   - Barrel as Euler-Bernoulli beam: f₁ ≈ (1/2π)·(λ²/L²)·√(EI/ρA), λ = 4.73 for fixed-fixed.
   - Target f₁ > 2× dominant drive frequency.
5. **Input to FMEA**: every flagged item becomes a mode with S ≥ 7 if performance-critical.

## Outputs
- `outputs/thermal-sensitivity.csv` — focal shift, element by element
- `outputs/modal-firstcut.csv` — mount natural frequencies
- `user-docs/thermal-vibe-review.md` — narrative with mitigations
