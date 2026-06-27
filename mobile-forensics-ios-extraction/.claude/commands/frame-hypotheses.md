# /frame-hypotheses

Convert the investigative question into a set of **mutually-exclusive, collectively-exhaustive** competing hypotheses — the setup step of Analysis of Competing Hypotheses (ACH). Done before deep-diving the data, to pre-empt confirmation bias.

## Inputs

- The precise investigative question (one sentence, falsifiable).
- Known context (who, what device, what window of interest).
- The data sources expected to bear on the question.

## Steps

1. **Sharpen the question** into a single falsifiable statement (e.g. "The disputed messages were sent from this device by its primary user on 2026-06-26").
2. **Enumerate hypotheses** that together cover the possibility space — include the obvious lead, plausible benign explanations, and the *null* ("the event did not occur as alleged" / "artifact was synced or fabricated").
3. **Check exclusivity & exhaustiveness** — no two hypotheses can both be fully true; together they leave no realistic gap. Merge or split as needed.
4. **For each hypothesis, predict its evidence signature** — what artifacts *should* exist if it were true, and what *should be absent*.
5. Hand the list to `/build-diagnosticity-matrix`.

## Output

`outputs/hypotheses-YYYY-MM-DD.md`: the sharpened question and the numbered hypothesis set (H1…Hn), each with its predicted evidence signature (present + absent) for later diagnosticity scoring.

## Notes

- Always include a "someone/something else" and a "fabrication/sync" hypothesis; their omission is a classic bias trap.
- Predicting *absent* evidence is as important as present — a missing expected log discriminates hypotheses.
