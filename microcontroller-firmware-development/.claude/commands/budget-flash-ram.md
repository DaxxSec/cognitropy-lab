# /budget-flash-ram

Allocate and track the flash and RAM budget from real `.map`/`size` data, and decide cut-vs-optimize when a feature threatens the reserve — so the binary never overflows two weeks before tape-out.

## Inputs

- Part flash/RAM ceiling and a target headroom reserve (e.g. keep 15–20% free)
- Current `arm-none-eabi-size` totals and the `.map` file for module attribution
- Worst-case stack/heap estimate

## Steps

1. Record the **ceiling** and the **reserve**; compute the spendable budget.
2. Attribute current flash/RAM to modules from the `.map`; save the baseline.
3. On each feature, re-measure; if the reserve is threatened, open a **cut-or-optimize** decision (hand to `/optimize-roi`).
4. Verify the **worst-case stack** fits RAM with margin — stack overflow is silent and corrupts everything.
5. Rank reductions by `bytes_saved ÷ engineering_hours`, apply only enough high-ROI ones to restore the reserve, and stop.

## Output

`outputs/projects/<name>/memory-budget.md` — the ceiling/reserve, per-module attribution, the trend, and any cut/optimize decision with its bytes-per-hour rationale.

## Notes

- Cheap structural wins first — `--gc-sections`, `newlib-nano`, drop an unused HAL — before hand-optimizing code.
- If high-ROI cuts still don't fit, escalate to an **MCU re-spin** (`/select-mcu`) rather than unmaintainable micro-optimization.
