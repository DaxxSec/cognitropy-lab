# Report Templates

> User-facing report templates. The `/post-show-report` command produces these in `outputs/reports/`; this document explains the shape and how to read it.

## Post-Show Report Shape

The post-show report borrows from cybersecurity post-incident write-ups. Each section answers a specific question:

| Section | Question Answered |
|---|---|
| Summary | "What happened, in one paragraph?" |
| Timeline | "What happened, in order?" |
| Detected Anomalies | "Which rules fired, and was each firing real?" |
| Calibration Findings | "What was off-baseline, and by how much?" |
| What Went Well | "What do we want to preserve?" |
| What Surprised Us | "What's a candidate for a new rule or a tuning?" |
| Action Items | "Who is doing what, by when?" |
| Rules Affected | "Which rules touched this performance?" |

## Example Skeleton

```markdown
# Post-Show Report — The Tempest (touring) — 2026-05-01

## Summary

Friday-evening proscenium house at the Smith Center. 612 in attendance. Show
ran clean except for a brief slack-pose drift on Prospero's right shoulder
during 4.2 (the magic-circle scene). One existing rule fired
(`string-system-drift--right-shoulder-stretch`); disposition: tune
threshold from 4mm to 5mm to handle the new venue's humidity profile.

## Timeline

### Act 1
- ...

### Act 4 — scene 2 (the magic circle)
- 1:47:12 — string_tension event: prospero/right-shoulder-support, 5.3mm
  drift from baseline. Rule `string-system-drift--right-shoulder-stretch`
  v1.0 fired. Disposition: real anomaly; venue humidity ~62% RH (home
  baseline 45%); proposed tune.

## Detected Anomalies

| Rule | Version | Firings | Disposition |
|---|---|---|---|
| string-system-drift--right-shoulder-stretch | 1.0 | 1 | tune (humidity-dependent threshold) |

## Calibration Findings

(none — pre-show audit clean)

## What Went Well

- Bunraku-style Ariel handoff at 2.3 was clean across three iterations.
- Mateo's debut as second-string Prospero handler held the cue list within
  the senior tier (no `omozukai-hidari-phase-lag` firings).

## What Surprised Us

- Backstage temperature was 8°C above home baseline; we have no
  temperature-aware rule for marionette mechanism drift. Likely worth a
  draft.

## Action Items

| Action | Owner | Deadline | Peer-review required? |
|--------|-------|----------|-----------------------|
| Tune string-system-drift--right-shoulder-stretch threshold for humidity | Lena | 2026-05-03 | yes |
| Draft `tactic.environment-induced.technique.thermal-shift` rule | Mateo | 2026-05-08 | yes |
| Refresh prospero-marionette baseline at next break | Mateo | 2026-05-04 | yes (baseline review) |

## Rules Affected

- `outputs/rules/active/string-system-drift--right-shoulder-stretch.yml` (tuning queued)
- `outputs/rules/draft/<new>` (proposed)
```

## Reading a Report

When reviewing someone else's post-show report:

1. Read **Summary** first — orient.
2. Skim **Detected Anomalies** — see what fired.
3. Read **What Surprised Us** — this is where new rules originate.
4. Look at **Action Items** — anything you own?
5. Only then read the full **Timeline** — most readers don't need the play-by-play.

## Reports as Training

Reports accumulate into the company's institutional memory. After 6–12 months, a new performer's onboarding includes reading the last quarter's reports — they are the most efficient way to understand what kinds of failures the company actually sees, and how the company has historically responded.
