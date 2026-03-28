# Domain Workflows — Aquaponics ICS/OT Security

## Overview
This document defines repeatable security workflows for aquaponics control system assessments. Each workflow references the Purdue Model zone taxonomy defined in `environment.md` and maps to the slash commands in `CLAUDE.md`.

---

## Workflow 1: Site Onboarding & Scope Definition
**Command: `/onboard`**

### Purpose
Establish a complete understanding of the site before any security work begins. Document the biological system alongside the technical infrastructure — they are inseparable.

### Steps

**Phase 1A — Biological System Profile**
1. Capture system type: NFT, DWC, media bed, hybrid
2. Record stocking density and species (tilapia, trout, catfish, etc.)
3. Document plant production: leafy greens, fruiting crops, herbs
4. Note daily operating schedule: feed times, harvest cycles, maintenance windows
5. Identify critical process dependencies:
   - Minimum uptime requirements per system component
   - Acceptable maintenance window durations
   - Recovery time objectives for each automation component

**Phase 1B — Technical Infrastructure Discovery**
1. Request existing network diagrams (if any)
2. Document physical access controls to controller cabinets
3. Identify all internet-connected components (cloud platforms, remote access)
4. Note any recent changes: new equipment, firmware updates, network changes
5. Document all vendor/contractor remote access arrangements
6. Identify data flows: what sensor data goes where, who has access

**Phase 1C — Engagement Scope Agreement**
1. Confirm authorized zones for assessment
2. Agree on maintenance windows for any active testing
3. Establish communication contacts (biological operator + IT/OT contact)
4. Define deliverables and timeline
5. Confirm authorization document is signed

**Output**: Completed site profile document in `planning/site-profile.md`

---

## Workflow 2: Asset Inventory & Zone Classification
**Command: `/asset-inventory`**

### Purpose
Build a complete, zone-classified inventory of all OT/IoT assets. You cannot secure what you don't know exists.

### Discovery Methods (Passive First)
1. **Document review**: Review any existing network diagrams, procurement records, manual wiring diagrams
2. **Physical walkthrough**: Photograph all controller panels, junction boxes, sensor nodes
3. **DHCP lease analysis**: Pull lease tables from network switches/routers to enumerate devices
4. **Passive network capture**: 15-minute tcpdump on each network segment, analyze in Wireshark for protocol/device fingerprinting
5. **Active enumeration (authorized only)**: Nmap light sweep — `nmap -sV -p 502,1883,80,22,23,5900 --timing 2 [subnet]`

### Asset Classification Template
For each discovered asset, document:
```
Asset ID:          [sequential, e.g., AQ-CTL-001]
Device Name:       [hostname or label]
Device Type:       [PLC | HMI | Sensor | Gateway | PC | Network]
Manufacturer:      [e.g., Allen-Bradley, Raspberry Pi Foundation]
Model:             [e.g., MicroLogix 1100]
Firmware Version:  [if obtainable]
Zone:              [0-5 per Purdue Model]
IP Address:        [or MAC if no IP]
Protocols:         [Modbus | MQTT | HTTP | SSH | etc.]
Internet-Exposed:  [Yes | No | Unknown]
Auth Method:       [Password | Certificate | None | Unknown]
Last Patched:      [date or Unknown]
Criticality:       [Critical | High | Medium | Low]
Criticality Basis: [brief explanation, e.g., "controls primary pump — failure = fish kill in 2h"]
```

### Criticality Rating Guide
- **Critical**: Failure directly causes fish mortality or total crop loss within hours
- **High**: Failure degrades system significantly, operator intervention required within 24h
- **Medium**: Failure reduces efficiency or monitoring visibility, manageable short-term
- **Low**: Failure has no immediate biological impact, administrative/reporting only

**Output**: Asset inventory spreadsheet in `outputs/asset-inventory.xlsx` or `outputs/asset-inventory.csv`

---

## Workflow 3: Threat Modeling
**Command: `/threat-model`**

### Purpose
Identify realistic attack scenarios specific to aquaponics environments. Use STRIDE methodology applied to OT/ICS context, informed by MITRE ATT&CK for ICS.

### Threat Actor Profiles for Aquaponics
| Actor | Motivation | Capability | Likelihood |
|-------|-----------|-----------|-----------|
| Script kiddie via Shodan | Curiosity, vandalism | Low | HIGH — Shodan exposes many aquaponics HMIs |
| Ransomware operator | Financial extortion | Medium-High | MEDIUM — growing OT ransomware trend |
| Disgruntled insider | Sabotage | Medium | MEDIUM — small operations with poor access revocation |
| Competitor sabotage | Business disruption | Low-Medium | LOW — rare but documented in food production |
| Supply chain compromise | Software/firmware backdoors | High | LOW-MEDIUM — via vendor remote access |
| Nation-state (food security) | Critical infrastructure disruption | Very High | LOW — only relevant for large commercial operations |

### Attack Surface Analysis
**Zone 5 → Zone 4 (Internet-Facing Entry Points)**
- Shodan-discoverable HMI panels (search: `port:502 "Modbus"`, `"InduSoft"`, `"Ignition"`)
- Exposed MQTT brokers on port 1883
- Cloud platform credentials (Blynk, GroPal accounts)
- VPN concentrators with weak authentication
- Port-forwarded RDP/VNC for remote operator access

**Zone 4 → Zone 3 (IT to OT Pivot)**
- Shared credentials between IT workstations and OT engineering laptops
- USB drives carried between zones
- Flat networks with no IT/OT segmentation
- Vendor laptops with dual network access

**Zone 3 → Zone 2 (Engineering to Supervisory)**
- SCADA/HMI with default admin password
- Unencrypted historian data streams
- Unsecured backup configurations on engineering workstation

**Zone 2 → Zone 1/0 (Supervisory to Control)**
- Modbus TCP with no authentication — any device on the network can write setpoints
- PLC logic upload/download without authentication
- Firmware update process with no signature verification

### STRIDE Application to Aquaponics ICS
| Threat | Example Scenario | Impact |
|--------|----------------|--------|
| **Spoofing** | Attacker sends forged Modbus responses to SCADA — falsely reports normal pH while actual pH spikes | Fish killed due to undetected chemical imbalance |
| **Tampering** | Attacker modifies PLC setpoints — overrides pump speed, sets DO thresholds to lethal levels | Hypoxia event, mass fish mortality |
| **Repudiation** | No centralized logging — operator cannot determine who changed feed schedule | Forensic investigation impossible |
| **Information Disclosure** | MQTT broker has no auth — production data, sensor readings, and system topology exposed | Competitive intelligence, targeted attack planning |
| **Denial of Service** | Flood UDP port 47808 — legacy BACnet gateway crashes, takes SCADA offline | Operator blind to active biological events |
| **Elevation of Privilege** | SCADA runs as Windows local admin — malware escalates to domain controller | Full OT network compromise |

### MITRE ATT&CK for ICS Mapping
Key techniques relevant to aquaponics environments:
- T0843 — Program Download (unauthenticated PLC firmware modification)
- T0831 — Manipulation of Control (setpoint modification via Modbus)
- T0856 — Spoof Reporting Message (false sensor data injection)
- T0816 — Device Restart/Shutdown (denial of service to controllers)
- T0862 — Supply Chain Compromise (malicious firmware via vendor update)
- T0845 — Program Upload (intellectual property theft — automation logic)

**Output**: Threat model document in `outputs/threat-model.md`

---

## Workflow 4: Network Segmentation Audit
**Command: `/network-audit`**

### Purpose
Assess whether the OT network is properly segmented from IT and the internet, and identify pathways for lateral movement.

### Assessment Steps

**Step 1 — Topology Reconstruction**
1. Request switch port mappings and VLAN configurations
2. Perform passive traffic capture per segment (identify cross-zone communication)
3. Verify firewall/ACL rules between zones
4. Check for wireless access points in OT zones

**Step 2 — Segmentation Gap Analysis**
Test for (passively or with authorization):
```
# Can Zone 4 (IT) reach Zone 1 (Control) directly?
ping [PLC_IP] from IT workstation

# Is Modbus accessible from non-OT segments?
nmap -p 502 [control_subnet] from IT VLAN

# Are any controllers internet-accessible?
shodan search "port:502 org:[ISP_ASNAME]"
nmap -Pn -p 502,1883,80 [public_IP_range]
```

**Step 3 — Wireless Security Review**
- Identify SSIDs in OT/greenhouse areas
- Check encryption: WPA2-Enterprise preferred, WPA2-PSK acceptable, WEP/open = critical finding
- Test for guest VLAN isolation from OT VLAN
- Check for rogue access points

**Step 4 — Remote Access Review**
- Document all remote access paths (VPN, TeamViewer, AnyDesk, port forwarding)
- Verify MFA is enforced on all remote access
- Check for active but unauthorized remote access sessions
- Review vendor access: is it audited, time-limited, and revoked after use?

### Segmentation Findings Classification
| Finding | Severity | Example |
|---------|---------|--------|
| Internet directly reaches control device | CRITICAL | PLC port-forwarded, no firewall |
| IT VLAN can reach OT VLAN | HIGH | No firewall between segments |
| OT devices on same VLAN as operations PCs | HIGH | Flat network |
| Wireless AP in OT zone with WPA2-PSK | MEDIUM | Passphrase potentially shared |
| Remote access without MFA | HIGH | VPN with password-only auth |
| Vendor access not time-limited | MEDIUM | Permanent vendor VPN account |

**Output**: Network diagram (annotated) in `outputs/network-diagram.md` + findings in `outputs/findings.md`

---

## Workflow 5: Firmware & Device Vulnerability Assessment
**Command: `/firmware-check`**

### Purpose
Identify known vulnerabilities in deployed devices and assess firmware for security weaknesses.

### Phase 1 — CVE Correlation (No Firmware Access Required)
1. For each device in asset inventory, extract: Manufacturer, Model, Firmware Version
2. Query NVD/CISA ICS-CERT advisories:
   - https://www.cisa.gov/ics-advisories
   - https://nvd.nist.gov/vuln/search (search: vendor name + product)
3. Check vendor security bulletins directly
4. Cross-reference with known exploited vulnerabilities (CISA KEV):
   - https://www.cisa.gov/known-exploited-vulnerabilities-catalog

### Phase 2 — Firmware Analysis (When Binary Available)
```bash
# Step 1: Identify firmware format
file firmware.bin
binwalk firmware.bin

# Step 2: Extract filesystem
binwalk -e firmware.bin
cd _firmware.bin.extracted/

# Step 3: Hunt for credentials and sensitive strings
find . -name "*.conf" -o -name "*.cfg" -o -name "shadow" -o -name "passwd"
grep -r "password\|passwd\|secret\|api_key\|token" --include="*.conf" --include="*.json" --include="*.py" .
strings firmware.bin | grep -iE "admin|pass|key|secret|credential"

# Step 4: Check for hardcoded network targets
strings firmware.bin | grep -E "([0-9]{1,3}\.){3}[0-9]{1,3}" | sort -u
strings firmware.bin | grep -E "https?://"

# Step 5: Identify embedded components for CVE correlation
find . -name "*.so" -o -name "busybox" | xargs strings | grep -E "version [0-9]"
cat squashfs-root/etc/os-release 2>/dev/null
```

### Common Aquaponics Controller Vulnerabilities
| Platform | Common Issues |
|----------|--------------|
| Raspberry Pi (Raspbian) | Default `pi:raspberry` credentials never changed; SSH exposed |
| Arduino (Ethernet shield) | No authentication on HTTP configuration interface |
| Atlas Scientific EZO | I2C/UART bus — physical access = full control |
| Unitronics Vision PLCs | CVE-2023-6448: authentication bypass (CISA KEV!) |
| Weintek HMIs | Default Modbus address 1, no ACL on configuration port |
| Ignition SCADA | Historically: XXE, auth bypass issues — check patch level |
| Node-RED | Default no authentication on editor (port 1880) — critical if internet-exposed |

**Output**: Firmware/CVE findings appended to `outputs/findings.md`

---

## Workflow 6: ICS Incident Response
**Command: `/incident-response`**

### Purpose
Structured response to a suspected compromise of aquaponics control systems. Balance security containment with biological system continuity.

### Immediate Triage (First 15 Minutes)
1. **DO NOT take systems offline without biological safety confirmation**
2. Confirm biological system status: pumps running? DO nominal? Fish visibly healthy?
3. Identify scope of suspected compromise
4. Alert biological operator — establish manual monitoring watch
5. Determine if manual fallback is possible for critical systems

### Phase 1 — Contain (Without Killing Fish)
**Safe containment actions:**
- Block internet access at perimeter (firewall rule) — does NOT disrupt local OT
- Isolate compromised IT segment from OT segment (if separate)
- Revoke all vendor/external remote access credentials
- Change SCADA/HMI passwords from known-clean workstation

**Risky containment actions (confirm with biological operator first):**
- Rebooting PLCs — risk: pump/feeder disruption during reboot
- Isolating control segment entirely — risk: loss of SCADA visibility
- Firmware reimaging — only with maintenance window, manual monitoring in place

### Phase 2 — Investigate
```bash
# Network forensics
tcpdump -i [OT_interface] -w capture.pcap
# Look for: unusual Modbus function codes, new MAC addresses, beaconing patterns

# Windows SCADA host
# Collect: event logs, prefetch, running processes, scheduled tasks
wevtutil epl Security security.evtx
wevtutil epl System system.evtx
autorunsc -a -c > autoruns.csv

# Linux Pi controllers
last -w > logins.txt
ps aux > processes.txt
cat /var/log/auth.log > auth.log
crontab -l > crontab.txt
find / -newer /etc/passwd -mtime -7 2>/dev/null > recent_files.txt
```

### Phase 3 — Evidence Preservation
- Chain of custody log for all collected artifacts
- Hash all evidence files: `sha256sum *.pcap *.evtx *.log > evidence_hashes.txt`
- Document timeline of events with timestamps

### Phase 4 — Eradicate & Restore
1. Restore PLC logic from verified clean backup
2. Reimage compromised hosts from clean baseline
3. Reset ALL credentials: PLCs, HMIs, SCADA, VPN, cloud platforms
4. Verify each restored system against known-good configuration
5. Confirm biological parameters stable before returning to automated operation

**Output**: IR timeline + evidence log in `work-log/incident-[date].md`

---

## Workflow 7: Hardening Checklist Generation
**Command: `/harden`**

### Purpose
Generate device-specific or architecture-level hardening guidance.

### Universal ICS Hardening Principles
1. **Change all default credentials** before deployment — no exceptions
2. **Disable unused services**: Telnet, FTP, unused HTTP ports, unnecessary Modbus functions
3. **Enable logging** on all devices that support it, ship logs to central collector
4. **Network whitelist**: only explicitly permitted traffic between zones
5. **Patch management process**: scheduled review with biological maintenance windows
6. **Physical security**: locks on controller cabinets, tamper-evident seals
7. **Backup configs**: encrypted offline backups of all PLC/HMI configurations

### Platform-Specific Hardening

**Raspberry Pi Controllers**
```bash
# Change default password
passwd pi

# Disable SSH password auth, use keys only
echo "PasswordAuthentication no" >> /etc/ssh/sshd_config
echo "PermitRootLogin no" >> /etc/ssh/sshd_config

# Enable firewall
ufw allow from [OT_subnet] to any port 22
ufw allow from [OT_subnet] to any port 1883
ufw deny 22
ufw enable

# Enable automatic security updates
apt install unattended-upgrades
dpkg-reconfigure unattended-upgrades

# Disable unused services
systemctl disable bluetooth avahi-daemon
```

**Node-RED Instances**
```json
// settings.js — enable authentication
adminAuth: {
    type: "credentials",
    users: [{
        username: "admin",
        password: "$2b$08$...", // bcrypt hash
        permissions: "*"
    }]
},
// Enable HTTPS
https: {
    key: fs.readFileSync('privkey.pem'),
    cert: fs.readFileSync('cert.pem')
}
```

**MQTT Broker (Mosquitto)**
```conf
# mosquitto.conf
allow_anonymous false
password_file /etc/mosquitto/passwd
listener 8883
cafile /etc/mosquitto/ca.crt
certfile /etc/mosquitto/server.crt
keyfile /etc/mosquitto/server.key
require_certificate false
```

**Network Architecture Hardening**
```
Minimum viable segmentation for small commercial operation:
[Internet] → [Firewall] → [IT VLAN/10.0.1.0/24]
                        → [DMZ/10.0.2.0/24] (cloud gateway, historian)
                        → [OT VLAN/10.0.3.0/24] (SCADA, HMIs)
                        → [Control VLAN/10.0.4.0/24] (PLCs, sensors)

Firewall rules:
- IT → OT: DENY all except authorized historian replication
- OT → Control: ALLOW specific Modbus TCP (port 502) from SCADA IP only
- Control → OT: ALLOW historian data push
- Internet → DMZ: ALLOW HTTPS only
- Internet → OT/Control: DENY all
```

---

## Workflow 8: Compliance Gap Analysis
**Command: `/compliance`**

### IEC 62443 Security Level Mapping
| SL | Definition | Typical Aquaponics Application |
|----|------------|-------------------------------|
| SL-0 | No security requirements | Below minimum acceptable |
| SL-1 | Protection against casual/unintentional misuse | Minimum: basic auth, patching |
| SL-2 | Protection against intentional misuse with low motivation/capability | Target for most commercial operations |
| SL-3 | Protection against sophisticated intentional attacks | Large commercial, FDA-registered facilities |
| SL-4 | Protection against state-sponsored attacks | Not typically applicable |

### NIST SP 800-82 Rev 3 Control Families
Key control families mapped to aquaponics ICS:
- **AC (Access Control)**: Unique accounts, least privilege, revoke on termination
- **AU (Audit)**: Log all controller access, SCADA logins, config changes
- **CM (Configuration Management)**: Baseline configs documented, change control process
- **IA (Identification and Authentication)**: MFA for remote access, no shared accounts
- **IR (Incident Response)**: ICS-specific IR plan with biological continuity provisions
- **MA (Maintenance)**: Secure remote maintenance, vendor access controls
- **SC (System and Communications Protection)**: Network segmentation, encrypted comms
- **SI (System and Information Integrity)**: Malware protection, firmware integrity

**Output**: Compliance matrix in `outputs/compliance-gap-[standard]-[date].md`
