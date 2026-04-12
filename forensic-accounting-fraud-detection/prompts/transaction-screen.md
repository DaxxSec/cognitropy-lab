# Prompt: AP/GL Transaction Screening

Use this prompt to start a transaction-level fraud screening session.

---

I need to run a forensic screen on an accounts payable / general ledger dataset to identify potential fraud indicators.

**Dataset overview:**
- Source system: [e.g., SAP, QuickBooks, NetSuite, manual export]
- Date range: [start] to [end]
- Total transactions: [count]
- Total dollar volume: $[amount]
- Approval threshold policy: payments above $[X] require [approval level]

**Data fields available:**
[list the column headers from your export]

**Context:**
[Describe why you're looking at this — e.g., "We received a hotline tip about a vendor relationship," or "Routine annual fraud risk assessment," or "We noticed unusual expense spikes in Q3"]

**Paste your data below (or describe the top anomalies you've already spotted):**
[paste CSV rows or describe what you've seen]

Please run the full forensic screen: Benford's Law, duplicate payment detection, threshold avoidance, timing anomalies, and vendor risk flags. Show the code for each test and provide a risk-ranked findings summary.
