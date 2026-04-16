# Supply Chain Security Audit Workspace

An AI-powered agent workspace for conducting comprehensive software and hardware supply chain security audits. This workspace applies a novel **triage methodology** — borrowing systematic assessment techniques from palliative care symptom management — to bring structure and prioritization to the complex problem of supply chain risk.

## Why This Workspace?

Software supply chain attacks have exploded in frequency and impact — from SolarWinds to the xz-utils backdoor, attackers are targeting the build pipeline and dependency graph rather than the application itself. Most organizations lack a systematic, repeatable audit process for their supply chains. This workspace provides one.

## The Triage Methodology

Traditional supply chain audits produce massive spreadsheets of CVEs with little prioritization. This workspace applies the **Assess → Score → Treat → Comfort → Monitor** cycle borrowed from palliative care:

| Phase | Supply Chain Equivalent | Output |
|-------|------------------------|--------|
| Assessment | Dependency inventory, vendor catalog, build process map | SBOM, vendor matrix |
| Severity Scoring | Risk score combining CVSS, exploitability, business impact, vendor trust | Prioritized risk register |
| Treatment Plan | Targeted remediations ranked by urgency and feasibility | Action plan with owners |
| Comfort Measures | Quick mitigations while deeper fixes are in progress | Pin versions, enable signing, add monitoring |
| Ongoing Monitoring | Scheduled reassessment, new CVE triage, vendor check-ins | Living dashboard |

## Key Features

### Software Composition Analysis
- Parse dependency manifests across ecosystems (npm, PyPI, crates.io, Go modules, Maven, NuGet)
- Identify transitive dependencies and their risk profiles
- Cross-reference against NIST NVD, GitHub Advisory Database, and OSV

### SBOM Generation & Management
- Generate SBOMs in CycloneDX 1.5 and SPDX 2.3 formats
- Merge SBOMs from multiple build stages into a unified bill of materials
- Track SBOM drift across releases

### Vendor Security Assessment
- Evaluate vendors against NIST SP 800-161r1 criteria
- Score vendor maturity on SLSA levels (1-4)
- Assess code signing practices, build reproducibility, and incident response history

### CI/CD Pipeline Integrity
- Audit build pipeline configurations for injection risks
- Check for pinned actions/images vs. mutable tags
- Verify artifact signing and provenance attestation (Sigstore/in-toto)

### Knowledge Base & FAQ System
- Auto-generate FAQs for different audiences (executive, engineering, compliance)
- Maintain a living knowledge base of threats, patterns, and mitigations
- Searchable reference library with curated supply chain security resources

## Directory Structure

```
supply-chain-security-audit/
├── CLAUDE.md                          # Agent instructions and personality
├── README.md                          # This file
├── CREATION_REPORT.md                 # Build rationale and methodology
├── .claude/commands/                  # Slash commands
│   ├── audit-dependencies.md          # /audit-dependencies — full SCA scan
│   ├── vendor-assessment.md           # /vendor-assessment — evaluate a vendor
│   ├── generate-sbom.md               # /generate-sbom — produce SBOM output
│   ├── triage-cve.md                  # /triage-cve — score and prioritize a CVE
│   └── onboard.md                     # /onboard — workspace orientation
├── context/
│   ├── role.md                        # Agent role definition
│   ├── project.md                     # Project scope and goals
│   ├── constraints.md                 # Operating constraints
│   └── for-agent/
│       ├── domain-knowledge.md        # Supply chain security knowledge base
│       ├── environment.md             # Runtime environment details
│       ├── tools.md                   # Available tools and integrations
│       └── workflows.md              # Standard operating procedures
├── prompts/
│   ├── initial-audit.md               # First-time audit kickoff prompt
│   ├── incident-response.md           # Supply chain incident response prompt
│   └── executive-briefing.md          # Generate exec-level summary
├── planning/
│   └── audit-plan-template.md         # Reusable audit plan structure
├── resources/
│   ├── threat-catalog.md              # Known supply chain attack patterns
│   ├── framework-reference.md         # NIST, SLSA, SSDF reference guide
│   └── faq-template.md               # FAQ generation template
├── outputs/                           # Generated audit artifacts
├── user-docs/
│   ├── getting-started.md             # Quick start guide
│   └── report.md                      # Report template
└── work-log/
    └── session-log.md                 # Audit session history
```

## Getting Started

1. Clone this workspace into your Claude Code project
2. Run `/onboard` to get oriented with the workspace capabilities
3. Point the agent at a project's dependency manifests with `/audit-dependencies`
4. Review the triage output and prioritized findings
5. Generate an SBOM with `/generate-sbom` for compliance or sharing

## Frameworks Referenced

- **NIST SP 800-161r1** — Cybersecurity Supply Chain Risk Management Practices
- **SLSA (Supply-chain Levels for Software Artifacts)** — Build integrity framework
- **NIST SSDF (SP 800-218)** — Secure Software Development Framework
- **CycloneDX 1.5** — SBOM standard by OWASP
- **SPDX 2.3** — SBOM standard by Linux Foundation
- **CISA SBOM Guidance** — Minimum elements for SBOMs
- **OpenSSF Scorecard** — Automated security health checks for open source

## Ideal Users

- Security engineers conducting supply chain audits
- DevSecOps teams hardening CI/CD pipelines
- Compliance teams preparing for FedRAMP, SOC 2, or executive orders (EO 14028)
- Engineering managers assessing open-source dependency risk
- CISOs needing executive-level supply chain risk summaries

## Crossover Note

This workspace was built as a **Cognitropy crossover** between Cyber & DFIR and Medical & Health. The palliative care symptom management model (assess severity, prioritize treatment, provide comfort measures, monitor continuously) maps remarkably well to supply chain security, where the volume of findings can overwhelm teams without a systematic triage process. The "comfort measures" concept — quick mitigations that reduce risk while proper fixes are developed — is particularly valuable in supply chain contexts where full remediation often requires vendor cooperation and extended timelines.
