# Supply Chain Threat Catalog

A curated reference of known supply chain attack patterns, notable incidents, and defensive strategies.

## Attack Pattern Index

### 1. Dependency Confusion
- **Description**: Exploiting package manager resolution order to substitute malicious public packages for private ones
- **Notable Incidents**: Alex Birsan's 2021 research affecting Apple, Microsoft, PayPal
- **Detection**: Monitor for unexpected package sources in build logs; compare resolved packages against internal registry
- **Prevention**: Scoped namespaces, registry priority configuration, package source pinning

### 2. Typosquatting
- **Description**: Publishing packages with names similar to popular libraries
- **Notable Incidents**: crossenv (npm, 2017), python3-dateutil (PyPI, 2019)
- **Detection**: New dependency review process, name similarity checks
- **Prevention**: Lock files with integrity hashes, organizational approval for new dependencies

### 3. Maintainer Account Compromise
- **Description**: Gaining access to legitimate maintainer accounts to push malicious updates
- **Notable Incidents**: event-stream (npm, 2018), ua-parser-js (npm, 2021), colors.js (npm, 2022)
- **Detection**: Behavioral analysis of package updates, code review for dependency updates
- **Prevention**: MFA enforcement on registries, multi-maintainer signing requirements

### 4. Build System Injection
- **Description**: Injecting malicious code during the build process rather than in source code
- **Notable Incidents**: SolarWinds SUNBURST (2020), Codecov (2021)
- **Detection**: Build reproducibility checks, provenance verification
- **Prevention**: Hermetic builds, SLSA compliance, build provenance attestation

### 5. Upstream Source Compromise
- **Description**: Long-term social engineering to become a trusted contributor, then inserting backdoors
- **Notable Incidents**: xz-utils (CVE-2024-3094, 2024)
- **Detection**: Multi-person code review, automated behavioral analysis of commits
- **Prevention**: Contributor trust models, reproducible builds, binary transparency logs

### 6. Protestware / Self-Sabotage
- **Description**: Maintainers intentionally breaking their own packages for political or personal reasons
- **Notable Incidents**: colors.js and faker.js (2022), node-ipc (2022)
- **Detection**: Automated testing of dependency updates, behavioral change detection
- **Prevention**: Version pinning, fork maintenance capability, dependency diversity

### 7. Installer/Binary Tampering
- **Description**: Compromising download infrastructure to serve modified binaries
- **Notable Incidents**: Linux Mint website hack (2016), Handbrake (2017), ASUS Live Update (2019)
- **Detection**: Checksum verification from multiple independent sources
- **Prevention**: Code signing verification, reproducible builds, download from authenticated channels

## Emerging Threats
- **AI-generated malicious packages**: Using LLMs to generate plausible-looking malicious code at scale
- **CI/CD credential harvesting**: Targeting pipeline secrets through malicious PR contributions
- **Container base image poisoning**: Compromising popular base images on public registries
- **IaC module supply chain**: Malicious Terraform modules or Helm charts with hidden resources
