# /defect-stratigraphy

Trace a named crumb fault back through the build to the stage that produced it — stratigraphic root-cause analysis, reading the layers like archaeological strata to find where the damage entered.

## Inputs

- A diagnosis from `/diagnose-crumb` (the named fault and severity).
- The run transcription from `/transcribe-bake` (the deviations and ambient conditions).
- The codex (the intended build) for comparison.

## Steps

1. Build the **stratigraphic column**: list the build stages in order (lock-in → turn 1 → rest → turn 2 → … → proof → bake).
2. For the named fault, walk the column and mark each stage as **consistent / inconsistent** with having caused it, using the deviation log.
3. Identify the **earliest stage** whose deviation can explain the fault — earlier causes propagate, so the deepest stratum wins.
4. Distinguish **primary cause** from **aggravating factors** (e.g. warm lock-in primary; short rest aggravating).
5. State the **corrective action** at the originating stage, with the target window from `context/references.md`.

## Output

A root-cause record at `outputs/rootcause-<product>-<date>.md`: the stratigraphic column, the implicated stage, primary vs aggravating factors, and a specific corrective action.

## Notes

- Faults caught at a shallow stratum (proof, bake) are often recoverable; deep-stratum faults (lock-in temper, turn welding) usually mean a rebuild.
- One fault can have layered causes — name them in order of depth, not severity.
