# Sensor ID Correlation

Use this template when you want to build or verify a wheel-position map for your sensor IDs — especially useful when rotating between summer and winter tires.

---

## Prompt Template

```
I want to correlate TPMS sensor IDs to specific wheels/vehicles.

**Vehicle(s):**
1. [YEAR MAKE MODEL] — [Primary / Secondary / Tire set name]
2. [optional additional vehicles or tire sets]

**Sensor IDs captured:**
[PASTE rtl_433 JSON or list of sensor IDs here]

**Known assignments (if any):**
- Front Left: [ID or Unknown]
- Front Right: [ID or Unknown]
- Rear Left: [ID or Unknown]
- Rear Right: [ID or Unknown]
- Spare: [ID or Unknown]

**Context:**
- Just completed tire rotation: [Yes/No]
- Just swapped seasonal tires: [Summer → Winter / Winter → Summer]
- Any sensors showing faults or missing: [describe]

Please:
1. Verify the sensor count (should be 4 unique IDs for a standard set)
2. Flag any IDs that appeared in previous sessions but are now absent
3. Identify any new IDs that weren't in my previous inventory
4. Suggest a wheel-assignment identification procedure if positions are unknown
5. Check if any sensor is transmitting unusual values (possible fault)
```

---

## Wheel Position Identification Procedure

If you don't know which ID maps to which wheel:
1. Deflate one tire by ~5 PSI, leave others at correct pressure
2. Capture for 2–3 minutes
3. The sensor showing the lower pressure reading = that wheel
4. Re-inflate, repeat for other wheels if needed
5. Record assignments in `work-log/sensor-inventory.md`
