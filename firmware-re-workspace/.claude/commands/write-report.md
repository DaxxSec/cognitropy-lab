# /write-report — Firmware Analysis Report Generator

Compile all findings from the current investigation into a formal firmware analysis report.

## Prerequisites
- At least one analysis stage completed
- Findings documents in `outputs/`

## Inputs
Ask:
1. Who is this report for? (internal team / vendor CVD / public / client)
2. What classification level? (TLP:WHITE / TLP:GREEN / TLP:AMBER / Confidential / Internal)
3. Should CVE/CVD information be included?
4. What's the report title or project name?

---

## Pre-Report Data Gathering

Collect from existing outputs and context:

```bash
# Survey what's been documented
ls outputs/
cat context/project.md
cat work-log/*.md 2>/dev/null | head -100
```

Ask the user to confirm:
- All findings have been documented in `outputs/`
- Severity ratings have been assigned
- Remediation recommendations are ready

---

## Report Template

Generate the following report structure as `outputs/report-[target]-[date].md`:

```markdown
# Firmware Security Analysis Report

**Document Title:** [title]
**Target Device:** [device name and model]
**Firmware Version:** [version]
**Firmware SHA256:** [hash]
**Analysis Date:** [start] — [end]
**Analyst:** [name/handle]
**Report Version:** 1.0
**Classification:** [TLP / Confidential / etc.]

---

## 1. Executive Summary

[2-4 sentences: what was analyzed, what was found, overall severity, recommended action]

**Severity Summary:**
| Severity | Count |
|---|---|
| Critical | [n] |
| High | [n] |
| Medium | [n] |
| Low | [n] |
| Informational | [n] |

---

## 2. Target Information

| Field | Value |
|---|---|
| Device | [name and model] |
| Firmware Version | [version] |
| Firmware Source | [where obtained] |
| File Hash (SHA256) | [hash] |
| Architecture | [arch + endianness] |
| Operating System | [OS + version] |
| Filesystem | [type] |
| Analysis Date | [date range] |

---

## 3. Methodology

**Tools Used:**
- [tool 1] — [purpose]
- [tool 2] — [purpose]
- ...

**Analysis Stages Completed:**
- [x] Initial triage and identification
- [x] Filesystem extraction
- [x] Automated scanning (firmwalker)
- [x] Manual filesystem review
- [x] Binary analysis
- [x] Attack surface mapping
- [x] Vulnerability discovery
- [ ] Dynamic analysis / emulation (if not completed)

---

## 4. Findings

[For each finding, use this template]

### [FW-001] [Finding Title]
**Severity:** [Critical / High / Medium / Low / Informational]
**CWE:** [CWE-XXX — Name]
**CVSS v3.1 Score:** [score] ([vector string])
**Affected Component:** `[file or binary path]`

**Description:**
[Technical description of the vulnerability or finding]

**Evidence:**
```
[Terminal output, code snippet, or disassembly excerpt showing the issue]
```

**Impact:**
[What an attacker can achieve by exploiting this]

**Remediation:**
[Specific actionable fix recommendation]

---

## 5. Additional Observations

[Informational findings, configuration issues, outdated components, etc. that don't rise to vulnerability level but are worth noting]

---

## 6. Recommendations Summary

| Priority | Recommendation |
|---|---|
| Immediate | [action] |
| Short-term | [action] |
| Long-term | [action] |

---

## 7. Appendices

### Appendix A: Tool Versions
[List exact versions of all tools used]

### Appendix B: File Hashes
[SHA256 of firmware and any extracted artifacts]

### Appendix C: Full Secrets Inventory
[Redacted list of all secrets found, per SECRET-XXX IDs]

### Appendix D: Attack Surface Map
[Full attack surface from /map-attack-surface output]

---

*Report generated with Firmware RE Workspace*
*Classification: [classification]*
```

---

## Post-Report Actions

1. Save report to `outputs/report-[target-name]-[date].md`
2. If DOCX format requested: note that user can run `pandoc report.md -o report.docx`
3. Update `context/project.md` to reflect report completed
4. Log to `work-log/[date].md`
5. Remind user of any responsible disclosure obligations based on `context/constraints.md`
