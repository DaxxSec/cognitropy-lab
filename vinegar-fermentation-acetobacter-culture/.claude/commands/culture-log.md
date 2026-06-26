# /culture-log

Record a mother-culture maintenance or back-slop event with strain lineage and vigor tracking, so culture health is a trend rather than a guess.

## Inputs

- Mother/culture ID (or assign one for a new lineage).
- Event type: `split`, `feed/back-slop`, `transfer`, `revive`, `discard`.
- Strain/genus if known (or "wild/unknown"), substrate fed, volumes, date.
- Vigor observations: pellicle thickness/appearance, acidity-rise rate, aroma.

## Steps

1. Read `context/workflows.md` §E (maintenance cadence).
2. Resolve or create the lineage record under `outputs/culture/<culture-id>.md` (generation counter, parent ID).
3. Append this event with date, type, substrate, volumes, and vigor notes.
4. Compute time since last feed and flag if the culture has been dormant long enough to risk a slow next-batch lag.
5. Assess health: translucent forming pellicle + steady acidity rise = healthy; sunken inert mass + flat acidity = vitality problem (point to `/troubleshoot-batch`).
6. If the event reveals a reusable lesson (e.g. "this lineage stalls above 9% ABV"), capture it as a `microbiology`/`troubleshooting` KB entry.

## Output

- Updated `outputs/culture/<culture-id>.md` lineage log.
- A health verdict + next-feed recommendation in chat.

## Notes

- Give every mother a stable ID and generation number — lineage is what lets you correlate vigor with strain and handling.
- Dechlorinate water for feeds; chlorine stresses AAB.
- A vigorous, recently fed culture is the cheapest insurance against spoilage in the next batch's lag phase.
