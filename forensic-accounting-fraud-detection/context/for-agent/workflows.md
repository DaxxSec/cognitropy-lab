# Investigation Workflows

## Workflow 1: Transaction Dataset Screening (AP/GL Focus)

### Inputs Required
- General ledger export or accounts payable transaction file (CSV/XLSX)
- Vendor master file (vendor ID, name, address, bank info, EIN/TIN)
- Optional: employee directory (for cross-referencing)

### Steps
1. **Profile the dataset**
   - Row count, date range, total dollar volume
   - Identify key fields: transaction ID, date, amount, vendor/payee, GL account, preparer, approver
   - Check for nulls in critical fields; flag incomplete records

2. **Duplicate payment test**
   - Match on: vendor ID + amount + date (±3 days) + invoice number
   - Flag matches for review; calculate dollar exposure

3. **Benford's Law test**
   - Extract first and first-two digits from transaction amounts
   - Calculate actual vs. expected frequency
   - Compute Z-statistics for each digit; flag |Z| > 1.96 (95% CI) or > 2.576 (99% CI)
   - Chi-square goodness-of-fit across all digits

4. **Round number test**
   - Count transactions ending in .00 vs. expected baseline
   - Flag excess of $X,000, $X,500 patterns

5. **Split transaction / threshold avoidance**
   - Identify approval thresholds from policy (e.g., $5,000, $10,000, $25,000)
   - Flag sequences of payments to same vendor within 7 days totaling above threshold
   - Flag individual payments at $X minus $1–$99 below common thresholds

6. **Vendor analysis**
   - Vendors with PO Box only (no street address)
   - Vendors with same address/phone/email as another vendor
   - Vendors sharing address with any employee in directory
   - Vendors added to master file within 30 days before a payment spike
   - Single-transaction vendors (potential pass-through)

7. **Timing analysis**
   - Journal entries posted on weekends, holidays, or outside business hours
   - Transactions posted in closed accounting periods (backdated)
   - End-of-period spikes in transaction volume

8. **Output**: Anomaly summary table ranked by risk score (High/Medium/Low)

---

## Workflow 2: Financial Statement Manipulation Screen

### Inputs Required
- Income statement (2 years minimum)
- Balance sheet (2 years)
- Cash flow statement
- Optional: MD&A section, auditor's report

### Steps
1. **Ratio trend analysis**
   - Gross margin, operating margin, net margin trends
   - Days Sales Outstanding (DSO) trend — rising DSO signals possible revenue inflation
   - Days Inventory Outstanding (DIO) — rising may signal inventory overstatement
   - Cash conversion cycle

2. **Accruals quality analysis**
   - Operating accruals = Net Income − Operating Cash Flow
   - High accruals relative to assets = earnings management risk

3. **Beneish M-Score calculation**
   - Compute all 8 variables from provided financials
   - Calculate composite M-Score
   - Flag scores above -1.78 with specific variable drivers

4. **Revenue recognition red flags**
   - Channel stuffing signals: Q4 revenue spike + Q1 returns spike
   - Bill-and-hold indicators in footnotes
   - Related-party revenue without arm's-length pricing disclosure

5. **Expense analysis**
   - R&D or marketing expense drops during strong revenue growth (cookie jar)
   - Capitalized costs that appear operational
   - COGS components growing faster than revenue

6. **Footnote and MD&A review**
   - Changes in accounting policies or estimates (lowered depreciation, extended useful lives)
   - Auditor changes (especially mid-year)
   - Going-concern language
   - Significant related-party transactions

---

## Workflow 3: Entity Structure and Beneficial Ownership Mapping

### Inputs Required
- Target entity name(s) and jurisdiction(s)
- Any known principals, addresses, or EINs

### Steps
1. **Corporate registry search**
   - State/jurisdiction of formation
   - Registered agent name and address
   - Officers and directors
   - Filing history (amendments, reinstatements, dissolutions)

2. **Ownership chain tracing**
   - Identify parent entities and subsidiaries
   - Flag jurisdictions known for opacity (Delaware LLCs, Wyoming, Nevada, BVI, Cayman, Seychelles)
   - Note any nominee director/shareholder arrangements

3. **Address and agent clustering**
   - Check if registered agent serves hundreds/thousands of entities (formation agent vs. substantive office)
   - Flag entities sharing physical address across unrelated industries

4. **Principal cross-referencing**
   - Officers/directors appearing across multiple entities
   - Adverse media screening for principals
   - OFAC SDN list check
   - Court record search (judgments, liens, prior fraud cases)

5. **Financial footprint consistency**
   - Revenue vs. employee count (high revenue, minimal employees = possible pass-through)
   - Bank account jurisdictions vs. operating jurisdictions
   - Known assets vs. reported income

6. **Output**: Entity map (text-based relationship diagram) + risk-ranked finding summary

---

## Workflow 4: Investigation Workpaper Assembly

### Inputs Required
- Findings from one or more of the above workflows
- Case number / matter name
- Examiner name(s)
- Date of work

### Structure
1. **Cover page**: Matter, date, examiner, scope statement, data sources
2. **Executive summary**: Top 3–5 findings, estimated dollar exposure, recommended next steps
3. **Methodology section**: Tests performed, population size, date ranges, tools used
4. **Findings detail** (one page per significant finding):
   - Finding description
   - Evidence: transaction IDs, document citations, screenshots/exhibits
   - Risk classification: Confirmed / Probable / Possible / Indicator
   - Dollar exposure (if quantifiable)
   - Recommendation
5. **Limitations**: What was not tested, data gaps, reliance on representations
6. **Appendices**: Raw anomaly tables, Benford charts, entity diagrams

---

## Workflow 5: Crypto/Digital Asset Transaction Tracing

### Inputs Required
- Wallet addresses, transaction hashes, or exchange account identifiers
- Known context (e.g., "this address received ransomware payments")

### Steps
1. **On-chain data collection**
   - Pull transaction history from relevant blockchain explorer
   - Identify input/output addresses, amounts, timestamps, fees

2. **Clustering analysis**
   - Common-input-ownership heuristic: inputs from same transaction likely controlled by same entity
   - Identify exchange deposit addresses (known cluster labels from Chainalysis/Elliptic-style databases)

3. **Flow mapping**
   - Trace funds forward (where did they go?) and backward (where did they come from?)
   - Flag mixer/tumbler touchpoints (CoinJoin patterns, Tornado Cash, etc.)
   - Identify exchange on-ramps/off-ramps (KYC attachment points)

4. **Risk scoring**
   - Proximity to sanctioned addresses (OFAC-listed)
   - Exposure to dark market addresses
   - Illicit service exposure percentage

5. **Output**: Transaction flow diagram + narrative memo
