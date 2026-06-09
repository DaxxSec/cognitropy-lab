# /plan-sediment-basin

Size a sediment basin from storm sediment-yield demand and trap efficiency, then project storage drawdown to a design life and a cleanout cadence — capacity drawdown and refresh, explicitly.

## Inputs

- Drainage area and the RUSLE/MUSLE factors for the contributing slope.
- Design storm peak Q and runoff volume (from `/forecast-runoff-capacity`).
- Target trap efficiency or particle-size distribution to capture.
- Outlet/spillway configuration (principal + emergency).
- Acceptable cleanout interval (operational constraint) or target design life.

## Steps

1. Read `context/concepts.md` "Sediment storage & trap structures" and "RUSLE" (MUSLE).
2. Estimate **single-storm sediment yield** with MUSLE `Y = 11.8·(Q·qₚ)^0.56·K·LS·C·P`, and an annual sediment-delivery estimate from RUSLE A × delivery ratio.
3. Size live (sediment) storage volume; set the required surface area / detention time for the target settling velocity.
4. Estimate **trap efficiency** (Brune curve from capacity/inflow ratio) and confirm it meets the target for the design particle size.
5. **Capacity drawdown:** project stored sediment accumulation per year → time for live storage to fill = **design life**. Utilization(storage) = stored/live-volume over time.
6. Derive the **cleanout cadence** (capacity refresh): the interval that keeps utilization below the trap-efficiency-collapse threshold; hand to `/schedule-maintenance-capacity`.
7. Size the principal + emergency spillway to a higher return period so the basin passes large storms without embankment overtopping.

## Output

`outputs/basins/sediment-basin-<site>-YYYY-MM-DD.md` — live + total storage, surface area / detention time, trap efficiency, sediment-yield demand, the drawdown curve to design life, the cleanout cadence, and spillway sizing.

## Notes

- A basin without a funded cleanout cadence silts to zero and trap efficiency collapses — the refresh schedule is part of the design.
- Emergency spillway return period must exceed the principal storage design storm or the embankment is the failure point.
- For permanent water-quality detention vs temporary construction basins, the design storm and standards differ — state which regime applies.
