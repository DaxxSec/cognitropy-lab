# /competency-signoff

Grade a completed threat-assessment artifact against the competency rubric and log entrustment evidence toward the relevant EPA — the core fusion command.

## Inputs

- The finished artifact (path in `outputs/`) and the EPA(s) it claims to evidence
- The apprentice author and the assessor
- The apprentice's current entrustment level for that EPA (from `outputs/roster.md`)

## Steps

1. Confirm which **EPA(s)** the artifact evidences and the **Miller level** it reaches (knows-how / shows-how / does — was it scenario or live?).
2. Score the rubric dimensions: **completeness, threat reasoning, decisions-derived (not just inventory), reproducibility, communication** — each 1–5 with a one-line justification.
3. Assign an **entrustment observation** for this instance (1–5 on the scale in `context/references.md`) — what level of supervision did this performance actually warrant?
4. Guard against **halo effect** (one strong artifact ≠ promotion) and ensure the grade is **reproducible** by a second assessor.
5. Append a dated, signed **evidence record** to the apprentice's portfolio; update the EPA evidence count in `outputs/roster.md` (do **not** change the entrustment *level* here — that is `/progression-review`'s job).

## Output

`outputs/signoff-<apprentice>-<epa>-<date>.md` — rubric scores, Miller level, entrustment observation, halo/reproducibility check, and a portfolio evidence line. Roster evidence count incremented.

## Notes

- Grade the **operational quality first**; the development signal must never inflate or deflate the operational verdict.
- A single observation never raises an entrustment level — it only adds evidence.
