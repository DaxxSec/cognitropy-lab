# /verify-schedule

Discharge the specification catalog against the cue sheet — prove each obligation or return a concrete counterexample.

## Inputs

- The canonical cue sheet (`outputs/cue-sheet-*.md`).
- The spec catalog (`outputs/spec-catalog-*.md`).
- *(Optional)* an external model checker (UPPAAL / TLC / Z3) for machine-checked discharge of the heavy obligations.

## Steps

1. Load both files; confirm they reference the same cue-sheet revision (else abort — never verify a stale model).
2. Discharge the interval/resource obligations directly: REUSE (`t_fire(next) ≥ t_clear(prev)` per position), CHAN (no pin double-booked), CURR (`K ≤ max_simultaneous` per module/settle-window), RUNTIME (`max t_clear ≤ track_len + tail`), DENSITY (`≤ N` live at any instant).
3. Delegate the geometry-heavy obligations: SEP/FALLOUT to `/separation-proof`, SYNC to `/beat-sync-check`, CURR/CHAN feasibility to `/rack-allocation`. Collect their verdicts.
4. For each obligation emit a verdict: `discharged` (+ robustness margin), `refuted` (+ counterexample: the cue ids, the violated quantity, the amount, the time), `assumed` (premise, with the assumption id), or `open` (not checkable yet — say why).
5. *(If a checker is wired)* encode the model, run it, and translate the tool's trace back into a human-readable counterexample.
6. Summarize: counts by verdict, the tightest margin per obligation (the show's slack), and the ordered list of refutations to triage.

## Output

`outputs/verification-report-YYYY-MM-DD.md`: per-obligation verdict table, every counterexample written out, the slack summary, and a "ready / not-ready for sign-off" line (not-ready if any safety obligation is `refuted` or `open`).

## Notes

- `open` is not `discharged`. A safety obligation left `open` blocks sign-off.
- Always report the margin, not just pass/fail — the margin is what survives the next cue edit.
- Re-run after every cue-sheet change; feed refutations to the constraint-violation triage tree in `context/workflows.md`.
