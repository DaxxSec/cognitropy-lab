# Monthly Spectrum Vitals Report

## Purpose

A recurring (monthly default) status report for a site that fuses control-chart status with longitudinal symptom trajectory. The recipient is typically a non-RF stakeholder (facilities owner, business sponsor) who needs to know whether the spectrum is healthy enough to keep doing what they're doing.

## Prompt Template

```
Compose the monthly spectrum vitals report for site [SITE_NAME], for the period [START_DATE] to [END_DATE].

- **Baseline reference:** [BASELINE_PATH]
- **Primary tracked metrics:** [LIST e.g. "noise floor (median dBm)", "Ch 36 occupancy %", "telemetry packet-loss %"]
- **Active subjects under monitoring:** [LIST_FROM_TRAJECTORY_OR_"--all-active"]
- **SLA / spec limits per metric:** [PROVIDE]
- **Audience:** [E.g. "facilities lead, biomedical engineering, business sponsor — non-RF audience"]

Please:
1. For each primary metric: report current X-bar (or EWMA) value, control-chart status (in-control / OOC + rule fired), and the trend over the period.
2. For each active subject: state current severity tier, trajectory classification (stable-low / stable-elevated / improving-post-intervention / worsening / relapsing-remitting / data-gap), and whether intervention is currently active.
3. Report capability indices (Cpk/Ppk) for each metric against the provided SLA. Verdict per metric (excellent / capable / marginal / not-capable).
4. Highlight follow-up debt: any subject overdue for re-assessment, with the consequence in plain language.
5. Make 1–3 concrete recommendations for the next period — explicit owner, action, due date.
6. Keep the body under 800 words; charts and tables don't count.
```

## Expected Output

- A short executive summary (≤ 5 sentences) in plain language.
- A "vitals" table (one row per metric: value, chart status, capability verdict).
- A "patients" table (one row per active subject: tier, classification, last assessment, intervention status).
- A follow-up debt list.
- A numbered recommendations list with owners and due dates.
- Embedded or referenced trajectory plots from `outputs/trajectories/`.
