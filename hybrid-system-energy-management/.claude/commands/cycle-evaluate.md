# /cycle-evaluate

Run a controller against standard drive cycles and report fuel / emissions / SOC.

## Inputs

- Controller specification or pointer to the implementation (Simulink model, Python `do-mpc` setup, etc.).
- Cycle list: any subset of `WLTP-class-3b`, `CLTC-P`, `FTP-75`, `HWFET`, `ARTEMIS-Urban/Road/Motorway`.
- Initial conditions: start-SOC, ambient temperature, fuel grade.
- For PHEV: CD-only, CS-only, or full SAE J2841 utility-factor weighting.

## Steps

1. Read `context/references.md` for the cycle definitions and expected reporting units.
2. Validate vehicle parameters and battery state are identical across all candidates being compared.
3. For each cycle:
   - Set initial SOC and temperature.
   - Run the controller through the speed trace.
   - Log per-step (SOC, motor torque, engine torque, fuel rate, electrical power flow).
4. Aggregate per-cycle metrics: fuel consumption (L/100km), CO₂ (g/km), net ΔSOC (%), peak/RMS motor & engine torque, battery throughput (Ah).
5. For PHEV: compute the J2841-weighted result combining CD and CS phases at the regional utility factor curve.
6. Tabulate side-by-side with any prior baseline runs.

## Output

A markdown file `outputs/cycle-eval-YYYY-MM-DD.md` containing the per-cycle table, the J2841-weighted summary if applicable, and any notes on cycles where the controller approached a constraint (motor torque limit, battery power limit, SOC bound).

## Notes

- Net ΔSOC > ±1% on a CS-mode cycle = result is suspect; either the initial SOC was wrong or the controller is cheating.
- Cold-start cycles (FTP-75 phase 1) dominate HEV results; report them separately, not just the composite.
- Always state the simulator (Autonomie, GT-SUITE, FASTSim) and the model resolution — comparisons across simulators need calibration.
