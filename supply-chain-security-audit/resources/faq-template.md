# FAQ Template

Use this template to generate supply chain security FAQs for different audiences.

## Executive FAQ

**Q: What is a software supply chain attack?**
A: A supply chain attack targets the tools, processes, or components used to build your software rather than the software itself. Think of it like tampering with ingredients at a food processing plant rather than poisoning the finished product — the contamination gets baked into everything the plant produces.

**Q: Why should we care about this now?**
A: Supply chain attacks have increased dramatically. Federal Executive Order 14028 now requires SBOMs (ingredient lists for software) from government contractors. Major incidents like SolarWinds and the xz-utils backdoor showed that even sophisticated organizations are vulnerable.

**Q: What is an SBOM and why do we need one?**
A: A Software Bill of Materials (SBOM) is a complete inventory of every component in your software — like a nutrition label for code. It lets you quickly determine if you're affected when a new vulnerability is disclosed, and it's increasingly required for compliance.

**Q: How do we prioritize what to fix?**
A: We use a triage scoring model (0-10) that considers not just technical severity but business impact, exploitability in your specific environment, and vendor responsiveness. This prevents the "everything is critical" problem that paralyzes many teams.

## Engineering FAQ

**Q: How do I check if my project is affected by a specific CVE?**
A: Run `/triage-cve` with the CVE ID. The agent will check your dependency tree (including transitive dependencies) and score the risk in your specific context.

**Q: What's the difference between CycloneDX and SPDX?**
A: Both are SBOM standards. CycloneDX (by OWASP) is more focused on security use cases and is simpler to generate. SPDX (by Linux Foundation, ISO standard) has deeper license compliance features. For pure security auditing, CycloneDX is usually the better fit. For compliance that includes licensing, consider SPDX.

**Q: What are "comfort measures" in this context?**
A: Quick mitigations you can apply immediately while working on deeper fixes — like pinning dependency versions, enabling automated scanning, or adding integrity checks. They reduce risk now while you plan longer-term remediation.

**Q: How often should we re-audit?**
A: Continuously if possible (automated scanning in CI/CD), with a structured manual review monthly. Vendor reassessment should be quarterly. Any time a major supply chain incident is disclosed, run an immediate triage.

## Compliance FAQ

**Q: Does this meet EO 14028 requirements?**
A: The SBOM generation follows NTIA minimum elements. Combined with the audit process, it addresses the software supply chain security requirements. Specific compliance mapping should be reviewed with your compliance team.

**Q: Can this produce evidence for SOC 2 audits?**
A: Yes. The audit reports, SBOM records, and vendor assessments serve as evidence for the supply chain management controls within SOC 2 Trust Services Criteria.
