# /elasticity-risk-matrix — Build a 2D Elasticity-Based Risk Matrix

Build a portfolio-wide risk matrix where each cell holds SKUs/segments scored on two elasticity axes. Used to surface intrinsic vulnerability before any specific scenario hits.

## Required Inputs

1. **Portfolio scope** — list of SKUs, segments, or product families to score. Pull from `context/project.md` if defined.
2. **Axis pair** — pick one (or run multiple matrices for the same portfolio):
   - **Own-price × cross-elasticity to a named substitute** → substitution vulnerability.
   - **Own-price × income elasticity** → macro-cycle vulnerability.
   - **Supply elasticity × demand elasticity** → equilibrium-rigidity matrix.
3. **Elasticity source** — internal regression / literature prior / hybrid.
4. **Confidence intervals** — required if any source claims to be quantitative.

## Procedure (follows Workflow C in `context/for-agent/workflows.md`)

### Step 1 — Estimate or look up elasticities per SKU/segment
- Internal data → log-log regression: `log(Q) = α + β log(P) + γ log(P_substitute) + δ log(Y) + ε`. Report β, γ, δ with SEs.
- No internal data → cite priors from `resources/elasticity-reference.md`.
- No priors → mark cell "unknown" and recommend data acquisition before publishing.

### Step 2 — Tier-ize elasticities per the workspace's standard mapping (see `workflows.md` §C, Step 3)
- Default thresholds map continuous elasticity to 1–5 tiers per axis.
- Adjust per the user's market if there's a strong reason; document in `constraints.md`.

### Step 3 — Build the matrix
- Render as 5×5 (or whatever scale was set in `constraints.md`) with SKU/segment labels in cells.
- Cells with multi-SKU populations get a count + the top-N SKU names visible; full list in companion CSV.
- CIs that straddle tiers → SKU appears in *both* cells with a "(±)" annotation.

### Step 4 — Identify the red zone
SKUs in the (5,5) cell of any axis pairing get auto-generated scenario-card stubs in `outputs/` for follow-up scoring (one stub per SKU; the user runs `/score-demand-shock` to fill them).

### Step 5 — Output
- `outputs/elasticity-matrix-<axis-pair>-<YYYY-MM-DD>.md` — narrative + numerical table.
- `outputs/elasticity-matrix-<axis-pair>-<YYYY-MM-DD>.png` — heat map.
- `outputs/elasticity-matrix-<axis-pair>-<YYYY-MM-DD>.csv` — long-format for downstream tools.
- Update `planning/risk-register.md` with the red-zone SKUs as new "intrinsic vulnerability" register rows.

## Heat Map Conventions

- Use `viridis` colormap or COSO green→amber→red.
- Always render numeric tier inside each cell (color alone is insufficient).
- Annotate the axis labels with the chosen elasticity definition and CI methodology (e.g., "Own-price εd, log-log OLS, internal Q1-2026 transactional data, 95% CI").
- Include a one-line note about horizon: "Elasticities estimated for <horizon>; SR/LR mismatch will distort scoring."

## Example Outputs (Format Reference)

```
| εd ↓ \ εxy → | Low (1) | Med-Low (2) | Med (3) | Med-High (4) | High (5) |
|---|---|---|---|---|---|
| 5 (very elastic) | – | – | – | SKU-A21 | **SKU-B07** ✦ |
| 4 | – | – | SKU-C12 | SKU-D33 | SKU-E04 |
| 3 | SKU-F09 | SKU-G14 | SKU-H22 | – | – |
| 2 | many (count: 18) | many (count: 11) | – | – | – |
| 1 (very inelastic) | many (count: 9) | – | – | – | – |
```

`✦` = (5,5) — auto-generates a follow-up scenario card.

## Output

Report: paths, count of SKUs in each tier, count and names of (5,5) red-zone SKUs, suggested next command (usually `/score-demand-shock` for each red-zone SKU).
