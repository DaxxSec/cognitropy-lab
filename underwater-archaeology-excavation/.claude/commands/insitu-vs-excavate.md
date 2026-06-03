# /insitu-vs-excavate

Run the discipline's central decision as an explicit cost-benefit comparison: preserve the site in place, or excavate it.

## Inputs

- Site summary: type (wreck, harbour deposit, drowned landscape), depth, environment, preservation state.
- Significance score (from `/site-significance-score`) or the inputs to derive one.
- Threat profile (from `/threat-decay-model`) — mechanism, annual probability, lead time.
- Cost inputs: fieldwork day-rates, conservation estimates, curation rate, and a discount rate.
- The decision-maker and the planning horizon (years).

## Steps

1. Read `context/concepts.md` ("In-Situ Preservation Doctrine") and start from the UNESCO 2001 Annex Rule 1 default — excavation carries the burden of proof.
2. Define both options concretely: (a) in-situ management = monitoring ± stabilisation, recurring cost; (b) excavation = the lifecycle cost chain. Neither is free.
3. Build the **excavation lifecycle cost**: survey + fieldwork (`/dive-budget-model`) + conservation (`/conservation-cost-forecast`) + perpetual curation + post-ex. Discount to present value.
4. Build the **in-situ lifecycle cost**: monitoring cadence × horizon + any stabilisation, discounted.
5. Value the **benefit of excavation** (realised knowledge + recovered material, via significance) and the **option value of in-situ** (site remains available for cheaper future technique).
6. Value the **cost of inaction** = significance × probability of loss over the horizon (threat-discounted loss).
7. Apply the decision rule: NPV/benefit-cost ratio if monetisable, else weighted MCDA. State which.
8. Hand off to `/cba-sensitivity-sweep` and only then write the recommendation.

## Output

A decision memo `outputs/insitu-vs-excavate-<site>-YYYY-MM-DD.md`: the two costed options side by side, the benefit and threat valuations, the decision rule and result, an explicit statement of which assumptions the result depends on, and a clear recommendation with its justification against the in-situ default.

## Notes

- A high-significance / low-threat site usually argues *for* in-situ — the option value is large and irreversibility is avoided.
- If conservation cost exceeds realisable benefit, recommend a diagnostic sample only, not full excavation.
- War graves and sovereign wrecks: legal/ethical constraints can override the CBA outright — flag, don't quietly net them out.
