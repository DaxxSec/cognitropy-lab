# Workflows

## W1. First-Order Design Workflow
1. **Extract specs** from `context/project.md`. If any of {waveband, FOV, f/#, detector, environment} are TBD, stop and ask.
2. **Paraxial layout**: compute EFL, EPD, image height, chief-ray angles.
3. **Pick starting point**: from `resources/starting-designs.md` or Smith's *Modern Lens Design*.
4. **Sanity check**: Airy diameter vs pixel pitch, etendue vs source emittance, aberration budget vs spec.
5. **Output**: write element table to `outputs/prescription-v{N}.csv`, record rationale in `work-log/`.

## W2. Design FMEA Workflow
1. **Decompose** system into functions (imaging, focusing, filtering, mounting, thermal path, EMI, safety).
2. **For each function, brainstorm modes** — use the starter catalog in `resources/fmea-catalog.md` plus domain-specific modes.
3. **Score each mode** (S, O, D) using the rubrics in `resources/rpn-rubric.md`.
4. **Compute RPN**, sort desc.
5. **Propose mitigation** for RPN ≥ 100 and any S=10.
6. **Re-score after mitigation** and document residual risk.
7. **Write to** `outputs/fmea-worksheet.csv` with columns: Function, Mode, Effect, Cause, S, O, D, RPN, Mitigation, New_RPN, Owner, Due.

## W3. Tolerance Analysis Workflow
1. Start from converged prescription.
2. Define tolerance set: choose commercial / precision / high-precision from `domain-knowledge.md` §6.
3. Run **sensitivity**: one-at-a-time perturbation, rank by ΔMTF or ΔWFE.
4. Run **Monte Carlo**: 1000+ trials, collect MTF@Nyquist distribution, fit to find 90/95/99th percentile.
5. Output: `outputs/tolerance-sensitivity.csv`, `outputs/tolerance-mc.csv`.
6. Feed hot tolerances back into FMEA as updated Occurrence scores.

## W4. Stray-Light Audit Workflow
1. Build a **source/scatter/receiver** map.
2. Identify **critical objects** (seen by detector) and **illuminated objects** (seen by source).
3. Intersect the two sets — these are the **first-order scatter paths**.
4. For each first-order path, compute BRDF·GCF (geometrical config factor).
5. Propose baffles, vanes, black coating (Acktar, Vantablack, Chemglaze Z306).
6. Record in `outputs/stray-light-report.md`.

## W5. Thermal / Vibration Workflow
1. **Athermalization**: compute dF/dT for each element, pick housing CTE to cancel.
2. **Bond-line stress**: σ = E·ΔCTE·ΔT (thin-bond approx); flag if > 1 MPa.
3. **Modal**: estimate first mode via Euler-Bernoulli for barrel; target f₁ > 2× drive PSD peak.
4. **Input to FMEA**: every thermal/modal failure becomes an entry.

## W6. Deliverable / Sign-Off Workflow
1. When user says "review ready" or equivalent, assemble `user-docs/design-review.md`:
   - System overview
   - Prescription + drawing stubs (ISO 10110)
   - MTF, spot, WFE plots
   - Full FMEA worksheet
   - Tolerance report summary
   - Open risks
2. Cross-check against hard rules in `context/constraints.md`.
3. Never mark review "complete" without user approval.

## Decision Tree: When to Push Back

```
User request arrives
├─ Is {waveband, FOV, f/#, detector, env} specified?
│   ├─ No → ask, halt
│   └─ Yes → proceed
├─ Does it involve Class 3B+ laser?
│   ├─ Yes, no safety paragraph → halt, cite IEC 60825
│   └─ Else → proceed
├─ Does it involve retinal hazard geometry?
│   ├─ Yes → require explicit MPE calc in constraints.md
│   └─ Else → proceed
└─ Design proposal ready?
    └─ Always pair with ≥3 failure modes before writing to outputs/
```
