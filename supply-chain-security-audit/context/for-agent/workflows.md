# Workflows

## Workflow 1: Initial Supply Chain Audit

### Phase 1 — Assessment (Inventory)
1. Collect all dependency manifests from the project
2. Parse direct and transitive dependencies
3. Catalog vendors and upstream sources
4. Map the build pipeline (CI/CD configuration review)
5. Generate baseline SBOM

### Phase 2 — Severity Scoring (Triage)
1. Cross-reference dependencies against vulnerability databases
2. Apply the triage severity model (0-10 scale)
3. Assess business impact for each finding
4. Factor in vendor trust level and mitigation availability
5. Produce prioritized risk register

### Phase 3 — Treatment Plan (Remediation)
1. Group findings by remediation type (update, replace, mitigate, accept)
2. Identify quick wins (comfort measures): version pins, monitoring, signing
3. Develop longer-term remediation roadmap
4. Assign ownership and timelines
5. Document risk acceptance decisions

### Phase 4 — Comfort Measures (Quick Mitigations)
1. Pin all dependency versions in lock files
2. Enable automated vulnerability scanning in CI/CD
3. Configure dependency update automation (Dependabot, Renovate)
4. Implement package provenance checks where supported
5. Add SBOM generation to the release pipeline

### Phase 5 — Ongoing Monitoring
1. Schedule periodic re-assessment (monthly recommended)
2. Configure alerts for new CVEs affecting inventoried components
3. Track SBOM drift between releases
4. Conduct vendor reassessment quarterly
5. Update knowledge base with lessons learned

## Workflow 2: Incident Response — Supply Chain Compromise

1. **Identify**: Determine scope of compromised component usage
2. **Contain**: Pin to last-known-good version, block affected artifacts
3. **Assess**: Determine if compromised code was executed in your environment
4. **Remediate**: Replace component or update to patched version
5. **Report**: Document timeline, impact, and lessons learned
6. **Harden**: Implement preventive controls identified during response

## Workflow 3: Vendor Security Assessment

1. Review vendor's public security practices (security.txt, disclosure policy)
2. Check OpenSSF Scorecard (if open source)
3. Assess build reproducibility and artifact signing
4. Review incident response history and communication track record
5. Evaluate maintenance activity (commit frequency, issue response time)
6. Score against NIST SP 800-161r1 relevant controls
7. Produce vendor risk profile with recommendations
