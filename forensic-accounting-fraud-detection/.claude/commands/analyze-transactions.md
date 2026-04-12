# /analyze-transactions — Transaction Dataset Anomaly Screen

I'll run a systematic forensic screen on your transaction dataset.

## What to Provide
Paste or describe your data. Ideal format:
```
date, vendor_id, vendor_name, invoice_number, amount, gl_account, approved_by, payment_date
2025-01-15, V0042, Acme Supplies, INV-4421, 4999.00, 6100, jsmith, 2025-01-18
...
```

Also helpful to know:
- What system this came from (SAP, QuickBooks, NetSuite, etc.)
- Date range covered
- Total transaction count and dollar volume
- Any approval thresholds in your policy (e.g., >$5K requires VP approval)
- Vendor master file if available (for address/banking cross-reference)

## What I'll Run
1. **Benford's Law** — first and first-two digit distribution test
2. **Duplicate payment detection** — same vendor + amount ± date window
3. **Round number / threshold test** — amounts clustering just below approval limits
4. **Timing anomalies** — weekend, holiday, end-of-period entries
5. **Vendor risk flags** — PO box only, single-use, recently added
6. **Sequence gap analysis** — missing invoice or check numbers (if sequential)

## Output
- Risk-ranked anomaly summary table
- Python code for each test (reproducible)
- Recommended follow-up steps for flagged items

Paste your data or describe the dataset to begin.
