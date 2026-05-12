# /draft-risk-register — Consolidate Scenarios into an ISO 31000-Aligned Register

Sweep `outputs/` for scenario cards and the running `planning/risk-register.md`, and produce a clean, distributable risk register at `outputs/risk-register-<YYYY-MM-DD>.md`. Suitable for executive review or GRC tool import.

## Required Inputs

None required — the agent reads:
- `planning/risk-register.md` (running register).
- All scenario cards in `outputs/supply-*.md`, `outputs/demand-*.md`, `outputs/stress-*.md`.
- Calibration scales from `context/constraints.md`.
- Output preferences from `context/role.md`.

## Procedure

### Step 1 — Sweep scenario cards
Build an internal table indexed by scenario slug. Take the *most recent* score per scenario (date-stamped). Surface drift: if a scenario was re-scored, append a "drift" annotation showing prior tier → current tier.

### Step 2 — Validate completeness
For each row, confirm presence of:
- ID (assign `R-<YYYY>-<NNN>` if missing)
- Title, Cause, Event, Consequence
- Inherent L, I, RPN
- Existing controls (may be empty — flag for the user to fill)
- Residual L, I, RPN (after existing controls)
- Treatment plan (Avoid / Reduce / Transfer / Accept)
- Owner (single named person — flag if missing)
- Review date (default = horizon end if missing)
- Single most fragile assumption
- Microeconomic anchor (the elasticity, surplus, or curve-shift evidence)

If any field is missing for any row, the agent prints the gap list and asks the user before proceeding.

### Step 3 — Render the register

```
# Risk Register — <market scope from project.md> — <YYYY-MM-DD>
**Horizon:** <H> · **Scoring scale:** <5×5 L×I> · **Risk appetite bands:** see `context/constraints.md`

| ID | Title | Cause | Event | Consequence | L | I | RPN | Tier | Existing Controls | Residual L | Residual I | Residual RPN | Treatment | Owner | Review Date | Fragile Assumption | Microecon Anchor |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R-2026-001 | Brazil arabica drought | NOAA forecast / WASDE | Supply contraction 8–15% | Revenue +12–18%, margin −180 bps | 4 | 4 | 16 | Red | None | 4 | 3 | 12 | Reduce — hedge 60% Q3 exposure | A. Patel | 2026-07-31 | εs assumed unchanged under drought | εs ≈ 0.2 (ICO 2019); ΔP*/P* ≈ +12–18% |
| ...
```

### Step 4 — Add appendices

- **Appendix A — Calibration scales** (copy of the L, I, D anchor tables from `constraints.md`, dated).
- **Appendix B — Sources & methods** (list of scenario card paths, elasticity sources, standards cited).
- **Appendix C — Out-of-scope risks** (verbatim from `project.md`, restated to manage reader expectations).
- **Appendix D — Drift log** (any scenario that was re-scored since the prior register, with old → new tier and rationale).

### Step 5 — Render alternate formats per `context/role.md`
- Markdown (always).
- CSV in long format (always; one row per register row, one per appendix table).
- Slide-ready bullets (if requested): top 5 red-tier risks each as 3 bullets (what, impact, treatment).
- BI long-format CSV (if requested): one row per (scenario × period × axis-tier) for time-series tracking.

### Step 6 — Append work-log entry summarizing the register state.

## Output

The agent reports back:
- Path to the rendered register (and CSV/slide variants if requested).
- Count of rows by tier (green/yellow/amber/red).
- Top 3 red-tier risks (one-line each).
- Drift summary (if any).
- Completeness gaps that still need user input.
- Suggested cadence: typical re-runs are quarterly + after any new scenario card.

## Notes

- **Do not aggregate across horizons.** If the workspace contains scenarios at different horizons, the register is split into one section per horizon. Do not sum or compare RPNs across horizon sections.
- **Inherent vs. residual.** If existing controls are unknown for a row, residual = inherent and the row is flagged. Don't silently assume controls exist.
- **The register is a snapshot.** It's dated. Tomorrow's register may differ. The running `planning/risk-register.md` is the always-current source; the dated `outputs/risk-register-*.md` is the immutable distribution copy.
