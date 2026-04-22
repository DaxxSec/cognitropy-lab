# /trend

Display symptom trajectory for a placeholder across the last N captures of a given instrument.

## Input

- Session placeholder.
- Instrument (ESAS-r, IPOS, PAINAD, Abbey, PPS, …).
- N (default 5).

## Steps

1. Pull the last N captures of the specified instrument for this placeholder from session history.
2. Produce a table: capture date, composite, key items, flags.
3. For each item, describe direction of change across the window (improving / stable / worsening).
4. Flag any items that crossed the team's threshold in the most recent capture.
5. Do **not** interpret cause. Output is descriptive only.
6. "Draft — clinician review required" footer.

## Reminders

- A trend is not a diagnosis.
- A worsening trend is not a treatment recommendation.
