# Vendor-Specific Hardening Profiles

## Purpose

Most aquaponics automation is built on three platform families. Each has different default configurations, common vulnerabilities, and hardening approaches. This guide provides specific, actionable hardening steps for each.

---

## Profile 1: Raspberry Pi + Custom Stack

**Risk level:** HIGH — these systems are typically built by aquaculture practitioners, not security engineers.

### Common Vulnerabilities
- Default `pi`/`raspberry` credentials left unchanged
- SSH exposed on port 22 with password auth
- No firewall — all ports open on the local network
- Sensor data transmitted unencrypted over I2C/UART (physical access risk)
- Web dashboards (Grafana, Node-RED, custom Flask) with no authentication
- MQTT broker with no auth (anonymous publish/subscribe)
- No automatic updates — known CVEs persist indefinitely
- SD card unencrypted — physical theft exposes all config and data

### Hardening Checklist

**Immediate (do now):**
- [ ] Change default password: `sudo passwd pi`
- [ ] Disable password SSH, enable key-only: edit `/etc/ssh/sshd_config` → `PasswordAuthentication no`
- [ ] Enable UFW firewall: `sudo ufw enable && sudo ufw default deny incoming`
- [ ] Allow only needed ports: `sudo ufw allow from 192.168.1.0/24 to any port 22` (SSH from LAN only)
- [ ] Set MQTT broker auth: add `password_file /etc/mosquitto/passwd` to `mosquitto.conf`
- [ ] Add auth to web dashboards (Grafana: built-in, Node-RED: `adminAuth` in settings.js)

**Short-term (this week):**
- [ ] Enable automatic security updates: `sudo apt install unattended-upgrades`
- [ ] Move SSH to non-standard port: `Port 2222` in sshd_config
- [ ] Set up fail2ban: `sudo apt install fail2ban`
- [ ] Enable HTTPS for web dashboards (Let's Encrypt or self-signed)
- [ ] Segment IoT network from main LAN (VLAN or separate subnet)
- [ ] Disable unused services: `sudo systemctl disable bluetooth avahi-daemon`

**Medium-term (this month):**
- [ ] Encrypt SD card (LUKS): protects against physical theft
- [ ] Set up VPN for remote access instead of port forwarding
- [ ] Implement TLS for MQTT: `listener 8883` with cert configuration
- [ ] Add watchdog: `sudo apt install watchdog` — auto-reboot on hang
- [ ] Backup configuration to encrypted off-device storage

---

## Profile 2: Unitronics PLCs (Vision/Samba/UniStream)

**Risk level:** CRITICAL — these are the PLCs cited in the 2023 CISA Unitronics advisory (AA23-335A).

### Common Vulnerabilities
- Default password `1111` on all Vision and Samba series PLCs
- PCOM protocol on TCP/20256 — no authentication, no encryption
- VNC on TCP/5900 with default or no password (HMI remote access)
- Web server on TCP/80 (UniStream) with default credentials
- Firmware update mechanism has no signature verification (pre-2024 firmware)
- No audit logging — unauthorized changes leave no trace
- Often directly exposed to the internet via port forwarding for "remote monitoring"

### Hardening Checklist

**Immediate (do now — CISA AA23-335A compliance):**
- [ ] Change default password from `1111` — use 8+ characters, alphanumeric
- [ ] Disable VNC if not needed: VisiLogic > PLC > VNC > Disable
- [ ] Block TCP/20256 (PCOM) from internet: firewall rule at network edge
- [ ] Block TCP/5900 (VNC) from internet
- [ ] Block TCP/80 (web server) from internet
- [ ] Verify PLC firmware is current: check Unitronics download center

**Short-term (this week):**
- [ ] Segment PLC onto dedicated OT VLAN — no direct path from IT network
- [ ] Implement jump host for PLC programming (don't connect laptop directly to OT network)
- [ ] Enable PLC access logging if firmware supports it (UniStream v1.31+)
- [ ] Document all PLC IP addresses, firmware versions, and access credentials in asset inventory
- [ ] Set up network monitoring on OT VLAN (even basic pcap)

**Medium-term (this month):**
- [ ] Deploy industrial firewall between IT and OT segments (Fortinet, Palo Alto OT, or open-source OPNsense with Suricata)
- [ ] Implement MFA for remote access to PLC programming environment
- [ ] Establish change management: no PLC program changes without documented approval
- [ ] Back up PLC programs to version-controlled repository
- [ ] Test backup restoration procedure — can you rebuild from backup?

---

## Profile 3: Arduino/ESP32 + DIY Controllers

**Risk level:** MEDIUM-HIGH — less capable than Pi systems but often completely unhardened.

### Common Vulnerabilities
- OTA (Over-The-Air) update enabled with no authentication
- WiFi credentials hardcoded in firmware source code
- Web server for configuration with no auth (common in ESP32 projects)
- mDNS/Bonjour broadcasting device identity on local network
- No encryption on sensor data transmission
- No firmware signing — anyone on the network can push a malicious update
- Serial/UART debug ports left enabled in production

### Hardening Checklist

**Immediate (do now):**
- [ ] Disable OTA update or set OTA password: `ArduinoOTA.setPassword("strong_password")`
- [ ] Remove hardcoded WiFi credentials: use WiFiManager library or config portal
- [ ] Add basic auth to web configuration interface
- [ ] Disable serial debug output in production firmware: `#define DEBUG 0`

**Short-term (this week):**
- [ ] Segment IoT devices onto dedicated WiFi SSID/VLAN
- [ ] Disable mDNS if not needed: remove `MDNS.begin()` from firmware
- [ ] Implement HTTPS on ESP32 web server (self-signed cert is better than HTTP)
- [ ] Use MQTT with TLS + username/password (not anonymous)
- [ ] Set WiFi to WPA3 if access point supports it

**Medium-term (this month):**
- [ ] Implement firmware signing: verify updates before flashing
- [ ] Add hardware watchdog timer to detect and recover from crashes
- [ ] Consider ESP32 secure boot (eFuse-based, one-time programmable)
- [ ] Move sensitive config to NVS encrypted partition
- [ ] Conduct wireless scan to ensure no rogue devices on IoT VLAN

---

## Cross-Reference

For biological monitoring of the systems these controllers manage, see the companion workspace: **[Aquaponics Anomaly Monitor](../aquaponics-anomaly-monitor/)**

A compromised controller can spoof sensor readings. If your anomaly monitor shows sudden perfect readings after a period of fluctuation, consider whether the data is real or whether the controller has been tampered with. When in doubt: **verify sensor data against physical observation** (look at the fish, look at the plants, smell the water).

---

## Domain Accuracy Note

The Unitronics vulnerabilities and CISA advisory references are current as of March 2026. The Raspberry Pi and Arduino/ESP32 hardening steps reflect standard security practices. PLC-specific firmware capabilities vary by model and version — consult Unitronics documentation for your specific hardware. **This guide should be reviewed by an OT security practitioner before use in production environments.** If you identify inaccuracies or missing CVEs, please open an issue.
