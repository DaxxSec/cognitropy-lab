# Getting Started (for the human)

## 1. Read before you run anything
- `README.md` — what this workspace does and does not do.
- `context/constraints.md` — especially the **no real PII in committed files** rule.

## 2. Initialize
Run `/onboard`. Take 5 minutes. Be honest about caveats.

## 3. Pick a test subject
Use a fictional profile to practice:
- Clearance: Secret
- Tier: T3R
- Eligibility: 2022
- Mission criticality: 3
- Prior issues: Guideline F only (moderate, mitigated)

Run `/intake-subject` and make the ID `SUBJ-0001`. Inspect `outputs/subjects/SUBJ-0001/baseline.md`.

## 4. Your first drift scan
Run `/drift-scan SUBJ-0001`. The agent will walk you through each guideline. Answer "no change" for most; inject a synthetic signal on one (e.g., "subject reported a new $12k credit card debt") and see how the composite and trend respond.

## 5. Plan reinvestigation
Run `/schedule-reinvestigation SUBJ-0001` to get your first condition-based plan.

## 6. Tune
Look at `resources/risk-scoring-rubric.md`. Change the weights to match your mission. Re-run the scan. Confirm the recommendations change in a direction you'd expect.

## 7. Adopt
Once the synthetic flow feels right, begin intake on real (pseudonymized) cases. Keep the `context/constraints.md` rules in front of you.
