---
name: run-fmea
description: Run a structured Design FMEA pass over the current design with RPN scoring.
---

# /run-fmea

## Inputs
- Current prescription: `outputs/prescription-v{latest}.csv`
- Seed modes from `/design-optical-system`: `outputs/fmea-worksheet.csv`
- Reference: `resources/fmea-catalog.md`, `resources/rpn-rubric.md`

## Steps (AIAG-VDA 7-step)
1. **Structure**: decompose into functions. Walk the user through: optical path, mechanical mount, thermal path, electrical/control, safety.
2. **Functions**: list intended functions per structure element.
3. **Failure analysis**: for each function, brainstorm modes → effects → causes. Use the catalog plus domain-specific modes.
4. **Risk analysis**: score S, O, D using `resources/rpn-rubric.md`. Ask the user when uncertain; do not guess on safety-critical items.
5. **Compute RPN** = S × O × D. Sort desc.
6. **Mitigation**: for every RPN ≥ 100 and every S=10, propose at minimum two mitigations (design change, process control, detection method).
7. **Re-score** after mitigation; record residual risk.

## Output
Update `outputs/fmea-worksheet.csv` with columns:
```
ID, Function, Mode, Effect, Cause, S, O, D, RPN, Mitigation, New_S, New_O, New_D, New_RPN, Owner, Due
```

Also write a narrative summary to `user-docs/fmea-summary.md` with:
- Top 5 RPN before mitigation
- Top 5 RPN after mitigation
- All Severity=10 items
- Open actions list

## Hard Rules
- Never assign Severity based on user optimism — use `resources/rpn-rubric.md`.
- Any safety-to-human mode is auto-S=10.
- Coating/contamination modes default to D=6+ unless detection method is documented.
