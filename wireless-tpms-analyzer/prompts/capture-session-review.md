# Capture Session Review

Use this prompt template after completing a TPMS capture session to get a structured analysis.

---

## Prompt Template

```
I just completed a TPMS capture session. Here is the rtl_433 output:

[PASTE JSON OUTPUT HERE]

Session details:
- Date/time: [DATE TIME]
- Vehicle: [YEAR MAKE MODEL] or [Unknown]
- Region/frequency used: [315 MHz / 433.92 MHz]
- Duration: [X minutes]
- SDR hardware: [RTL-SDR / HackRF]
- Antenna: [type and placement]

Please:
1. Summarize how many unique sensors were detected and their IDs
2. Decode each sensor's latest pressure and temperature readings
3. Identify the manufacturer/protocol for each sensor
4. Flag any anomalies (missing sensors, unusual values, unknown protocols)
5. List any sensors that appear in the raw/unrecognized category and suggest next steps for those
6. Provide a sensor inventory table I can add to my work log
```

---

## Expected Output Structure

Signal Ghost will produce:

1. **Session Summary** — total packets, unique sensor IDs, protocol breakdown
2. **Sensor Inventory Table** — ID, manufacturer, pressure, temperature, battery, wheel position (if known)
3. **Anomaly Notes** — anything outside expected parameters
4. **Unknown Protocol Log** — unrecognized sensors with signal characteristics for further RE
5. **Recommended Next Steps** — what to do before next session
