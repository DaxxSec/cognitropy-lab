# alloy-gfa-scorecard

## Purpose

Generate a standardized glass-forming-ability scorecard for a candidate alloy composition, ending in a castable-thickness (capacity feasibility) verdict. Use when screening a new or modified alloy before committing melt time.

## Prompt Template

```
You are a BMG foundry process engineer. Score the glass-forming ability of this candidate alloy and translate it into a maximum castable thickness.

Candidate alloy:

- **Composition (at%):** [VALUE]
- **Tg / Tx / Tl (K):** [VALUE] (note DSC heating rate + convention)
- **Intended product min-cooling section (mm):** [VALUE]
- **Casting route:** [VALUE — e.g. Cu-mold suction]
- **Context:** [any prior data, anchor alloys, cost constraints]

Please:
1. Compute Trg, ΔTx, γ (and γm/δ if borderline); compare to thresholds in context/references.md.
2. Classify GFA and note any parameter disagreement and what it implies for casting vs TPF.
3. Estimate Rc and Dmax, naming the anchor alloy used, as a range.
4. Give the capacity feasibility verdict for the target section: castable / marginal / infeasible.
5. Flag beryllium or other safety hazards and any Be-free alternative of comparable γ.
```

## Expected Output

- A scorecard table (Trg, ΔTx, γ, γm, δ vs thresholds) with GFA class.
- Estimated Rc and Dmax range with the anchoring alloy named.
- Feasibility verdict for the stated geometry, with the kinetic margin.
- Safety flag (Be / reactive melt) and alternatives where relevant.
