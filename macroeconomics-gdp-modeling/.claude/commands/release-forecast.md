# /release-forecast — Build a Sealed, Signed Forecast Package for Publication

Assemble a publication-ready forecast bundle with a complete custody manifest. The output is what ships externally and what auditors can use to reproduce every published number.

## Required Inputs

- Forecast artifacts to publish (one or more JSON files under `outputs/forecasts/`).
- Audience: `internal`, `client`, `public`, `regulator`.
- Cover note: short narrative paragraph(s) the agent expands from `work-log/` notes.
- Optional GPG key fingerprint — required if `audience` is `client`, `public`, or `regulator`.

## Steps

### 1. Validate prerequisites
- Git working tree clean.
- All referenced forecast artifacts exist and are listed in `outputs/manifests/INDEX.json`.
- For each forecast, every input vintage referenced is also sealed and present.
- For each model artifact referenced, the joblib file is present and its hash matches the manifest.

If any check fails, abort and produce a gap report — never publish a forecast that cannot be reconstructed.

### 2. Resolve full lineage
Recursively walk: forecast → model artifact → input vintages → raw response files. Build a flat closure of every artifact required to reproduce the forecast bit-for-bit.

### 3. Assemble the release bundle
Create `outputs/forecasts/release__<YYYY-MM-DD>/`:
- `forecast.json` — the published numbers (point, bands, decomposition).
- `cover-note.md` — the narrative.
- `manifest.json` — the custody manifest (full lineage closure with sha256 of every artifact).
- `inputs/` — copies (or symlinks documented in manifest) of every sealed vintage parquet referenced.
- `models/` — copies of every model joblib referenced.
- `code-pin.txt` — the git SHA, plus `git diff --stat HEAD` (must be empty).
- `library-versions.txt` — `pip freeze` output for the active environment.

### 4. Sign
If GPG key fingerprint provided:
- `gpg --detach-sign --armor --local-user <fp> manifest.json` → `manifest.json.asc`.
- Optionally also sign `forecast.json` for external consumers who want to verify the headline number independently of the manifest.

### 5. Append to the custody index
Add a `kind: "release"` entry to `outputs/manifests/INDEX.json` with the bundle directory, signing key fingerprint, audience, and timestamp.

### 6. Optional — produce a reproducibility receipt
A short markdown file at the bundle root (`README.md`) explaining: how to verify signatures, how to replay vintages, how to refit the model from sealed inputs. This receipt is what external auditors read first.

### 7. Final integrity check
Re-hash every file in the bundle and confirm the hashes match the manifest. Any mismatch aborts the release and surfaces the offending file.

## Output

A self-contained, optionally-signed release bundle under `outputs/forecasts/release__<YYYY-MM-DD>/`. This bundle is the publication unit — never ship a forecast number outside this workflow.

## Publication Checklist (agent prints before exit)

- [ ] All referenced inputs sealed and copied into bundle.
- [ ] All referenced models copied into bundle with matching hash.
- [ ] `code-pin.txt` clean diff confirmed.
- [ ] `manifest.json` validates against schema in `resources/custody-manifest-schema.md`.
- [ ] (If applicable) GPG signature verifies (`gpg --verify`).
- [ ] Cover note describes methodology and any judgmental adjustments.
- [ ] Embargo timestamps respected — no series in the bundle is under embargo at publication time.
- [ ] Conflict-of-interest disclosure included if `context/constraints.md` requires it.

The agent must affirmatively check each item — do not publish a bundle with any unticked box.
