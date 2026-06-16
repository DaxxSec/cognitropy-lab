# /log-evidence

Append one hand-collected piece of evidence to the append-only, hash-linked chain-of-custody ledger.

## Inputs

- The evidence: a smoke-test result, scope/waveform trace, fuel-pressure reading, vacuum reading, visual finding, photo path, or part-swap outcome
- The conditions under which it was collected (engine temp, load, fuel level, etc.)
- Collector/tool identity and timestamp
- The open case ID

## Steps

1. Read the current tail of the ledger to get the latest entry's hash (`prev-hash`).
2. Structure the new entry: **what / value-or-result / when / who / where-how / prev-hash**.
3. If this entry *corrects* an earlier one, do **not** edit the old entry — write a new entry that cites and supersedes it.
4. Compute the entry hash over its content + `prev-hash`; append.
5. Print the appended entry and the new ledger length.

## Output

One new evidence node appended to `outputs/cases/<case-id>/ledger.md`, chained to its predecessor.

## Notes

- **Append-only is the whole point.** Editing in place breaks tamper-evidence and the case's defensibility. Supersede, never overwrite.
- Record conditions every time — a leak test at the wrong fuel level or a trim reading at the wrong load is not reproducible evidence.
