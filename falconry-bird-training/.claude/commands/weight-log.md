# /weight-log

Build or interpret a flying-weight and condition log, and produce a husbandry summary any stakeholder can read.

## Inputs

- Daily entries: date, pre-flight weight (grams), food given (type + grams), response/behavior note, weather.
- The bird's identity (species, source, band number) and its discovered flying-weight band, if known.
- Optional: body-condition (keel palpation) notes.

## Steps

1. Ingest the entries (CSV/table under `outputs/` or pasted inline).
2. Plot or tabulate weight over time; mark the flying-weight band.
3. Correlate **response** against weight — identify the window where the bird is keen but safe.
4. Flag any **unplanned** drop below the band as a possible "going light" event → recommend `/vet-intake`, not a lower target.
5. Summarize the period: typical flying weight, response quality, flights/feeds, and trend.
6. Write a plain-language husbandry summary suitable for a sponsor, vet, or inspector.

## Output

`outputs/weight-log-YYYY-MM-DD.md` (and/or an updated `outputs/weight-log.csv`): the time series with the flying-weight band marked, the response-vs-weight read, any going-light flags, and a stakeholder-readable summary.

## Notes

- Flying weight is individual and seasonal — discover it empirically; never read it from a chart.
- Advance training on response **at a safe weight**, never on low weight alone.
- A sharp, prominent keel signals low condition even if the scale looks "fine."
