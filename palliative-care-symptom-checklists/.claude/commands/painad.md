# /painad

Run a PAINAD (Pain Assessment in Advanced Dementia) observer-rated assessment.

## Input

- Session placeholder.
- Observation context: at rest / during care activity / after care activity.
- Observer placeholder (e.g., "Observer RN").

## Steps

1. Capture each of 5 items (0–2 each):
   - Breathing (independent of vocalization)
   - Negative vocalization
   - Facial expression
   - Body language
   - Consolability
2. Sum to total (0–10). Map to band: 1–3 mild, 4–6 moderate, 7–10 severe.
3. Flag: total ≥ 4, or upswing from prior total < 2 to current ≥ 3.
4. Produce draft note with item scores, band, flags, observation context, "Draft — clinician review required" footer.
5. Append de-identified `work-log` entry.

## Reminders

- PAINAD is for adults with advanced dementia or others who cannot verbally self-report.
- For patients who can verbally self-report, offer `/esas` (item 1: pain) or a numeric rating scale instead.
