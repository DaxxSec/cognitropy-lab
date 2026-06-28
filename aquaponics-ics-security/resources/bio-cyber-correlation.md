# Bio-Cyber Cross-Correlation Guide

## Purpose

In aquaponics, the biological system and the cyber system are inseparable. A sensor anomaly might be biology (biofilter crash) or it might be cyber (spoofed sensor data). This guide helps operators distinguish between the two — and recognize when a biological anomaly is actually a cyber indicator, or vice versa.

This document bridges the **[Aquaponics Anomaly Monitor](../aquaponics-anomaly-monitor/)** (biological monitoring) and this workspace (cyber security).

---

## The Core Problem

**A compromised controller can make a dying system look healthy.**

If an attacker gains access to the sensor reporting chain — the MQTT broker, the database, the dashboard — they can replace real readings with fabricated ones. The dashboard shows pH 7.0, DO 7.5, NH3 0.05. Everything looks perfect. Meanwhile, the actual water is crashing.

Conversely, **a compromised controller can make a healthy system look sick.**

An attacker who can inject false sensor data could trigger automated responses — dosing pumps adding chemicals that aren't needed, feeders shutting off, alarms exhausting operator attention (alert fatigue as a tactic).

---

## Bio → Cyber Indicators

When the biological monitoring system flags an anomaly, ask: **could this be cyber?**

| Biological Anomaly | Possible Cyber Cause | How to Distinguish |
|--------------------|---------------------|-------------------|
| Sudden perfect readings after fluctuation | Sensor data being overwritten with static values | Compare controller reading to manual test kit reading. If they disagree, suspect sensor chain compromise. |
| All parameters change simultaneously | Controller firmware replaced or config overwritten | Legitimate bio events affect parameters in sequence (NH3 rises first, then NO2, then pH drops). Simultaneous change across unrelated parameters is suspicious. |
| Readings inconsistent with physical observation | Sensor data spoofed at reporting layer | Look at the fish. If fish are surfacing but DO reads 8.0 mg/L, the sensor is lying. |
| Automated responses triggering without anomaly | Attacker sending commands directly to actuators | Check command logs. Did the dosing pump receive a command that the control logic didn't generate? |
| Readings frozen (exact same value repeated) | Sensor polling stopped, last value cached | Real sensors have noise — 0.01-0.05 variation is normal. Exact repetition (7.000, 7.000, 7.000) across multiple readings means the sensor isn't being polled. |

## Cyber → Bio Indicators

When the security monitoring system flags an anomaly, ask: **what's the biological impact?**

| Cyber Anomaly | Biological Risk | Response Priority |
|---------------|----------------|-------------------|
| Unauthorized access to controller | Immediate: attacker can modify pump/feeder/dosing schedules | **CRITICAL** — verify all actuator states physically |
| MQTT broker compromise | Sensor data integrity lost — monitoring becomes unreliable | **HIGH** — switch to manual monitoring until broker is verified |
| Dashboard credentials compromised | Observation capability lost — attacker can see but not act (unless dashboard has write access) | **MEDIUM** — rotate credentials, check for write permissions |
| Network scan detected on OT VLAN | Reconnaissance phase — attack likely incoming | **HIGH** — isolate OT network, increase monitoring frequency |
| Firmware update pushed outside maintenance window | Controller behavior may be modified — unknown impact | **CRITICAL** — do not trust sensor data until firmware is verified |
| DNS or NTP manipulation | Logging timestamps unreliable — forensic integrity lost | **MEDIUM** — verify system time, check for time-based automation triggers |

## The Validation Protocol

When any anomaly is detected — biological or cyber — run this cross-validation:

### Step 1: Physical Ground Truth
- **Look at the fish.** Behavior is a leading indicator. Gasping at surface = low DO regardless of what the sensor says.
- **Look at the plants.** Wilting, yellowing, or root discoloration that doesn't match sensor data = suspect data integrity.
- **Smell the water.** Ammonia has a distinctive smell at concentrations above 0.5 ppm. If the sensor says 0.05 but you can smell it, the sensor is wrong.
- **Use a manual test kit.** API, Hanna, or Salifert test kits are the ground truth. Compare to controller reading.

### Step 2: Sensor Chain Verification
- **Compare sensor output to controller input.** If the sensor probe reads differently from what the controller reports, the chain is compromised between probe and controller.
- **Check MQTT messages against database values.** If MQTT published 6.5 but the database shows 7.0, something is modifying data in transit or at rest.
- **Check dashboard against database.** If the database shows 6.5 but the dashboard shows 7.0, the visualization layer is compromised.
- **Check controller logs for unexpected commands.** Pumps, feeders, and dosing systems should only respond to commands from the control logic. Orphan commands indicate unauthorized access.

### Step 3: Timeline Correlation
- **When did the biological anomaly start?**
- **When did the last cyber event occur?** (Failed login, network scan, firmware update, config change)
- **Do they correlate?** If ammonia started rising 30 minutes after an unauthorized SSH login to the controller, that's correlation.
- **Check for the "too quiet" signal.** If the system was generating normal sensor noise and suddenly goes perfectly flat, that's the data equivalent of a phone going dead — silence is a signal.

---

## Integration Workflow

For operators running both workspaces:

1. Run `/scan` in the Anomaly Monitor with current readings
2. If anomaly detected, check this guide's Bio → Cyber table
3. If cyber cause suspected, switch to ICS Security workspace
4. Run `/incident-response` if compromise is likely
5. Run the Validation Protocol regardless of initial assessment
6. Log findings in both workspaces' `work-log/` directories

For security assessors evaluating an aquaponics site:

1. Run `/asset-inventory` and `/network-audit` in ICS Security
2. For each finding, check this guide's Cyber → Bio table for biological risk
3. Prioritize findings by biological impact, not just technical severity
4. A low-severity IT finding (default password on dashboard) becomes critical if that dashboard has write access to actuators

---

## Key Principle

**In aquaponics, every cyber event is also a biological event.**

A firewall rule misconfiguration doesn't just create a security exposure — it creates a path from the internet to the pump that keeps 10,000 fish alive. A default password isn't just a compliance finding — it's the only thing standing between an attacker and the feeding schedule that determines whether a crop lives or dies.

Security assessments that ignore biological impact are incomplete. Biological monitoring that ignores cyber integrity is naive. The two workspaces exist as a pair for this reason.

---

## Domain Accuracy Note

The bio-cyber correlation patterns in this document are based on published ICS security research (CISA advisories, SANS ICS whitepapers) and aquaculture monitoring best practices. The specific sensor behavior patterns (noise characteristics, response sequences) reflect general aquaponics system behavior — your system may differ based on sensor brand, calibration frequency, and controller firmware. **This guide should be reviewed by both a security practitioner and an aquaponics operator before use in incident response.** If you identify inaccuracies, please open an issue.
