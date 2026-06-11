# /superelasticity-window

Map the temperature-and-stress window in which the alloy behaves pseudoelastically (full strain recovery on unload) versus where it traps residual strain or yields.

## Inputs

- Transformation temperatures (Af especially) from `/dsc-transformation-map`.
- The dσ/dT slope from `/clausius-clapeyron-fit`, or isothermal stress–strain loops at several temperatures.
- Service temperature range, peak applied strain, and the recovery requirement (e.g. ≥ 99% strain recovery for a stent).

## Steps

1. Read `context/concepts.md` for the Af-to-Md window: superelasticity exists only for **Af < T < Md** (above Md, slip precedes transformation and recovery is lost).
2. Establish the lower bound: T must exceed Af so austenite is the unloaded-stable phase. Add margin — near Af the unloading plateau is low and residual strain creeps in.
3. Establish the upper bound Md from the σ–T line crossing the austenite yield stress; above it, stress-induced martensite never fully forms before plastic slip.
4. Within the window, extract the **upper/lower plateau stresses**, the recoverable strain (typically up to 6–8%), and the residual strain per cycle at the design strain amplitude.
5. Overlay the service temperature band; report the worst-case corner (coldest + highest strain) and confirm it still recovers.
6. If the window is too narrow for the service band, recommend composition or processing changes and loop back to `/composition-temperature-tune`.

## Output

`outputs/superelastic-window-<alloy>-YYYY-MM-DD.md`: the Af/Md bounds, a (temperature, plateau-stress) map, recoverable vs. residual strain at the design point, the service-band overlay, and a pass/fail on the recovery requirement.

## Notes

- Body temperature (37 °C) sits just above Af for medical NiTi by design — a few degrees of Af drift moves a stent out of its superelastic window.
- Residual strain accumulates cycle-by-cycle; a single-cycle window check is necessary but not sufficient — pair with `/functional-fatigue-budget`.
- Md is rarely measured directly; estimate it from the σ–T line and the austenite yield, and label it as an estimate.
