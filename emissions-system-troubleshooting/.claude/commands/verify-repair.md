# /verify-repair

Confirm the repair "replicated" — re-run the affected monitors to readiness, prove the DTC stays cleared over a drive cycle, and confirm the system returned to spec — before closing the case.

## Inputs

- The committed diagnosis and its repair plan
- Post-repair scan access (live data + Mode 06 + readiness)
- The OEM (or generic) drive-cycle procedure for the affected monitor

## Steps

1. Clear codes *after* the repair (now legitimate — the freeze frame is already preserved in the ledger) and reset readiness.
2. Run the OEM drive cycle for the affected monitor; confirm the monitor completes and **passes** (Mode 06 back in limits, not just "no code yet").
3. Confirm the repaired symptom is gone: trims back to band, sensor behavior normal, no return of the DTC or its followers.
4. Append the verification evidence (monitor results, post-repair live data, drive-cycle log) to the ledger.
5. If the monitor **fails** or the code returns, the commit did not replicate — reopen: the root cause was wrong or incomplete. Go back to `/cross-validate-sensors` / `/build-quorum`.

## Output

A verification node appended to the ledger (pass/fail with the monitor evidence) and, on pass, a case-closed marker. On fail, a reopen note pointing back to the phase to revisit.

## Notes

- "Code didn't come back in the parking lot" is **not** verification — a non-continuous monitor must actually run and pass its self-test.
- Note fuel level and conditions; some monitors (EVAP) won't run to readiness outside their window, which can masquerade as a failed fix.
