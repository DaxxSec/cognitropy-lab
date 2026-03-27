# /analyze-tune — ECU Map & Calibration Analysis

Analyze ECU maps, tables, and scalars for safety issues, performance characteristics, and tuning opportunities.

---

## When to Use This Command
- You've received a new tune from your tuner and want a sanity check
- You've made changes to your own calibration and want a second opinion
- You want to understand what a specific table does and how to interpret it
- You want to compare current tune values against known-safe baselines for your platform

---

## How to Provide Tune Data

You can provide tune data in several ways:
1. **Paste map values as text** — e.g., copy the table from RomRaider or HP Tuners as CSV/text
2. **Describe the values** — e.g., "my ignition advance table shows 18° at 3500 RPM / 100 kPa"
3. **Screenshot or image** — describe what you see or attach if vision is available
4. **File path** — if filesystem MCP is configured, provide the path to your ROM or tune file

---

## What to Tell Me

Before analyzing, provide:
1. **Fuel type:** What fuel is in the car right now?
2. **Current boost target:** At what PSI are you running?
3. **Which table(s) to analyze:** (e.g., "ignition advance table," "fueling/VE table," "boost control target")
4. **Any specific concerns:** (e.g., "I'm seeing knock at 4500 RPM under load")

---

## What the Analysis Covers

### Safety Audit (Always First)
- **Fuel/VE table:** Are WOT cells targeting safe AFRs for the fuel type?
- **Ignition timing:** Are high-load cells within safe windows for the platform?
- **Boost control:** Does the boost target stay within constraints.md hard limits?
- **Rev limiter:** Is it set appropriately for the engine build?
- **Fuel cut / safety functions:** Are knock-response retard values reasonable?

### Performance Review
- Areas where timing could be safely advanced (typically light-load cruise)
- Fueling efficiency (avoiding excessive enrichment at cruise)
- Mid-range torque optimization opportunities
- Cold start / warm-up calibration quality

### Platform Comparison
- Compare values to known-good community baselines for your platform
- Flag any values that are notably more aggressive or more conservative than typical

---

## Output Format

The analysis will be delivered as:

1. **Safety Summary** — CRITICAL / WARNING / OK status for each key area
2. **Detailed Findings Table:**
   | Parameter | Current Value | Assessment | Recommendation |
3. **Priority Action List** — ordered from most urgent to optional refinement
4. **Safe to Pull On?** — a clear go/no-go recommendation based on the data provided

---

## Important Notes

- This analysis is based on the data you provide. Incomplete data = incomplete analysis.
- If AFR targets or knock retard values aren't available, this will be flagged explicitly.
- Always verify recommendations against your wideband data on the first pull after any change.
- This tool augments — it does not replace — hands-on tuning expertise and dyno verification.
