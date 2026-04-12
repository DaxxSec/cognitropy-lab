# Environment Notes

## Expected Data Inputs

The agent works with financial data in these forms:

1. **Pasted text** — user pastes CSV rows, financial statement line items, or transaction excerpts directly into the conversation
2. **File attachment** — user attaches CSV, XLSX, or PDF files for analysis
3. **Manually described data** — user narrates a scenario ("we have 50,000 AP transactions for FY2025…") and agent provides guidance
4. **EDGAR/public filings** — agent can reference publicly available SEC filings by company name and period

## Python Environment
The agent can generate and execute Python code for:
- Statistical analysis (pandas, numpy, scipy)
- Visualization (matplotlib, seaborn)
- PDF extraction (pdfplumber)
- Data profiling and cleaning

When executing code, always:
- Show the code before running it
- Explain what each section does
- Display output with interpretation
- Save generated charts and CSVs to `outputs/`

## Preferred Output Directory
All generated files (workpapers, charts, CSVs) → `outputs/`

## Sensitivity Handling
Financial data often contains PII and confidential business information:
- Recommend users redact names, SSNs, account numbers before sharing
- Never log or persist sensitive data outside the current session
- Offer anonymized examples when users need to illustrate a pattern without sharing real data

## Tooling Assumptions
- Python 3.10+ available with standard data science stack
- No proprietary forensic software assumed (ACL/IDEA commands provided as reference)
- Blockchain explorer data can be retrieved manually by user and pasted in
- SEC EDGAR accessible via web
