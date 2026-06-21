# /tune-rule

Re-tune an in-production rule whose reliability has drifted — it's storming (fell below the LUF) or has gone silent (drifted above the MUF). Phase 8 correction.

## Inputs

- The drifting rule + its current FOT band.
- Recent alert outcomes (TP/FP feedback from `/triage-tree` branch paths).
- The drift symptom: storming (FP surge) vs silent (no fires when it should).
- Current noise floor + diurnal baseline, and the latest `/space-weather` snapshot.

## Steps

1. Classify the drift:
   - **Storming** → the noise floor rose; the rule is now below its LUF. Cause is usually an environmental change (new log source, fleet growth).
   - **Silent** → the baseline shifted up or telemetry degraded; the rule is now above its MUF, or a blackout opened.
2. Confirm the environment is quiet (K0–2) before measuring anything — never retune during a storm.
3. Refresh the noise floor (`/noise-floor`) and diurnal baseline (`/diurnal-baseline`).
4. Recompute the threshold band (`/threshold-band`); reset the operating point to the new FOT.
5. Re-run the backtest gate (`/backtest-rule`) to confirm recall survived the change.
6. Version-bump the rule and record the root-cause disturbance (the space-weather event that caused the drift).

## Output

`outputs/tune-<rule>-YYYY-MM-DD.md` — drift diagnosis (storming/silent), old vs new FOT, before/after FP load and recall, the root-cause space-weather note, and the new rule version.

## Notes

- Always name the *cause*, not just the new number. A retune without a root cause will drift again next month.
- If every retune lands on a narrower window, the rule is fundamentally fragile on this telemetry — consider a correlation rule or better signal instead of chasing the threshold.
