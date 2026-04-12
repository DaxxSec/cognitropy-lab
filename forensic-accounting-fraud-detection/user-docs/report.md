# Investigation Report Template

**PRIVILEGED AND CONFIDENTIAL**  
**ATTORNEY-CLIENT COMMUNICATION** *(if applicable)*

---

## FORENSIC ACCOUNTING INVESTIGATION REPORT

**Matter**: [Case Name / Matter Number]  
**Prepared by**: [Examiner Name(s)]  
**Date**: [Date]  
**Engagement Period**: [Start] – [End]  
**Report Version**: Draft / Final

---

## EXECUTIVE SUMMARY

### Investigation Trigger
[Briefly describe what initiated the investigation]

### Scope
[Describe what was examined — entities, time periods, data sources]

### Summary of Findings

| # | Finding | Risk Level | Estimated Exposure |
|---|---|---|---|
| 1 | [Finding description] | High / Medium / Low | $[X] |
| 2 | | | |

### Recommended Actions
1. [Immediate action — e.g., suspend access, freeze payments]
2. [Short-term — e.g., additional data requests, interviews]
3. [Long-term — e.g., control enhancements, regulatory referral]

---

## METHODOLOGY

### Data Sources
| Source | Description | Date Range | Record Count |
|---|---|---|---|
| GL Export | Full general ledger | [dates] | [rows] |
| Vendor Master | AP vendor file | [as of date] | [rows] |
| [Other] | | | |

### Analytical Tests Performed
- [ ] Benford's Law (first digit, first-two digit)
- [ ] Duplicate payment detection
- [ ] Threshold avoidance / split transaction test
- [ ] Timing anomaly analysis
- [ ] Vendor master cross-reference
- [ ] Financial ratio analysis
- [ ] Beneish M-Score
- [ ] Entity/ownership research
- [ ] Other: [specify]

### Tools Used
- Python (pandas, numpy, scipy, matplotlib)
- [Other tools]

---

## FINDINGS

### Finding 1: [Title]

**Risk Classification**: Confirmed / Probable / Possible / Indicator  
**Estimated Dollar Exposure**: $[X]

**Description**:
[Clear, factual description of what was found]

**Evidence**:
- Transaction ID(s): [list]
- Document reference(s): [list]
- [Other evidence]

**Analysis**:
[Explain why this is a red flag and what scheme it may indicate]

**Recommendation**:
[Specific next steps]

---

*(Add additional Finding sections as needed)*

---

## LIMITATIONS

1. [Data limitation — e.g., "Vendor master did not include deleted records prior to 2023"]
2. [Scope limitation — e.g., "Cash transactions were not available for review"]
3. [Reliance — e.g., "We relied on representations from management regarding approval thresholds"]

---

## DISCLAIMER

This report was prepared as analytical assistance only. It does not constitute a professional audit opinion, legal opinion, or regulatory submission. All findings represent analytical observations and should be reviewed by qualified forensic accountants and legal counsel before any action is taken. Nothing in this report should be construed as a determination that any individual committed fraud or violated any law.
