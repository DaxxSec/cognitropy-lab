# /select-method

The "appropriateness criteria" consult: choose basic, reverse, or frozen-reverse spherification for a given liquid and emit a starting recipe with the reason.

## Inputs

- Target liquid description + measured (or estimated) **pH**, **calcium content** (dairy? mineral water?), **alcohol %**, and **viscosity** (thin/syrupy).
- Desired output: caviar / large spheres / ravioli-yolk; serve-now vs make-ahead.
- Pantry constraints (which calcium salt, xanthan, citrate available).

## Steps

1. Run the method decision tree in `context/workflows.md` (Workflow 3): acid/alcohol/high-Ca → reverse; large/make-ahead → frozen reverse; thin → xanthan first; else basic.
2. If pH < 3.6, prescribe a sodium-citrate buffer target and re-check whether reverse is still required.
3. Select a starting recipe from the `references.md` quick-reference (alginate %, calcium salt + %, bath-time band, buffer/viscosity adds).
4. State the **reason** the method fits this liquid, and the one property that would change the recommendation.
5. Hand off the bath-time band to `/membrane-titration` for calibration.

## Output

A short consult note: chosen method, starting recipe, rationale, and risk flags (acid, dairy, alcohol). Save to `outputs/method-<liquid>-YYYY-MM-DD.md`.

## Notes

- Acidic, alcoholic, and dairy bases almost always indicate **reverse** — basic spherification fights all three.
- Never put calcium chloride in the eaten base (bitter); use calcium lactate / lactate gluconate for reverse bases.
