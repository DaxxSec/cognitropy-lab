# Renewable Energy Siting Analysis — Workflows

The decision trees that drive the workspace commands. Each tree is identified by its prefix (`A-*`, `C-*`, `P-*`, `W-*`, `S-*`, `Y-*`, `R-*`); every verdict the agent emits cites a node from one of these trees.

The trees are **decision graphs**, not optimisations. They favour explainability over closeness-to-global-optimum: a `REWORK` from `C-2-b` is a sentence the analyst can quote to a project lead; a number from a black-box LCOE solver is not. The technique field — *with capacity planning models* — shapes the leaves: every verdict ends in a capacity-planning quantity (CF, ELCC, LOLE, EUE, slack score) traced back to a node.

## §1. Articulation walk (`A-*`) — drives `/articulate-portfolio`

```
A-0 Intake gate
  ├── any joint missing tech/nameplate/POI?         → REJECT (cannot articulate)
  ├── any linkage missing rating or loading?        → REJECT
  └── pass                                          → A-1

A-1 Joint enumeration                                → assign J-1..J-n, descending nameplate
A-2 Linkage enumeration                              → assign L-1..L-m, POI-toward-load
A-3 Drive enumeration                                → assign D-1..D-k, mark binding / non-binding
A-4 Adjacency closure
  ├── every joint reaches load via ≥1 linkage?      → yes: A-5
  └── stranded joint?                               → A-REWORK (cite J-id)
A-5 Resource-shed grouping
  ├── joints within MERRA-2 cell or proximity radius shed-tagged
  └── ≥2 joints in one shed?                        → emit "audit /sympathetic-motion" recommendation
A-6 Initial capacity credit                          → ISO class rating × nameplate per joint
A-7 Final verdict                                    → A-PASS | A-REWORK | A-REJECT (cite node)
```

## §2. Centerline walk (`C-*`) — drives `/centerline-resource-walk`

```
C-0 Intake gate
  ├── source ∈ allowed list?                        → C-1; else REJECT
  ├── years_of_record < 5?                          → REWORK (note short record)
  ├── time-step > hourly?                           → REJECT
  └── missing data > 5%?                            → REWORK

C-1 Annual envelope
  ├── compute CF_annual
  ├── apply source bias correction (Table R-3)
  ├── CF_annual outside published class envelope?   → REWORK (cite envelope row)
  └── inside envelope                               → C-2

C-2 Monthly envelope
  ├── per-month CF table (12 rows)
  ├── any month CF outside [μ-2σ, μ+2σ]?            → flag for weight-transfer; not a fail
  └── continue                                       → C-3

C-3 Capacity-coincident envelope
  ├── CF over top-100 net-load hours
  ├── this is the *capacity credit* input, not the CF
  └── continue                                       → C-4

C-4 Drought-year envelope
  ├── repeat C-1..C-3 over worst year in record
  ├── CF_drought < 0.6 × CF_annual?                 → MONITOR (large drought sensitivity)
  └── continue                                       → C-5

C-5 Per-month + annual verdict                       → PASS | REWORK | REJECT | MONITOR
```

## §3. Pairing walk (`P-*`) — drives `/lead-follow-pairing`

```
P-0 Feasibility gate
  ├── every lead has C-3 output?                    → P-1; else route back to /centerline-resource-walk

P-1 Per-pair walk
  ├── size storage follower: P = max(forecast_err_p95, lead_capcoin_shortfall);
  │                          E = P × min(4h, recovery_window)
  ├── size firm follower: deeper of capacity-coincident shortfall or worst 8-hour from rehearsal
  ├── compute ELCC (method: ISO class | regression | production-cost)
  ├── apply sympathetic-motion adjustment (Y-* output)
  ├── pair ELCC × nameplate ≥ target?               → PASS pair
  ├── pair within 80-100% of target?                → REWORK (cite shortfall)
  └── pair < 80% of target?                         → REJECT pair (re-select follower or lead)

P-2 Portfolio walk
  ├── Σ pair ELCC × nameplate ≥ obligation?         → PASS portfolio
  └── else                                           → REWORK
```

## §4. Weight-transfer walk (`W-*`) — drives `/weight-transfer-plan`

```
W-0 Intake (pairing complete, BA identified, ≥4 representative days) → W-1; else REWORK

W-1 ACE-budget check per representative day
  ├── 10-min net-load ramp ≤ BAAL?                  → next day
  └── ramp > BAAL?                                  → flag for follower upsize or DR commitment

W-2 Ramp-rate feasibility per joint
  ├── follower's mechanical ramp ≥ required ramp?   → next joint
  └── else                                           → REWORK (cite joint + window)

W-3 Sympathetic-motion echo
  ├── pull /sympathetic-motion-audit
  └── shed-correlated ramp window?                  → use combined ramp, not sum-of-individual

W-4 Seasonal narrative                               → summer / winter / shoulder / low-net-load themes

W-5 Per-day + portfolio verdict                      → PASS | REWORK
```

## §5. Slack walk (`S-*`) — drives `/slack-budget-check`

```
S-0 Intake (loading series + storage state, ≥8760h, aligned) → S-1; else REWORK

S-1 Linkage walk
  ├── hours pre-contingency loading > 75%?         → REWORK threshold
  ├── hours pre-contingency loading > 90%?         → REJECT threshold
  └── any hour post-n-1 loading > emergency rating? → REJECT (structural)

S-2 Storage walk
  ├── min SOC < 5% or max SOC > 95%?               → REWORK
  └── cycles/year > rated cycle life ÷ project years? → MONITOR

S-3 Drive walk
  ├── curtailment hours > PPA cap?                 → REJECT for pair
  └── DR calls > contract cap?                     → REJECT for drive

S-4 Slack closure trace
  └── every non-PASS finding traced to upstream joint on the face of the output

S-5 Aggregate                                       → portfolio slack score 0-1
```

## §6. Sympathetic-motion walk (`Y-*`) — drives `/sympathetic-motion-audit`

```
Y-0 Intake (centerlines + shed assignments + hourly resolution) → Y-1; else REWORK

Y-1 Annual ρ within portfolio
  ├── per shed: Pearson & Spearman ρ between every joint pair
  └── ρ > 0.6?                                      → flag

Y-2 Capacity-coincident ρ
  └── restrict to top-100 net-load hours

Y-3 Drought-year ρ                                   → highest-stakes correlation

Y-4 Cumulative shed (add external developers' shadow joints)
  └── shadow-joint ρ uplift?                         → marginal ELCC declines per Table R-4

Y-5 Site-shift candidates                            → propose alternate cells with ρ_target < 0.3

Y-6 ELCC penalty + portfolio adjustment              → number flows into P-1 step 6
```

## §7. Rehearsal walk (`R-*`) — drives `/load-following-rehearsal`

```
R-0 Intake (pairing + plan + slack audit + aligned year) → R-1; else REWORK

R-1 Cue detection per hour-step
  ├── follower SOC mid-range & no drive call         → CLEAN
  ├── follower at SOC ceiling/floor or ramp limit    → STIFFENING
  ├── 1-hour lag between lead drop and follower      → DROPPING-A-BEAT
  ├── followers exhausted, drives partial            → HOLD
  └── load shed event                                → PULL-FROM-SERVICE

R-2 LOLE + EUE tally
  ├── LOLE_year vs target (0.1 day/year typical)
  └── EUE_year (MWh)

R-3 Cue clustering by time-of-year and meteorology

R-4 Site / size-shift backflow per cue cluster

R-5 Financial overlay (curtailment lost-revenue, LMP-weighted revenue, capacity payment)

R-6 Aggregate verdict                                → RA-PASS | RA-REWORK | RA-REJECT
```

## §8. When to walk back

Backflows are intentional — they're the productive output of a `REWORK`:

- `C-5 REWORK` → revise resource series source, or re-classify the site.
- `P-1 REWORK` → upsize follower or change pair selection.
- `P-2 REWORK` → consider adding a joint (back to `/articulate-portfolio`).
- `W-1 REWORK` → expand follower size or commit binding DR.
- `S-1 REWORK` → transmission upgrade, or re-route via different POI.
- `Y-6 REWORK` → site shift (different shed) for at least one joint.
- `R-6 REWORK` → returns to whichever upstream walk `R-4` named as responsible.

A clean run is `A-PASS → C-PASS (per joint) → Y-acceptable penalty → P-PASS → W-PASS → S-PASS → R-PASS`. Most real portfolios cycle through 2-4 REWORKs before landing — the cycles *are* the analysis, not friction. Treat a one-pass-clean rehearsal as a red flag for hidden constraints, not a triumph.
