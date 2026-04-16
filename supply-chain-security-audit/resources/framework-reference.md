# Framework Reference Guide

Quick reference for the major supply chain security frameworks and standards.

## NIST SP 800-161r1 — C-SCRM Practices
**Scope**: Cybersecurity Supply Chain Risk Management for Systems and Organizations
**Key Takeaways**:
- Integrate C-SCRM into enterprise risk management
- Establish C-SCRM teams with cross-functional representation
- Assess suppliers before acquisition and continuously after
- Maintain provenance records for all critical components
- Include supply chain scenarios in incident response planning

**Most Relevant Controls**:
- SR-1: Policy and procedures
- SR-2: Supply chain risk management plan
- SR-3: Supply chain controls and processes
- SR-5: Acquisition strategies and tools
- SR-6: Supplier assessments and reviews
- SR-11: Component authenticity

## SLSA — Supply-chain Levels for Software Artifacts
**Scope**: Framework for ensuring the integrity of software artifacts throughout the supply chain
**Levels**:
- Level 1: Provenance exists (build process documented)
- Level 2: Hosted build platform generates provenance (tamper-resistant)
- Level 3: Hardened builds in isolated environments with tamper-evident provenance
**Key Requirements**: Build as code, hermetic builds, provenance generation, verification

## NIST SSDF (SP 800-218)
**Scope**: Secure Software Development Framework
**Practice Groups**:
- Prepare the Organization (PO)
- Protect the Software (PS)
- Produce Well-Secured Software (PW)
- Respond to Vulnerabilities (RV)

## CycloneDX 1.5
**Scope**: OWASP SBOM standard
**Capabilities**: Component inventory, dependency graph, vulnerability data, license info, build metadata
**Formats**: JSON, XML, Protocol Buffers

## SPDX 2.3
**Scope**: Linux Foundation SBOM standard (ISO/IEC 5962:2021)
**Capabilities**: Package identification, relationships, licensing, annotations, file-level detail
**Formats**: JSON, RDF, tag-value, YAML, XML

## OpenSSF Scorecard
**Scope**: Automated security health checks for open source projects
**Key Checks**: Branch protection, CI tests, code review, dependency update tools, fuzzing, license, maintained, pinned dependencies, SAST, security policy, signed releases, token permissions, vulnerabilities
**Scoring**: 0-10 per check, aggregate available
