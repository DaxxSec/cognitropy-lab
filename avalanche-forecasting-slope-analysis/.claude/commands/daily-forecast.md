---
description: Build today's hazard bulletin from observations and weather inputs.
---

# /daily-forecast

## Inputs (ask the user to paste or point to file)

1. Overnight + current weather: T, HN24, HNW24, wind speed/direction, RH, pressure trend, station sanity flags.
2. Observations in last 24 h from InfoEx / MIN / field teams. Note which are public vs. professional.
3. Any weather outlook (next 24-48 h).
4. Optional: prior bulletin to evolve from.

## Steps

1. **Sanity check telemetry.** Flag any weather station with suspect readings and add a PM action to the mitigation plan.
2. **Update PWL tracker** in `work-log/pwl-tracker.md` - for each tracked layer, record today's evidence (ECT/PST, natural activity, quiet periods).
3. **Classify problem types** by aspect and elevation band. Use the official 9-type list; do not invent new categories.
4. **Assign likelihood + size** per problem per band.
5. **Derive hazard rating** per band from the CMAH logic.
6. **Draft bulletin** following `resources/bulletin-template.md`:
   - Bottom line (one paragraph)
   - Problem(s) with location + travel advice
   - Forecast discussion
   - Weather outlook
   - Confidence level + justification
7. **Output** to `outputs/YYYY-MM-DD-bulletin-draft.md`.
8. **Flag** any paragraph that cites InfoEx-protected observations with an inline [PRO] tag so a human can redact before public publication.

## Output Format

- Markdown draft in `outputs/`
- Summary of PWL tracker delta
- List of flagged telemetry anomalies
- List of recommended PM actions

## Non-Negotiables

- Never publish directly. Draft only.
- Do not use the word "safe."
- State confidence explicitly.
