# /threat-model — Threat Modeling

Build a structured threat model for the aquaponics control system environment.

## Steps
1. Confirm asset inventory exists or gather minimal system description
2. Build threat actor profile table relevant to this specific site:
   - Consider site size, internet exposure, public profile, competitor landscape
   - Assign likelihood ratings based on site specifics

3. Enumerate attack surface by zone (Zone 5 → Zone 0 attack paths):
   - List all internet-entry points
   - Map IT-to-OT pivot paths
   - Identify within-OT lateral movement opportunities

4. Apply STRIDE methodology to critical systems:
   - For each critical asset: identify applicable threat categories
   - Provide concrete attack scenario for each STRIDE category that applies
   - Include biological impact in the scenario description

5. Map findings to MITRE ATT&CK for ICS:
   - Identify the top 5-8 most relevant techniques
   - For each: provide technique ID, name, and how it applies to this specific environment

6. Produce threat model document:
   - Executive summary (operator-language)
   - Threat actor profiles
   - Attack surface analysis
   - STRIDE scenarios with impact
   - ATT&CK technique mapping
   - Priority remediation focus areas
   - Save to `outputs/threat-model.md`

Reference: `context/for-agent/workflows.md` — Workflow 3
