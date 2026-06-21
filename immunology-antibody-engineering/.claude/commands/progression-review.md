# /progression-review

Review a trainee's logged engineering work against the competency ladder, decide which competencies advance a tier, and assign the next milestone — the periodic "have they grown" checkpoint.

## Inputs

- Trainee profile (`outputs/apprentices/<id>/`) including the current `competency-map`.
- The logbook of work since the last review: which commands they ran, the `outputs/` artifacts they authored, and the role they played (observed / assisted / led / supervised others).
- Mentor observations and any workplace-based assessments (mini-CEX / direct-observation notes).
- The review window (e.g. quarterly) and any role/promotion decision riding on it.

## Steps

1. Read `context/concepts.md` "Apprenticeship & competency model" and the trainee's current `competency-map`.
2. For each competency, gather the logged evidence in the window — count independent reps, not exposures — and map each artifact to the competency it demonstrated (every command output names this).
3. Apply the advancement rule from `context/workflows.md` "Loop C — progression": a tier advances only when there is *consistent* evidence at the new level across multiple instances and a mentor entrustment event, not a single good day.
4. Decide per competency: advance / hold / remediate; update the entrustment level; record the specific evidence justifying each decision (so the call is auditable).
5. Set the next milestone for the binding-constraint competencies and note any competency drifting stale from disuse.
6. Update the `competency-map` and write the review; if a role gate is in play, state whether the entrustment threshold for that role is met.

## Output

- `outputs/apprentices/<id>/progression-review-<date>.md` — per-competency advance/hold/remediate decision with cited evidence, updated entrustment levels, next milestones, and a role-readiness verdict if applicable.
- Demonstrates competency: **(meta) progression assessment** — the reviewing mentor's own evidence.

## Notes

- Reward independent reps, not hours logged or tasks merely observed; "watched a humanization" is Novice evidence.
- Make decisions auditable: cite the artifact, not an impression. A progression review that can't be challenged on its evidence is a popularity contest.
- Advancement should sometimes be "hold" — inflating tiers to keep morale up corrupts the ladder for everyone behind them.
