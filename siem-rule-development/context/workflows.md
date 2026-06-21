# SIEM Rule Development — Workflows and Methodology

What the agent *does*, tied to this build's technique: **decision-tree triage workflows**. The detection lifecycle is modeled as HF circuit planning — survey the path, characterize the noise, find the usable frequency window, predict reliability, then operate and triage. Concepts live in `concepts.md`; this file is procedure.

## The Propagation-Modeled Detection Lifecycle (8 phases)

### Phase 1 — Path survey
Define the detection objective and its endpoints. What behavior (ATT&CK technique) is the target, and which telemetry "carries" it (Sysmon, EDR, Windows Security, cloud audit, proxy, DNS)? No telemetry = no circuit, regardless of how good the rule is. Output a one-line objective + the required log fields. *(`/draft-detection`)*

### Phase 2 — Noise-floor characterization
Measure the benign event rate for the chosen source/entity over a full diurnal cycle (≥ 2–4 weeks). Compute median, p95, peak, and the top noise contributors (service accounts, scanners, chatty hosts). This sets the SNR the detection must clear. *(`/noise-floor`)*

### Phase 3 — Threshold-band determination
Sweep the operating point. Find the **LUF** (the loosest threshold before FP load blows the budget) and the **MUF** (the strictest threshold before recall drops below the floor). The usable window is between them; set the operating point at the **FOT ≈ 0.85 × MUF** — strict enough to clear noise, with margin so normal variation doesn't close the circuit. *(`/threshold-band`)*

### Phase 4 — Propagation forecast
Project the rule's reliability across the diurnal/weekly cycle (the VOACAP REL analog). Predict benign fires per hour-of-day bucket at the chosen threshold, flag **blackout windows** (peaks where the rule will storm or be muted), and recommend either per-bucket thresholds or a schedule. *(`/propagation-forecast`)*

### Phase 5 — Backtest gate (go / no-go)
Replay the rule against a historical window before production. Count would-be alerts, sample/classify precision, and confirm it fires on known-bad (atomic red-team tests, prior incidents). Compare to the FP budget. This is prediction-before-deployment — the rule does not reach prod without it. *(`/backtest-rule`)*

### Phase 6 — Deploy at FOT with a diurnal baseline
Ship at the FOT operating point, referencing a time-of-day / day-of-week baseline so the threshold adapts instead of being tuned to the mean. *(`/diurnal-baseline`)*

### Phase 7 — Triage via decision tree
Every alert is dispositioned through the triage decision tree below — the heart of this build's technique. *(`/triage-tree`)*

### Phase 8 — Drift monitoring and retune
Watch the environment ("space weather"). When deployments, new log sources, incidents, or campaigns shift the baseline, reliability drifts: the rule starts storming (fell below the LUF) or goes silent (drifted above the MUF). Diagnose and retune to the FOT. *(`/space-weather`, `/tune-rule`)*

## The alert-triage decision tree

Apply top-down to each incoming alert. Record the branch path taken — it is tuning feedback for the rule that produced the alert.

```
ALERT
 │
 ├─ Q1. Is the environment disturbed right now?
 │      (active incident/outage, mass change, known FP campaign — a "geomagnetic storm")
 │      YES → the noise floor is elevated. Treat single, uncorroborated alerts as
 │            suspected FP-by-conditions. Suppress-and-batch, watch for correlation.
 │            Do NOT re-baseline now (avoid baseline poisoning). → END (defer)
 │      NO  → continue
 │
 ├─ Q2. Does the signal clear the required SNR margin for THIS time bucket?
 │      (deviation vs the diurnal baseline at this hour-of-day, not the daily mean)
 │      BELOW margin → likely benign noise the static view mislabeled.
 │            Close-benign + flag the rule for diurnal re-baselining. → END (close)
 │      ABOVE margin → continue
 │
 ├─ Q3. Is there ATT&CK corroboration?
 │      (a paired technique, a kill-chain neighbor, the same entity lighting up
 │       a second analytic — a "second circuit confirming the opening")
 │      YES → escalate. Multi-source correlation is high-confidence. → ESCALATE
 │      NO  → continue
 │
 ├─ Q4. Is the entity high-criticality?
 │      (crown-jewel host, privileged account, internet-facing asset)
 │      YES → enrich and escalate with lower threshold — the cost of a miss dominates.
 │      NO  → enrich, hold for analyst, lower priority. → ENRICH/QUEUE
 │
 └─ Default → ENRICH/QUEUE with the branch path attached for feedback.
```

### Decision points for threshold selection
- **FP load > budget at the FOT** → the LUF has risen (noise floor grew). Re-characterize the noise floor before loosening anything (`/noise-floor`).
- **Recall < floor at the FOT** → operating too close to / above the MUF, or the technique is no longer detectable in current telemetry (a "blackout"). Check coverage (`/coverage-map`) before tightening further.
- **Reliability good at the mean but bad at peak/trough** → switch from a static threshold to per-bucket thresholds from the diurnal baseline.
- **Sudden one-off spike** → suspected Sporadic-E (transient). Do not retune on a single transient; confirm it recurs before changing the operating point.

## Tuning-feedback loop
Triage dispositions (Q2 closes, Q3 escalations) feed back into the next `/tune-rule` cycle. A rule generating mostly Q2-closes is sitting below its LUF and needs tightening toward the FOT; a rule that never reaches Q3 may be above its MUF and missing corroboration it should be catching.
