# /forecast-runoff-capacity

The capacity-planning core: forecast design-storm runoff demand, compare it against a structure's conveyance/storage capacity across return periods, and report utilization, headroom, and overtopping risk.

## Inputs

- Drainage area, land cover, soil hydrologic group, and slope.
- Time of concentration Tc (or the data to estimate it).
- IDF / rainfall-frequency source (e.g. NOAA Atlas 14) for the return periods of interest (e.g. 2, 10, 25, 100-yr).
- The structure's capacity (Q_cap from `/size-grassed-waterway` / `/design-terrace-interval`, or storage volume).
- Design return period (the service-level target).

## Steps

1. Read `context/concepts.md` "Runoff hydrology" and "The capacity-planning analogy".
2. Estimate Tc; for each return period read the design intensity i (at duration = Tc) from the IDF source.
3. Compute peak runoff **demand**: rational `Qₚ = C·i·A` for small areas, or CN method `Q=(P−0.2S)²/(P+0.8S)` for larger/ungauged areas — state which and why.
4. Build the demand-vs-capacity table across return periods: Qₚ (or runoff volume), Q_cap (or storage), **utilization = Qₚ/Q_cap**, and **headroom** (freeboard depth remaining, or spare storage).
5. Identify the return period at which utilization crosses 1.0 — that is the structure's true capacity ceiling and the overtopping threshold.
6. State the **residual risk**: at storms above the design return period, what happens (safe overflow path vs uncontrolled breach)? A design without a safe overflow path is incomplete.

## Output

`outputs/capacity/runoff-capacity-<structure>-YYYY-MM-DD.md` — the demand/capacity/utilization/headroom table across return periods, the overtopping threshold, the design return period highlighted, and the documented residual risk.

## Notes

- Lengthening Tc (contouring, longer flow paths) lowers peak intensity and demand — a free capacity gain worth noting.
- Rational method validity fades above ~80–200 ac; switch to CN/TR-55 for larger drainages.
- This command produces the utilization numbers that `/stress-test-design-storm` escalates and that the bottleneck ranking depends on.
