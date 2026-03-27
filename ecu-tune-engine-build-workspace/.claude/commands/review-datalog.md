# /review-datalog — ECU Datalog Analysis

Parse and interpret ECU datalogs to identify knock events, lean conditions, boost anomalies, and thermal issues.

---

## When to Use This Command
- After any WOT pull, track session, or road tune pass
- When investigating a suspected problem (knock, misfire, power loss)
- After a dyno run to review what actually happened vs. what was expected
- As a routine health check after any significant tune change

---

## How to Provide Datalog Data

1. **Paste CSV data directly** — copy/paste the relevant rows from your log file
2. **Describe key values** — e.g., "peak boost was 18psi, AFR held at 11.5:1, I saw 2 counts of knock around 4800 RPM"
3. **Upload file** — if filesystem MCP is configured, provide the path to the .dlg, .csv, or log file
4. **Screenshot description** — describe what you're seeing in the log software

For best results, include at minimum: RPM, TPS, MAP/Boost, AFR/Lambda, and Knock data.

---

## Tell Me About the Run

Before reviewing, provide context:
1. **Type of run:** WOT pull / street drive / cold start / idle / track lap
2. **Fuel used:** (octane and ethanol content)
3. **Conditions:** Ambient temperature, IAT at start of pull (if known)
4. **Any observations:** Did you feel or hear anything unusual?
5. **Specific concern:** What are you worried about, if anything?

---

## Review Process

I will analyze the following channels in priority order:

### Critical Channels
1. **Knock / Knock Retard** — any non-zero value triggers investigation
2. **AFR / Lambda** — lean WOT excursions are the #1 engine-killer
3. **Boost** — compare actual vs. target; check for spikes or drops

### Thermal Channels
4. **Coolant Temperature** — WOT above 100°C is a warning; 105°C+ is abort territory
5. **IAT / IAT2** — elevated IAT reduces knock resistance; note heat soak
6. **Oil Temperature** — verify engine was fully warmed before WOT

### Load Channels
7. **Injector Duty Cycle** — above 85% is approaching injector limit
8. **Throttle Position** — confirm full throttle was achieved
9. **Vehicle Speed / Gear** — confirm expected gear engagement

---

## Output Format

1. **Run Summary Table:**
   | Channel | Min | Max | Average (WOT) | Status |

2. **Flagged Events:**
   | Timestamp / RPM | Event | Severity | Interpretation |

3. **Assessment:**
   - Overall verdict: Safe / Marginal / Unsafe
   - Most critical finding (if any)
   - Root cause hypothesis (if issues found)

4. **Recommended Actions:**
   - Immediate (must do before next pull)
   - Investigate (worth understanding before next session)
   - Monitor (keep an eye on, not urgent)

---

## Red Flag Reference

| Finding | Severity | Default Response |
|---------|----------|-----------------|
| Knock retard > 4° | CRITICAL | Stop. Do not pull again. Investigate fuel and timing. |
| AFR > 13.5:1 at WOT (gasoline) | CRITICAL | Fix fuel delivery before any more WOT. |
| AFR > 12.2:1 sustained boosted WOT | WARNING | Investigate — safe target is typically 11.0–11.8:1 |
| Injector duty > 90% | WARNING | Injectors near limit. Reduce boost or upgrade injectors. |
| Boost spike > 3 psi over target | WARNING | Check wastegate and boost control. |
| Coolant > 102°C at WOT | WARNING | Check cooling before next session. |
| IAT > 50°C at pull start | INFO | Heat soak degrading intercooler. Consider cooldown. |
| Missing AFR data | WARNING | Cannot safely assess tune without wideband data. |
