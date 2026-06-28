# /error-rounds

Diagnostic-error retrospective on a batch that failed in service: name the cognitive or process error and install a guardrail — the morbidity-and-mortality / error-conference analog.

## Inputs

- The failed batch's structured report (or a reconstruction of what was read and decided).
- What actually went wrong on the pass, and what the read concluded.

## Steps

1. Reconstruct the read: what findings were logged, what differential was chosen, what action was taken.
2. Classify the error:
   - **Satisfaction of search** — a co-occurring defect was missed after the first was found.
   - **Anchoring / premature closure** — fixed on one cause (often alginate %) too early.
   - **Adequacy skip** — read a non-diagnostic batch as if it were diagnostic.
   - **Calibration drift** — the recipe/bath moved and no re-titration caught it.
   - **Scale ambiguity** — the burst/texture call was undefined (κ problem).
3. Identify the **single guardrail** that would have caught it (a checklist line, a float test, a re-titration trigger, a definition).
4. Install the guardrail in the FMEA (lower Detection) and/or the workflow; assign an owner.

## Output

`outputs/error-rounds-<batch>-YYYY-MM-DD.md` — the timeline, the named error class, and the one guardrail added. The point is a system fix, not blame.

## Notes

- Favor **repair over punishment**: every failure becomes a guardrail, not a reprimand.
- One guardrail per round — a checklist that grows by ten lines after every failure stops being read.
