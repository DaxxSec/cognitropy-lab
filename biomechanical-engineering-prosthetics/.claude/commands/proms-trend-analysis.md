# /proms-trend-analysis

Statistical trend analysis on patient-reported outcome measures (PEQ, AMP-PRO, PROMIS-PF, Houghton Scale of Use) across encounters — reports trends with within-subject SEM and against published MCID thresholds.

## Inputs

- **PROM dataset** — per-encounter scores per patient per instrument. Long format preferred: `patient_id, encounter_date, instrument, subscale, score`.
- **Instrument coverage** — which instruments are in scope: PEQ (9 subscales), AMP-PRO (1 score 0-47), PROMIS-PF (T-score, computer-adaptive variants OK), Houghton Scale of Use (0-12), and/or domain-specific (LCI-5 for amputee K-level, OPUS modules).
- **Cohort definition** — which patients are included (e.g. all TT fittings completed in the last 12 months; K3/K4 only; specific component family).
- **Time window** — analysis period (typical: trailing 90 days, 180 days, 1 year).
- **MCID source** — citation for the Minimal Clinically Important Difference threshold per subscale (varies by population; cite the source).

## Steps

1. Read `context/references.md` "Outcome measure scales" for instrument-specific scoring, normative ranges, and published MCID values.
2. Validate input: flag patients with <2 encounters in the window (no trend possible); flag instruments with subscales below published reliability thresholds for the population.
3. Per patient × subscale, compute within-subject change: linear regression of score on time-since-baseline OR paired test if only 2 encounters.
4. Aggregate to cohort: report distribution of within-subject slopes (mean, median, IQR), percentage with statistically significant change (p<0.05 after FDR-BH correction across subscales), percentage exceeding MCID.
5. Stratify: by K-level, by time-since-fit (≤90d / 91-180d / >180d), by component family, by fitter. Identify subgroups with disproportionate change.
6. Cross-reference cohort declines with `/socket-fit-control-chart` outputs for the same patients — same-period out-of-control signals in fit data co-occurring with PROM decline = high-confidence fit-causation.
7. Generate cohort memo at `outputs/proms-trends/<YYYY-MM-DD>-<cohort>.md` with: summary distribution per subscale, statistically-significant findings (after FDR), clinical significance check against MCID, subgroup signals, recommended follow-ups.

## Output

A markdown cohort memo containing: cohort definition + N, period, instrument list, per-subscale distribution of within-subject slopes (with CIs), FDR-adjusted significant findings, MCID-exceeding cases, subgroup stratification, recommended next actions (which patients to recall, which subgroups to investigate, which fit-related signals to triangulate against).

## Decision points

- **If sample size N < 30 for any subgroup** → report effect size + 95% CI rather than p-value; under-powered subgroups should not produce decisive claims.
- **If a single fitter accounts for most of the cohort's variation** → blind the analysis from the fitter-ID, re-run to check the signal isn't operator-confounded.
- **If MCID is unpublished for the specific population (e.g. paediatric TF, congenital)** → use the closest-population MCID with explicit caveat OR report "clinically interpretable change" without a threshold.

## Notes

- PEQ subscales vary in within-subject SEM by ~6-12 points depending on subscale (Legro et al. 1998 + subsequent test-retest studies). Quote the SEM alongside any reported change.
- PROMIS computer-adaptive scoring depends on item bank version; results across CAT vs. fixed forms are *not* directly comparable.
- Don't conflate "no significant change" with "stable" — verify the cohort had power to detect MCID before claiming stability. A flat trend with wide CIs is uninformative.
- Pair this analysis with utilisation data (Houghton sub-scales for hours/day worn) — declining PEQ scores in patients who've also reduced wear time tell a different story than declines in actively-using patients.
