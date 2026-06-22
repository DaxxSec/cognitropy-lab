# /misfire-triage

Build the misfire / dud / hangfire decision-tree runbook — the shooter's live contingency card. Sequences the *decision*, defers all physical handling to the permit/NFPA/product guidance.

## Inputs

- The cue sheet (to know each cue's position, downstream dependencies, and finale chains).
- The governing permit + NFPA stand-off / wait-time intervals (operator supplies the binding numbers).
- Site plan: abort signal, safed-state procedure, personnel positions.

## Steps

1. Enumerate the anomaly classes from `context/workflows.md`: no-fire (no report), low/partial break, suspected hangfire, and cascading/safety-relevant failure.
2. For each class, write the decision branch: immediate action (hold downstream chain, safe the module), the wait/stand-off interval (referenced to the permit — leave the number as a parameter the operator fills), and the continue-vs-abort criterion.
3. Encode the **never** rules explicitly: never approach a suspected hangfire, never re-fire a no-fire cue blindly, never compress the mandated wait.
4. Map each branch to the specific positions/channels it applies to (e.g. which finale sub-chain to hold if rack 3 partials).
5. Render as a one-page tree the shooter can read at the firing position under pressure.

## Output

`outputs/misfire-runbook-YYYY-MM-DD.md`: the decision tree (anomaly → action → wait → continue/abort), the explicit never-rules, and the per-position dependency map. Designed to be printed for the firing line.

## Notes

- This command sequences operational decisions only; it never specifies how to physically handle a live device — that is the licensed operator's domain under their permit.
- Keep wait intervals as named parameters tied to the permit/NFPA, not hardcoded — they vary by jurisdiction and product.
- Tie each branch to the as-fired log so a real misfire updates the proof ledger's assumptions.
