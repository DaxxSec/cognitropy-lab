# /sequence-content

Recommend the next objective(s) for a learner from the skill graph and current posteriors —
adaptive, mastery-driven sequencing that never skips ahead of unmet prerequisites.

## Inputs
- The skill graph (`/build-skill-graph`).
- Current per-objective posteriors (`/update-mastery`).
- Optional: learner goals / target leaf objectives, time budget.

## Steps
1. Mark each node MET / NOT-MET from its posterior and the decision rule.
2. Find the frontier: unmet nodes whose prerequisites are all MET — these are learnable now.
3. Rank the frontier by expected value: prefer nodes that unlock the most downstream objectives
   and that sit on the critical path to the learner's target.
4. If a recent failure implicated a prerequisite, route **backward** to that prerequisite instead
   of advancing.
5. If no frontier node exists (a prerequisite is borderline), recommend more practice on the
   blocking node rather than forcing progress.
6. Give a one-line rationale per recommendation tied to the graph and the posteriors.

## Output
A ranked next-step list (objective ID, action: learn / re-teach / practice, rationale). Saved to
`outputs/next-steps-<learner>.md`.
