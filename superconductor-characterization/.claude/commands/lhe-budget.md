# /lhe-budget

Forecast liquid-helium consumption and burn-rate headroom for the planned measurement queue, against current tank inventory and recovery throughput. Produces an LHe demand profile and a procurement / queue-throttle recommendation.

## Inputs

- Current LHe inventory: tank dewar volume (L), storage dewar volume (L), last-fill date and quantity (L)
- Recovery plant throughput (L/day liquefied, average over last 30 days) and recovery efficiency (returned mass / boil-off mass)
- Planned measurement queue for the horizon: cryostat × duration × ramp class (no-field, low-field ≤2 T, high-field ≥9 T, persistent-mode dwell, ramp-down)
- Static boil-off per cryostat (L/day at idle) and dynamic boil-off per ramp class (L/T·hr or L/hr at field)
- Quench-loss reserve target (default: 1 quench-equivalent worth of LHe, per magnet)

## Steps

1. Compute baseline static burn for the horizon: Σ (cryostats × static boil-off L/day × horizon days).
2. Compute dynamic burn per planned measurement using its ramp class coefficient (see `context/references.md → Cryogen consumption coefficients`).
3. Add safety reserves: quench-loss reserve + transfer-loss allowance (typically 8–15 % of total transfers).
4. Subtract recovery throughput × horizon × recovery efficiency to obtain *net* burn.
5. Forecast inventory(t) = inventory(0) − cumulative_net_burn(t); identify the first day below the 15 % low-tank threshold.
6. Compare to procurement lead-time. If forecast crosses the threshold inside lead-time, trigger one of: (a) order more LHe, (b) defer low-priority high-field runs (see `/sample-queue-plan`), (c) shift to closed-cycle cryostats where feasible.
7. Emit the burn-rate plot, a per-measurement helium cost table, and a single-paragraph procurement recommendation.

## Output

Markdown report at `outputs/lhe-budget-<YYYY-MM-DD>.md` containing:
- Inventory(t) forecast table (daily)
- Per-measurement helium cost ranking (most → least expensive)
- Procurement recommendation: order now / order by <date> / no action
- A capacity-impact note that feeds `/sample-queue-plan`

## Notes

- LHe latent heat of vaporisation is ~20.7 J/g (~2.6 kJ/L of liquid); a 1 W parasitic heat leak boils ~1.4 L/day. Use this rule-of-thumb to sanity-check vendor-quoted static boil-off.
- Recovery efficiency degrades after compressor maintenance gaps; verify the 30-day rolling figure isn't masking a drift.
- VTI runs at ~1.8 K (superfluid) burn substantially more than 4.2 K bath runs — keep them on a separate cost line.
- A persistent-mode magnet at field has near-zero added burn beyond the static cryostat load; the ramps either side are where the helium goes.
