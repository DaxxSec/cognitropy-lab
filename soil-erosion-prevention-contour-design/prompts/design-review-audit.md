# Design-Review Audit

## Purpose

Use this to review an existing or proposed erosion-control design (yours or someone else's) for capacity adequacy and the common failure modes — before construction or sign-off.

## Prompt Template

```
You are an erosion-control agent performing a design review.
Read context/concepts.md "Common Failure Modes" and "Hydraulic capacity fundamentals".

Audit this design:

- **Design documents / sizing artifacts:** [paths or description]
- **Stated design return period:** [VALUE — or "not stated" — flag if missing]
- **Structures included:** [terraces, waterway, basin, check dams, diversions]
- **Soil-loss claim:** [reported A and A/T, if any]
- **Maintenance plan provided?:** [yes/no]

Please:
1. Verify each capacity number has its design storm/return period attached; flag any that don't.
2. For each channel, confirm BOTH the conveyance (Qₚ/Q_cap + freeboard) AND the velocity/shear check were done.
3. Confirm every graded structure discharges to a designed stable outlet.
4. Check the soil budget: is A ≤ T, with the right (sheet+rill) scope, not used where gully methods are needed?
5. Confirm a capacity-refresh maintenance cadence exists for any storage structure.
6. List findings as PASS / FLAG / FAIL with the specific failure mode each maps to, and the residual risk.
```

## Expected Output

- A per-structure PASS/FLAG/FAIL table mapped to named failure modes.
- Explicit callouts for missing return periods, skipped velocity checks, or undefined outlets.
- A soil-budget adequacy check with scope/validity verification.
- A maintenance-cadence check and an overall residual-risk statement, with a recommendation on whether engineer sign-off is needed.
