# crystallization-risk-memo

## Purpose

Assess the crystallization risk of a proposed process change (new geometry, hotter TPF hold, feedstock swap, mold change) *before* it is run, so a capacity-improving change doesn't quietly destroy yield. Use as a pre-change gate.

## Prompt Template

```
You are a BMG foundry process engineer assessing crystallization risk for a proposed change.

Proposed change:

- **What is changing:** [VALUE — e.g. section 4→6 mm, T_form +15 K, new Zr sponge grade]
- **Alloy + Rc/Dmax + kinetics:** [VALUE]
- **Current process margins (cooling margin, TPF time margin, oxygen level):** [VALUE]
- **Capacity motivation for the change:** [VALUE]
- **Context:** [anything else relevant]

Please:
1. Identify which kinetic margin the change consumes (cooling-to-Rc, TPF time-to-onset, nucleation density).
2. Estimate the new margin and the resulting crystalline-fraction / yield impact (JMAK where applicable).
3. Verdict: safe / tighten-controls / reject — with the margin number behind it.
4. If risky, propose the mitigation that preserves the capacity gain (composition, flux/oxygen, cooling).
5. Surface any safety implication (Be, HF, reactive melt) the change introduces.
```

## Expected Output

- The consumed kinetic margin, quantified before and after.
- Yield / crystalline-fraction impact estimate.
- A clear safe / tighten / reject verdict with its margin.
- A capacity-preserving mitigation and any safety flag.
