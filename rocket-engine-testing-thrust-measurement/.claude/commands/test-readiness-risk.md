# /test-readiness-risk

Walk the test card and FMEA through the `T-*` decision tree (`context/workflows.md` §1) to produce the pre-fire MIL-STD-882E 5×5 likelihood × severity matrix with ALARP-justified mitigations.

## Inputs

- `test_id` — identifier for the upcoming hot-fire (e.g. `RX-DEV-0042-FIRE-007`).
- `test_card_path` — path to the test card PDF / markdown, or inline summary.
- `fmea_path` — path to the engine FMEA / FMECA. Required.
- `propellants` — list of propellants and inventories (e.g. `[{"name":"LOX","mass_kg":1200},{"name":"RP-1","mass_kg":520}]`).
- `measurement_objective` — `development` | `acceptance` | `qualification`. Drives downstream sensitivity to the uncertainty budget.
- `prior_test_log_path` — optional; if present, used for empirical likelihood priors in `T-3`.

## Steps

1. Run `T-0` intake. Reject the package if test card, FMEA, propellant inventory, or measurement objective is missing.
2. Enumerate failure modes from the FMEA at `T-1`. Output an ordered list `FM_1..FM_n` with immediate effect and MEOP impact for each.
3. Walk `T-2` (severity per failure mode). Cite the MIL-STD-882E §4.3.4 definition for every assignment; do not down-band on engineering vibes.
4. Walk `T-3` (likelihood per failure mode). Prefer vendor MTBF or comparable-engine data; if only engineering judgment, apply the anti-optimism bias (one band more frequent) and record the rationale.
5. Plot each cell at `T-4`. Use the matrix in `context/references.md` to map cell → band.
6. For each cell at band ≥ MEDIUM, walk `T-5` for mitigations. Prefer severity reductions over likelihood reductions; emit both pre- and post-mitigation cells.
7. Apply the ALARP gate at `T-6`. HIGH cells must be mitigated down before fire authorization. SERIOUS cells require named-authority sign-off; MEDIUM cells require ALARP rationale.
8. Aggregate at `T-7`. Emit GO_CANDIDATE / NO_GO / NO_GO_PENDING_SIGNOFF with the cited cells driving each band.
9. Write the full matrix and the GO/NO-GO disposition to `outputs/readiness/<test_id>-readiness-<YYYYMMDD>.md`.

## Output

Markdown file containing:
- Test ID, measurement objective, propellant inventory, FMEA reference hash.
- Pre-mitigation 5×4 matrix with cell counts.
- Per-failure-mode table: `FM_id`, severity (I–IV, with cited definition), likelihood (A–E, with cited basis), cell, band, mitigation, residual cell, residual band, sign-off authority, ALARP rationale.
- Post-mitigation matrix.
- Aggregate disposition (GO_CANDIDATE / NO_GO / NO_GO_PENDING_SIGNOFF) with the binding cells.
- Auto-suggested follow-up commands (`/redline-set`, `/thrust-uncertainty-budget`, `/range-safety-matrix`).
- Reproducibility footer: FMEA hash, test card hash, git SHA of this workspace.

## Notes

- Do not redefine MIL-STD-882E severity to fit the schedule. If "Catastrophic" applies, score Catastrophic.
- A `HIGH` cell is never ALARP-justified for fire authorization; it must be mitigated down to SERIOUS or lower.
- Anti-optimism bias on judgment-only likelihoods is intentional. Operators systematically underestimate failure rates on development hardware.
- If the FMEA is older than the engine build state, request a refresh before scoring; an out-of-date FMEA invalidates the matrix.
- Cross-reference: if a failure mode is in the matrix at severity I/II, it MUST have redline coverage in `/redline-set`. The aggregate verdict in T-7 should not GO_CANDIDATE without that linkage.
