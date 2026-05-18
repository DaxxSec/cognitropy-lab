# Pre-Fire Test Readiness Review

## Purpose

Use to walk an entire hot-fire test card through the workspace's full pre-fire scorecard before the formal TRR (Test Readiness Review) meeting. Routes the test card and FMEA through `T-*`, `R-*`, `U-*`, `C-*`, and `S-*` and produces a single GO_CANDIDATE / NO_GO assessment with all matrix cells aggregated. Saves the test conductor from running each command individually for a routine fire.

## Prompt Template

```
You are a ground-test propulsion engineer performing the pre-fire risk review for an upcoming
hot-fire test on a stationary thrust stand. Walk the test through the full readiness-review
phases (1–6 in context/workflows.md) and produce a single decision-tree-traced verdict.

Test details:
- **Test ID:** [e.g. "RX-DEV-0042-FIRE-007"]
- **Engine variant + build state:** [engine designation + FMEA version]
- **Propellants + inventory:** [list with masses in kg]
- **Planned burn time + throttle profile:** [seconds, % throttle vs. time]
- **Chamber pressure target:** [bar or psi]
- **Measurement objective:** [development / acceptance / qualification]
- **Stand layout + personnel positions:** [reference to layout drawing]
- **Load cell serial + cal cert reference:** [serial number + cert path]
- **DAQ channel list reference:** [path]
- **Controller architecture:** [software-only / hardware-independent / mixed]
- **Prior anomalies in trailing 5 tests:** [list with dispositions]
- **Context:** [program phase, customer expectations, schedule pressure]

Please:
1. Run `/load-cell-calibration-check` for every cell in use. Reject the package if any cell fails.
2. Run `/thrust-uncertainty-budget` and compare expanded uncertainty to the measurement objective.
3. Run `/test-readiness-risk` and emit the pre/post mitigation 5×5 matrix.
4. Run `/redline-set` and verify 100% coverage of severity I/II failure modes.
5. Run `/range-safety-matrix` and emit per-personnel-position cells.
6. Aggregate to a single GO_CANDIDATE / NO_GO with binding cells named and sign-off authorities listed.
7. Identify the top 5 risks heading into the fire with cell ids and proposed in-fire watch items.
8. Recommend any test-card amendments (throttle range reduction, burn-time cut, propellant inventory reduction, added redlines) before the TRR.
```

## Expected Output

- A single readiness verdict (GO_CANDIDATE / NO_GO_PENDING_SIGNOFF / NO_GO) with the binding cells.
- Roll-up matrices: thrust uncertainty PASS/REWORK, calibration PASS/REJECT per cell, readiness matrix pre/post mitigation, redline coverage cross-check, range-safety per-position cells.
- Top-5 watch list for the fire (which redlines are most likely to trip, which channels need extra eyes, what counts as a "normal" anomaly vs. "stop the test" anomaly).
- Sign-off block listing required authorities by band.
- Explicit caveat that this output is decision support, not the formal TRR record; the TRR remains a human-conducted review.
