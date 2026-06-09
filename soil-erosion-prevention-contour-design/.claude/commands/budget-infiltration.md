# /budget-infiltration

Compare design rainfall intensity against the soil's infiltration capacity to size the excess (overland) runoff the contour system must intercept — the demand handed to conveyance sizing.

## Inputs

- Soil infiltration parameters: Horton (f₀ initial, f_c final, decay k) or Green-Ampt (Ks, suction, porosity), or a hydrologic soil group as a fallback.
- Design storm hyetograph or IDF intensity at the relevant duration/return period.
- Antecedent moisture condition (dry/normal/wet).
- Surface cover / residue (affects effective infiltration and ponding).

## Steps

1. Read `context/concepts.md` "Runoff hydrology" (infiltration capacity).
2. Build the infiltration-capacity curve over the storm: Horton `f(t)=f_c+(f₀−f_c)e^{−kt}` or Green-Ampt cumulative front.
3. Overlay rainfall intensity i(t). **Excess (runoff) occurs wherever i(t) > f(t)** — integrate the excess to get runoff depth/volume (infiltration-excess / Hortonian generation).
4. Adjust for antecedent moisture (wetter soil → lower f₀, more runoff) and ponding/depression storage.
5. Express the result as the **demand** for the contour interception system: peak excess rate and total excess volume per unit area.
6. Note where increased infiltration (cover crops, residue, level terraces, key-line spreading) would shrink the excess and lower downstream conveyance demand.

## Output

`outputs/infiltration/runoff-budget-<field>-YYYY-MM-DD.md` — the infiltration-capacity vs intensity overlay, excess runoff depth/volume, antecedent-moisture sensitivity, and the demand figure passed to `/forecast-runoff-capacity`.

## Notes

- Antecedent moisture swings runoff dramatically — always state the AMC assumed and test the wet case for the design storm.
- Level terraces and high residue can convert infiltration-excess runoff into stored/infiltrated water, shrinking conveyance demand upstream of sizing.
- This is the soil-surface demand-vs-capacity comparison; downstream channel capacity is `/forecast-runoff-capacity`.
