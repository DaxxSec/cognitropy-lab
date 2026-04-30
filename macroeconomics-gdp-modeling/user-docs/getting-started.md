# Getting Started

A 30-minute first session that takes you from empty workspace to first sealed nowcast.

## 1. Install prerequisites

```bash
python --version  # 3.10 or 3.11
pip install -r requirements.txt    # if a requirements.txt is present
# or:
pip install pandas numpy statsmodels scikit-learn pyarrow requests
```

Set your FRED API key:

```bash
export FRED_API_KEY=...
```

## 2. Initialise git

If this workspace is not yet a git repo:

```bash
git init
git add .
git commit -m "bootstrap macroeconomics-gdp-modeling workspace"
```

The agent refuses to run any custody operation against a dirty tree, so commit before the first command.

## 3. Run /onboard

Inside Claude Code, run:

```
/onboard
```

Answer the interview questions (jurisdiction, target series, modeling approach, embargo policy, signing policy). The command writes `context/project.md`, `context/role.md`, `context/constraints.md`, `context/for-agent/environment.md`, and bootstraps `outputs/manifests/INDEX.json`.

## 4. Pull the first vintage

```
/ingest-vintage
```

This pulls today's sealed snapshot of every configured series and produces `outputs/manifests/v<today>.json` plus per-series parquet files. Re-run on any new release day; idempotent on no-op days.

## 5. Build the first nowcast

```
/build-nowcast
```

Produces a current-quarter point forecast with 68% / 95% bands and an indicator-contribution decomposition. The fitted model artifact is saved under `outputs/models/`.

## 6. Read the work-log

`work-log/<today>.md` summarises what happened, lists the artifact paths, and names the next recommended command.

## 7. Optional — fit a horizon-extending model

```
/estimate-model --class bvar --lags 4
```

This is the BVAR horseraced against the DFM nowcast. The validation backtest takes a couple of minutes.

## 8. Optional — first comparison

Once you've accumulated a few weeks of nowcasts:

```
/compare-forecasts
```

Compares your forecasts against external benchmarks (GDPNow, NY Fed Nowcast) using realised vintages and a stable later-revision target.

## 9. When you're ready to publish

```
/release-forecast --audience client --gpg-fingerprint <your-key>
```

Produces a self-contained signed bundle under `outputs/forecasts/release__<today>/`. The bundle is what ships externally — never publish numbers outside this workflow.

## What to expect

- The first ingestion seals ~50 KB / series / vintage. Disk grows linearly with retention.
- The first BVAR fit takes ~30s on a typical laptop; the DSGE alternative can take minutes.
- The custody manifest grows by 5–20 entries per active day.
- Every artifact is hash-verifiable; if a hash ever fails, the agent stops and surfaces the discrepancy.

## When something goes wrong

- **Dirty tree refusal:** commit your changes; the agent will not pin a manifest to an uncommitted state.
- **Hash mismatch:** read `context/for-agent/workflows.md` § "Custody Recovery Procedure". Do not silently fix.
- **Embargo violation refusal:** wait until `embargoed_until` lifts, or remove the offending series from the bundle.
- **Schema drift on retrieval:** the agent surfaces the diff; do not coerce silently.
