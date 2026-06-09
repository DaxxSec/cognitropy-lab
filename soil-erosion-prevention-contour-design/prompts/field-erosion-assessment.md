# Field Erosion Assessment

## Purpose

Use this at the start of a project to turn raw field, soil, and climate data into a RUSLE soil-loss estimate, an A/T utilization verdict, and a first-pass practice recommendation — before any structure is sized.

## Prompt Template

```
You are an erosion-control agent working in the soil-erosion-prevention-contour-design workspace.
Read context/concepts.md and context/workflows.md (Workflow A) first.

I need a soil-loss assessment for a field:

- **Location / region (for R-factor & IDF):** [VALUE]
- **Slope steepness & length:** [e.g. 6%, 250 m]
- **Soil (mapping unit or texture):** [VALUE — note if K and T are from survey or estimated]
- **Current cover / management:** [e.g. conventional-till corn-soy, residue removed]
- **Current support practice:** [e.g. up-and-down-slope rows]
- **Concentrated-flow paths observed:** [yes/no — describe any swales/gullies]
- **Units preference:** [t/ac/yr or t/ha/yr]

Please:
1. Resolve the RUSLE factors (R, K, LS, C, P), stating the source of each.
2. Compute A and the A/T utilization for the current (do-nothing) practice.
3. If A > T, propose the minimal practice set (per the decision tree) and recompute A/T for it.
4. Flag whether observed concentrated flow needs a structure regardless of A.
5. Recommend next commands (/design-terrace-interval, /size-grassed-waterway, etc.).
```

## Expected Output

- A factor table with sources and the do-nothing A and A/T.
- A pass/over-utilized verdict against tolerance T with units stated.
- A proposed practice set with the recomputed A/T and which factor moved.
- A note on concentrated-flow / RUSLE-validity caveats and the recommended next commands.
