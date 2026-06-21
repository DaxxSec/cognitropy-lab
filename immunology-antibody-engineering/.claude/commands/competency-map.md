# /competency-map

Establish or refresh a trainee antibody engineer's competency profile — map their current skill level on each antibody-engineering competency to a Dreyfus tier and an entrustment level, and set the next milestone.

## Inputs

- Trainee identifier and start date (or existing profile in `outputs/apprentices/<id>/`).
- Self-assessment and/or mentor assessment notes per competency.
- The competency framework in `context/references.md` ("Competency ladder") — the 8 core antibody-engineering competencies and their level descriptors.
- Prior logged work (any `outputs/` artifacts the trainee authored or co-authored) to ground the assessment in evidence rather than self-report.

## Steps

1. Read `context/concepts.md` "Apprenticeship & competency model" and `context/references.md` "Competency ladder".
2. For each of the 8 core competencies (sequence-liability assessment, humanization, affinity-maturation design, developability triage, binding-kinetics QC, epitope mapping, format/engineering strategy, regulatory/IP awareness), place the trainee on the Dreyfus scale (Novice → Advanced Beginner → Competent → Proficient → Expert) **using logged evidence**, not self-report alone.
3. Assign an entrustment level per competency on the supervision scale (1 = observe only → 5 = can supervise others); flag any competency where self-rating and evidence diverge by more than one tier.
4. Identify the 1–2 competencies that are the binding constraint on the trainee's next role and set a concrete, deliverable-anchored milestone for each (e.g. "lead a humanization campaign end-to-end under indirect supervision").
5. Record the gaps and milestones as the trainee's active learning plan; cross-link to `/skills-gap-plan` for the task sequence.

## Output

- `outputs/apprentices/<id>/competency-map-<date>.md` — per-competency Dreyfus tier, entrustment level, supporting evidence, divergence flags, and the next 1–2 milestones with their entrustment target.

## Notes

- A competency map is a snapshot, not a verdict — re-run after every few logged tasks; tiers can also drop if a skill goes stale.
- Evidence beats self-report. "I can humanize an antibody" without a logged campaign is a Novice claim, not a Competent one.
- Keep the map and the engineering work in the same repo: every command's output should name the competency it demonstrates, so the map stays evidence-grounded.
