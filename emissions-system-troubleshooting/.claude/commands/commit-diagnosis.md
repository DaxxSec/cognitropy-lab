# /commit-diagnosis

Commit a root-cause diagnosis to the ledger — the consensus "commit" — only when a quorum holds and no sensor remains flagged Byzantine.

## Inputs

- A candidate root cause that passed `/build-quorum`
- A resolved split (if there was one) from `/resolve-split`
- The sensor-trust map (no open Byzantine flags relevant to this cause)

## Steps

1. **Precondition check:** quorum met, no open Byzantine flag on any witness, no unresolved split. If any fails, refuse to commit and name the gap.
2. Write the committed diagnosis: the root cause, the list of supporting evidence-entry hashes (its quorum), a confidence level, and the **repair plan** (fix to OEM spec).
3. Mark follower DTCs as explained-by-this-root so they aren't separately repaired.
4. Run the **legality check**: the plan must be a real repair, never a code-clear-to-pass or a control defeat. Refuse and surface the legal alternative if it isn't.
5. Append the committed-diagnosis entry (hash-linked) and advance the case state to "awaiting repair + verification."

## Output

A committed-diagnosis node in `outputs/cases/<case-id>/ledger.md`: root cause, supporting hashes, confidence, and repair plan. This is the value the whole case agreed on.

## Notes

- A commit is **not** the end — it is only valid once `/verify-repair` confirms the fix "replicated" through a drive cycle.
- If new contradicting evidence appears after commit, supersede with a new committed entry citing the old one; don't silently edit history.
