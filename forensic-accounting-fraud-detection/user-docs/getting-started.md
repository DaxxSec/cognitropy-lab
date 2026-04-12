# Getting Started: Forensic Accounting & Financial Fraud Detection

## Who This Workspace Is For
- Internal auditors and compliance professionals
- Corporate investigators and legal teams
- DFIR practitioners expanding into financial crime
- Researchers and students studying financial fraud
- Anyone who needs to screen financial data for anomalies

## Quick Start (5 minutes)

### Step 1: Open in Claude Code or Cowork
Clone this workspace directory and open it. The agent will load the context from `CLAUDE.md` automatically.

### Step 2: Run /onboard
Type `/onboard` to get an orientation and describe your scenario. The agent will guide you to the right workflow.

### Step 3: Bring Your Data
The agent works best with:
- **Transaction files**: CSV or XLSX exports from your accounting system
- **Financial statements**: Annual report figures, 10-K data
- **Entity names**: Company names, addresses, known principals

**Before sharing data**: Remove or replace SSNs, full account numbers, and personal home addresses with anonymized identifiers.

### Step 4: Follow a Workflow
Pick the workflow that matches your situation:

| Your Situation | Command to Start |
|---|---|
| "I have an AP transaction file I want to screen" | `/analyze-transactions` |
| "I want to check a company's financials for manipulation" | `/beneish-score` |
| "I need to research a suspicious vendor/company" | `/trace-entity` |
| "I have findings I need to document" | `/draft-workpaper` |

---

## Example Sessions

### Example 1: Vendor Fraud Screen
```
You: /analyze-transactions

Agent: [asks for dataset info]

You: We have 8,500 AP transactions for FY2025, exported from QuickBooks.
     Our approval threshold is $5,000. Here's a sample:
     
     date,vendor_id,vendor_name,invoice_num,amount,gl_account,approved_by
     2025-01-08,V0142,Acme Consulting,INV-0041,4999.00,7200,jdoe
     2025-01-09,V0142,Acme Consulting,INV-0042,4998.00,7200,jdoe
     2025-01-15,V0142,Acme Consulting,INV-0043,4997.00,7200,jdoe
     ...

Agent: [flags threshold avoidance pattern, runs Benford's test, checks vendor]
```

### Example 2: Financial Statement Analysis
```
You: /beneish-score

Agent: [asks for financial data]

You: Here are TechCorp's figures:
     Year T: Revenue $45.2M, AR $8.1M, COGS $28.3M...
     Year T-1: Revenue $31.8M, AR $4.2M, COGS $20.1M...

Agent: [computes M-Score, flags DSRI of 1.8 (threshold: 1.465), 
        notes AR growing 93% while revenue grew 42%]
```

---

## Tips for Best Results

**Be specific about your concern.** "I think there's a ghost employee" gets more targeted help than "something seems off with payroll."

**Provide volume context.** "500 transactions" vs. "500,000 transactions" changes what statistical tests are meaningful.

**Share the approval structure.** Knowing your authorization thresholds enables threshold-avoidance detection.

**Iterate on findings.** Start with the automated screen, then deep-dive the top flagged items together.

**Document as you go.** Use `/draft-workpaper` regularly — building documentation during investigation is much easier than reconstructing it afterward.

---

## Important Reminders

⚠️ **This is analytical assistance, not a professional attestation.** All findings should be reviewed by qualified forensic accountants and legal counsel before any action is taken.

⚠️ **Preserve originals.** Never alter source data. Keep hash values of original files.

⚠️ **Privilege.** If your investigation is directed by legal counsel, discuss whether attorney-client privilege applies before creating documentation.
