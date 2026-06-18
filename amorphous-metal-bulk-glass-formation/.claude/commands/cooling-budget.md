# /cooling-budget

Compare the cooling rate a given mold and part geometry can actually deliver against the alloy's critical cooling rate Rc — the per-mold capacity envelope that says how thick a section this route can freeze amorphous.

## Inputs

- Alloy Rc estimate (from `/gfa-assess`) and Tl.
- Casting route and mold: material (copper, steel, silica), casting method (suction, injection, drop, water quench), and the interfacial heat-transfer coefficient h if known.
- Part **maximum section thickness** (mm) and shape (plate, rod, complex).
- Mold condition/age, if reconditioning is in question.

## Steps

1. Read `context/concepts.md` §2 and §4 for the Rc / Dmax / TTT-nose relationships.
2. Estimate the **centre cooling rate** for the section: for conduction-limited cooling use the Newtonian/heat-conduction approximation (Dmax ≈ (a/Rc)^½ inverted, or a Biot-number-aware estimate when h is finite). Use the slowest-cooling location, not the surface.
3. Compute the **margin to Rc**: achievable_rate / Rc. Margin > ~2× = comfortable; 1–2× = tight (yield-sensitive); < 1× = will crystallize at centre.
4. Identify which **section thickness** drops the centre rate to exactly Rc — that's the route-specific **max castable section** (may be below the alloy's intrinsic Dmax if h or mold conductivity limits).
5. If mold age/condition is in play, estimate the heat-extraction decay and the thinnest product it endangers first (mold-capacity degradation).
6. State the capacity consequence: max castable section → which products this mold/route can make.

## Output

`outputs/cooling-budget-<alloy>-<mold>-YYYY-MM-DD.md`: achievable centre cooling rate, margin to Rc, route-specific max castable section, the limiting factor (alloy Rc vs mold heat extraction), and a recondition/replace flag if the mold is decaying. Cross-link to `/crystallization-yield` for the fraction-crystalline consequence.

## Notes

- Surface cools far faster than centre — a glassy-looking surface over a crystalline core is the classic too-thick failure. Always budget the centre.
- Copper molds extract heat far better than steel; a worn, oxidised, or cracked mold face loses contact conductance and silently lowers the achievable rate.
- This is a first-order estimate; for tight-margin geometries, recommend a thermal FE simulation (Code-execution MCP) rather than the closed-form approximation.
