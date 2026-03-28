# /network-audit — OT Network Segmentation Audit

Assess network segmentation, firewall posture, and lateral movement paths.

## Steps
1. Request available network information:
   - Network diagrams (even hand-drawn)
   - Firewall/ACL rule exports
   - VLAN configuration
   - Wireless network details
   - Remote access configuration

2. Reconstruct network topology:
   - Draw zone map using Purdue Model
   - Identify cross-zone communication paths
   - Flag any flat/un-segmented areas

3. Assess segmentation gaps:
   - Can IT reach Control directly?
   - Are any OT devices internet-facing?
   - Are wireless APs in OT zones?
   - Are there unauthorized cross-zone connections?

4. Review remote access:
   - All remote access paths documented?
   - MFA enforced on all remote access?
   - Vendor access time-limited and audited?
   - Any stale/unauthorized access credentials?

5. Generate findings:
   - Classify each gap by severity (Critical/High/Medium/Low)
   - For each finding: describe the gap, attack scenario, biological impact, and remediation
   - Generate network diagram annotations showing risk areas
   - Save to `outputs/network-audit-[date].md`

6. Provide prioritized remediation roadmap:
   - Quick wins (firewall rule changes, disabling services)
   - Medium-term (VLAN implementation, MFA rollout)
   - Long-term (architecture redesign if needed)

Reference: `context/for-agent/workflows.md` — Workflow 4
