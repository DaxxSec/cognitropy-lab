# Environment Setup

## Toolchain Expectations

### Network Analysis Tools (Host-Side)
When working with captured network data, the following tools are commonly available:
- **Wireshark/tshark**: Modbus, DNP3, EtherNet/IP dissectors available
- **Nmap**: Service fingerprinting of OT devices (use with caution, low-and-slow only)
- **Shodan CLI**: Internet exposure enumeration for cloud-facing components
- **MQTT Explorer**: Broker enumeration and topic inspection
- **OpenPLC Runtime**: Reference for PLC logic review

### Script Support
Agent can generate:
- Python scripts using `pymodbus` for safe Modbus read operations
- `nmap` command lines with appropriate timing for OT environments
- Node-RED flow JSON for monitoring/alerting integrations
- InfluxDB/Grafana dashboard JSON for security metrics
- Sigma rules for SIEM detection of ICS-specific anomalies
- Yara rules for firmware string/pattern matching

### Firmware Analysis Pipeline
When a firmware binary is provided:
1. `binwalk` — filesystem extraction and entropy analysis
2. `strings` — credential and endpoint extraction
3. `radare2` / `ghidra` — disassembly for logic review
4. `cve-search` / NVD API — component CVE correlation
5. `firmwalker` — automated sensitive file discovery

## Workspace File Conventions
```
work-log/          — Assessment journals, daily notes, evidence custody log
planning/          — Engagement scopes, timelines, asset lists
outputs/           — Reports, diagrams, hardening checklists
user-docs/         — Operator-facing guides, training materials
resources/         — Reference material, CVE lists, protocol guides
```

## Network Zone Nomenclature (Purdue Model Adapted)
| Zone | Label | Examples in Aquaponics |
|------|-------|----------------------|
| Zone 0 | Field Devices | pH probes, DO sensors, flow meters, relay boards |
| Zone 1 | Control | PLCs, RTUs, Arduino/Pi controllers |
| Zone 2 | Supervisory | SCADA/HMI, data historian, alarm system |
| Zone 3 | Operations | Operator workstations, engineering laptops |
| Zone 3.5 | DMZ | Historian replication, remote access gateway |
| Zone 4 | Enterprise IT | Business systems, cloud integrations |
| Zone 5 | External | Internet, vendor remote access, cloud platforms |

## Supported Protocol Reference
| Protocol | Port | Common Use | Risk Level |
|----------|------|-----------|-----------|
| Modbus TCP | 502 | PLC comms | HIGH — no auth |
| BACnet/IP | 47808 | Building/HVAC crossover | MEDIUM |
| MQTT | 1883/8883 | IoT sensor data | HIGH if 1883 unencrypted |
| HTTP | 80 | HMI web interface | HIGH — plaintext |
| SSH | 22 | Pi/Linux controllers | LOW if hardened |
| Telnet | 23 | Legacy controllers | CRITICAL — disable |
| VNC | 5900 | Remote HMI access | HIGH — often default auth |
| RDP | 3389 | Windows SCADA | HIGH if internet-exposed |
