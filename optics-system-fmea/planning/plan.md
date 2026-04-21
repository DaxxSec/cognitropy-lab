# Active Plan

> Status: **awaiting /onboard**. After onboarding this plan will be customized.

## Phase 1 — First-Order Design
- [ ] Capture requirements via `/onboard`
- [ ] Run `/design-optical-system` for first-order layout
- [ ] User approves candidate architecture
- [ ] Write `outputs/prescription-v1.csv`

## Phase 2 — Design FMEA
- [ ] Run `/run-fmea` against prescription-v1
- [ ] Populate `outputs/fmea-worksheet.csv`
- [ ] Action all RPN ≥ 100 and S=10 items
- [ ] Re-score after mitigation
- [ ] Summary in `user-docs/fmea-summary.md`

## Phase 3 — Robustness & Review
- [ ] Run `/tolerance-analysis`
- [ ] Run `/stray-light-audit`
- [ ] Run `/thermal-vibration-review`
- [ ] Assemble `user-docs/design-review.md`
- [ ] User sign-off

## Pivots
See `planning/pivots/` for any documented scope changes.

## Key Risks to Monitor
- Tooling gap: user may not have a non-sequential ray tracer for stray light — plan to use hand-analysis plus BRDF lookup.
- Schedule pressure could force skipping thermal-vibe review — do not allow; it is the #1 source of field failures.
