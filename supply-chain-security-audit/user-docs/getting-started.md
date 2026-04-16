# Getting Started with Supply Chain Security Audit

## Quick Start (5 minutes)
1. Open this workspace in Claude Code
2. Run `/onboard` to understand the methodology and capabilities
3. Point the agent at your project: share dependency manifest paths or the project root
4. Run `/audit-dependencies` for a full assessment
5. Review the prioritized findings — start with items scored 7+

## Your First Audit
The fastest path to value is scanning an existing project:
1. Provide your `package.json`, `requirements.txt`, `go.sum`, or equivalent
2. The agent will inventory all dependencies (including transitive ones)
3. Each finding gets a triage score from 0 (no risk) to 10 (critical, act now)
4. You'll get both an executive summary and detailed technical findings
5. "Comfort measures" are highlighted — these are quick wins you can apply today

## Ongoing Use
After the initial audit, use this workspace for:
- Triaging new CVE disclosures with `/triage-cve`
- Assessing new vendors or open-source dependencies with `/vendor-assessment`
- Generating SBOMs for compliance with `/generate-sbom`
- Responding to supply chain incidents using the incident response prompt
- Building your organization's supply chain security knowledge base

## Customization
- Add your organization's specific vendors to `resources/` for faster assessments
- Customize the triage scoring weights in `context/for-agent/domain-knowledge.md`
- Add your compliance requirements to `context/project.md`
- Create additional slash commands for your specific workflows
