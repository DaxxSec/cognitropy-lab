# /failure-hypothesis-rank

Enumerate the candidate root causes for an engine-block failure and assign prior odds, producing the starting posterior the rest of the investigation will update.

## Inputs

- Part identity and intended grade (e.g. CGI ISO GJV-450 diesel block)
- Symptom description and failure location (crack between bore and jacket, scuffed cylinder, separated bulkhead)
- Service context: mileage/hours, overheat or coolant-loss events, lot/date code, single part vs. cluster
- Optional: any composition or visual evidence already in hand

## Steps

1. Build the hypothesis space — list mutually-distinguishable root causes for this part + symptom (casting defect, thermal fatigue, overheat/abuse, mechanical overload, wear/lubrication, plus an "undetermined" catch-all). Confirm each is separable by *some* test.
2. Anchor base rates from `context/references.md` priors table: zero-hours warranty → material/casting tilt; high-mileage field return → service tilt; lot cluster → process-escape tilt.
3. Adjust the prior for any evidence already known (off-spec composition raises the material prior) — but never collapse to certainty.
4. Express priors as probabilities summing to 1, then convert the leading pair to odds for downstream updating.
5. Name, for each hypothesis, the *most diagnostic* test that would confirm or refute it — this seeds the value-of-information plan.

## Output

A `outputs/<case-id>/hypothesis-prior.md` table: hypothesis | prior probability | rationale | most-diagnostic test. This is the input ledger for `/bayes-evidence-update`.

## Notes

- Keep an "undetermined" bucket so the posterior can stay honest when evidence is thin.
- Two hypotheses that no available test can separate should be merged or flagged as jointly-unresolved, not both ranked.
