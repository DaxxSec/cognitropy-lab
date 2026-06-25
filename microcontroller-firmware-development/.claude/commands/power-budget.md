# /power-budget

Model duty cycle and sleep modes to hit a battery-life target, and price every feature addition in microamps of average current — the energy equivalent of the flash/RAM budget.

## Inputs

- Battery capacity (mAh) and the target life
- The duty cycle: events per hour, active time per event, sleep mode between events
- Per-mode current (run, sleep, stop/deep-sleep, radio TX/RX) from datasheet or measurement

## Steps

1. Lay out the **duty cycle** as time fractions per mode over a representative period.
2. Get the **current in each mode** — prefer a measured ammeter/power-profiler number over the datasheet typical.
3. Compute **average current** = Σ(mode_current × time_fraction); **battery life = capacity ÷ average current**.
4. Identify the **dominant term** (usually radio TX or a leaky always-on peripheral) and target it first.
5. Price any proposed feature in **µA of average current** before accepting it; log the running budget.

## Output

`outputs/projects/<name>/power-budget.md` — the duty-cycle table, per-mode currents, computed average current and battery life, and the dominant-term analysis.

## Notes

- Attack the dominant term (TX duty, deeper sleep, a lower-leakage part) before chasing micro-savings.
- A pricier MCU with much lower stop-mode current can pay for itself in battery — feed that back into `/select-mcu`.
