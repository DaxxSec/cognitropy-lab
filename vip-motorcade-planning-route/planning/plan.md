# Plan — VIP Motorcade Planning Workspace

This is the active plan for the workspace's *operating cycle*. Refresh per movement window.

## Status

- Workspace: **scaffolded** (Day 34, 2026-04-28)
- First movement window: not yet onboarded
- Threat baseline: not yet built

## Standing Operating Cycle

Per movement window, the planner walks:

1. `/onboard` — capture principal placeholder, threat tier, jurisdictions, motorcade resources, operator profile, posture.
2. `/threat-baseline` — build the actor / capability / indicator baseline; document expiry.
3. For each leg in the window:
   3a. `/route-survey` against ≥ 3 candidate routes.
   3b. `/risk-score` against each surveyed route.
   3c. `/route-compare` to pick primary, alternate, abort.
   3d. `/contingency-plan` for High+ residual segments.
4. `/advance-checklist` at appropriate lead time.
5. `/movement-brief` at T-2 h.
6. Movement.
7. `/after-action` at T+24 h.

## Active Items

_(none — first onboarding pending)_

## Comparison Weights — Defaults

```
max_residual:       0.35
high_plus_count:    0.20
total_time:         0.10
time_variance:      0.05
deconfliction:      0.10
profile_signal:     0.10
principal_comfort:  0.10
```

Tunable per movement; document any change in `planning/comparison-weights.md` (created on first onboard).

## Posture Reminders (printed at top of every session)

- Residual ceiling default: Moderate (≤9). High requires sign-off; Extreme is veto.
- Three legs always: primary, alternate, abort.
- Defensive only.
- Sanitize before sync.

## Pivot History

_(none yet)_
