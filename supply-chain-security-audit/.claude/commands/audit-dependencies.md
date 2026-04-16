# Audit Dependencies

Conduct a comprehensive dependency audit on the target project.

## Instructions
1. Ask the user to provide the path to dependency manifests (or the project root)
2. Parse all dependency manifests found (package.json, requirements.txt, go.sum, etc.)
3. Build a complete dependency tree including transitive dependencies
4. Cross-reference each dependency against known vulnerability databases
5. Apply the triage severity scoring model (0-10) to each finding
6. Produce a prioritized findings table sorted by severity
7. Identify "comfort measures" — quick mitigations that can be applied immediately
8. Generate an executive summary and detailed technical findings
9. Save results to `outputs/` with timestamp

## Output Format
- Executive summary (2-3 paragraphs)
- Findings table: Component | Version | Severity (0-10) | CVE(s) | Recommended Action
- Quick wins section
- Full technical appendix
