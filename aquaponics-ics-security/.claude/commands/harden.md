# /harden — Security Hardening Checklist

Generate device-specific or architecture-level hardening guidance.

## Steps
1. Ask what should be hardened:
   - Specific device type (Raspberry Pi, Arduino, Node-RED, MQTT broker, etc.)?
   - Network architecture?
   - Remote access?
   - Cloud integrations?
   - Full system hardening plan?

2. For device-specific hardening:
   - Provide step-by-step commands/configuration
   - Include verification steps to confirm hardening was applied
   - Note any biological system precautions during implementation

3. For architecture hardening:
   - Generate network segmentation recommendations calibrated to site size
   - Firewall rule recommendations
   - Remote access architecture

4. Generate hardening checklist:
   - Organize by: Critical (must-do immediately), High (within 30 days), Medium (within 90 days), Low (best practice)
   - For each item: description, implementation steps, verification method, biological system precautions
   - Save to `outputs/hardening-checklist-[date].md`

5. Estimate implementation effort:
   - Time estimate per item
   - Required skills (operator self-service vs. IT professional vs. OT specialist)
   - Estimated cost if any tooling/licensing required

Reference: `context/for-agent/workflows.md` — Workflow 7
