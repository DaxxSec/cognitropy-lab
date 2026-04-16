# Environment

## Runtime
This workspace operates within Claude Code or similar AI-assisted development environments. The agent has access to:
- File system (read/write within workspace directory)
- Shell commands for running analysis tools
- Web search for CVE lookups and advisory research

## Recommended External Tools (when available)
- `syft` — SBOM generation from container images and source trees
- `grype` — Vulnerability scanner for container images and SBOMs
- `trivy` — Comprehensive security scanner (dependencies, IaC, containers)
- `npm audit` / `pip-audit` / `cargo audit` — Ecosystem-specific auditors
- `cosign` — Container/artifact signing verification (Sigstore)
- `slsa-verifier` — SLSA provenance verification
- `scorecard` — OpenSSF Scorecard for open source project health

## Data Sources
- NIST National Vulnerability Database (NVD)
- GitHub Advisory Database (GHSA)
- OSV (Open Source Vulnerabilities)
- deps.dev — Open source dependency insights
- Snyk Vulnerability Database
- Package registry APIs (npm, PyPI, crates.io, etc.)

## Output Formats
- Markdown reports (default for human consumption)
- JSON (for machine-readable findings, SBOMs)
- CycloneDX XML/JSON (SBOM format)
- SPDX JSON/tag-value (SBOM format)
