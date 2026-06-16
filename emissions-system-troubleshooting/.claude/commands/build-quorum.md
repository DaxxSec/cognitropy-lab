# /build-quorum

For a candidate root cause, assemble the minimum set of **independent** corroborating evidence required to commit — and report whether quorum is met or what is still missing.

## Inputs

- A candidate root cause (from `/classify-faults`)
- The admissible (faithful) evidence nodes in the ledger
- The per-DTC quorum guidance in `context/workflows.md`

## Steps

1. State the candidate as a falsifiable claim (e.g. "catalytic converter B1 has lost oxygen storage").
2. Enumerate the **quorum set** — the independent tests that would each have to agree: e.g. for a dead cat → Mode 06 fail **and** rear-mirrors-front O₂ **and** no exhaust leak **and** upstream O₂ proven faithful.
3. Mark each quorum member: satisfied / failed / not-yet-collected. Members must be *independent* — two readings from the same suspect sensor are one witness, not two.
4. Decide: **quorum met** (majority of independent witnesses agree, none contradict) → ready to commit; **not met** → list the exact missing/contradicting evidence and the test that would resolve it.
5. Append the quorum tally to the ledger.

## Output

A quorum report appended to the ledger: the claim, its witness set with each member's status, and a met / not-met verdict with the next test if not met.

## Notes

- **A single passing or failing test is never a quorum.** This is the gate that stops the parts cannon.
- If two *different* candidates both reach partial support, stop and run `/resolve-split` instead of forcing a quorum on one.
