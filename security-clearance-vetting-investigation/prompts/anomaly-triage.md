# Anomaly Triage

Use when the user has a single suspicious signal on a subject and wants to decide whether it warrants further action.

```
Subject SUBJ-NNNN just surfaced an anomaly. Help me triage it predictive-maintenance style:

Signal:
- Source: [Criminal | Financial | Terrorism/Foreign | Public Records | Self-Report | Employer]
- Severity (my initial estimate): [low | moderate | high]
- Summary (redacted): …
- Time since last scan: …

Walk through:
1. Which SEAD 4 guideline(s) this maps to.
2. What this signal means about the subject's "wear indicators" — is a condition trending toward a disqualifying threshold?
3. What the shortest reasonable inquiry looks like (records, interview, collateral).
4. Whether this should trigger an out-of-cycle scan or can wait for the next scheduled one.
5. Recommended disposition language for the case file — framed as analyst lead, not determination.

Save the result as a CE alert under outputs/ce-alerts/ and cross-link from the subject folder.
```
