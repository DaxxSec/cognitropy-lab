# /troubleshoot-batch

Diagnose a stalled or off vinegar batch from its symptoms, return ranked causes and corrective actions, and capture the resolution back into the knowledge base.

## Inputs

- Symptom description (e.g. "acidity stuck at 2%", "mother sank", "surface film", "smells like nail polish").
- Batch parameters: substrate, starting ABV, current acidity, temperature, aeration mode, days elapsed, strain/mother source.
- Any titration history available.

## Steps

1. Read `context/workflows.md` §C (troubleshooting tree) and §A (lifecycle).
2. Classify the symptom into a branch: no acidity rise / acidity rose-then-fell / surface film / mold / contamination (eels, flies) / aroma fault.
3. Walk the decision tree, eliminating causes against the supplied parameters (aeration, temperature, ABV vs. ethanol tolerance, inoculum size, water chlorination, strain overoxidation tendency).
4. Produce a **ranked** cause list (most→least likely) with the evidence for each, and a concrete corrective action per cause.
5. State the single highest-value next action and what measurement would confirm the diagnosis.
6. Capture the diagnosis + resolution as a `troubleshooting` KB entry (via the `/kb-ingest` schema) so recurrence is a lookup.

## Output

- A ranked diagnosis + action plan printed to chat.
- `outputs/troubleshooting/<batch-id>-YYYY-MM-DD.md` with the full reasoning.
- A new/updated `outputs/kb/troubleshooting/` entry.

## Notes

- "Acetone/nail-polish" aroma points to acetaldehyde accumulation — often aeration or a stressed culture, not necessarily a ruined batch.
- A sunken mother is rarely fatal on its own; treat the underlying aeration/vitality cause, not the pellicle.
- Discard for **mold** (fuzzy, colored) but not for kahm film or vinegar eels — those are recoverable.
