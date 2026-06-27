# /draft-objectives

Draft measurable learning objectives for a topic or competency, each with a Bloom level, ABCD
parts, and an explicit prior mastery assumption so it can be assessed Bayesianly.

## Inputs
- Topic / competency / accreditation outcome to cover.
- Target Bloom level(s) and cohort context (novice, returning, prerequisite courses taken).
- Optional: number of objectives wanted, any pretest/baseline data.

## Steps
1. Decompose the competency into atomic, assessable sub-skills (4–12).
2. For each, choose a Bloom verb that matches the intended cognitive level (see
   `context/references.md`; reject non-observable verbs like "understand").
3. Write the objective in ABCD form — Audience, Behavior (the verb), Condition, Degree. The
   **Degree** must be a standard a posterior can later clear (e.g. "≥ 90% of cases").
4. Attach a starting prior assumption: a one-line rationale plus a `Beta(α₀, β₀)` or BKT `p-init`
   (hand off to `/elicit-prior` if it needs real elicitation).
5. Note the prerequisite relationships you see (feeds `/build-skill-graph`).
6. Flag any objective you could not make observable and propose a rewrite.

## Output
A numbered objective set (Markdown table) with columns: ID, objective text, Bloom level, ABCD
degree/threshold, starting prior, prerequisites. Saved to `outputs/objectives-<topic>.md`.
