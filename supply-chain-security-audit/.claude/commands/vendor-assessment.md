# Vendor Assessment

Evaluate a software vendor or open-source project's supply chain security posture.

## Instructions
1. Ask the user for the vendor/project name and any context (criticality, usage scope)
2. Research the vendor's public security practices
3. Check for: security.txt, vulnerability disclosure policy, incident response history
4. If open source: check OpenSSF Scorecard, maintenance activity, contributor diversity
5. Assess build practices: artifact signing, reproducible builds, SLSA level
6. Score against relevant NIST SP 800-161r1 controls
7. Produce a vendor risk profile with overall trust score (0-10)
8. Include specific recommendations for risk reduction

## Output Format
- Vendor Profile Summary
- Trust Score: X/10 with breakdown
- Strengths and Concerns
- Recommendations (prioritized)
- Comparison to industry benchmarks (if applicable)
