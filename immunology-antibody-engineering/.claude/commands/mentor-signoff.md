# /mentor-signoff

Record a single, specific entrustment decision — moving one competency from supervised to independent practice (or the next rung) — with the evidence and the boundary conditions of the entrustment.

## Inputs

- Trainee, the competency in question, and the current entrustment level.
- The triggering evidence: the specific task/artifact and the trainee's role in it.
- The mentor making the call and the proposed new entrustment level (the supervision scale in `context/references.md`).
- Any boundary conditions the entrustment should carry (e.g. "independent for standard IgG humanization, still supervised for unusual scaffolds").

## Steps

1. Confirm the competency's current level from the `competency-map` and that a `progression-review` (or sufficient logged reps) supports the step.
2. State the entrustment decision precisely: which competency, from which level to which level, effective when.
3. Scope it — entrustment is rarely blanket. Record what the trainee may now do unsupervised and what still requires a check (the "indirect supervision available" caveat).
4. Attach the evidence: the artifact(s), the observed behavior, and any red-flag conditions that would revoke the entrustment.
5. Append the sign-off to the trainee's record and update the `competency-map` entrustment level; this is the auditable credential the `competency-portfolio`/role decision draws on.

## Output

- `outputs/apprentices/<id>/signoff-<competency>-<date>.md` — the scoped entrustment decision, mentor, evidence, boundary conditions, and revocation triggers.
- Demonstrates competency: **(meta) entrustment decision** — recorded against the mentor.

## Notes

- Entrustment is about *safety to practice unsupervised*, not perfection — calibrate to "would I let this go out under their name without re-checking?"
- Scope tightly: over-broad sign-offs are how unusual cases blow up. It's fine to entrust standard work and hold the edge cases.
- A sign-off is revocable; record the conditions under which it lapses (new format, new target class, a quality miss) rather than treating it as permanent.
