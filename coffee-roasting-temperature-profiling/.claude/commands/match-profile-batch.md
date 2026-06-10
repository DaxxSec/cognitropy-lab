# /match-profile-batch

Score a production batch against its golden/reference profile and flag out-of-tolerance batches — the reproducibility and QC gate.

## Inputs

- The golden profile (markers, times, RoR shape, DTR, expected weight-loss band) and its version.
- The batch's roast log + drop weight + charge weight.
- Tolerances (defaults if unset: TP ±5 s, dry-end ±15 s, FC ±15 s, drop time ±15 s, DTR ±2 pts, weight loss ±0.7 pt) — tune per roastery.

## Steps

1. Read `context/concepts.md` ("markers") and `context/references.md` (RoR/DTR + weight-loss bands).
2. Align the batch curve to the golden by charge/TP; tabulate each marker's delta (batch − golden) in time and BT.
3. Compute DTR and weight loss for the batch; compare to the golden's band.
4. Score: count markers within tolerance; classify the batch **in-tolerance / drifting / out-of-tolerance**. Note any RoR-shape divergence (crash/flick) even if endpoints match.
5. If out of tolerance, route to `/diagnose-roast-curve` and recommend a disposition (release / quarantine / rework / blend-down).
6. Append the batch's score to the profile's history so drift over the lot's life is visible.

## Output

`outputs/batches/<batch-id>-match-YYYY-MM-DD.md` — the marker-delta table, DTR + weight-loss comparison, the in/out verdict with the failing markers named, and the disposition. Score also appended to `outputs/profiles/<sku>-history.md`.

## Notes

- Endpoint match is necessary but not sufficient — a batch can hit FC and drop on time yet crash in between; check the RoR shape too.
- Persistent one-direction drift (every batch FC later) usually means a machine/calibration change, not random variation — re-verify with `/calibrate-roaster`.
- This is also the Workflow D recall tool: pulling all batch scores for a lot bounds whether a defect is one batch or the whole lot.
