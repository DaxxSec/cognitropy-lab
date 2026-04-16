# Tools

## Built-in Capabilities
- **Dependency Manifest Parsing**: Read and analyze package.json, requirements.txt, Pipfile.lock, Cargo.toml, go.sum, pom.xml, .csproj, and similar manifests
- **SBOM Generation**: Create CycloneDX and SPDX formatted SBOMs from parsed manifests
- **CVE Lookup**: Search NVD and advisory databases for known vulnerabilities
- **Risk Scoring**: Apply the triage severity model to findings
- **Report Generation**: Produce structured reports in Markdown, JSON, or tabular formats
- **Knowledge Base Management**: Maintain and search the workspace threat catalog and FAQ

## Slash Commands
- `/audit-dependencies` — Scan a project's dependency manifests, identify risks, and produce a prioritized finding list
- `/vendor-assessment` — Evaluate a vendor or open-source project's security posture
- `/generate-sbom` — Produce a standards-compliant SBOM from project manifests
- `/triage-cve` — Score and prioritize a specific CVE in the context of your environment
- `/onboard` — Get oriented with workspace capabilities and methodology

## Integration Points
- CI/CD pipeline integration via generated scripts and configuration snippets
- Policy-as-code output compatible with OPA/Rego for automated enforcement
- SARIF output for integration with GitHub Code Scanning / Azure DevOps
