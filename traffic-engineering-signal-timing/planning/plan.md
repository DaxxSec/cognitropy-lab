# Active Retiming Plan

> Created at workspace instantiation; replace placeholders with actual corridor info during `/onboard`.

## Corridor
**Project:** _to be set in /onboard_
**Limits:** _from / to_
**Intersection count:** _N_
**Study period(s):** AM / MD / PM / off-peak

## Phase Plan
1. **Onboard** — register corridor, controllers, fleet mix, air-quality basin (`/onboard`)
2. **Baseline characterization** (`/timing-baseline`)
   - Pull programmed timing from each controller
   - Pull ATSPM operating reality (Split Monitor, PCD, Approach Volume)
   - Build HCM 7 capacity model
   - Field-validate with floating-car runs
3. **Multi-objective optimization** per peak (`/eco-optimize`)
   - Webster bootstrap
   - Pareto search across cycle / splits
   - Pick knee-point or constraint-bound point
4. **Coordination design** if 3+ adjacent signals (`/coordination-design`)
   - Common cycle selection
   - Eco-weighted Maxband / Multiband
   - Time-space diagram, stress test
5. **Project-level emissions** on finalist plans (`/emissions-model --moves`)
6. **Scenario comparison** (`/scenario-compare`)
7. **EIA report** (`/report-eia`)
8. **Field deployment** — load timing into controllers, monitor for 30 days, re-tune as needed.

## Pivots
_(record any plan changes with date, reason, decision-maker)_

## Open Questions
- _list constraints not yet resolved_

## Milestones
| Milestone | Target Date | Status |
|-----------|-------------|--------|
| Onboard complete | TBD | pending |
| Baseline complete | TBD | pending |
| Optimization complete | TBD | pending |
| MOVES4 finalist runs | TBD | pending |
| Draft EIA | TBD | pending |
| Final EIA + signoff | TBD | pending |
| Field deployment | TBD | pending |
| Post-deployment audit | TBD (deploy + 30d) | pending |
