# /tpf-window

Compute the thermoplastic-forming (TPF) time–temperature processing window — the per-heat time budget in the supercooled-liquid region before crystallization onset — and convert it into a parts-per-heat throughput.

## Inputs

- Kinetic model K(T), Ea, n (from `/kissinger-kinetics`) and the supercooled-liquid bounds Tg, Tx (from `/dsc-landmarks`).
- Viscosity data or VFT parameters (η₀, D, T₀) if available — sets how fast features fill.
- Required forming time per part (fill / emboss / blow time) and the allowable crystalline fraction (e.g. X ≤ 1%).
- Heater/press cycle time (heat-up + form + cool-down + unload) for the throughput figure.

## Steps

1. Read `context/workflows.md` Workflow 3 for the TPF determination method.
2. For a grid of forming temperatures T_form across Tg→Tx, compute **time-to-onset t_x(T_form)** from JMAK at the allowable X: solve X = 1 − exp[−(K(T_form)·t)ⁿ] for t.
3. Estimate **viscosity** at each T_form (VFT) → whether the part can be filled/formed in the required time at that temperature.
4. Compute the **net time margin** = t_x(T_form) − required forming time. Feasible where margin > 0; pick the T_form maximising parts-per-heat while keeping a safety margin (e.g. ≥30%).
5. Convert to capacity: **parts/heat = floor(t_x / cycle-per-part)**; parts/hr = parts/heat × heats/hr.
6. Report the recommended T_form, the usable seconds, parts-per-heat, and the trade-off curve (hotter = faster fill but shorter window).

## Output

`outputs/tpf-window-<alloy>-YYYY-MM-DD.md`: the feasible T_form range, recommended forming temperature, time-to-onset and net margin, viscosity at T_form, parts-per-heat and parts/hr, and the temperature–time trade-off. Feeds `/line-throughput`.

## Notes

- TPF's whole advantage is forming metal like a thermoplastic in the supercooled liquid — but the TTT nose is a **hard deadline**: over-dwell crystallizes the part irreversibly. Treat the window as a takt-time ceiling, not a target to push past.
- A narrow ΔTx alloy may have no usable window for slow-fill features — recommend a wider-ΔTx alloy rather than a hotter, riskier hold.
- Repeated heat cycles accumulate crystallization (additivity) — a reheated part has a shorter remaining window than a fresh one.
