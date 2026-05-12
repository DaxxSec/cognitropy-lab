# /onboard — Initialize the GDP Modeling Workspace

Run an interview to populate `context/project.md`, `context/role.md`, `context/constraints.md`, and `context/for-agent/environment.md`. Then validate that the operating environment can satisfy the chain-of-custody policy.

## Required Inputs (gather via interview)

- **Target jurisdiction(s):** country or region (e.g. United States, euro area, Brazil).
- **Target series:** primary GDP series (e.g. `GDPC1`, `CLVMNACSCAB1GQEA19`) and any high-priority components (consumption, investment, net exports, IP, payrolls).
- **Modeling approach:** top-down expenditure / bottom-up nowcast (DFM/MIDAS/bridge) / BVAR / DSGE / ML regressor / mixture.
- **Forecast horizons:** nowcast (current quarter), short-term (h=1..4), medium-term (h=5..12).
- **Vintage retention policy:** how long sealed vintages must persist (legal minimum, internal policy).
- **Publication regime:** internal-only / client research / public report / regulator submission.
- **Signing keys:** is GPG signing required on release manifests? If so, which key fingerprint?

## Steps

### 1. Interview the user
Ask each of the inputs above. Default to FRED for US, Eurostat for euro area, OECD MEI for cross-country. If the user has Bloomberg/Refinitiv access, record license restrictions.

### 2. Write `context/project.md`
Capture: jurisdiction, target series with full IDs, component series, modeling approach, horizons, expected publication cadence.

### 3. Write `context/role.md`
Capture: the user's role (e.g. desk strategist, central bank researcher, sovereign analyst, methodology auditor), their experience with vintages, and their tooling comfort (Python / R / Stata).

### 4. Write `context/constraints.md`
Capture: data licensing (which sources can be redistributed), embargo handling, conflict-of-interest disclosures, internal review steps required before publication.

### 5. Write `context/for-agent/environment.md`
Probe the local environment:
- Python version, presence of `pandas`, `statsmodels`, `arch`, `scikit-learn`, optional `pymc`, `dynamax`, `linearmodels`.
- Presence of `git` (required — every model fit pins to a commit) and `gpg` (optional — only if signing).
- API keys present in env (`FRED_API_KEY`, `OECD_API_KEY` if needed). Never write the key value to context — only its presence.
- Disk available for sealed vintages (default budget: 2 GB / year of daily snapshots for a typical series set).

### 6. Bootstrap the custody index
Create `outputs/manifests/INDEX.json` with `{ "schema": 1, "items": [] }` if not present. This is the append-only ledger for evidence and run records.

### 7. Validate
Confirm: git repo is clean, the user can authenticate to the chosen data source, the disk budget is met, and (if signing) `gpg --list-secret-keys <fingerprint>` succeeds.

### 8. Write a `work-log/<YYYY-MM-DD>.md` entry
Record the onboarding session: jurisdictions, series, approach, environment summary, any unresolved gaps.

## Output

A populated `context/` tree, a bootstrap `outputs/manifests/INDEX.json`, and a dated work-log entry. The agent then reports back to the user with a one-paragraph summary and the first recommended next command (typically `/ingest-vintage`).
