# /report — Security Assessment Report

Generate a formal security assessment report from completed workflow outputs.

## Steps
1. Gather completed outputs:
   - Asset inventory (`outputs/asset-inventory.md`)
   - Threat model (`outputs/threat-model.md`)
   - Network audit findings (`outputs/network-audit-*.md`)
   - Firmware/CVE findings (`outputs/firmware-cve-*.md`)
   - Hardening checklist (`outputs/hardening-checklist-*.md`)
   - Compliance gap analysis (`outputs/compliance-gap-*.md`)
   - Incident response log (if applicable)

2. Generate executive summary:
   - Overall risk rating (Critical/High/Medium/Low)
   - Key findings summary (top 5 issues)
   - Most critical recommended actions
   - Written for: site owner / management (non-technical)

3. Generate technical findings section:
   - All findings with: severity, description, evidence, biological impact, remediation
   - CVSS scores where applicable
   - ATT&CK technique references

4. Generate remediation roadmap:
   - Immediate (within 7 days): Critical findings only
   - Short-term (within 30 days): High findings
   - Medium-term (within 90 days): Medium findings
   - Long-term: Architecture improvements, Low findings
   - Each with: effort estimate, required skills, biological precautions

5. Appendices:
   - Asset inventory
   - Network diagram
   - CVE reference table
   - Compliance gap matrix

6. Save final report to `outputs/security-assessment-report-[date].md`

Reference: All workflows in `context/for-agent/workflows.md`
