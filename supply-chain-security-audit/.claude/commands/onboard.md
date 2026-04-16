# Onboard

Welcome to the Supply Chain Security Audit workspace.

## Introduction
This workspace helps you conduct systematic supply chain security audits using a triage methodology inspired by palliative care symptom management. Instead of drowning in CVE lists, we assess, score, prioritize, and treat — with "comfort measures" for quick wins while deeper fixes are developed.

## Available Commands
- `/audit-dependencies` — Scan a project's dependencies and produce prioritized findings
- `/vendor-assessment` — Evaluate a vendor or open-source project's security posture
- `/generate-sbom` — Create a standards-compliant Software Bill of Materials
- `/triage-cve` — Score and contextualize a specific CVE for your environment

## Getting Started
1. Share a project's dependency manifests (or point to a project directory)
2. Run `/audit-dependencies` for a full assessment
3. Review the prioritized findings and quick wins
4. Use `/triage-cve` for deep-dives on specific vulnerabilities
5. Generate an SBOM with `/generate-sbom` for compliance needs

## Key Concepts
- **Triage Score (0-10)**: Every finding gets a composite severity score combining technical and business factors
- **Comfort Measures**: Quick mitigations you can apply while waiting for full remediation
- **Living Audit**: This isn't a point-in-time report — the workspace supports ongoing monitoring and reassessment

## Resources
Check `resources/` for the threat catalog, framework reference guide, and FAQ templates.
