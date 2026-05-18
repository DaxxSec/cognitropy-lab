# Post-Anomaly Recovery Plan

## Purpose

Use after a hot-fire produces one or more flagged anomalies that need a structured next-test posture. Compiles `/anomaly-risk-score` outputs into a recovery plan that explicitly maps each anomaly to mitigation in the next test card, with named owners, target dates, and a re-firing prerequisite checklist.

## Prompt Template

```
You are a ground-test propulsion engineer producing the recovery plan after a hot-fire that
flagged one or more anomalies. Walk each anomaly through the `A-*` tree, then aggregate into
a recovery plan suitable for distribution to the test conductor, responsible engineer, range
safety officer, and program management.

Anomaly inventory:
- **Test ID:** [test id of the just-completed fire]
- **Anomaly 1:** [type, time on test, sensor evidence summary, immediate effect]
- **Anomaly 2:** [type, time on test, sensor evidence summary, immediate effect]
- **Anomaly N:** [...]
- **Post-fire borescope / teardown findings:** [summary]
- **Recovery time pressure:** [target re-fire date, program criticality]
- **Available resources:** [spare hardware, lab time, test stand availability]

Please:
1. For each anomaly, run `/anomaly-risk-score` and capture the disposition (PROCEED / PROCEED_WITH_MITIGATION / HOLD / SCRUB) with the matrix cell.
2. Identify the worst-disposition anomaly — it sets the campaign posture.
3. List the mitigation actions per anomaly: owner, action, success criterion, target completion date.
4. List the prerequisites the next fire must satisfy before authorization: hardware swaps, design reviews, FMEA updates, redline adjustments, customer / authority notifications.
5. If the worst disposition is HOLD or SCRUB, name the authority that must sign residual-risk acceptance before re-fire.
6. Flag any anomaly whose recurrence trend (3+ same-type in trailing 5 tests) warrants a campaign-level pattern review.
7. Provide an optional re-fire readiness checklist: when the items in step 4 are checked off, what `/test-readiness-risk` re-run is required, and what the GO criteria look like.
```

## Expected Output

- An anomaly disposition table: anomaly id, type, severity, likelihood, cell, band, disposition.
- A worst-disposition headline driving the campaign posture (e.g. "Campaign posture: HOLD — re-fire blocked pending injector pattern review per Anomaly A2").
- A per-anomaly mitigation table: owner, action, success criterion, target completion date, sign-off authority.
- A re-fire prerequisite checklist with explicit gating items.
- Pattern-review flags if recurrence trends warrant.
- Recommended test-card amendments for the next fire (throttle adjustments, additional redlines, instrumentation upgrades).
- Explicit caveat that the actual re-fire authorization is the human test-conductor + range-safety officer's call, not the workspace's output.
