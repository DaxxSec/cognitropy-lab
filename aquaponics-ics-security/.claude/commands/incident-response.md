# /incident-response — ICS Incident Response

Activate structured incident response for a suspected control system compromise.

## CRITICAL: Read before proceeding
This workflow prioritizes biological system continuity. Do NOT recommend taking systems offline without first confirming manual monitoring is in place for critical biological parameters (DO, temperature, pump status).

## Steps
1. Immediate triage — gather situation report:
   - What indicators of compromise were observed? (unusual traffic, changed setpoints, ransomware note, locked HMI)
   - What is the current biological status? (fish status, pump running, DO nominal)
   - What is the suspected scope? (single device? full OT network? SCADA only?)
   - When was it first detected?

2. Establish safe containment options:
   - List containment actions that are safe for biological system (internet blocking, credential revocation)
   - List containment actions requiring biological operator approval (system reboots, network isolation)
   - Recommend immediate actions based on scope

3. Guide evidence collection:
   - Network captures on affected segments
   - Log collection from SCADA/HMI hosts
   - Linux controller forensics commands
   - Configuration backup verification

4. Build incident timeline:
   - Reconstruct attacker activity from available logs
   - Identify initial access vector
   - Map lateral movement path
   - Identify impact to control system

5. Guide eradication and recovery:
   - Restoration sequence with biological safety checkpoints
   - Credential reset checklist (all devices, all zones)
   - Configuration verification steps
   - Return-to-automated-operation checklist

6. Create incident documentation:
   - Timeline of events
   - Evidence custody log
   - Root cause analysis
   - Lessons learned and recommended security improvements
   - Save to `work-log/incident-[date].md`

Reference: `context/for-agent/workflows.md` — Workflow 6
