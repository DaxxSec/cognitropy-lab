# Protocol Security Audit

Use this prompt when you need a comprehensive security audit of a satellite communication protocol or system design, going deeper than the `/vuln-scan` command.

---

**Prompt:**

Perform a comprehensive security audit of the following satellite communication system: [DESCRIBE YOUR SYSTEM]

Protocol(s) in use: [LIST PROTOCOLS]
Authentication mechanism: [DESCRIBE OR "NONE"]
Encryption: [DESCRIBE OR "NONE"]
Orbital regime: [LEO/MEO/GEO]
Mission criticality: [COMMERCIAL/AMATEUR/RESEARCH/CRITICAL INFRASTRUCTURE]

Please structure your audit as follows:

**1. System Architecture Review**
Map the full communication chain from ground station → RF → satellite and identify all trust boundaries and interfaces.

**2. Attack Surface Enumeration**
List all interfaces and channels that an adversary could interact with, including:
- RF uplink/downlink channels
- Ground station networks
- Protocol parser inputs
- Physical access points

**3. Threat Actor Analysis**
For each realistic threat actor (opportunistic, motivated hobbyist, organized, nation-state), assess:
- Capability required to exploit
- Motivation and intent
- Likely attack vectors

**4. Vulnerability Findings**
For each finding, provide: Finding ID, title, severity (Critical/High/Medium/Low/Info), detailed description, step-by-step attack scenario, proof-of-concept frame or code, remediation recommendation, and relevant standards reference.

**5. Protocol Implementation Review**
Specifically assess:
- Frame parsing for length-based attacks, off-by-one errors
- State machine for invalid state transitions
- Authentication bypass possibilities
- Rate limiting and resource exhaustion

**6. Comparison to Standards**
How does the current design compare to CCSDS 352.0-B-2 security recommendations? What is the gap?

**7. Risk Matrix**
Present all findings in a risk matrix (Likelihood × Impact).

**8. Prioritized Remediation Roadmap**
Quick wins, short-term, and long-term recommendations with estimated implementation effort.

This audit is for defensive research and system improvement purposes only.
