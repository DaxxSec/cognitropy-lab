# Domain Knowledge: Forensic Accounting & Financial Fraud Detection

## The ACFE Fraud Tree

The Association of Certified Fraud Examiners classifies occupational fraud into three branches:

### 1. Asset Misappropriation (86% of cases, median $100K loss)
- **Cash theft**: skimming (pre-recording), larceny (post-recording), payroll fraud
- **Billing schemes**: fictitious vendors, personal purchases, overbilling
- **Check tampering**: forged maker, forged endorsement, altered payee
- **Expense reimbursement**: mischaracterized, overstated, fictitious
- **Non-cash theft**: inventory theft, misuse of assets, theft of IP

### 2. Corruption (50% of cases, median $200K loss)
- Bribery (kickbacks, bid rigging)
- Conflicts of interest
- Extortion
- Illegal gratuities

### 3. Financial Statement Fraud (9% of cases, median $800K loss)
- Revenue overstatement (fictitious revenue, premature recognition)
- Expense understatement (capitalizing operating costs, underaccrual)
- Asset overstatement (inventory inflation, depreciation manipulation)
- Liability understatement (hidden obligations, off-balance-sheet structures)

---

## Key Analytical Tests

### Benford's Law
In any naturally occurring dataset with a wide range of values, the first significant digit follows a logarithmic distribution:
- d=1: 30.1%, d=2: 17.6%, d=3: 12.5%, d=4: 9.7%, d=5: 7.9%
- d=6: 6.7%, d=7: 5.8%, d=8: 5.1%, d=9: 4.6%

**When it applies**: Accounts payable, check amounts, journal entries, expense reports, sales transactions (large populations, >300 items, no assigned numbers)
**When it doesn't**: Zip codes, phone numbers, ATM transactions (bounded amounts), prices set by policy

**Interpretation**: Chi-square or Kolmogorov-Smirnov tests quantify deviation. Z-statistics identify specific first-two-digit combinations that are over/under-represented.

### Beneish M-Score (8-Variable Model)
M = −4.84 + 0.920(DSRI) + 0.528(GMI) + 0.404(AQI) + 0.892(SGI) + 0.115(DEPI) − 0.172(SGAI) + 4.679(TATA) − 0.327(LVGI)

| Variable | Formula | Red Flag Direction |
|---|---|---|
| DSRI | (Rec_t/Sales_t) / (Rec_{t-1}/Sales_{t-1}) | >1.465 |
| GMI | GM_{t-1}/GM_t | >1.193 |
| AQI | (1 - (CA+PPE)/TA)_t / (same)_{t-1} | >1.254 |
| SGI | Sales_t / Sales_{t-1} | >1.607 |
| DEPI | (Dep/(Dep+PPE))_{t-1} / (same)_t | >1.077 |
| SGAI | (SGA/Sales)_t / (SGA/Sales)_{t-1} | >1.041 |
| TATA | (ΔCA - ΔCash - ΔCLD - ΔTax - Dep) / TA | >0.031 |
| LVGI | ((LTD+CLD)/TA)_t / (same)_{t-1} | >1.111 |

**Cutoff**: M > -1.78 → possible manipulator; M > -2.22 → possible manipulator (lower sensitivity)

### Altman Z-Score (Public Companies)
Z = 1.2X1 + 1.4X2 + 3.3X3 + 0.6X4 + 1.0X5
- X1 = Working Capital / Total Assets
- X2 = Retained Earnings / Total Assets  
- X3 = EBIT / Total Assets
- X4 = Market Cap / Total Liabilities
- X5 = Sales / Total Assets

**Zones**: Z > 2.99 (safe), 1.81–2.99 (grey), Z < 1.81 (distress)

---

## Common Fraud Schemes (Detailed)

### Ghost Employee Scheme
- Fraudster adds fictitious employee to payroll or retains terminated employee
- Paycheck goes to fraudster's account or accomplice
- **Detection**: Cross-reference payroll roster vs. HR records; look for employees with no benefits enrollment, no supervisor, shared bank account numbers or addresses; duplicate SSNs

### Vendor Kickback / Bid Rigging
- Vendor inflates invoices; employee receives portion as kickback
- Or employee tips vendor to winning bid in exchange for payment
- **Detection**: Employees with vendor relationships not disclosed; vendors sharing address/phone/banking with employees; single-source vendors with no competition; invoice amounts just below competitive-bid thresholds

### Lapping Scheme (A/R Fraud)
- Fraudster steals customer payment, covers with next customer's payment, and so on
- Creates rolling shortfall in A/R
- **Detection**: Customers report applying payments that aren't reflected in aging; unusual number of adjustments to customer accounts; one person handling both receipts and posting

### Check Tampering
- Altered payee name on issued checks
- Forged signatures on stolen blank checks
- **Detection**: Payee names inconsistent with check register; checks clearing out of sequence; dual endorsements; unusual payees in vendor master

### Expense Report Fraud
- Mischaracterized: personal expenses submitted as business
- Overstated: receipts inflated
- Fictitious: fake receipts, non-existent trips
- **Detection**: Weekend/holiday charges for "business" meals; round-number amounts; same location appearing for different employees same date; duplicate receipts across reports

---

## Money Laundering — The Three Stages

1. **Placement**: Introducing dirty cash into the financial system (structuring/smurfing, cash-intensive business co-mingling)
2. **Layering**: Obscuring the trail through complex transactions (shell companies, multiple wire transfers, cryptocurrency mixing)
3. **Integration**: Returning funds to legitimate economy (real estate purchases, luxury goods, loan-back schemes)

**FinCEN Red Flags**:
- Transactions just below CTR ($10,000) or SAR reporting thresholds — structuring
- Rapid movement of funds through accounts (in and out same/next day)
- Accounts with multiple beneficial owners across jurisdictions
- Unexplained wealth inconsistent with known income sources

---

## Regulatory & Legal Framework

| Law/Standard | Jurisdiction | Key Provision |
|---|---|---|
| Foreign Corrupt Practices Act (FCPA) | US (extraterritorial) | Anti-bribery; books & records requirements for public companies |
| Sarbanes-Oxley (SOX) Sections 302/404 | US public companies | CEO/CFO certification; internal controls over financial reporting |
| Bank Secrecy Act (BSA) | US financial institutions | AML program; CTR and SAR filing requirements |
| Anti-Money Laundering Act 2020 | US | Expanded FinCEN authority; beneficial ownership registry |
| FATF Recommendations | Global | 40 recommendations for national AML/CFT frameworks |
| GAAP (US) / IFRS (international) | Financial reporting | Revenue recognition (ASC 606 / IFRS 15), lease accounting, etc. |

---

## Key Databases and Public Sources

| Source | What It Contains | Access |
|---|---|---|
| SEC EDGAR | 10-K, 10-Q, 8-K, proxy filings for US public companies | Public, free |
| FinCEN BOI Registry | Beneficial ownership for US entities (post-CTA 2024) | Law enforcement + regulators |
| OFAC SDN List | Sanctioned individuals, entities, jurisdictions | Public, free |
| OpenCorporates | Corporate registry data across 140+ jurisdictions | Free (limited) / API |
| Bloomberg / Refinitiv | Financial data, ownership, adverse media | Commercial |
| LexisNexis / PACER | Court records, liens, judgments | Subscription / per-search |
| Blockchain explorers | On-chain transaction history | Public (Etherscan, blockchain.com, etc.) |
