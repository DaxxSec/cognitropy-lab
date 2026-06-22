# /sampling-plan — ANSI/ASQ Z1.4 Acceptance Sampling

Generate an attributes acceptance-sampling plan for a batch — incoming trade frames or a finished batch of re-glued joints — so a lot can be accepted or rejected from a sample instead of 100% inspection.

## Inputs

- **Lot size N** and what a "unit" is (a frame, a joint, a re-glued corner block).
- **AQL** (acceptable quality level, %) and **inspection level** (default General Level II).
- The **defect definition** (what counts as a defective unit) and its classification (critical/major/minor).
- Whether single, double, or sequential sampling is wanted (default single).

## Steps

1. **Eligibility gate:** if the lot is antique/irreplaceable, **reject sampling** and require 100% inspection — sampling is only valid for replaceable batches.
2. Map N + inspection level → **sample-size code letter**, then look up **n** and the **Ac/Re** numbers for the AQL (`context/references.md`).
3. State the rule: draw **n** units at random; **accept if defectives ≤ Ac, reject if ≥ Re**.
4. Summarize the **OC-curve implication** — producer's risk (α, rejecting a good lot) and consumer's risk (β, accepting a bad lot) at the chosen AQL.
5. If a rejected lot is likely, recommend feeding the found defects into `/defect-pareto` and switching to tightened inspection per the Z1.4 switching rules.

## Output

A sampling plan card: N, code letter, n, Ac/Re, AQL, inspection level, the accept/reject rule, and the OC-curve risk note. Save to `outputs/<lot-id>-sampling-plan.md`.

## Notes

- Sampling controls *batch* risk; it never proves an individual unit good. For high-value pieces, inspect every one.
- AQL is not a "target defect rate" — it's the quality the plan will routinely accept; setting it loose to pass a bad supplier is self-deception.
- Use Z1.4 **switching rules** (normal ↔ tightened ↔ reduced) to react to a supplier's recent history, not just the current lot.
