# Design Adaptation Brief

## Purpose

Use when you want to cut a specific published design but in a material it wasn't drawn for — to rescale every angle correctly (tangent ratio), confirm it still closes, and verify the machine can hold the new tolerances.

## Prompt Template

```
You are the faceting-optimization agent. Adapt a published design to a new material.

I want to cut this design in a different material:

- **Design name / source:** [e.g. "Standard Round Brilliant, Long & Steele"]
- **Design reference RI:** [VALUE the design was cut for]
- **Design angles:** [pavilion main, break facets, crown main, stars, girdle — or the full (angle, index) list]
- **Target material / RI:** [MATERIAL, RI]
- **Machine condition (latest):** [spindle TIR, lap flatness]

Please:
1. Compute the tangent ratio from the design's pavilion main to the target material's recommended pavilion main.
2. Rescale every angle via θ_new = arctan(TR · tan(θ_old)); leave index values unchanged.
3. Verify meet points still close and no pavilion facet falls below the new critical floor.
4. State the new hold tolerance and run the angle-error budget against my machine.
5. Output the original→adapted angle table with a GO/CAUTION/NO-GO verdict.
```

## Expected Output

- The tangent ratio and the per-facet original→adapted angle table.
- A meet-point and critical-floor verification.
- New hold tolerance and a tolerance-budget verdict.
- The adapted design saved to `outputs/`.
