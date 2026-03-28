# /asset-inventory — OT/IoT Asset Enumeration

Build a complete, zone-classified inventory of all control system assets.

## Steps
1. Ask what discovery artifacts are available:
   - Existing network diagrams?
   - Switch DHCP lease tables?
   - Physical walkthrough photos or notes?
   - Passive network captures (pcap files)?
   - Any active scan results?

2. For each known/discovered asset, collect:
   - Device type, manufacturer, model, firmware version
   - IP address, MAC address, hostname
   - Protocols in use (Modbus, MQTT, HTTP, SSH, etc.)
   - Purdue Model zone classification (0-5)
   - Internet exposure status
   - Authentication method
   - Criticality rating (Critical/High/Medium/Low) with biological impact basis

3. Generate the asset inventory:
   - Format as a structured table
   - Flag internet-exposed assets prominently
   - Flag assets with default/no authentication
   - Flag assets with unknown firmware versions
   - Save to `outputs/asset-inventory.md`

4. Produce a summary:
   - Total asset count by zone
   - Count of internet-exposed assets
   - Count of assets with auth concerns
   - Top 5 highest-criticality assets
   - Recommended next step (threat model or network audit)

Reference: `context/for-agent/workflows.md` — Workflow 2
