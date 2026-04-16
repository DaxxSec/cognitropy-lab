# Triage CVE

Score and prioritize a specific CVE in the context of your environment.

## Instructions
1. Ask the user for the CVE ID and any environment context
2. Look up the CVE details (affected component, CVSS score, attack vector)
3. Determine if the affected component exists in the user's dependencies
4. Apply the triage severity model:
   - CVSS base score (40% weight)
   - Exploitability in context (20% — is the attack vector reachable?)
   - Business impact (20% — what would compromise mean?)
   - Vendor trust level (10% — how quickly will the vendor respond?)
   - Mitigation availability (10% — is a patch/workaround available?)
5. Calculate composite triage score (0-10)
6. Recommend response based on score tier
7. Identify available comfort measures if full remediation isn't immediate

## Response Tiers
- 0-2: Routine review, no immediate action
- 3-4: Schedule remediation within 30 days
- 5-6: Prioritize within 14 days, apply comfort measures now
- 7-8: Act within 72 hours, implement all available mitigations
- 9-10: Immediate action required, consider emergency change process
