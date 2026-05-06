# Session Log Template

Copy this template into `work-log/<YYYY-MM-DD>-<engagement-name>.md` at the start of each session.

```markdown
# Session: <YYYY-MM-DD> — <engagement-name>

## Setup
- SDR: <model + serial>
- Reference clock: <internal / GPSDO / external 10 MHz>
- Antenna: <description>
- Calibration evidence: <path or "not yet run">
- Authorisation document: <path>

## Captures Taken Today
| Capture | Center | Sample rate | Duration | SNR | Notes |
|---------|--------|------------:|---------:|----:|-------|
|         |        |             |          |     |       |

## Commands Run
| Time | Command | Capture / Args | Outcome | Notes |
|------|---------|----------------|---------|-------|
|      |         |                |         |       |

## Posterior Snapshots
- Hop rate (latest): <mean ± CI>
- K (latest): <mean ± CI>
- Sequence type: <posterior tuple>
- Jammer activity: <none / narrowband / sweep / follower>

## Decisions
- (e.g. "Re-ran /dehop-bayes with N_int = 0.85*dwell because per-dwell quality dropped to 0.6")

## Open Questions / Followups
- ?

## Next Session
- ?
```

## Logging Conventions

- One file per session per engagement.
- Always include the calibration evidence link, even if it's a stale calibration.
- Always cite the SigMF metadata path of every capture referenced.
- When a posterior contradicts a prior assumption (e.g. user expected 100 hops/s, posterior says 1600 hops/s), document the surprise and update the prior used in subsequent runs.
- When a downstream demod fails after a successful dehop, document why; this often points to dwell mis-estimate or channelizer boundary mismatch.

## Workspace Genesis

Workspace created: 2026-05-06 (Cognitropy day 42, RF/SDR/Signals × frequency hopping analysis × Bayesian probability assessment).
