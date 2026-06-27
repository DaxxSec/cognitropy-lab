# /map-evidence

Bind each learning objective to the assessment items that evidence it and define the evidence
model — the slip and guess parameters that make Bayesian updating possible (ECD evidence model).

## Inputs
- The objective set and an item bank (or item descriptions).
- Optional: historical item statistics (p-value, point-biserial) to inform slip/guess.

## Steps
1. For each objective, select ≥ 1 item that elicits the *same Bloom level* as the objective
   (an "apply" objective needs an "apply" item — see `/audit-alignment`).
2. For each item set the evidence parameters: `slip s = P(incorrect | mastered)` and
   `guess g = P(correct | ¬mastered)`. Use item format to bound `g` (4-option MC ⇒ g≈0.25 floor)
   and clarity to bound `s`.
3. Flag items with `g > 0.30` or `s > 0.30` as low-evidence — recommend revision or more items.
4. Detect dependence: items sharing a stem/scaffold are not independent evidence; mark them to be
   scored as one cluster.
5. Produce the objective→item map and the per-item evidence model in a form `/update-mastery` and
   `/calibrate-bkt` can consume.

## Output
An objective→item matrix with per-item `(s, g)`, low-evidence flags, and dependence clusters.
Saved to `outputs/evidence-model-<topic>.md`.
