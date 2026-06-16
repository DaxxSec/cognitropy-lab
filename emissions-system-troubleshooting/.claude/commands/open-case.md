# /open-case

Open a new diagnostic case — the consensus "term" for one vehicle and one complaint — and initialize its tamper-evident chain-of-custody ledger.

## Inputs

- VIN, year/make/model/engine, odometer
- The customer/operator complaint, verbatim, plus when/how it occurs
- Ambient conditions and state at intake: temperature, fuel level, MIL on/flashing, recent work/history
- A case ID (default: VIN + date)

## Steps

1. Create `outputs/cases/<case-id>/` and write `ledger.md` (or `ledger.jsonl`).
2. Record **entry #0 (genesis)**: case ID, VIN, vehicle, complaint, intake conditions, technician/tool, timestamp. Compute its hash; this seeds the chain.
3. State the scope and the **legality posture** up front: this case will diagnose and repair to spec, never defeat a control.
4. Note any constraints (fuel level for EVAP, cold-soak needed, intermittent complaint) that gate which monitors can run.
5. Print the open case header and the next recommended command (`/ingest-scan`).

## Output

`outputs/cases/<case-id>/ledger.md` with a genesis entry (hash-anchored) and a one-line case header. All later evidence chains from here.

## Notes

- One term per complaint. A second unrelated complaint on the same VIN gets its own case.
- Do not skip intake conditions — EVAP and several non-continuous monitors only run in specific windows, and the freeze frame is interpreted against intake state.
