# /star-rating-confidence — Credibility Interval Around Predicted Consumer Rating

Convert the per-occupant, per-mode posterior injury distributions into a **credibility interval on the consumer rating** (Euro NCAP Adult Occupant, IIHS Good/Acceptable/Marginal/Poor, US NCAP star rating). Designed to be the gate before any rating is published.

## Inputs

- Test ID list comprising the complete rating bundle (e.g. for Euro NCAP Adult Occupant: full-width frontal, frontal MPDB, side mobile barrier, side pole, far-side, oblique, whiplash front + rear).
- Per-test outputs from `/injury-posterior` and `/restraint-likelihood`.
- Rating protocol version (e.g. Euro NCAP 2026, IIHS Small Overlap 2024 revision) — selects the weighting formula.
- Optional: a comparator vehicle's published rating for context.

## Steps

1. **Aggregate posteriors.** For each test in the bundle, pull posterior samples for the body regions that contribute to the rating formula. Maintain joint samples across tests (do not collapse to medians).
2. **Apply the protocol's weighting formula.** Euro NCAP awards points per body region per test, with modifiers; IIHS applies a categorical rating per test then a combined letter. Implement the formula as a deterministic function over the joint posterior sample.
3. **Sample the rating.** For each of N (default 10,000) joint posterior draws, compute the rating; build the empirical posterior over rating outcomes.
4. **Compute the credibility interval.** Median rating, 5th/95th percentile ratings. For star ratings, report the probability mass at each star level. For IIHS, the probability of Good / Acceptable / Marginal / Poor.
5. **Flag publication risk.** If the credibility interval spans more than one rating tier, hold publication; an additional test or re-analysis is warranted. The headline rating that has < 60% posterior mass is not safe to publish.
6. **Comparator context.** If a comparator vehicle's rating is provided, compute the posterior probability that this vehicle's rating is strictly worse / equal / better than the comparator.

## Output

`outputs/<test-id-bundle>/rating/`:
- `rating-posterior.json` — full posterior distribution over rating outcomes.
- `rating-posterior.png` — bar chart of posterior probability per rating tier.
- `publication-risk.md` — go/no-go memo: rating to publish + confidence, or "hold" with the specific tests driving uncertainty.

## Notes

- Euro NCAP and IIHS protocol formulas change yearly; pin the protocol version in the input and store the formula implementation in `outputs/_rating-protocols/<version>.py` for re-use.
- Whiplash protocols use seat-mounted dummies (BioRID) — different injury risk curves than Hybrid III / THOR. Pull the right family in `/injury-posterior`.
- The credibility interval on a rating is far less familiar to consumer publications than a single number; lead the published deliverable with the median, but document the interval prominently in the methodology section.
