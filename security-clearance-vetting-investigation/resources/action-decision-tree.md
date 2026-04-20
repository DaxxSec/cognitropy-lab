# Action Decision Tree

Applied at the end of every `/drift-scan`.

```
┌─ Any single guideline score ≥ 5?
│   └─ YES → Recommend referral to adjudicator. Draft /adjudicate.
│   └─ NO ↓
├─ Any single guideline score ≥ 4?
│   └─ YES → Recommend out-of-cycle investigation, focused on that guideline.
│   └─ NO ↓
├─ Composite ≥ 3.51?
│   └─ YES → Out-of-cycle focused inquiry + shorten scan to 30-45 days.
│   └─ NO ↓
├─ Two consecutive "degrading" trends?
│   └─ YES → Focused inquiry + shorten scan interval by 50%.
│   └─ NO ↓
├─ Composite 2.51 – 3.50?
│   └─ YES → Scheduled re-scan at 90 days; documented inquiry on highest guideline.
│   └─ NO ↓
├─ Composite 1.51 – 2.50?
│   └─ YES → Routine re-scan at 120 days.
│   └─ NO ↓
└─ Composite < 1.51?
    └─ YES → Extend scan interval to 180 days; consider downgrade to annual scan after 3 consecutive stable reads.
```

## Sentinel events (short-circuit the tree)
Regardless of composite, the following trigger immediate action:
- Criminal felony arrest.
- Unreported foreign contact or travel.
- Confirmed unauthorized disclosure.
- Credible insider-threat indicator from facility security.
- Self-report of any SEAD 3 category that changes the risk picture.

Sentinel events bypass the scan schedule and route to `/continuous-eval`.
