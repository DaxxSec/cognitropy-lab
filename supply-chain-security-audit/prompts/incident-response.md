# Supply Chain Incident Response

Use this prompt when a supply chain compromise has been disclosed and you need to assess your exposure.

## Prompt

A supply chain compromise has been disclosed:

- **Affected component**: [package name and version range]
- **CVE/Advisory**: [CVE ID or advisory URL]
- **Attack vector**: [compromised maintainer / dependency confusion / build system / etc.]
- **Disclosure date**: [date]

I need to:
1. Determine if we're using the affected component (directly or transitively)
2. Assess whether the malicious code path was reachable in our environment
3. Identify the blast radius if we were affected
4. Get immediate containment recommendations (comfort measures)
5. Develop a full remediation plan
6. Draft an incident timeline for our records

Please prioritize speed — start with containment, then assess scope.
