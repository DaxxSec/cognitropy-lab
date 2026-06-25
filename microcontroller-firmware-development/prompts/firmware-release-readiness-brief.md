# Firmware Release-Readiness Brief

## Purpose

Drive a ship / slip decision by triaging open defects and tech debt on cost-benefit, while enforcing that safety and security defects block the release unconditionally.

## Prompt Template

```
You are deciding firmware release readiness by cost-benefit defect triage.

I have a release candidate:

- **Product + release type:** [PRODUCTION / OTA PATCH / BETA]
- **Open defects (severity, impact, likelihood, fix cost/risk):** [LIST]
- **Open tech debt items:** [LIST]
- **Proximity to freeze + regression risk of late changes:** [VALUE]
- **Budget status (flash/RAM/power) + build reproducibility:** [VALUE]

Please:
1. Classify each item by severity and mark any safety/security items as blocking.
2. For non-blocking items, weigh user impact × likelihood against fix cost + regression risk near the freeze.
3. Give a fix-now / defer-to-patch / won't-fix verdict per item with rationale.
4. Give an overall ship / slip recommendation, confirming budgets hold and the build is reproducible.
```

## Expected Output

- A severity-classified defect/debt list with blocking items called out
- Per-item verdicts with cost-benefit rationale
- An overall ship-or-slip recommendation
- A budget + reproducibility sign-off
