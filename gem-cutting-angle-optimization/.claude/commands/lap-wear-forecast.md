# /lap-wear-forecast — Forecast Lap Dressing / Replacement

Track a lap's flatness and cut-rate decay over usage and forecast when it needs dressing, recharging, or replacement — keeping lap-induced angle error and polish loss inside budget.

## Inputs

- Lap identity: grit/type (e.g. 1200 sintered diamond, BATT polish lap) and its cumulative machine-hours / stones.
- Current condition: flatness deviation (dial sweep across the lap, µm), and cut-rate proxy (time-to-flat for a standard facet vs the lap's baseline).
- (Optional) visible glazing / loaded grit / worn-through plating notes.

## Steps

1. Log the reading (date, hours, flatness µm, cut-rate ratio, notes) to the lap's record in `outputs/`.
2. Trend flatness deviation and cut-rate ratio over the lap's history.
3. Compare against thresholds in `context/references.md`: flatness watch ~12–25 µm / limit > 25 µm; cut-rate decay watch ×1.3 / dress-or-recharge at ×2.
4. Distinguish the failure mode: **glazing** (cut-rate decay, fixable by dressing/recharging) vs **dishing/wear** (flatness loss, may need resurfacing or replacement) vs **plating worn through** (replace).
5. Forecast hours/stones to the relevant threshold (RUL) and recommend the action and its timing.

## Output

A lap forecast: current flatness + cut-rate, trends, failure mode, RUL, and a recommended dress/recharge/replace action with target timing. Save/append to `outputs/lap-<id>-forecast.md`.

## Notes

- A dished lap shifts delivered angle with radial position — it corrupts geometry, not just polish; treat flatness as an angle-budget item, not cosmetics.
- Glazed fine-polish laps recover with a charge/dress; worn sintered laps lose plating and must be replaced.
- Match lap action to the cutting calendar — dress before a fine-meet-point job, not in the middle of one.
