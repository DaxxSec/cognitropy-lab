# Broken Emulsion Triage Prompt

## Purpose

Use this prompt the moment an emulsion fails, to classify the failure, recover the batch if possible, and assign a root cause that fixes the formula rather than the symptom.

## Prompt Template

```
You are diagnosing a failed emulsion. Work the break-diagnosis decision tree; distinguish creaming (re-mixable) from a true coalesced break from a thermal curdle.

My emulsion failed:

- **Sauce type:** [cold mayo/aïoli / warm hollandaise/béarnaise / vinaigrette]
- **Symptom:** [greasy/oily / curds or grains / weeping / too thin / split]
- **Does re-whisking re-blend it?** [yes = likely creamed / no]
- **Process so far:** [oil-addition rate, oil:water ratio, temperature reached, emulsifier used]
- **Batch value / can I afford to restart?:** [salvage priority]

Please:
1. Classify the failure (creamed / coalesced break / thermal curdle).
2. Prescribe the exact repair pathway, step by step, for this sauce type.
3. If unrecoverable, give the restart procedure.
4. Assign the most likely root cause and the single variable to change next time.
5. State what to record so the next review round addresses the cause.
```

## Expected Output

- A failure classification with the reasoning.
- A step-by-step repair or restart procedure.
- A named root cause and the one variable to change.
- The log entry to feed back into `/formula-normalize`.
