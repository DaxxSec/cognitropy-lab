# Shodan Dork Library — Aquaponics & Smart Agriculture

## Purpose

These Shodan search queries help identify exposed aquaponics and smart agriculture infrastructure on the public internet. Use them during `/network-audit` to check whether your own systems are externally visible, or during threat modeling to understand the attack surface of the sector.

**Ethical use only.** These queries identify publicly exposed systems. Do not access, probe, or interact with systems you do not own or have authorization to assess.

---

## Unitronics PLCs (CISA AA23-335A targets)

```
# Unitronics Vision/Samba — PCOM protocol
port:20256 "Unitronics"

# Unitronics web interface
http.title:"Unitronics" port:80

# Unitronics VNC (HMI remote access)
port:5900 "Unitronics"

# UniStream web server
http.title:"UniStream" OR http.title:"Unilogic"
```

## MQTT Brokers (Sensor Data)

```
# Open MQTT brokers (no auth)
port:1883 "MQTT"

# MQTT with aquaponics/agriculture topics (rare but findable)
port:1883 "aqua" OR "greenhouse" OR "hydro"

# MQTT WebSocket interface
port:9001 "MQTT"

# Mosquitto broker version disclosure
port:1883 product:"Mosquitto"
```

## Raspberry Pi Controllers

```
# Raspberry Pi SSH (default config)
port:22 "SSH" os:"Linux" "raspbian" OR "Raspberry"

# Node-RED (common automation UI)
http.title:"Node-RED"

# Grafana dashboards (sensor visualization)
http.title:"Grafana" "aqua" OR "fish" OR "greenhouse" OR "hydro"

# InfluxDB (sensor time-series database)
port:8086 product:"InfluxDB"
```

## SCADA / HMI Systems

```
# General SCADA web interfaces
http.title:"SCADA" "water" OR "pump" OR "ph" OR "temperature"

# Modbus TCP (industrial protocol, no auth by design)
port:502 "Modbus"

# DNP3 (less common in aquaponics but used in water treatment)
port:20000 "DNP3"

# BACnet (building automation — greenhouses)
port:47808 "BACnet"
```

## Greenhouse & Environmental Controllers

```
# Argus Controls (commercial greenhouse)
http.title:"Argus Controls"

# Priva (greenhouse climate control)
http.title:"Priva"

# Growlink / GroPal
http.title:"Growlink" OR http.title:"GroPal"

# Generic environmental monitoring
http.title:"Environmental Monitor" "temperature" "humidity"
```

## Webcams (Physical Observation)

```
# IP cameras in greenhouse/aquaculture settings
http.title:"camera" "fish" OR "aqua" OR "greenhouse" OR "grow"

# Common camera brands in agricultural settings
http.title:"HIKVISION" "farm" OR "greenhouse"
```

## Compound Queries (High Signal)

```
# Unitronics PLC + default port (highest risk — CISA advisory target)
port:20256

# Open MQTT + open Grafana on same network (full sensor visibility)
port:1883 port:3000 "Grafana"

# Modbus + water/agriculture keywords
port:502 "water" OR "pump" OR "aqua"
```

---

## How to Use These Queries

### Check Your Own Exposure

```bash
# Search for your public IP in Shodan
shodan host YOUR_PUBLIC_IP

# Search for your organization name
shodan search "org:YOUR_ORG_NAME" port:20256,1883,502,80

# Monitor for new exposure (Shodan Monitor — paid)
shodan alert create "My Aquaponics" YOUR_IP/24
```

### Assess Sector Exposure (Research)

```bash
# Count exposed Unitronics PLCs globally
shodan count port:20256

# Count exposed MQTT brokers
shodan count port:1883 product:"Mosquitto"

# Export results for analysis (researcher API key required)
shodan download aquaponics-exposure port:20256
```

### Integrate with `/threat-model`

When running `/threat-model`, reference these queries to identify realistic attack vectors:
- "Shodan shows X Unitronics PLCs exposed on port 20256 globally"
- "MQTT brokers without auth are discoverable — here's what an attacker sees"
- "Your Node-RED instance is accessible from the internet"

---

## Responsible Disclosure

If you discover exposed aquaponics or agriculture infrastructure that is not your own:
1. Do NOT access, probe, or interact with the system
2. Attempt to identify the owner through WHOIS, Shodan org data, or reverse DNS
3. If identifiable, notify the owner through appropriate channels
4. If critical infrastructure (water treatment, food production), consider notifying CISA: https://www.cisa.gov/report
