# Threat-Driven Rescue Justification

## Purpose

Make the expected-value case for a rescue excavation forced by imminent loss (development, scour, trawling, looting, climate). Use when a site is at risk and a fast, defensible justification is needed.

## Prompt Template

```
You are justifying a rescue excavation under a cost-benefit framework. The economic case rests on
expected heritage loss if the site is NOT excavated. Be explicit about probabilities and separate
aleatoric from epistemic uncertainty.

Site & threat:
- **Site & significance (weighted score + tier):** [VALUE]
- **Threat mechanism(s):** [VALUE]
- **Annual probability of significant loss:** [VALUE]
- **Lead time to loss / mobilisation time:** [VALUE]
- **Planning horizon & discount rate:** [VALUE]

Rescue options:
- **Minimum-sufficient excavation scope:** [VALUE]
- **Excavation lifecycle cost (PV):** [VALUE]
- **Stabilisation / protection alternative & cost:** [VALUE]
- **Conservation capacity available:** [VALUE]

Please:
1. Compute expected heritage loss = significance × cumulative loss probability over the horizon, discounted.
2. Compare rescue excavation, stabilisation, and do-nothing on cost vs. avoided loss.
3. Check feasibility: if lead time < mobilisation time, pivot to stabilisation.
4. Confirm conservation capacity exists before recommending lifting; otherwise recover only at-risk diagnostic material.
5. Recommend, with the probability assumptions foregrounded.
```

## Expected Output

- An explicit, discounted expected-loss figure.
- A three-way comparison (rescue / stabilise / do-nothing).
- A feasibility check on lead time vs. mobilisation.
- A capacity-gated recommendation with its key probabilities stated.
