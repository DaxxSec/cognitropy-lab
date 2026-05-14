# Element Design Review

## Purpose

Use when an engineer hands you a fresh element design (loop, airtime hill, zero-g roll, helix, etc.) and wants a structured first-pass review before committing to a simulator run. Routes the element through the `F-*` and `R-*` trees on best-available data plus engineering estimates.

## Prompt Template

```
You are a ride-dynamics engineer reviewing a roller coaster element. Walk it through the
force-envelope and restraint trees in this workspace and produce a decision-tree-traced
verdict.

Element under review:
- **Element name / type:** [e.g. "Stengel dive into vertical loop"]
- **Centerline summary:** [radius, height, entry/exit headings — a 3-5 line geometric sketch]
- **Estimated entry speed:** [V_entry m/s, with source: from sim, hand calc, or speed budget]
- **Banking profile:** [θ at entry, apex, exit — degrees]
- **Train assumption:** [seat height, restraint class assumed]
- **Sim trace available?:** [yes — pass via /force-envelope-check; no — engineering estimates]
- **Context:** [why this element, what it replaces, what design budget it must fit]

Please:
1. Verify frame and data quality at F-0; reject with a request if data is missing.
2. If no sim trace, build a rough force estimate from the geometry (centripetal at apex, +z at pullout, lateral on entry/exit) and walk F-1..F-5 against those.
3. Run the R-tree to determine the minimum restraint class implied by the estimate.
4. Identify the top 3 risks (lateral kick on entry, head-bang at apex, jerk in transition, etc.) with node ids.
5. Recommend the simulator runs needed to convert the engineering estimate into a binding verdict.
```

## Expected Output

- A pre-simulation verdict (PASS / REWORK / REJECT, marked "preliminary").
- A walked path through the F-tree on estimated values.
- The R-tree result (which restraint class this element forces).
- A "what to simulate next" list — sample rate, segments to instrument, fidelity expectations.
- Explicit caveat that this is a screening pass, not an approval.
