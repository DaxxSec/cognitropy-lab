# /emulsify-baseline

Formulate and fully document a reproducible baseline mother emulsion to serve as the control specimen every later formula is reviewed against.

## Inputs

- Which mother to baseline (mayonnaise / hollandaise / vinaigrette) and intended use (dip, dress, coat, hold-for-service).
- Available ingredients (oil type, acid, egg source — note if pasteurised) and equipment (whisk vs immersion blender, bain-marie).
- Any house constraints (target thickness, allergen limits, batch size).

## Steps

1. Read `context/workflows.md` "Building the mother emulsion" for the chosen mother.
2. Run the safety pre-screen: raw-yolk → pasteurised egg; warm sauce → define hold conditions. Abort if it can't pass.
3. Build the emulsion per the workflow, logging every controlled variable as you go (phase ratio, emulsifier load, oil-addition rate, shear method, temperature, total time, final pH).
4. Repeat for a second replicate (and ideally a second preparer) — a single batch cannot be a baseline.
5. Hand the logged formula to `/formula-normalize` to express it in ratio notation.
6. Tag it as the control specimen with a formula ID; record nominal sensory + stability expectations so deviations are visible later.

## Output

`outputs/baseline-<mother>-YYYY-MM-DD.md`: normalised baseline formula, full variable log for ≥2 replicates, control formula ID, expected stability tier, allergen list, and the conditions under which this baseline is valid.

## Notes

- The baseline is only as good as its variable log — an undocumented "great mayo" is not a control.
- Re-baseline when a core ingredient changes (new oil, different egg supplier); the old control no longer represents the kitchen.
