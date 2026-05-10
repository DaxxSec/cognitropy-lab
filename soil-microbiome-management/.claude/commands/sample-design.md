# /sample-design

Plan or audit replication, cadence, depth, compositing, and storage for a soil-microbiome study.

## Inputs

- Study question (e.g. "Did treatment X shift the microbiome?", "Is soil health trending up?", "How fast does the community recover from fumigation?").
- Available budget (samples per round, sequencing cost, total duration).
- Field constraints (plot count, accessible depths, sampling-window weather).
- Sequencing pipeline preference (16S V4 515F/806R, ITS1F/ITS2, shotgun).

## Steps

1. Read `context/workflows.md` "Designing or Auditing a Sampling Programme".
2. Map the study question to a question class: trend / treatment-comparison / disturbance-recovery / characterisation.
3. Recommend replication: minimum 3 plots per treatment; 4-6 if budget allows.
4. Recommend cadence by question class: monthly for seasonal cycles, dense early (week 1, 2, 4) tapering for disturbance recovery, quarterly to annually for long-term trends.
5. Recommend depth strata: 0-10 cm and 10-30 cm minimum; deeper if subsoil is in scope.
6. Specify compositing protocol: 5-10 cores per plot, mixed in field, subsampled.
7. Specify storage: liquid N flash-freeze or -80°C; dry ice as field minimum.
8. Specify the locked sequencing pipeline (primer set, kit, denoiser, reference DB version) — switching mid-study creates fake biology.
9. Specify covariate capture: temperature, moisture, pH, EC, total C/N, prior management — every visit.

## Output

A markdown plan in `outputs/sample-design-YYYY-MM-DD.md` containing: study question, classification, replication plan, cadence schedule (with dates), depth strata, compositing protocol, storage protocol, sequencing-pipeline lock, and covariate-capture checklist.

## Notes

- If treatments could be confounded with sampling time-of-day → randomise sampling order across treatments.
- If budget forces a choice → trend studies tolerate sparser cadence; disturbance studies cannot.
- Remind the user that storage warmer than dry ice biases the community within hours.
