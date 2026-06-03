# In-Situ vs. Excavate Decision Memo

## Purpose

Produce a funder/regulator-ready memo that recommends in-situ preservation or excavation for a specific submerged site, with the full cost-benefit ledger and a robustness verdict. Use after the component models exist.

## Prompt Template

```
You are a maritime-archaeology project agent applying a cost-benefit analysis framework.
Start from the UNESCO 2001 Annex Rule 1 default that in-situ preservation is the first option.

Site:
- **Name / identifier:** [VALUE]
- **Type & period:** [VALUE]
- **Depth & environment:** [VALUE]
- **Preservation state:** [VALUE]

Inputs:
- **Significance (weighted score + tier):** [VALUE]
- **Threat profile (mechanism, annual P(loss), lead time):** [VALUE]
- **Excavation lifecycle cost (fieldwork + conservation + curation + post-ex, PV):** [VALUE]
- **In-situ management cost (monitoring ± stabilisation, PV):** [VALUE]
- **Discount rate:** [VALUE]
- **Decision-maker & horizon:** [VALUE]

Please:
1. Lay out the two options side by side with their costs and benefits.
2. Value the cost of inaction (significance × cumulative loss probability, discounted).
3. Apply a decision rule (NPV/BCR or weighted MCDA — state which and why).
4. State which assumptions the result depends on and whether it is robust or fragile.
5. Give a clear recommendation justified against the in-situ default, flagging any war-grave / sovereign-wreck override.
```

## Expected Output

- A side-by-side costed comparison of the two options.
- An explicit cost-of-inaction figure.
- A stated decision rule, result, and robust/fragile verdict.
- A one-paragraph recommendation with its justification and any legal/ethical override flagged.
