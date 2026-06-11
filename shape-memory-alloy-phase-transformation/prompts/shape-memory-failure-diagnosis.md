# Shape Memory Failure Diagnosis

## Purpose

Diagnose why an SMA part lost its shape memory or superelasticity in service — sort functional fatigue from overheating, composition drift, oxidation, and structural fracture.

## Prompt Template

```
You are an SMA failure analyst. Diagnose why this part stopped behaving as designed.

The symptom is:

- **Observed failure:** [lost stroke / no longer recovers strain / set in wrong shape / cracked / stuck]
- **Part and alloy:** [actuator wire / stent / coupling; alloy if known]
- **Service history:** [cycle count, peak temperature seen, peak strain, environment, time in service]
- **What changed:** [gradual drift vs. sudden failure; any thermal/overload event]
- **Available evidence:** [post-service DSC, dimensional measurement, fractography, none]

Please:
1. Generate a ranked differential: functional fatigue, overheating above shape-set/training temp, composition/aging drift, oxidation/interstitial pickup, structural (crack) fatigue, mechanical overload/detwinning.
2. For each candidate, state the discriminating test or observation that confirms or rules it out.
3. Give the most likely root cause with confidence, and the evidence that would raise that confidence.
4. Recommend a corrective action (redesign strain amplitude, cap service temperature, change surface finish, re-spec alloy).
```

## Expected Output

- A ranked differential of failure mechanisms with discriminators for each.
- The most-likely root cause with a stated confidence level.
- The single confirming test to run next.
- A concrete corrective action tied to the root cause.
