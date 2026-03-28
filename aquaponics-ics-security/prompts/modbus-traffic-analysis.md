# Prompt: Modbus Traffic Forensic Analysis

Use this prompt when you have captured Modbus TCP traffic and need to analyze it for anomalies or malicious activity.

---

**Prompt:**

I've captured network traffic from my aquaponics OT network. Here is a summary/excerpt of Modbus TCP traffic I'm seeing:

```
[PASTE WIRESHARK SUMMARY OR TSHARK OUTPUT]
```

My normal system configuration:
- SCADA/HMI IP: [IP]
- PLC 1 IP: [IP], Modbus Unit ID: [ID]
- PLC 2 IP: [IP], Modbus Unit ID: [ID]
- Expected function codes in use: [e.g., FC3 Read Holding Registers, FC16 Write Multiple Registers]
- Expected register ranges for setpoints: [e.g., HR 0-20 for pump setpoints, HR 40-60 for alarm thresholds]

Please analyze for:
1. Unexpected source IPs initiating Modbus requests (unauthorized devices)
2. Unexpected function codes (especially FC5/FC6/FC15/FC16 writes that shouldn't be occurring)
3. Writes to register addresses outside normal operational ranges (potential setpoint tampering)
4. Abnormal request frequency (scanning behavior vs. normal polling)
5. Any evidence of Modbus reconnaissance (function code 43/MEI, unit ID enumeration)

For any anomalies found, describe:
- What the activity suggests (misconfiguration, unauthorized access, active attack)
- The potential biological impact
- Recommended immediate response
