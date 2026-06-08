# /optimize-pavilion-angle — Pavilion Main for Maximum Light Return

Find the pavilion main angle that maximizes light return for a given material, sitting above the critical-angle floor but below the over-steep nailhead zone.

## Inputs

- Refractive index (RI), and the critical angle / floor from `/critical-angle-calc`.
- Stone outline and intended design family (standard round brilliant, barion, step cut, etc.).
- (Optional) yield priority — whether the rough's shape pushes you toward a shallower (more yield) or deeper (more brilliance) pavilion.

## Steps

1. Start at the recommended pavilion (`θ_critical + 3–4°`) and bracket a search band of roughly ±3° around it.
2. For each candidate angle, reason about TIR: how many pavilion bounces return through the crown vs leak. Lower angles approach the window; higher angles approach extinction/nailhead.
3. Identify the band where light return is near its plateau — the broad maximum, not a knife-edge — and pick the center of that plateau for tolerance robustness.
4. Cross-check against the typical pavilion main for this material in `references.md`; deviate only with a reason.
5. Adjust for yield: if the rough is shallow, take the shallowest angle still safely on the plateau; if deep, you have room to optimize for color saturation/path length.
6. State the resulting pavilion main and the ±tolerance the design needs held (feeds `/tolerance-budget`).

## Output

A recommendation block: chosen pavilion main, the safe band around it, the rationale (plateau center, yield, material), and the hold tolerance required. Append to the material's optimization file in `outputs/`.

## Notes

- A *broad plateau* angle beats a marginally-brighter knife-edge angle — it survives machine error and is the whole reason `/tolerance-budget` exists.
- For deeply colored material, a slightly steeper pavilion lengthens the light path and deepens color; weigh that against weight retention.
