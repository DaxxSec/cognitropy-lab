# vuln-scan

Perform a structured security audit of a satellite communication protocol or implementation.

When this command is invoked:

1. **Scope the audit** — Ask for:
   - What are we auditing? (A protocol spec, a specific implementation, a ground station system, a cubesat design)
   - What protocol(s) are involved?
   - Is authentication in use? Encryption? Sequence numbering?
   - What is the threat model — who might attack this? (Malicious amateur, nation-state, insider, opportunistic)
   - Is this for a real system or educational/research purposes?

2. **Apply the satellite threat model** — Work through STRIDE for the satellite context (see domain knowledge):
   - Spoofing: Can an attacker forge valid-looking frames?
   - Tampering: Can frames be modified in transit?
   - Repudiation: Can command origin be denied?
   - Information Disclosure: Can telemetry/data be read?
   - Denial of Service: How easy is jamming or flooding?
   - Elevation of Privilege: Can low-privilege commands escalate?

3. **Check protocol-specific vulnerability classes**:
   - **No authentication** → Can anyone send commands? What callsign/ID is trusted?
   - **No encryption** → All data visible to any receiver in range
   - **No anti-replay** → Can a recorded command frame be replayed later?
   - **No frame integrity** → CRC is error detection, not authentication
   - **Weak addressing** → AX.25 callsigns trivially spoofable
   - **No rate limiting** → Uplink flooding attack possible?
   - **Debug interfaces** → Are test modes accessible from the ground?

4. **Produce security findings** in structured format:
   ```
   FINDING: SATCOM-SEC-001
   Title: No Command Authentication on TC Uplink
   Severity: HIGH
   Protocol: CCSDS TC Transfer Frame (without CCSDS 352)
   -------------------------------------------------------
   Description: The TC uplink accepts any valid CCSDS TC frame
   addressed to SCID=0x42 with no authentication. An attacker
   with uplink capability can inject arbitrary commands.

   Attack Scenario:
   1. Attacker obtains SCID from public satellite documentation
   2. Attacker transmits valid TC frame with VCID=0, FSN=0
   3. Frame is accepted and command executed

   Proof of Concept Frame (Python):
   [code to generate example frame]

   Remediation:
   Implement CCSDS Space Data Link Security Protocol (CCSDS 352.0-B-2)
   with AES-256-GCM authentication and replay window of 32 frames.

   References: CCSDS 352.0-B-2; CVE-2024-XXXXX (Viasat incident)
   ```

5. **Severity ratings**:
   - Critical: Remote code execution or full spacecraft control loss
   - High: Unauthorized command execution or mission disruption
   - Medium: Data exfiltration or service degradation
   - Low: Information disclosure of non-sensitive data
   - Informational: Best practice recommendations

6. **Produce remediation roadmap** — Ordered by priority:
   - Quick wins (no hardware change)
   - Short-term (software update)
   - Long-term (design change for next mission)

Note: This analysis is for research, education, and defensive purposes. Do not use findings to interfere with real satellite operations — that is illegal and unethical.
