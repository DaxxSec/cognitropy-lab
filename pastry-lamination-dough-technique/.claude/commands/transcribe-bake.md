# /transcribe-bake

Diplomatically transcribe an actual production run against its codex — recording exactly what happened, deviations and all, the way a diplomatic transcription preserves a text including its scribal errors.

## Inputs

- The relevant codex (from `/codify-lamination`).
- The run log: actual dough/butter temps, actual rest times, ambient temperature and humidity, oven readings, timings.
- Any in-process corrections or improvisations the baker made.

## Steps

1. Lay the run **beside** the codex stage by stage (lock-in, each turn, proof, bake).
2. Record the **actual** value at each stage next to the **specified** value; mark every divergence with a Δ.
3. Capture corrections faithfully — note what was changed and when, without smoothing it into the spec.
4. Log **ambient conditions** (T/RH) prominently — they are the most common silent driver of lamination drift.
5. Summarise the deviation set: which Δ's are within tolerance and which are candidates for `/diagnose-crumb` / `/defect-stratigraphy`.

## Output

A transcription at `outputs/run-<product>-<date>.md`: a spec-vs-actual table with Δ markers, an ambient-conditions block, and a flagged list of out-of-tolerance deviations.

## Notes

- **Faithful first, judgement later.** Do not normalise the record to match the codex — the value of the transcription is precisely the deviations it preserves.
- One transcription per run; never overwrite a prior run's record (the archive is the diagnostic trail over time).
