# Aquaponics ICS/OT Security

### Cybersecurity for Smart Agriculture Control Systems

**The Cognitropy Lab — Day 3 Workspace (Variant B)**

> *"The aquaponics industry discovered automation before it discovered security. Today, thousands of fish farms run PLCs with default passwords, Modbus TCP on flat networks, and SCADA dashboards exposed to the internet via Shodan. The next fish kill might not be pH. It might be a port scan."*

---

## What This Is

A full AI agent workspace for securing the **automation and control infrastructure** of aquaponics and smart agriculture systems. This is the security-focused companion to the [Aquaponics Anomaly Monitor](../aquaponics-anomaly-monitor) workspace — where that workspace focuses on detecting biological anomalies, this one focuses on detecting and remediating **cybersecurity threats** to the control systems themselves.

Modern aquaponics automation is built on PLCs, Raspberry Pi controllers, MQTT brokers, SCADA dashboards, and cloud-connected monitoring platforms. Most of this infrastructure was designed by aquaculture engineers with no cybersecurity background. Default passwords persist. Networks are flat. Ports are forwarded directly to PLCs.

This workspace gives you the analytical framework to assess, harden, and respond to threats against your aquaponics automation stack — without killing your fish in the process.

---

## Who This Is For

- Aquaponics operators who want to harden their automation infrastructure
- OT/ICS security consultants performing smart agriculture assessments
- IT staff taking ownership of OT systems at commercial aquaponics facilities
- Researchers studying smart agriculture cybersecurity
- Digital forensics investigators responding to compromised food production systems
- Anyone who has Googled "my Modbus port is open on Shodan" at 11 PM

---

## Why This Matters

In 2023, CISA issued an alert about active exploitation of Unitronics PLCs at water/wastewater facilities — the same PLCs used in thousands of commercial aquaponics operations. The default password "1111" was all that stood between attackers and direct control of pumps, feeders, and environmental systems.

A compromised aquaponics control system can:
- Kill 10,000+ fish within hours (pump shutdown, hypoxia)
- Destroy months of crop production (lighting/feeding schedule tampering)
- Disrupt food supply chains (commercial operations)
- Expose proprietary cultivation data (genetics, techniques, yields)
- Result in regulatory violations (FDA traceability, food safety records)

The biological system and the cyber system are inseparable. You cannot secure one without the other.

---

## Getting Started

### Quick Assessment (New to This?)
1. Run `/onboard` — describe your system, get a risk profile in minutes
2. Run `/asset-inventory` — catalog everything connected to your automation network
3. Run `/threat-model` — identify your realistic attack scenarios
4. Run `/harden` — get specific hardening steps for your platform

### Existing Incident?
Go straight to `/incident-response` — the workflow prioritizes biological system safety first.

### Compliance Requirement?
Run `/compliance` after completing the inventory and network audit.

---

## Workspace Structure

```
aquaponics-ics-security/
├── CLAUDE.md                          # Agent role + command reference
├── README.md                          # This file
├── context/
│   ├── project.md                     # Engagement types and scope
│   ├── role.md                        # Agent expertise definition
│   ├── constraints.md                 # Hard rules and limitations
│   └── for-agent/
│       ├── environment.md             # Tools, protocols, zone taxonomy
│       └── workflows.md               # 8 detailed security workflows
├── .claude/commands/
│   ├── onboard.md                     # Site initialization
│   ├── asset-inventory.md             # OT/IoT asset enumeration
│   ├── threat-model.md                # STRIDE + ATT&CK threat modeling
│   ├── network-audit.md               # Segmentation gap analysis
│   ├── firmware-check.md              # CVE correlation + firmware analysis
│   ├── incident-response.md           # ICS-specific IR playbook
│   ├── harden.md                      # Platform hardening generation
│   ├── compliance.md                  # IEC 62443 / NIST 800-82 gap analysis
│   └── report.md                      # Full assessment report generation
├── prompts/
│   ├── shodan-exposure-check.md       # Analyze Shodan results
│   ├── modbus-traffic-analysis.md     # Forensic Modbus traffic review
│   └── ics-risk-register.md          # Generate structured risk register
├── resources/
│   ├── ics-cve-watchlist.md          # Known CVEs for aquaponics platforms
│   ├── ot-network-design-guide.md    # Network segmentation patterns
│   └── incident-response-quick-reference.md  # IR decision matrix + checklists
├── work-log/                          # Assessment journals, evidence logs
├── planning/                          # Engagement scopes, site profiles
├── user-docs/                         # Operator-facing guides
└── outputs/                           # Reports, findings, checklists
```

---

## Command Reference

| Command | Purpose | When to Use |
|---------|---------|-------------|
| `/onboard` | Initialize for a specific site | First step for any new engagement |
| `/asset-inventory` | Enumerate and classify OT/IoT assets | After onboarding |
| `/threat-model` | Build STRIDE + ATT&CK threat model | After inventory |
| `/network-audit` | Audit OT network segmentation | After inventory |
| `/firmware-check` | CVE correlation + firmware analysis | After inventory |
| `/incident-response` | Activate ICS IR playbook | When compromise suspected |
| `/harden` | Generate hardening checklist | After assessment, or standalone |
| `/compliance` | IEC 62443 / NIST 800-82 gap analysis | When compliance required |
| `/report` | Compile full assessment report | After all assessment workflows complete |

---

## Workflows Summary

### Workflow 1: Site Onboarding
Profile the biological system alongside the technical infrastructure. Establish scope and identify top risk areas.

### Workflow 2: Asset Inventory
Enumerate all OT/IoT devices using passive discovery, physical walkthrough, and authorized active enumeration. Zone-classify each asset using the Purdue Model.

### Workflow 3: Threat Modeling
Apply STRIDE methodology to identify attack scenarios. Map to MITRE ATT&CK for ICS. Profile threat actors relevant to smart agriculture.

### Workflow 4: Network Segmentation Audit
Verify IT/OT separation, identify internet-exposed systems, review remote access architecture, assess wireless security.

### Workflow 5: Firmware & CVE Assessment
Correlate device firmware versions against NVD and CISA ICS-CERT advisories. Analyze firmware binaries when available.

### Workflow 6: ICS Incident Response
Structured 4-phase response (Contain → Investigate → Preserve → Restore) with biological safety checkpoints at each stage.

### Workflow 7: Hardening Checklist
Platform-specific hardening guidance for Raspberry Pi, Node-RED, MQTT brokers, SCADA systems, and network architecture.

### Workflow 8: Compliance Gap Analysis
Map posture against IEC 62443 security levels and NIST SP 800-82 Rev 3 control families.

---

## Key Resources Included

- **ICS CVE Watchlist**: Known vulnerabilities for common aquaponics platforms including the actively-exploited Unitronics CVE-2023-6448
- **OT Network Design Guide**: Purdue Model templates scaled from hobby systems to FDA-regulated commercial operations
- **Incident Response Quick Reference**: Decision matrix, evidence collection checklists, CISA reporting contacts

---

## Frameworks Referenced

- **IEC 62443** — Industrial cybersecurity standard (security levels 1-4)
- **NIST SP 800-82 Rev 3** — Guide to OT security
- **MITRE ATT&CK for ICS** — Adversary techniques in industrial control systems
- **NIST Cybersecurity Framework (CSF) 2.0** — Identify, Protect, Detect, Respond, Recover
- **Purdue Enterprise Reference Architecture** — OT network zone model

---

## Relationship to Other Workspaces

| Workspace | Focus | When to Use |
|-----------|-------|-------------|
| [aquaponics-anomaly-monitor](../aquaponics-anomaly-monitor) | Water chemistry & biological anomaly detection | Daily operations monitoring |
| **aquaponics-ics-security** (this one) | Control system cybersecurity | Periodic security assessments, incidents |

These workspaces are designed to complement each other. The anomaly monitor alerts you when your fish are stressed; this workspace alerts you when your control system is under attack.

---

## Disclaimer

This workspace is for authorized security assessment of systems you own or have explicit written permission to test. The agent will not assist with unauthorized access to systems. All active testing guidance includes explicit requirements for written authorization and maintenance windows.

---

*Built by The Cognitropy Lab — where an AI takes on a new creative challenge every day.*
*Domain: Aquaponics (variant: ICS/OT Security) | Technique: Automated Anomaly Detection applied to Cyber Threats*
