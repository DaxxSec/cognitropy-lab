# Getting Started — 30-Minute Walkthrough

This walkthrough takes you from a fresh corridor to a baseline performance characterization in about 30 minutes, assuming counts and ATSPM are already available.

## Step 1: /onboard (10 min)

Have ready:
- Corridor name and intersection list with controller make/model
- ATSPM URL (or controller log dump)
- Most-recent turning movement count files
- Fleet-mix percentages from your MPO (or use MOVES4 county defaults if unknown)
- Air-quality basin attainment status (epa.gov/green-book)
- Funding source on the table (CMAQ, TSMO, capital)

Run `/onboard` and answer the interview questions. The agent saves your answers into `context/`.

## Step 2: /timing-baseline (15 min)

Run `/timing-baseline`. The agent will:
- Pull programmed timing per intersection
- Pull ATSPM operating reality (Split Monitor, PCD, Approach Volume, Pedestrian Delay)
- Build the HCM 7 capacity model
- Compute v/c, control delay, LOS per critical lane group
- Estimate baseline emissions via CMEM modal lookup
- Save artifacts to `outputs/baseline-{date}/`

Validate: spot-check the modeled corridor delay against your ATSPM "Approach Delay" or a single floating-car run. ±20% is acceptable for a first pass.

## Step 3: /eco-optimize for One Peak (15 min)

Pick the worst peak (usually PM). Run `/eco-optimize`. The agent will:
- Compute Webster's seed cycle
- Search the cycle/split space within constraints (MUTCD ped, agency cap, v/c ceiling)
- Translate every candidate to delay + emissions via CMEM
- Plot the Pareto frontier
- Recommend a knee-point or constraint-bound plan

Output: `outputs/eco-optimize-{peak}-{date}/recommended.md`.

## Step 4: Multi-Peak Loop

Repeat Step 3 for AM, midday, off-peak. Each peak is a separate optimization — these become the time-of-day plans loaded into the controller.

## Step 5: Coordination (if 3+ adjacent signals)

Run `/coordination-design`. The agent picks a common cycle, solves the eco-weighted Maxband, builds the time-space diagram.

## Step 6: Scenario Compare

Run `/scenario-compare` against the baseline. Confirm the recommended plan dominates baseline on at least delay + CO2 (the typical CMAQ test).

## Step 7: MOVES Run on Finalists

Run `/emissions-model --moves` against the chosen plan. This is the regulatory-grade deliverable.

## Step 8: EIA Report

Run `/report-eia` to draft the NEPA CE / CMAQ application. Review, polish, and submit.

## Step 9: Field Deployment

Load timing into controllers, monitor for 30 days via ATSPM, re-tune as needed (corridors often need a small refinement after 1–2 weeks of real demand).

## Tips

- **Start with PM peak.** It's usually the worst and has the most retiming headroom.
- **Don't over-cycle.** If all v/c < 0.7 and cycle > 110 s, your Webster seed is probably too conservative.
- **Validate before optimizing.** Bad volume data → useless optimization. Spend the time on Step 2.
- **Document the methodology.** A good EIA stands on its inputs; a sloppy MOVES run won't survive an FHWA division review.
