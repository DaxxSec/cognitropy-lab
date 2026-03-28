# Prompt: ICS Risk Register Generation

Use this prompt to generate a structured risk register for an aquaponics control system.

---

**Prompt:**

Based on the following aquaponics site profile, generate a comprehensive ICS risk register:

**Site Profile:**
- System type: [NFT/DWC/media bed/hybrid]
- Scale: [volume, stocking density]
- Automation level: [describe]
- Internet-connected components: [list]
- Known security controls in place: [list or "none identified"]
- Regulatory environment: [FDA registered? local food safety requirements?]

For each risk, provide:
1. **Risk ID**: Unique identifier (e.g., AQ-RISK-001)
2. **Risk Description**: Clear statement of the risk
3. **Threat Source**: Who/what could cause this
4. **Vulnerability**: What weakness enables this risk
5. **Biological Impact**: Specific impact to fish/crops/operations
6. **Security Impact**: CIA impact (Confidentiality/Integrity/Availability)
7. **Likelihood**: 1-5 scale with justification
8. **Impact**: 1-5 scale with justification
9. **Risk Score**: Likelihood × Impact
10. **Current Controls**: Any existing mitigations
11. **Recommended Controls**: What should be added
12. **Residual Risk**: Risk score after recommended controls
13. **Priority**: Critical/High/Medium/Low

Sort the register by risk score descending. Include at minimum: physical access risks, network-based attack risks, insider threat risks, supply chain risks, and environmental/accidental risks.
