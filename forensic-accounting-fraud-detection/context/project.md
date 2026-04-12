# Project Context

## Purpose
This workspace supports forensic accounting investigations and financial fraud detection work. It is designed for:

- Internal audit teams screening for fraud risk
- Corporate investigators conducting internal investigations
- Compliance professionals assessing AML/CFT exposure
- DFIR practitioners expanding into financial crime investigations
- Researchers and students studying financial fraud patterns

## Typical Investigation Triggers
- Whistleblower complaint or hotline tip
- Anomalies surfaced in external audit
- Regulatory inquiry or subpoena
- M&A due diligence revealing inconsistencies
- Vendor or employee termination with unexplained patterns
- Suspicious Activity Report (SAR) trigger at a financial institution

## How to Use This Workspace

### For a New Investigation
1. Fill in the case details below (or in a new `context/project-[case-id].md`)
2. Describe the known facts and investigation trigger
3. List data sources available
4. Run `/onboard` to get oriented, then start with `/analyze-transactions` or the appropriate workflow

### Case Context Template (Fill In Per Investigation)
```
Case ID: 
Matter Name: 
Date Opened: 
Examiner(s): 
Investigation Trigger: 
Known Facts: 
Entities of Interest: 
Data Available: 
Estimated Scope (dollar, time period): 
Legal/Regulatory Context: 
```

## Data Handling Reminder
Remove or redact sensitive PII (SSNs, full account numbers, personal addresses) before including in context files. Use anonymized identifiers (Employee A, Vendor X, etc.) when possible.
