# /cross-elasticity-screen — Substitute and Complement Risk Screen

Build a cross-elasticity matrix across an own-product basket × candidate substitutes (and complements). Output a heat map and a ranked watchlist of substitution-vulnerable products.

## Required Inputs

1. **Own-product basket** — list of SKUs/segments to screen.
2. **Candidate substitutes** — known competitors + plausible entrants + cross-category alternatives. Don't filter; the agent will help triage.
3. **Per-substitute entry probability `ω_j`** — qualitative or quantitative estimate that substitute `j` is a credible alternative within the horizon. (For incumbents, `ω_j ≈ 1`.)
4. **Cross-elasticity source** — internal estimates / literature priors / qualitative anchor.

## Procedure (follows Workflow E in `context/for-agent/workflows.md`)

### Step 1 — Define the basket
Confirm own-product list and candidate substitutes. Add complement candidates if the user wants the matrix to include `εxy < 0` columns (useful for ecosystems — "if printer sales fall, ink sales fall").

### Step 2 — Estimate cross-elasticities
Per (own-product `i`, substitute `j`) pair:
- **Internal share data** → BLP-style demand estimation if the user has it; otherwise log-log regression with substitute price as a regressor.
- **Heuristic priors** (when no data) — from `resources/elasticity-reference.md`:
  - Same category, similar quality tier: `εxy ∈ [0.3, 1.5]`.
  - Cross-category functional substitute: `[0.1, 0.5]`.
  - Premium → economy under stress: `[0.5, 2.0]`.
  - Complements (negative): `[-1.5, -0.2]` typical for tight pairs.

Cite the source per cell in the companion CSV.

### Step 3 — Build the cross-elasticity matrix
Rows = own products, columns = substitutes (and complements, separated). Cell = `εxy` estimate (with CI if known).

### Step 4 — Score per-product substitution risk

For each own-product `i`:

```
substitution_risk_i = Σ_j max(0, εxy(i, j)) · ω_j
```

(Negative `εxy` for complements is scored separately — *complement-loss risk* — to avoid mixing signs.)

Map the resulting score to a 1–5 tier using thresholds in `resources/risk-matrix-templates.md`.

### Step 5 — Output

`outputs/cross-elasticity-<basket-name>-<YYYY-MM-DD>.{md,png,csv}`:

- Markdown table of the full matrix.
- Heat map PNG with own-products on the y-axis and substitutes on the x-axis; cells colored by `εxy` magnitude (diverging palette centered at 0; positive = warm, negative = cool).
- CSV in long format: `own_product, substitute, εxy, ci_low, ci_high, source, ω`.
- Ranked watchlist: top-decile substitution-risk own-products listed with their dominant substitute(s).

Auto-generate `/score-demand-shock` stub cards in `outputs/` for each watchlist product (one per dominant substitute), pre-populated with the substitute's price-move scenario.

### Step 6 — Append register rows + work-log entry.

## Notes

- **Cross-elasticity is symmetric only in special cases.** Don't assume `εxy(i,j) = εxy(j,i)`; estimate or look up both directions if both matter.
- **`εxy` depends on the choice of substitute.** A product can be elastic to one rival and inelastic to another. The matrix shows this; *do not* publish a single "this product is substitution-risky" score without naming the substitute.
- **Antitrust hard line.** If the user asks the workspace to coordinate pricing with a substitute supplier, refuse and remind of the constraint in `context/constraints.md`.
- **Complements section is for the user's own ecosystem only.** Modeling complement-loss across firms is fine; coordinating pricing across firms is not.
