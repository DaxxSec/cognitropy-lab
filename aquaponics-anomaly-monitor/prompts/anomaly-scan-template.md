# Anomaly Scan Prompt Template

Use this template when pasting sensor readings for a quick scan without running `/scan` formally.

---

**Prompt:**

```
Analyze these aquaponics readings for anomalies. Flag anything outside normal range, calculate rate-of-change if I've provided previous readings, and check for compound event patterns.

System: [brief description — e.g., 400L tilapia tank, DWC lettuce beds, 6-month-old media bed biofilter]

CURRENT READINGS [YYYY-MM-DD HH:MM]:
pH: 
Temp: °C
NH3 (total): ppm
NO2-: ppm
NO3-: ppm
DO: mg/L
EC: μS/cm (optional)
Flow: [normal/reduced/stopped]
Fish behavior: [normal/surfacing/lethargic/off-feed]
Notes: 

PREVIOUS READINGS [YYYY-MM-DD HH:MM] (optional, for trend analysis):
pH: 
Temp: °C
NH3: ppm
NO2-: ppm
DO: mg/L
```

Prioritize any immediate action items. If all clear, confirm and note any minor trends worth watching.
```
