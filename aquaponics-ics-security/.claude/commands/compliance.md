# /compliance — Compliance Gap Analysis

Assess posture against IEC 62443, NIST SP 800-82, or other applicable standards.

## Steps
1. Identify applicable standard(s):
   - IEC 62443 (target security level: SL-1 through SL-3)?
   - NIST SP 800-82 Rev 3?
   - Customer/regulatory requirement?
   - GDPR (for EU operations with cloud data logging)?

2. Determine target security level (IEC 62443):
   - Based on site size, criticality, and risk tolerance
   - Typical commercial aquaponics: SL-2
   - FDA-regulated seafood production: SL-2 to SL-3

3. For each control domain, assess current posture:
   - Not Implemented / Partially Implemented / Fully Implemented
   - Evidence of implementation (documentation, configuration, testing)
   - Gap description
   - Remediation recommendation

4. Produce compliance gap matrix:
   - Summary dashboard: % implemented by control family
   - Detailed findings table
   - Prioritized remediation roadmap
   - Compensating controls for gaps that cannot be quickly remediated
   - Save to `outputs/compliance-gap-[standard]-[date].md`

5. Executive summary for operators:
   - Plain-language summary of overall security maturity
   - Top 5 most critical gaps
   - Estimated timeline and effort to reach target security level

Reference: `context/for-agent/workflows.md` — Workflow 8
