# /equilibrium-stress-test — Comparative-Statics Scenario Engine

Quantitative companion to the qualitative scoring commands. Perturbs a baseline supply/demand system under a named scenario and reports `ΔP*`, `ΔQ*`, surplus shifts, and a composite RPN derived from the resulting impact magnitude.

## Required Inputs

1. **Baseline `(P*, Q*)`** — current equilibrium price and quantity for the market.
2. **Baseline elasticities** — `εd` and `εs` (with horizon).
3. **Perturbation specification** — one of:
   - **Demand intercept shift**: `Δa` (taste/income/macro shock).
   - **Supply intercept shift**: `Δc` (cost shock, capacity loss; positive `Δc` is a leftward shift in our linear formulation).
   - **Slope/elasticity change**: `b → b·k` (demand becomes more/less elastic) or `d → d·k` (supply).
   - **Tax wedge `t`**: consumer pays `P_c = P_s + t`.
   - **Price ceiling `P̄`** or **floor `P̲`**.
4. **Likelihood of the perturbation** — user-stated or pulled from a prior scoring session.

## Procedure (follows Workflow D in `context/for-agent/workflows.md`)

### Step 1 — Calibrate the linear baseline

```
b = -εd · Q* / P*    (b > 0 since εd < 0)
d =  εs · Q* / P*
a = Q* + b·P*
c = Q* - d·P*
```

So `Qd = a - b·P` and `Qs = c + d·P`. Equilibrium recovered: `P* = (a-c)/(b+d)`, `Q* = (a·d + b·c)/(b+d)`.

### Step 2 — Apply the perturbation
Update parameters per the perturbation spec. For taxes, solve the wedged system:
```
Qd(P_c) = Qs(P_s)  with  P_c = P_s + t
⇒ a - b·(P_s + t) = c + d·P_s
⇒ P_s* = (a - c - b·t) / (b + d)
⇒ P_c* = P_s* + t
⇒ Q*   = c + d·P_s*
```

For ceilings/floors that bind, report rationing (excess demand at the ceiling) or surplus (excess supply at the floor), not just the new equilibrium.

### Step 3 — Compute new equilibrium
Closed-form for linear cases. Report `(P*', Q*')` and `ΔP* = P*' - P*`, `ΔQ* = Q*' - Q*`.

### Step 4 — Surplus calculation

```
P_choke = a / b              # demand intercept
P_floor = max(0, -c / d)     # supply intercept (clipped)

CS_baseline = ½ · (P_choke - P*) · Q*
PS_baseline = ½ · (P* - P_floor) · Q*

CS_new      = ½ · (P_choke' - P*') · Q*'
PS_new      = ½ · (P*' - P_floor') · Q*'

ΔCS = CS_new - CS_baseline
ΔPS = PS_new - PS_baseline
```

If a tax wedge is in play, also compute:
- Tax revenue = `t · Q*'`
- DWL = `½ · t · |Q* - Q*'|` (Harberger triangle approximation)

### Step 5 — Translate to RPN
- Impact tier = mapping of `|ΔP* × Q*|` (or `|ΔPS|` for own-firm view) onto the calibrated impact scale in `constraints.md`.
- Likelihood tier = user input from Step 0, confirmed against base-rate anchors.
- RPN = L × I.

### Step 6 — Output

`outputs/stress-<slug>-<YYYY-MM-DD>.md`:

```
# Equilibrium Stress Test: <scenario>
**Date:** <YYYY-MM-DD> · **Horizon:** <H>

## Baseline
- (P*, Q*): <values>
- (εd, εs): <values, source>
- Implied (a, b, c, d): <values>

## Perturbation
<spec, including any wedge/control>

## New Equilibrium
- (P*', Q*'): <values>
- ΔP*: <value, %>
- ΔQ*: <value, %>

## Surplus
| Component | Baseline | New | Δ |
|---|---|---|---|
| CS | ... | ... | ... |
| PS | ... | ... | ... |
| Tax revenue | – | ... | ... |
| DWL | – | ... | ... |

## Plot
![supply-demand](stress-<slug>-<date>.png)

## Risk Translation
- Impact: tier <N>, mapping <which row in constraints.md>
- Likelihood: tier <N>, evidence <…>
- Composite RPN: <L × I = N> → <green/yellow/amber/red>

## Single Most Fragile Assumption
<one line — usually the elasticity estimate or the linearity assumption itself>
```

Plus a PNG: supply and demand curves before and after, equilibrium points marked, surplus regions shaded. Use matplotlib `Agg`; viridis-friendly palette.

### Step 7 — Append register row + work-log entry.

## Notes & Limits

- **Linearity is an approximation.** For large perturbations or constant-elasticity demand, switch to the nonlinear branch (the agent should mention this when `|ΔP*/P*| > 25%`).
- **Partial equilibrium only.** Doesn't model feedback to other markets (labor, capital, complement industries). For multi-market questions, flag the limitation in the register's "model risk" column.
- **No competitive reaction modeled.** If the market has ≤ 4 firms, mention oligopoly/Cournot/Bertrand caveats.
