# /amorphicity-qa

Verify that parts are fully amorphous (XRD halo / DSC residual enthalpy / TEM) and set a sampling plan sized so verification does not become the line's new bottleneck.

## Inputs

- Verification data: XRD pattern (halo vs Bragg peaks), DSC residual crystallization enthalpy vs a fully-glassy reference, or TEM/SAED for sub-XRD crystallinity.
- The amorphicity acceptance spec (max crystalline vol%).
- Lot size, QA-station cycle time per test, and the line throughput target (from `/line-throughput`).
- Risk context: process stability, recent yield trend, criticality of the part.

## Steps

1. Read `context/concepts.md` §5 for the verification methods and detection limits.
2. **Verdict per sample:** XRD broad halo + no Bragg peaks = amorphous; emerging sharp peaks = crystalline fraction present. Use **DSC residual enthalpy** (ΔH_residual/ΔH_full) to estimate the amorphous fraction quantitatively; escalate to **TEM/SAED** when crystallinity may be below XRD's ~2–5 vol% floor.
3. **Localize** any crystallinity (surface/skin vs centre) on sectioned samples — drives the root cause (oxygen vs cooling rate).
4. **Size the sampling plan:** choose sampling fraction/AQL from lot size, process stability, and part criticality; check that QA test-rate × required samples stays *below* the line bottleneck rate (Little's Law on the QA queue). If 100% inspection would dominate, justify sampling explicitly.
5. **Disposition** failed lots (scrap / downgrade / rework where possible) and feed the result back to `/crystallization-yield` and `/melt-flux-spec`.
6. Record everything for traceability (alloy, lot, method, convention, operator).

## Output

`outputs/amorphicity-qa-<lot>-YYYY-MM-DD.md`: per-sample amorphous/partial verdict with method and crystalline-fraction estimate, crystallinity localization, the sampling plan (n, AQL, fraction) with its bottleneck check, lot disposition, and root-cause hand-off. 

## Notes

- XRD confirms amorphicity to ~2–5 vol% crystallinity; for high-reliability parts, sample with TEM/SAED to catch nanocrystals XRD misses.
- A capacity-aware QA plan is the point: tighten sampling when yield is unstable, relax it (with justification) once the process is in control, so inspection tracks risk instead of becoming the constraint.
- DSC residual-enthalpy is the fast quantitative proxy; keep a fully-glassy reference ΔH for the alloy on file.
