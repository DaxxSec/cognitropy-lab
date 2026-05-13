# new-sample-intake-spec

## Purpose

Use at sample intake to capture every parameter needed for `/sample-queue-plan`, `/lhe-budget`, and the eventual IEC-compliant test report — in one pass, before the sample touches a cryostat. A missed contact spec or sample dimension turns into a re-mount at base temperature, which is the most expensive failure in this lab.

## Prompt Template

```
You are the characterization lab intake agent. I am submitting a new sample for measurement; build the intake spec.

I have a sample to characterize:

- **Sample ID:** [VALUE]
- **Material class:** [LTS NbTi / LTS Nb3Sn / HTS REBCO coated / HTS Bi-2212 round wire / HTS Bi-2223 tape / MgB2 / unconventional]
- **Geometry:** length × width × thickness in mm: [VALUE], substrate or sheath: [VALUE]
- **Contact configuration:** I-pad / V-pad positions, contact material, solder: [VALUE]
- **Expected critical parameters:** Tc [VALUE], Jc target at (T, B) [VALUE], Hc2 expected [VALUE]
- **Priority tier:** [P0 / P1 / P2] with target completion date: [VALUE]
- **Deliverable:** [vendor acceptance per IEC 61788-X / research-grade dataset / qualification for fabrication]
- **Anisotropy / angular sweep required?** [Y / N — if Y, see /jc-anisotropy-map]
- **Field range and temperature range of interest:** [VALUE]
- **Known hazards (radioactive, biohazard, magnetic mounting, embedded permanent magnet, etc.):** [VALUE]
- **Context:** [why this sample, who's waiting, what decision the result drives]

Please:
1. Confirm material class against expected Tc / Jc / Hc2 and flag inconsistencies.
2. Select the minimum measurement set (Phase 1/2/3 per `context/workflows.md → Methodology Phases`) that satisfies the deliverable.
3. Estimate per-measurement service time and total E[S] for the sample using `context/references.md → Service-time / cryogen tables`.
4. Recommend a target cryostat and magnet, with rationale (helium cost, magnet utilisation, angle capability).
5. Output a queue-plan delta: how does adding this sample shift ρ, L, and W for the next 4-week horizon? Reference the latest `/sample-queue-plan` run.
6. Output an LHe burn delta against the current `/lhe-budget` forecast.
7. Recommend a target IEC 61788 part for the eventual report.
8. Flag any hazard that requires safety review before mount.
```

## Expected Output

- Validated intake row appended to `outputs/_intake/intake-log.csv` (one row per sample).
- Measurement plan stub at `outputs/<sample-id>/plan.md` referencing the chosen commands.
- Quantified queue delta and helium delta forwarded to the next `/sample-queue-plan` and `/lhe-budget` invocations.
- Hazard flag, if any, escalated to the lab safety officer before scheduling.
- A go / no-go decision for scheduling within the next planning horizon.
