# Tools

How the agent uses external tooling. None of these are required — the workspace gracefully degrades to pure markdown.

## Markdown + git

The core stack. Logs are markdown; rules are YAML in markdown's neighborhood; reviews are markdown. `git` is the audit trail for every rule and review.

Recommended `.gitattributes` for the workspace:

```
work-log/*.md      diff=markdown
outputs/rules/**   text eol=lf
outputs/reviews/**  text eol=lf
```

## YAML Rule Linter

Optional `yamllint` (`pip install yamllint`) catches malformed rules early.

```
yamllint outputs/rules/draft/ outputs/rules/active/
```

## ffmpeg (for Tier 1+)

Used to extract frame-accurate timestamps from rehearsal video.

```
ffmpeg -i rehearsal.mov -vf "showinfo" -f null - 2>&1 | grep pts_time
```

## Python (for Tier 3)

Small DSP scripts, none of which are required by the workspace.

- IMU integration (orientation drift correction): `scipy.signal`
- Servo telemetry FFT (bearing-wear detection): `numpy.fft`
- Joint-angle smoothing: `scipy.signal.savgol_filter`

The agent will offer to write a one-off script to `outputs/scripts/` rather than blocking the workflow.

## Video Annotation

Tier 1 puppetry video annotation usually happens in:

- **Kinovea** (free, kinematic-focused) — for joint-angle measurement.
- **ELAN** (free, linguistic-annotation tool widely used in dance / performance studies) — for Laban Effort annotation.
- **DaVinci Resolve / Premiere** — for clip-marker-based annotation; export markers as CSV; the agent can ingest CSV markers into a `work-log/` event table.

## Detection-as-Code Workflow

The rule set follows detection-as-code conventions transplanted from cybersecurity:

- Every rule change is a git commit.
- Active rules are tagged in commits with `[rule:<slug>]`.
- Peer-review records reference the commit SHA they reviewed.
- Tunings bump the rule's `version:` field.

## Optional CI

If the company runs CI on this repo, the `/peer-review` records can be enforced as required-status-checks before merge — same pattern used by Elastic's `detection-rules` repo on GitHub.

## MCP Server Recommendations

If the agent runs in an MCP-aware environment:

- `filesystem` — read / write logs, rules, reviews.
- `shell` — `git log`, `git diff`, `yamllint`, `ffmpeg` invocations.
- `python` — small DSP scripts at Tier 3.
