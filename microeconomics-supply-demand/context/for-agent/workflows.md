# Workflows — Step-by-Step Scoring Procedures

These are the canonical procedures the slash commands invoke. Each is written so a competent analyst can run it manually if needed.

## Workflow A — Score a Supply-Side Shock

Invoked by `/score-supply-shock`. Used for any event that shifts the supply curve (input price spike, capacity loss, new regulation on producers, technology breakthrough on producer side).

### Step 1: Decompose the scenario into curve mechanics

Ask:
1. **Direction of the curve shift** — left (supply contraction) or right (supply expansion)?
2. **Magnitude** — what fraction of equilibrium quantity does the shift represent? Express as `δQ_s / Q*`. Use a *range*, not a point.
3. **Persistence** — transient (resolves within the horizon) or persistent? Persistent shocks score higher impact.
4. **Curve shape changes** — does the supply curve also become *steeper* (less elastic) under the shock? Common in capacity-constrained scenarios.

If the user can't answer (3) or (4), record `unknown — assumption: persistent / unchanged shape` and flag in the model-risk column.

### Step 2: Pull the demand-side parameters that determine impact

Look up or estimate:
- Own-price elasticity of demand `εd` for the affected product/segment, with CI.
- Time horizon (this changes εd materially — see domain knowledge §1.6).

### Step 3: Estimate equilibrium response

Apply `ΔP*/P* ≈ shift_size / (εs - εd)` for a first-cut. If εs and εd are both small (rigid market), even a small shock implies a large `ΔP*` — drive impact tier up.

Compute:
- Estimated `ΔP*` range
- Estimated `ΔQ*` range
- Estimated revenue impact = `ΔP* × Q*` ± user-side adjustment (pass-through, contracts, etc.)
- Estimated margin impact = `ΔP* × Q* × pass-through_fraction − ΔW × Q*` if input cost is the cause

### Step 4: Score Likelihood

Look at:
- Historical base rate over a comparable window (the calibration anchor in `constraints.md`).
- Leading indicators currently active (port congestion, futures pricing, weather, regulatory pipeline).
- If a leading indicator is already moving, bump L by 1 tier.

Pick the tier; record the base-rate evidence next to the score.

### Step 5: Score Impact

Map the revenue/margin impact range from Step 3 to the calibrated impact tier in `constraints.md`. If the range straddles two tiers, record both — render as a band on the heat map.

### Step 6: (Optional) Score Detectability

If using L × I × D mode:
- Forward markets exist for this input? D = 1.
- Detected only via quarterly reviews? D = 3.
- Visible only post-shock in sales/revenue data? D = 5.

### Step 7: Compute composite RPN

L × I (or L × I × D). Map to risk-appetite band.

### Step 8: Write the scenario card

Output to `outputs/supply-<scenario-slug>-<date>.md` with sections:
- Scenario title and brief
- Curve mechanics (Step 1)
- Demand parameters (Step 2)
- Equilibrium response (Step 3)
- Likelihood with evidence (Step 4)
- Impact with mapping (Step 5)
- Detectability if applicable
- RPN and tier
- Suggested controls and treatment options
- Single most fragile assumption

### Step 9: Append register row

Add to `planning/risk-register.md` (or create) with the ISO 31000-aligned schema from `domain-knowledge.md` §2.5.

### Step 10: Log

Append to `work-log/<YYYY-MM-DD>.md` with timestamp, scenario, score, and 1–2 sentence reflection on what was the hardest call.

## Workflow B — Score a Demand-Side Shock

Invoked by `/score-demand-shock`. Mirror of Workflow A with these substitutions:

- Step 1 asks about **demand-curve shift** direction, magnitude, persistence, and shape change.
- Step 1 also asks **which driver** moved the curve: income (`Y`), tastes (`T`), prices of substitutes/complements (`P_r`), expectations (`E`), population (`N`), or regulation. This drives Step 4 likelihood evidence:
  - Income-driven → look at macro indicators, employment, wage growth.
  - Substitute-driven → look at substitute pricing, substitute launch calendars.
  - Taste-driven → look at search-volume trends, social-listening proxies.
  - Regulation-driven → check legislative/agency pipelines.
- Step 3 uses `ΔP*/P* ≈ shift_size / (εs - εd)` again, but the sign of `ΔP*` is opposite (demand shift down → price down).
- Step 5 impact may include **CS impact** (relevant when brand loyalty / customer relationships are at stake).

## Workflow C — Build a 2D Elasticity Risk Matrix

Invoked by `/elasticity-risk-matrix`. Used to rank a portfolio of products/segments by intrinsic vulnerability.

### Step 1: Choose the axes

Common pairings:
- **Own-price × cross-elasticity to a substitute**: substitution vulnerability matrix.
- **Own-price × income elasticity**: macro-cycle vulnerability matrix.
- **Supply elasticity × demand elasticity**: equilibrium-rigidity matrix (which markets will respond most violently to any shock).

### Step 2: Estimate or look up elasticities

For each SKU/segment:
- If internal data is available, run a log-log regression:
  ```
  log(Q) = α + β log(P) + γ log(P_substitute) + δ log(Y) + ε
  ```
  β = own-price elasticity, γ = cross-elasticity, δ = income elasticity. Report SEs and CIs.
- If no internal data, use literature priors from `resources/elasticity-reference.md`. Mark as "prior."
- If even priors are unavailable, mark cell as "unknown" and recommend data acquisition before scoring.

### Step 3: Tier-ize the elasticities

Map continuous elasticity values to 1–5 tiers using thresholds in `resources/risk-matrix-templates.md`. Standard mapping:

| εd range | Tier (price-sensitivity = impact) |
|---|---|
| `εd > -0.5` | 1 (very inelastic) |
| `-1.0 < εd ≤ -0.5` | 2 |
| `-1.5 < εd ≤ -1.0` | 3 |
| `-2.5 < εd ≤ -1.5` | 4 |
| `εd ≤ -2.5` | 5 (very elastic) |

(Adjust per user's market.)

### Step 4: Plot the heat map

Render as a 5×5 grid with SKU labels in cells. PNG to `outputs/elasticity-matrix-<date>.png`. Include a CSV alongside for downstream tools.

### Step 5: Identify the red zone

SKUs in the (5,5) cell of any axis pairing get individual scenario cards generated automatically — they're the "watchlist" rows for the register.

## Workflow D — Equilibrium Stress Test

Invoked by `/equilibrium-stress-test`. Quantitative scenario engine.

### Step 1: Specify the baseline

Linear approximation usually adequate:
```
Qd = a - b·P
Qs = c + d·P
```
Equilibrium: `P* = (a-c)/(b+d)`, `Q* = (a·d + b·c)/(b+d)`.

Calibrate (a, b, c, d) from current `(P*, Q*)` plus elasticity estimates:
```
b = -εd · Q* / P*    (note: εd < 0 so b > 0)
d = εs · Q* / P*
```
`a` and `c` follow.

### Step 2: Apply the perturbation

User specifies one of:
- Demand intercept shift: `a → a + Δa` (taste/income/macro shock).
- Supply intercept shift: `c → c - Δc` (cost shock, capacity loss; use `+Δc` for tech breakthrough).
- Slope change: `b → b·k` or `d → d·k` (elasticity changes).
- Tax wedge: introduce `t` such that consumer pays `P_c = P_s + t`.
- Price control: ceiling `P̄` or floor `P̲` with rationing/surplus.

### Step 3: Solve the new equilibrium

Closed-form for the linear cases. Report `(P*', Q*')` and the deltas.

### Step 4: Compute surplus changes

```
CS = ½ · (P_choke - P*) · Q*       where P_choke = a/b
PS = ½ · (P* - P_floor) · Q*       where P_floor = -c/d (clip to ≥ 0)
```
`ΔCS`, `ΔPS`, and (if a wedge was introduced) DWL.

### Step 5: Translate to RPN

- `ΔP* × Q*` → revenue impact tier.
- `ΔPS` → margin impact tier (if user is on the producer side).
- Likelihood is the user's stated probability of this perturbation occurring; confirm against base-rate anchors.
- RPN = L × I.

### Step 6: Output

`outputs/stress-<scenario>-<date>.md` with:
- Baseline parameters
- Perturbation specification
- New equilibrium
- Surplus deltas
- DWL if applicable
- Plot (PNG): supply/demand curves before and after, equilibrium points marked.
- Composite RPN and tier.

## Workflow E — Cross-Elasticity Substitution Screen

Invoked by `/cross-elasticity-screen`. Used for portfolios facing competitive entry or shifting consumer preference.

### Step 1: Define the basket

The user's product list + plausible substitutes (existing competitors, anticipated entrants, broader category alternatives). For each pair (i, j), the agent estimates or asks for `εxy(i, j)`.

### Step 2: Estimate cross-elasticities

If no data, use heuristics from `resources/elasticity-reference.md`:
- Same category, similar quality tier: `εxy` typically `[0.3, 1.5]`.
- Cross-category functional substitute: `[0.1, 0.5]`.
- Premium → economy substitution under stress: `[0.5, 2.0]`.

### Step 3: Build the cross-elasticity matrix

Rows = own products, columns = potential substitutes. Cell = `εxy` estimate (with CI if known).

### Step 4: Score substitution risk per own-product

For each own-product `i`, substitution risk = `Σ_j εxy(i, j) · ω_j` where `ω_j` is the user's qualitative probability that substitute `j` becomes a credible alternative within the horizon (entry probability, capacity, marketing budget).

Map the resulting score to a 1–5 tier using thresholds in `risk-matrix-templates.md`.

### Step 5: Flag the watchlist

Top-decile substitution-risk products generate auto scenario cards (a `/score-demand-shock` invocation per product).

### Step 6: Output

`outputs/cross-elasticity-<date>.md` + `.csv` + heat map PNG.

## Decision Tree — Which Command to Run?

```
Is the trigger a single named scenario you want scored?
├─ Yes ─ Is the driver supply-side?
│        ├─ Yes ─ /score-supply-shock
│        └─ No  ─ /score-demand-shock
└─ No  ─ Are you scoring a portfolio (many SKUs/segments)?
         ├─ Yes ─ Is the question "which products are vulnerable to substitution?"
         │        ├─ Yes ─ /cross-elasticity-screen
         │        └─ No  ─ /elasticity-risk-matrix
         └─ No  ─ Do you need a quantitative "what if" with ΔP*, ΔQ*, surplus?
                  ├─ Yes ─ /equilibrium-stress-test
                  └─ No  ─ Have all scenarios been scored already?
                           ├─ Yes ─ /draft-risk-register
                           └─ No  ─ go back to top, score the missing scenarios
```

## Recovery — What to do if you make a bad score

Scores are dated. Re-score with the new evidence; do not edit the old entry. The register tracks "current" via the highest date stamp. Score drift is itself a signal worth visualizing — keep history.
