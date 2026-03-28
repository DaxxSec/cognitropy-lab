# OT Network Design Guide — Aquaponics Control Systems

## The Purdue Model Applied to Aquaponics

The Purdue Enterprise Reference Architecture (PERA) provides a zone-based model for separating OT from IT. Here's how it maps to aquaponics:

```
┌─────────────────────────────────────────────┐
│  ZONE 5 — EXTERNAL NETWORKS                 │
│  Internet, Cloud platforms, Vendor access   │
│  (Blynk, GroPal, AWS IoT, vendor VPN)       │
└───────────────┬─────────────────────────────┘
                │  [FIREWALL — DMZ]
┌───────────────▼─────────────────────────────┐
│  ZONE 3.5 — DEMILITARIZED ZONE (DMZ)        │
│  Remote access gateway (VPN concentrator)   │
│  Historian replication server               │
│  Cloud connector / data bridge              │
└───────────────┬─────────────────────────────┘
                │  [FIREWALL]
┌───────────────▼─────────────────────────────┐
│  ZONE 3/4 — OPERATIONS / ENTERPRISE IT      │
│  Office workstations, business systems      │
│  Engineering laptops (when in office)       │
└───────────────┬─────────────────────────────┘
                │  [FIREWALL — OT Boundary]
┌───────────────▼─────────────────────────────┐
│  ZONE 2 — SUPERVISORY                       │
│  SCADA/HMI servers and clients              │
│  Data historian (primary)                   │
│  Alarm management system                    │
│  Operator workstations                      │
└───────────────┬─────────────────────────────┘
                │  [FIREWALL / ACL]
┌───────────────▼─────────────────────────────┐
│  ZONE 1 — CONTROL                           │
│  PLCs (Allen-Bradley, Siemens, Click, etc.) │
│  Raspberry Pi / Arduino controllers         │
│  RTUs, relay panels                         │
└───────────────┬─────────────────────────────┘
                │  [Hardware isolation preferred]
┌───────────────▼─────────────────────────────┐
│  ZONE 0 — FIELD DEVICES                     │
│  pH probes, DO sensors, temp sensors        │
│  Flow meters, level sensors                 │
│  Pump relays, valve actuators               │
│  Fish feeder controllers                    │
└─────────────────────────────────────────────┘
```

## Minimum Viable Segmentation by Site Size

### Hobby / Small-Scale (< 1,000L, 1-2 people)
- **Minimum**: Separate IoT VLAN from main LAN on router (most home routers support this)
- **Cloud**: Use reputable platform with 2FA; no direct port forwarding to controllers
- **Remote access**: Cloud platform only (not direct VPN/port-forward to Pi)
- **Effort**: 1-2 hours, no specialist required

### Mid-Scale Commercial (1,000-50,000L, 2-10 staff)
- **Minimum**: Dedicated OT VLAN, managed switch with port isolation, basic firewall between IT/OT
- **Remote access**: Site-to-site VPN, MFA required
- **Monitoring**: Syslog aggregation, basic alerting
- **Wireless**: Separate SSID for OT devices, isolated from corporate Wi-Fi
- **Effort**: 1-3 days, IT-capable staff or consultant

### Large Commercial / FDA-Regulated (50,000L+)
- **Required**: Full Purdue Model implementation
- **Remote access**: Zero-trust architecture, PAM solution for OT access
- **Monitoring**: OT-aware SIEM (Claroty, Dragos, or open-source equivalent)
- **Documentation**: Asset management system, change management process
- **Compliance**: IEC 62443-2-1 assessment recommended
- **Effort**: Weeks to months, OT security specialist required

## Firewall Rule Templates

### Small Commercial (IT/OT Flat Network → VLAN Segmentation)
```
# Allow SCADA → PLC (Modbus TCP)
ALLOW TCP from [SCADA_IP] to [PLC_IP] port 502

# Allow operator workstations → SCADA HMI (HTTPS)
ALLOW TCP from [OT_WORKSTATION_SUBNET] to [SCADA_IP] port 443

# Allow SSH management from engineering laptop only
ALLOW TCP from [ENG_LAPTOP_IP] to [PI_CONTROLLER_SUBNET] port 22

# Allow historian → cloud (outbound only, specific destination)
ALLOW TCP from [HISTORIAN_IP] to [CLOUD_ENDPOINT] port 443

# Block all other IT → OT traffic
DENY IP from [IT_SUBNET] to [OT_SUBNET]

# Block all internet-initiated OT access
DENY IP from any to [OT_SUBNET]
```

## Remote Access Architecture Options

### Option 1: Cloud Platform Only (Hobby/Small)
```
[Aquaponics System] → [Pi/Controller] → [MQTT to Cloud] → [Operator Phone/Browser]
```
- Pros: No inbound firewall rules, simple, managed security
- Cons: Cloud dependency, data leaves site, limited control depth
- Acceptable for: Non-safety-critical monitoring only

### Option 2: VPN + Jump Server (Commercial)
```
[Operator Laptop] → [Internet] → [VPN Gateway in DMZ] → [Jump Server] → [OT Network]
```
- Requires: VPN solution (WireGuard, OpenVPN, or commercial), MFA
- Pros: Full control depth, data stays on-site, auditable
- Cons: More complex setup, server to maintain

### Option 3: Zero Trust / Cloud-Brokered (Enterprise)
```
[Operator Device] → [Cloud IdP with MFA] → [Broker] → [On-Site Agent] → [OT Network]
```
- Products: Cloudflare Access, Zscaler, Tailscale (for smaller deployments)
- Pros: No inbound firewall rules, strong identity, device posture checks
- Cons: Cost, complexity, cloud dependency for access

## Wireless Security Standards for OT

| Standard | Recommendation |
|---------|---------------|
| WEP | Never use — broken in minutes |
| WPA-TKIP | Never use — deprecated |
| WPA2-CCMP (AES) | Minimum acceptable |
| WPA2-Enterprise (802.1X) | Recommended for commercial |
| WPA3 | Best practice when hardware supports |
| Open (no encryption) | Never use for OT-connected devices |

**SSID Isolation Rule**: OT wireless devices must be on a VLAN isolated from:
- Corporate/guest Wi-Fi
- Staff personal devices
- Visitor networks
