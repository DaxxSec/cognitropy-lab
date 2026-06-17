# Condition & Containment

## Purpose

Use to turn a reconstruction into a per-host condition report and a prioritized containment plan that preserves volatile evidence — modeled on conservation condition-reporting (assess losses and damage before any intervention).

## Prompt Template

```
You are writing a condition report and containment plan for a compromised host. Stabilize without destroying evidence.

- **Host:** [HOSTNAME, ROLE, CRITICALITY, DATA SENSITIVITY]
- **Reconstruction:** [TIMELINE + STRATIGRAPHY SUMMARY]
- **Persistence found:** [RUN KEYS / SERVICES / TASKS / WMI]
- **Constraints:** [UPTIME REQUIREMENTS / LEGAL HOLD / EVIDENCE NEEDS]

Please:
1. Summarize condition: intact vs tampered vs lost components.
2. Table every persistence mechanism with the privilege it holds and whether it survives reboot.
3. Estimate data/credential exposure.
4. Give a containment plan ordered to preserve order of volatility — capture before cleanse where evidence matters — and never leave an active C2 channel open.
```

## Expected Output

- A condition summary (intact / tampered / lost).
- A persistence-and-privilege table flagged for reboot-survival.
- A prioritized containment plan with an explicit evidence-preservation sequence.
