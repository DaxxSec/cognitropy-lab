# /membrane-titration

Sweep bath time against membrane thickness and burst quality to find the optimum bath window — the quantitative "exposure" calibration for a recipe.

## Inputs

- A fixed recipe and method (from `/select-method`).
- A bath-time range to sweep (e.g. 30 s → 5 min) and a burst-quality scale.
- Optional: a way to estimate membrane thickness (cross-section, feel, or burst pressure).

## Steps

1. Pull spheres at each time step; for each, record membrane thickness (proxy) and burst quality (clean / weak / none).
2. Identify the **lower edge**: the shortest bath time that yields a membrane strong enough to survive handling (below it → ruptures).
3. Identify the **upper edge**: the longest bath time before the membrane is too thick / fully gelled (basic) or over-firm (above it → rubbery, no burst).
4. Set the **operating window** between the edges; pick a target ≈ 60–70% toward the lower edge so handling time doesn't push spheres past the upper edge (basic spheres keep gelling).
5. Record the margins — a wide window = a forgiving recipe; a narrow one needs tight timing.

## Output

`outputs/titration-<recipe>-YYYY-MM-DD.md` — the sweep table (time vs thickness vs burst), the identified edges, the chosen target time, and the margin.

## Notes

- For **basic** spherification, remember the membrane keeps thickening after the bath — bias toward the short end and rinse promptly.
- For **reverse**, gelling stops at bath exit, so the upper edge is more forgiving; the lower edge (rupture) is the real constraint.
