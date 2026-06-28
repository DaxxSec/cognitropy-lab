# /fmea-process

Build or maintain the spherification process FMEA — today's technique. Enumerate failure modes, score Severity × Occurrence × Detection, and rank corrective work by risk.

## Inputs

- The process step list (hydrate → rest → buffer → dose → form → bath → rinse → hold).
- Historical findings from past `/read-batch` and `/structured-report` runs (for Occurrence).
- The S/O/D scales in `references.md`.

## Steps

1. For each process step, list **failure modes** and their **effects** on the plate/guest.
2. Score each on 1–10: **Severity** (effect), **Occurrence** (use report frequencies), **Detection** (10 = nearly impossible to catch before service).
3. Compute **RPN = S × O × D**; optionally add **AIAG-VDA Action Priority** (H/M/L).
4. Rank descending; assign a corrective action + owner to every High-AP / top-RPN item. Prefer **detection** controls (a float test, a pH check) when D dominates.
5. Re-score after actions land; record the RPN/AP trend.

## Output

`outputs/fmea-spherification.md` — the living FMEA table (step, mode, effect, S, O, D, RPN, AP, action, owner, status) plus the trend since last revision.

## Notes

- Act on **Severity 9–10** modes (allergen mislabel, choking-size sphere) regardless of RPN — RPN never overrides a safety mode.
- When RPN is Detection-driven, add an inspection step rather than re-engineering the recipe; that's the cheapest risk reduction.
