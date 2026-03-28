# Project Context — Aquaponics ICS Security Workspace

## Purpose
This workspace supports security assessments, hardening engagements, and incident response for aquaponics and smart agriculture control systems. It is the second aquaponics workspace in the Cognitropy Lab — the first (`aquaponics-anomaly-monitor`) focuses on biological anomaly detection; this one focuses on the **cybersecurity of the automation infrastructure itself**.

## Scope
- Control system architecture review
- Asset inventory and classification (Purdue Model zones)
- Threat modeling for aquaponics OT environments
- Vulnerability assessment of IoT/OT devices
- Network segmentation and firewall policy review
- Firmware analysis and CVE correlation
- Incident response playbooks for ICS-specific scenarios
- Compliance gap analysis (IEC 62443, NIST 800-82, GDPR data considerations)

## Typical Engagement Types

### Security Assessment (New System)
Design review before deployment. Identify security gaps in proposed architecture, recommend segmentation, hardening standards, and monitoring tools before fish hit the water.

### Security Assessment (Existing System)
Passive audit of a live system. Asset enumeration, network capture analysis, configuration review. Minimal active scanning to protect operational availability.

### Incident Response
Active compromise of a control system. Follow the ICS-IR playbook: contain without killing the fish, preserve evidence, eradicate, restore operations.

### Compliance Review
Gap analysis against a specific standard (IEC 62443-2-1, NIST 800-82, or customer-specific requirements). Produce findings with severity, remediation, and compensating controls.

## Assets in Scope (Typical)
- PLCs: Allen-Bradley MicroLogix, Siemens S7-1200, Click PLCs, Unitronics Vision
- HMIs: Weintek, Proface, web-based SCADA (Ignition, InduSoft)
- IoT Sensors: Atlas Scientific EZO circuits, Raspberry Pi controllers, Arduino Mega
- Network: Managed switches, Wi-Fi APs, cellular gateways, VPN concentrators
- Cloud Platforms: Blynk, GroPal, custom MQTT brokers, InfluxDB/Grafana stacks
- COTS Software: Node-RED, Home Assistant, custom Python scripts

## Deliverables
- Asset inventory spreadsheet (zone-classified)
- Threat model document
- Vulnerability findings report (CVSS-scored)
- Network diagram with security annotations
- Remediation roadmap (prioritized by risk)
- Hardening checklists per device class
- Incident response plan (customized to site biology)
