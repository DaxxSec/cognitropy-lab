# /audit-alignment

Run a constructive-alignment audit across the curriculum: every objective ↔ activity ↔ assessment
triad must target the same verb at the same Bloom level. Misalignment makes every downstream
posterior measure the wrong construct, so this runs *before* trusting any mastery number.

## Inputs
- The objective set, the learning activities, and the assessment/item map.

## Steps
1. Build the alignment matrix: rows = objectives, columns = activities and assessments.
2. For each objective, check that at least one activity and one assessment exist and that their
   Bloom level matches the objective's verb (teaching "apply" but testing "remember" = misaligned).
3. Flag defects:
   - **Orphan objective** — no aligned activity or no aligned assessment.
   - **Mis-leveled** — assessment Bloom level ≠ objective Bloom level.
   - **Unassessed** — taught but never evidenced (no posterior possible).
   - **Untaught-but-assessed** — assessed with no instruction.
4. Recommend the minimal fix per defect (add item, re-level verb, add activity).
5. Confirm coverage: every objective traces to evidence the Bayesian model can update on.

## Output
An alignment matrix plus a defect list with severities and recommended fixes. Saved to
`outputs/alignment-audit-<topic>.md`.
