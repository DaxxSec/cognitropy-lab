# Prompt — Prior Elicitation Interview

Use this prompt to elicit a structured prior on `(hop_rate, K, sequence_type)` from a user who has domain knowledge but isn't a Bayesian. Output is a properly-shaped prior dictionary ready for `/hop-set-prior` and `/dehop-bayes`.

```
The user has knowledge of the target system but hasn't formalised it. Walk them through prior elicitation.

For each parameter, ask:
  - What do you EXPECT? (the centre of mass)
  - How CONFIDENT are you? (turns into the prior's spread)
  - What range would SURPRISE you? (turns into the prior's tails)

For hop_rate:
  - Expected: what hop rate do you think this system uses? (10, 100, 1000, 1600, ... hops/s)
  - Confident: would you bet a coffee on it? a beer? a paycheck?
       coffee → 50% prior credibility within ±20%
       beer    → 75% prior credibility within ±10%
       paycheck → 95% prior credibility within ±5%
  - Surprise: what value would you find clearly impossible? Use as the 0.001-quantile.

For K (channel count):
  - Expected: 79 (Bluetooth-class), 37 (BLE-class), 8 (WMBus-class), other?
  - Confident: same coffee/beer/paycheck scale.
  - Constraints: regulatory bands constrain K. Pull the constraint from FCC ID if available.

For sequence_type:
  - Ask: PN, table-driven, AFH, or unknown?
  - For each: what's your subjective probability?
  - Default if no opinion: [0.4, 0.3, 0.2, 0.1] for [pn, table, afh, unknown].

Convert their answers to numerical priors:
  - hop_rate: Lognormal(loc=log(expected), scale=confidence_scale)
  - K: Categorical with mass concentrated on expected ± surprise range
  - sequence_type: Categorical from their subjective probabilities

Save to outputs/<engagement>/prior-elicited.json. Reference this file in /hop-set-prior and /dehop-bayes.

Sanity check:
  - Sample from the prior; show 10 samples to the user.
  - Ask: "Do these samples look like reasonable systems?"
  - If user says no → re-elicit; their stated confidence didn't match their actual confidence.
```

## Why this matters

Most Bayesian disasters trace back to a prior that didn't reflect the analyst's actual beliefs. The coffee/beer/paycheck scale is informal but well-calibrated against real human confidence. The "show 10 samples" sanity check catches over-tight priors before they bias the posterior.

## When NOT to elicit

If the target system is fully specified by public documentation (Bluetooth, BLE, WMBus), use the system-specific prior from `domain-knowledge.md` §2 directly. Skip the interview.
