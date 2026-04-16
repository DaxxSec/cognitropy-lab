# Initial Supply Chain Audit

Use this prompt to kick off a first-time supply chain security audit for a project.

## Prompt

I need to conduct a supply chain security audit on my project. Here's what I have:

- **Project type**: [web app / API / library / container image / infrastructure]
- **Primary language(s)**: [e.g., JavaScript/TypeScript, Python, Go, Rust]
- **Package managers**: [e.g., npm, pip, cargo, go modules]
- **CI/CD platform**: [e.g., GitHub Actions, GitLab CI, Jenkins]
- **Compliance requirements**: [e.g., FedRAMP, SOC 2, EO 14028, none specific]

Please conduct a full audit using the triage methodology:
1. Inventory all dependencies (direct and transitive)
2. Score each finding on the 0-10 triage scale
3. Identify quick wins (comfort measures)
4. Produce a prioritized remediation plan
5. Generate an SBOM

I'd like both an executive summary and detailed technical findings.
