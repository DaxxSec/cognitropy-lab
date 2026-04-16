# Domain Knowledge: Supply Chain Security

## Key Attack Patterns

### Dependency Confusion / Substitution
An attacker publishes a malicious package to a public registry with the same name as a private/internal package. Build systems that check public registries first pull the attacker's version. Mitigations: use scoped packages, configure registry priority, implement namespace claiming.

### Typosquatting
Packages with names similar to popular libraries (e.g., `reqeusts` vs `requests`) contain malicious code. Mitigations: lock files, hash verification, organizational policies on new dependency approval.

### Compromised Maintainer Accounts
Attackers gain access to legitimate maintainer accounts (credential stuffing, phishing) and publish poisoned updates. Examples: ua-parser-js, event-stream. Mitigations: MFA enforcement, code review for all releases, reproducible builds.

### Build System Compromise
Attackers inject malicious code into CI/CD pipelines rather than source repositories. The SolarWinds attack used this vector. Mitigations: hermetic builds, build provenance (SLSA), pipeline-as-code with change review.

### Upstream Source Compromise
Malicious commits inserted into legitimate upstream projects. The xz-utils backdoor (CVE-2024-3094) is the canonical example — a multi-year social engineering campaign to become a trusted maintainer. Mitigations: multi-maintainer review requirements, reproducible builds, binary transparency.

### Malicious Installers / Pre-built Binaries
Compromised download infrastructure serves tampered binaries. Mitigations: signature verification, checksum validation from multiple sources, build from source when critical.

## Framework Quick Reference

### SLSA Levels
- **Level 0**: No guarantees
- **Level 1**: Documentation of the build process, provenance exists
- **Level 2**: Tamper resistance of the build service, hosted build platform generates provenance
- **Level 3**: Hardened builds, builds run in isolated environments with tamper-evident provenance

### NIST SP 800-161r1 Key Controls
- **C-SCRM Plans**: Documented supply chain risk management strategy
- **Supplier Assessment**: Due diligence on suppliers before acquisition
- **Provenance Tracking**: Ability to trace components to their sources
- **Vulnerability Management**: Process for handling supplier-disclosed vulnerabilities
- **Incident Response**: Supply chain-specific IR procedures

### SBOM Minimum Elements (NTIA)
- Supplier name
- Component name
- Component version
- Unique identifier (e.g., CPE, PURL)
- Dependency relationships
- Author of the SBOM
- Timestamp

## Severity Scoring Model (Triage Scale)

Adapted from the palliative care 0-10 symptom scale:

| Score | Label | Description | Response Time |
|-------|-------|-------------|---------------|
| 0 | None | No identified risk | Routine review |
| 1-2 | Minimal | Low-severity, no known exploits, limited exposure | Next scheduled cycle |
| 3-4 | Mild | Known CVE but low exploitability or limited blast radius | Within 30 days |
| 5-6 | Moderate | Exploitable vulnerability with meaningful impact potential | Within 14 days |
| 7-8 | Severe | Actively exploited or high-impact with clear attack path | Within 72 hours |
| 9-10 | Critical | Active exploitation in the wild, direct path to compromise | Immediate action required |

Scores combine: CVSS base score (40%), exploitability context (20%), business impact (20%), vendor trust level (10%), mitigation availability (10%).
