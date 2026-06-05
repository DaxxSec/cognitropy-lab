# /abatement-report

Generate a per-shift or per-period bird-abatement service report for a commercial client.

## Inputs

- Shift date(s), site, and falconer/bird(s) deployed.
- Sortie record: number of flights, target species observed, dispersal outcomes.
- Conditions: weather, wind, visibility; any incidents or no-fly periods.

## Steps

1. Log each sortie: time, bird flown, target species present, dispersal result (cleared / partial / reformed).
2. Tally target-species presence at start vs. end of shift to estimate efficacy.
3. Note conditions that limited operations (high wind, fog, bird in molt/off-weight).
4. Record any safety or compliance items (protected non-target species seen, near-miss, equipment).
5. Summarize the period if reporting weekly/monthly: trend in pressure, efficacy, recommendations.
6. Format for the client and archive.

## Output

`outputs/abatement-report-<client>-YYYY-MM-DD.md`: sortie table, target-species before/after counts, efficacy read, conditions/limitations, compliance notes, and (for period reports) a trend summary with recommendations.

## Notes

- Report efficacy honestly, including low days — clients renew on credibility plus results.
- Flag any protected non-target species immediately; abatement must stay within permit conditions.
