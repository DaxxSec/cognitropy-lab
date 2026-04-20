# /adjudicate

Produce an adjudicative analysis draft for human review. Applies the SEAD 4 whole-person concept.

## Inputs
- `SUBJ-ID` (required).
- Optional: specific guideline(s) to emphasize.

## Steps
1. Load baseline and the most recent drift scan.
2. For each guideline with score ≥ 3:
   a. Identify disqualifying conditions observed (quote from `resources/sead-4-adjudicative-guidelines.md`).
   b. Identify mitigating conditions observed.
   c. Cite evidence pointers (scan file, note file, alert ID).
3. Walk the **nine whole-person factors** explicitly:
   1. Nature, extent, seriousness
   2. Circumstances
   3. Frequency and recency
   4. Age/maturity at time of conduct
   5. Voluntariness of participation
   6. Rehabilitation
   7. Motivation
   8. Coercibility
   9. Likelihood of recurrence
4. Draft an **analyst lead**, never a determination. Acceptable phrasings:
   - "For analyst consideration: …"
   - "Recommend further inquiry on Guideline X."
   - "Recommend referral to the adjudicator."
5. Save to `user-docs/subjects/<id>/adjudicative-memo-YYYYMMDD.md`.
6. Append to `work-log/YYYY-MM-DD.md`.

## Output format
Markdown with a YAML header (id, scan reference, drafted by agent) plus three sections: Disqualifying Conditions, Mitigating Conditions, Whole-Person Analysis, Analyst Lead.

## Guardrails
- Never write "the subject's clearance should be denied/revoked."
- Never include un-redacted PII in the memo.
- Always include the standard disclaimer: *"This draft is a reasoning aid. The adjudicative determination rests with the cognizant adjudicative authority."*
