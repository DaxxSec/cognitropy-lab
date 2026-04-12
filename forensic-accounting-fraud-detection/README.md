# Forensic Accounting & Financial Fraud Detection

> **Cognitropy Lab** · Day 18 · Category: Finance & Economics  
> Built: 2026-04-12 · Technique: Pattern analysis workflows

An agent workspace for systematic financial fraud investigation — combining forensic accounting methodology with data-driven anomaly detection. Drop in financial records, transaction exports, or corporate filings and get structured investigative analysis following ACFE and SEC examination standards.

---

## What This Workspace Does

This agent applies the investigative toolkit of forensic accountants and financial examiners to help you:

- **Screen large transaction datasets** for statistical anomalies (Benford's Law, duplicate payments, round-number clustering)
- **Analyze financial statements** for earnings manipulation signals (Beneish M-Score, Altman Z-Score, revenue recognition irregularities)
- **Map entity structures** to expose shell company networks and beneficial ownership chains
- **Trace payment flows** through multi-hop transfers to identify layering patterns common in fraud and money laundering
- **Document findings** in structured workpapers suitable for legal, regulatory, or internal review

---

## Use Cases

| Scenario | What to Bring | What You Get |
|---|---|---|
| Expense report audit | CSV of transactions + employee IDs | Duplicate/split payment flags, policy violations, outlier analysis |
| Vendor fraud screen | Vendor master + AP transaction history | Ghost vendor indicators, address clustering, payment pattern anomalies |
| Financial statement review | 10-K / annual report | Ratio analysis, Beneish M-Score, footnote red flags |
| Internal investigation | GL export + journal entry log | Weekend/off-hours entries, unusual reversals, segregation of duties gaps |
| M&A due diligence | Target's financials | Quality of earnings concerns, hidden liabilities, revenue sustainability |
| Crypto/asset tracing | Transaction hash list or wallet exports | Flow mapping, mixer/tumbler patterns, exchange touchpoints |

---

## Forensic Framework

### 1. Benford's Law Analysis
Naturally occurring numbers follow a predictable first-digit distribution. Large deviations — especially in check amounts, expense reports, or invoice totals — indicate potential manipulation.

```
Expected first-digit frequency (Benford):
1: 30.1% | 2: 17.6% | 3: 12.5% | 4: 9.7% | 5: 7.9%
6: 6.7%  | 7: 5.8%  | 8: 5.1%  | 9: 4.6%
```

### 2. Beneish M-Score (Earnings Manipulation)
Eight financial ratios combined into a single score. Scores above **-1.78** suggest possible earnings manipulation.

Key indicators:
- **DSRI** (Days Sales Receivable Index): rising = possible channel stuffing
- **GMI** (Gross Margin Index): declining = margin pressure or manipulation
- **AQI** (Asset Quality Index): rising = capitalizing expenses
- **SGI** (Sales Growth Index): high growth + high M-Score = risk flag
- **TATA** (Total Accruals to Total Assets): high accruals = earnings management

### 3. Transaction Anomaly Screens
- **Duplicate payments**: same vendor + amount + date window
- **Split transactions**: amounts just below approval thresholds
- **Round-number test**: excess of $X,000 or $X,500 amounts vs. expected distribution
- **Sequence gaps**: missing invoice/check numbers (destroyed documents)
- **Timing anomalies**: journal entries on weekends, holidays, or fiscal year-end after close

### 4. Entity/Ownership Analysis
- Beneficial ownership lookups (FinCEN BOI, state registry filings)
- Registered agent clustering (same agent for multiple vendors)
- Address recycling detection (vendor + employee home address matches)
- EIN reuse across multiple entities

---

## Slash Commands

| Command | Description |
|---|---|
| `/analyze-transactions` | Full anomaly screen on a transaction dataset |
| `/beneish-score` | Compute Beneish M-Score from financial statement data |
| `/trace-entity` | Map corporate structure and ownership chain |
| `/draft-workpaper` | Generate an investigation workpaper from findings |
| `/onboard` | Guided introduction to the workspace |

---

## Getting Started

1. **Clone or open** this workspace in Claude Code / Cowork
2. **Review** `CLAUDE.md` for agent capabilities and constraints
3. **Run** `/onboard` to get oriented and describe your investigation scenario
4. **Drop in data**: paste transaction CSVs, financial statement text, or entity details
5. **Follow the workflow** in `planning/investigation-workflow.md`

---

## File Structure

```
forensic-accounting-fraud-detection/
├── CLAUDE.md                          # Agent role & operating constraints
├── README.md                          # This file
├── CREATION_REPORT.md                 # Build provenance
├── context/
│   ├── role.md                        # Agent identity
│   ├── project.md                     # Investigation context (fill in per case)
│   ├── constraints.md                 # Legal/ethical guardrails
│   └── for-agent/
│       ├── domain-knowledge.md        # Forensic accounting reference material
│       ├── workflows.md               # Step-by-step investigation processes
│       ├── tools.md                   # Analytical tools and techniques
│       └── environment.md             # Data formats and tooling notes
├── .claude/commands/
│   ├── onboard.md                     # /onboard command
│   ├── analyze-transactions.md        # /analyze-transactions command
│   ├── beneish-score.md               # /beneish-score command
│   ├── trace-entity.md                # /trace-entity command
│   └── draft-workpaper.md             # /draft-workpaper command
├── prompts/
│   ├── transaction-screen.md          # Starter: AP/GL transaction screening
│   ├── statement-analysis.md          # Starter: financial statement review
│   └── entity-mapping.md             # Starter: entity structure tracing
├── planning/
│   └── investigation-workflow.md      # Full investigation process plan
├── resources/
│   ├── fraud-schemes.md               # Catalog of common fraud patterns
│   └── regulatory-reference.md        # Relevant laws, standards, agencies
└── outputs/                           # Generated reports and workpapers
```

---

## Domain Background

Forensic accounting sits at the intersection of financial analysis, investigative methodology, and legal evidence standards. Practitioners are typically CPAs with CFE (Certified Fraud Examiner) credentials. They work with:

- **Law enforcement** (FBI Financial Crimes, IRS CID, SEC Enforcement)
- **Corporations** conducting internal investigations or pre-litigation discovery
- **Bankruptcy courts** reconstructing financial histories
- **Insurance carriers** evaluating claims for fraud
- **Regulators** (PCAOB, FINRA, FinCEN, OCC)

The field draws heavily on data analytics — large GL exports, payment rail data, wire transfer records — making it a natural fit for AI-assisted pattern recognition.

---

## Important Limitations

This workspace provides **analytical assistance only**. It does not:
- Render legal conclusions or constitute legal advice
- Certify the accuracy of financial statements
- Serve as a substitute for a licensed CPA, CFE, or attorney
- Guarantee detection of all fraud (sophisticated schemes may evade statistical screens)

All findings should be reviewed by qualified professionals before being used in legal or regulatory proceedings.

---

## Related Domains

- **DFIR / Cyber**: financial fraud increasingly intersects with BEC (Business Email Compromise), ransomware extortion payments, and crypto laundering
- **OSINT**: corporate registry mining, beneficial ownership databases, adverse media screening
- **Data Engineering**: processing large GL exports, normalizing multi-system data

---

*Part of the [Cognitropy Lab](https://github.com/DaxxSec/cognitropy-lab) — one agent workspace per day, across 22 domains.*
