# Apprenticeship Progression Report

## Purpose

Generate a trainee's periodic progression report — map logged engineering work to the competency ladder, justify each advance/hold/remediate decision with cited evidence, and state role-readiness. Use at quarterly reviews or before a promotion decision.

## Prompt Template

```
You are a mentor writing an evidence-based competency progression report.

I have a trainee to review:

- **Trainee ID & current tier per competency:** [VALUE or path to competency-map]
- **Review window:** [dates]
- **Logged work this window:** [list of artifacts/commands run and the trainee's role: observed / assisted / led / supervised-others]
- **Mentor observations / workplace assessments:** [VALUE]
- **Role decision in play (if any):** [target role and its required entrustment profile]

Please:
1. For each of the 8 core competencies, count the independent reps in the window and map each artifact to the competency it demonstrated.
2. Apply the advancement rule (consistent multi-rep evidence + entrustment event) and decide advance / hold / remediate — cite the specific artifact for every decision.
3. Update the entrustment level per competency and flag any competency going stale or any self-rating/evidence divergence > 1 tier.
4. Set the next milestone for the binding-constraint competencies.
5. If a role gate is in play, state plainly whether the required entrustment profile is met and what's missing.
```

## Expected Output

- A per-competency table: reps counted, decision, cited evidence, new entrustment level.
- Stale-competency and divergence flags.
- Next milestones for the binding constraints.
- A role-readiness verdict with the specific gaps, if applicable.
