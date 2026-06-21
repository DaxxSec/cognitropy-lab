# /skills-gap-plan

Turn the gap between a trainee's current competency profile and a target role into a concrete, task-anchored learning path — the forward-looking complement to `/progression-review`.

## Inputs

- The trainee's current `competency-map`.
- The target role/level and its required entrustment profile (the role's competency requirements from `context/references.md`).
- Real upcoming work the team has (so learning tasks are genuine deliverables, not exercises).
- Time horizon and how much supervision capacity the mentor can give.

## Steps

1. Diff the current competency/entrustment profile against the target role's required profile; list the gaps in priority order (binding constraints first).
2. For each gap, choose the cognitive-apprenticeship move that fits the current tier (`context/concepts.md` "Apprenticeship & competency model"): modeling/observation for Novice, scaffolded/coached reps for Advanced Beginner, supervised independent reps for Competent, edge-case exposure for Proficient.
3. Map each learning step onto **real upcoming work** — assign actual antibody-engineering tasks (a humanization, a developability triage, a maturation design) as the vehicle, so the trainee produces value while progressing.
4. Sequence the path with dependencies (binding kinetics QC before affinity maturation; liability scanning before humanization sign-off) and set checkpoint milestones tied to `/progression-review`.
5. Note the supervision load each step needs and flag where mentor capacity is the bottleneck (the apprenticeship analog of a capacity constraint).

## Output

- `outputs/apprentices/<id>/skills-gap-plan-<date>.md` — prioritized gap list, per-gap learning move + the real task that carries it, sequenced path with dependencies, checkpoint milestones, and supervision-load notes.
- Demonstrates competency: **(meta) learning-path design**.

## Notes

- Anchor learning to real deliverables — apprenticeship works because the work is real; contrived exercises don't transfer.
- Don't plan past the next 1–2 tiers; competency growth reveals new gaps and the plan should be re-cut at each `/progression-review`.
- Supervision is the scarce resource. A plan that needs more mentor hours than exist is a fantasy — sequence to fit the available coaching capacity.
