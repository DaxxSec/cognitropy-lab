# Prompt: Shodan Exposure Analysis for Aquaponics Systems

Use this prompt when you want the agent to analyze Shodan results for internet-exposed aquaponics control systems.

---

**Prompt:**

I have the following Shodan search results for my network's public IP range / for systems matching the query "[QUERY]":

```
[PASTE SHODAN OUTPUT HERE]
```

Please analyze this for:
1. Any directly exposed OT/ICS services (Modbus port 502, EtherNet/IP, BACnet, etc.)
2. Any exposed HMI or SCADA web interfaces
3. Any MQTT brokers without authentication
4. Any services with banner information revealing firmware/software versions with known CVEs
5. Any services using deprecated protocols (Telnet, FTP, HTTP without HTTPS redirect)

For each finding:
- Classify severity (Critical/High/Medium/Low)
- Describe what an attacker could do with this access
- Describe the potential biological impact (fish mortality risk, crop impact, etc.)
- Provide an immediate remediation step

Also check: are any of the banners matching known IoT/OT device fingerprints that commonly ship with default credentials?
