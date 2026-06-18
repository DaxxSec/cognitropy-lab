# /gfa-assess

Score an alloy's glass-forming ability and translate the score into a maximum castable thickness — the capacity feasibility envelope that decides which parts the alloy can make amorphous at all.

## Inputs

- Alloy composition (at%) and family, if known.
- Thermal landmarks: Tg, Tx, Tl (from `/dsc-landmarks` or literature). Tm optional.
- Intended product's **minimum-cooling section** (mm) — the thickest spot that must stay amorphous (optional; enables the feasibility verdict).
- Casting route, if fixed (copper-mold suction, injection, water quench, melt spin).

## Steps

1. Read `context/concepts.md` §3 and `context/references.md` for the GFA-parameter formulas and thresholds.
2. Compute **Trg = Tg/Tl**, **ΔTx = Tx − Tg**, **γ = Tx/(Tg+Tl)**; add γm and δ if the alloy is borderline.
3. Classify GFA (excellent / good / marginal / poor) using the joint thresholds — never a single parameter. Note any disagreement (e.g. high Trg but small ΔTx) and what it implies for casting vs TPF.
4. Estimate **Rc** and **Dmax**: anchor to the nearest representative alloy in `references.md` with a known (γ, Dmax) pair, then scale (Dmax ∝ Rc^(−1/2)). State the estimate as a range with the anchor named.
5. If a minimum-cooling section was given, return the **capacity feasibility verdict**: castable (section < Dmax with margin), marginal (within ~20%), or infeasible (section > Dmax).
6. Flag safety: if Be-bearing (e.g. Vitreloy), surface the beryllium hazard and note whether a Be-free alloy of comparable γ exists.

## Output

`outputs/gfa-<alloy>-YYYY-MM-DD.md`: a GFA scorecard table (Trg, ΔTx, γ, γm, δ vs thresholds), the GFA class, estimated Rc and Dmax with the anchoring alloy, the feasibility verdict for the target geometry, and any safety flag. Cross-link to `/cooling-budget` for the route-specific confirmation.

## Notes

- GFA parameters correlate with Dmax *with scatter* — they are a screen, not a guarantee. Always say "estimated."
- ΔTx is the right parameter when thermoplastic forming is planned (supercooled-liquid stability); Trg/γ track castable thickness.
- Off-eutectic compositions raise Tl → lower Trg → smaller Dmax; small at% errors matter. If composition is uncertain, widen the Dmax range.
