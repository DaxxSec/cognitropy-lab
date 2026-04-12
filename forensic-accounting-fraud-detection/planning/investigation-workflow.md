# Investigation Workflow Plan

## Phase 1: Intake & Scoping (Day 1–2)

### Objectives
- Understand the investigation trigger and known facts
- Identify available data sources and their limitations
- Define scope: entities, time period, transaction types, dollar thresholds
- Identify legal/regulatory framework (internal investigation vs. regulatory vs. litigation)

### Tasks
- [ ] Document investigation trigger (tip, audit finding, regulatory, M&A)
- [ ] Identify key entities, individuals, and relationships of interest
- [ ] Inventory available data (systems, date ranges, completeness)
- [ ] Establish document preservation hold (notify IT/legal)
- [ ] Define investigation hypotheses (top 3–5 possible schemes)
- [ ] Determine privilege status (attorney-client if legal involvement)

### Outputs
- Investigation scope memo
- Data request list
- Hypothesis register

---

## Phase 2: Data Collection & Profiling (Day 2–5)

### Objectives
- Obtain complete, unaltered data from source systems
- Understand data structure, quality, and completeness
- Document chain of custody for all data received

### Tasks
- [ ] Request GL export (full population, not pre-filtered)
- [ ] Request vendor master file (including inactive/deleted vendors)
- [ ] Request AP transaction detail with all fields
- [ ] Request payroll register (if payroll fraud in scope)
- [ ] Profile each dataset: row counts, date ranges, null rates, duplicates
- [ ] Document data anomalies (missing periods, suspicious gaps)
- [ ] Hash files to establish forensic integrity baseline

### Outputs
- Data receipt log with chain of custody
- Dataset profile report
- Data quality issues memo

---

## Phase 3: Automated Screening (Day 3–7)

### Objectives
- Run systematic statistical screens across full transaction population
- Generate initial hypothesis rankings based on screen results

### Tests to Run
- [ ] Benford's Law (first digit, first-two digit)
- [ ] Duplicate payment detection (vendor + amount + date window)
- [ ] Round number / threshold avoidance test
- [ ] Sequence gap analysis (invoice/check numbers)
- [ ] Timing anomaly test (weekends, holidays, after-close entries)
- [ ] Vendor master cross-reference (employee address matches, PO box only)
- [ ] Single-use vendor identification
- [ ] High-volume / high-value vendor ranking

### Outputs
- Anomaly summary table (ranked by risk: High/Medium/Low)
- Statistical charts (Benford's, distribution plots)
- Priority hypothesis list for deep-dive

---

## Phase 4: Deep-Dive Analysis (Day 5–15)

### Objectives
- Test priority hypotheses with transaction-level evidence
- Build evidence chains for each confirmed or probable finding

### Tasks
Per hypothesis, document:
- [ ] Specific transactions / documents reviewed
- [ ] Corroborating evidence found (or absence noted)
- [ ] Dollar exposure calculated
- [ ] Additional data/information needed
- [ ] Parties involved (with appropriate confidence level)

### For Financial Statement Manipulation
- [ ] Beneish M-Score computation
- [ ] Ratio trend analysis (DSO, DIO, gross margin, accruals)
- [ ] Revenue recognition footnote review
- [ ] Auditor correspondence (if available)

### Outputs
- Transaction-level evidence workpapers (one per finding)
- Entity/relationship diagrams
- Interview question lists (for any witness/subject interviews)

---

## Phase 5: Reporting (Day 14–20)

### Objectives
- Document all findings with evidence citations
- Provide recommendations for remediation and next steps
- Prepare for legal/regulatory use if required

### Report Components
- [ ] Executive summary (findings, exposure, recommendations)
- [ ] Methodology section
- [ ] Finding-by-finding detail (evidence, risk classification, exposure)
- [ ] Entity diagrams and transaction flow visualizations
- [ ] Appendices (raw anomaly tables, data profiles)
- [ ] Limitations and caveats
- [ ] Standard disclaimer

### Outputs
- Final investigation report
- Appendix package
- Recommendation tracker

---

## Phase 6: Remediation & Follow-Up

### Common Recommendations
- Personnel actions (termination, suspension pending investigation)
- Vendor debarment and clawback demands
- Insurance claims (fidelity/crime policy)
- Regulatory referral (DOJ, SEC, FinCEN, state AG)
- Law enforcement referral (FBI, IRS-CI, Secret Service)
- Control improvements (segregation of duties, approval workflow)
- System configuration changes (audit logging, alert thresholds)

### Monitoring
- Establish post-investigation monitoring for recurrence
- Re-run anomaly screens on next quarterly data cycle
- Track remediation action completion
