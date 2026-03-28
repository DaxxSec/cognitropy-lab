# /scan — Anomaly Detection Pass

Run a full three-tier anomaly detection scan on current sensor readings.

## Workflow
Follow the complete `/scan` workflow defined in `context/for-agent/workflows.md` — Workflow 1.

## Input Parsing
Accept readings in any reasonable format:
- Pasted inline text: `pH: 7.1, Temp: 28.2, NH3: 0.08, NO2: 0.03, DO: 7.1`
- CSV row
- Natural language: "pH is 7.1, temperature is 28 degrees, ammonia tested at 0.08"

If operator provides TWO readings (current + previous), calculate rate-of-change automatically.

## Output Format
```
══════════════════════════════════════════
  SYSTEM STATUS: [ALL CLEAR / WARNING / CRITICAL]
══════════════════════════════════════════

PARAMETER READINGS:
  pH:         X.X    [OK/WARN/CRITICAL]  [trend]
  Temp:       XX.X°C [OK/WARN/CRITICAL]  [trend]
  NH3:        X.XX   [OK/WARN/CRITICAL]  [trend]
  NO2-:       X.XX   [OK/WARN/CRITICAL]  [trend]
  NO3-:       XX     [OK/WARN/CRITICAL]  [trend]
  DO:         X.X    [OK/WARN/CRITICAL]  [trend]
  [others if available]

RATE-OF-CHANGE: [if previous reading available]
  [parameter]: Δ X.X/hr — [OK/WARN/CRITICAL]

COMPOUND EVENTS: [if detected]
  [event name] — [description]

ACTIONS REQUIRED:
  🔴 IMMEDIATE: [if any]
  🟠 HIGH: [if any]
  🟡 MEDIUM: [if any]
  🟢 ROUTINE: [if any]
══════════════════════════════════════════
```

## If Readings Look Suspicious
Flag potential sensor errors before analysis. Note: "This reading may indicate a sensor issue — interpret with caution."
