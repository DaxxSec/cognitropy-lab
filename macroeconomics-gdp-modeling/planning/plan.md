# Active Plan

> Single source of truth for what the agent is currently working on. Pivots go in `planning/pivots/<YYYY-MM-DD>-<topic>.md`.

## Current Focus

**Workspace bootstrap.** `/onboard` not yet run for a real user; default configuration in `context/project.md` describes the assumed US setup.

## Backlog (priority order)

1. Run `/onboard` to capture the actual user configuration.
2. Run `/ingest-vintage` for the configured series set; produce the first sealed manifest entry.
3. Run `/build-nowcast` for the current quarter using the sealed panel.
4. Run `/estimate-model --class bvar` to produce the first horizon-extending model artifact.
5. Establish a 20-quarter pseudo-real-time backtest baseline; record RMSFE in `outputs/forecasts/`.
6. Run `/compare-forecasts` against external benchmarks (GDPNow, NY Fed Nowcast) once a few weeks of own forecasts have accumulated.
7. Decide the cadence of `/release-forecast` if any external publication is planned.

## Open Questions

- Which model class is the headline (the one published) vs. parallel research candidates?
- Is GPG signing required for the release path? If yes, which key fingerprint?
- Backup policy for `outputs/vintages/` — git-lfs, S3, both?

## Done

(Empty until the first run.)
