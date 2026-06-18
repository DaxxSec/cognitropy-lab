# tpf-process-window-card

## Purpose

Produce a shop-floor process-window card for a thermoplastic-forming step: the safe forming temperature, the time-to-onset budget, and the parts-per-heat throughput. Use when releasing a TPF operation to production or revising one.

## Prompt Template

```
You are a BMG foundry process engineer writing a TPF process-window card for the shop.

Operation:

- **Alloy + supercooled-liquid bounds (Tg, Tx, K):** [VALUE]
- **Crystallization kinetics (Ea, n, K0):** [VALUE]
- **Required forming time per part (s):** [VALUE]
- **Allowable crystalline fraction (X):** [VALUE — e.g. 1%]
- **Press/heater cycle time (s):** [VALUE]
- **Context:** [feature geometry, viscosity/VFT data if any]

Please:
1. Compute time-to-onset t_x(T_form) across the supercooled-liquid region at the allowable X.
2. Recommend the forming temperature that maximises parts-per-heat while keeping a ≥30% time margin.
3. State viscosity at the recommended T_form and whether features can be filled in the required time.
4. Give parts-per-heat and parts/hr, and the temperature–time trade-off in one line.
5. Add the hard-deadline warning (over-dwell crystallizes the part) and any reheat-accumulation caveat.
```

## Expected Output

- Feasible T_form range and the recommended forming temperature.
- Time-to-onset, required forming time, and net margin.
- Parts-per-heat and parts/hr throughput.
- A one-line operator caution about the TTT-nose deadline and reheats.
