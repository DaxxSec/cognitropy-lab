# ISO 31000 / IEC 31010 Mapping Reference

How the workspace's microeconomic risk-scoring outputs map onto ISO 31000:2018 risk-register fields and IEC 31010:2019 method choices. Use this as the reference when integrating workspace outputs with a corporate risk-management framework.

## ISO 31000:2018 — Field-by-Field Mapping

| ISO 31000 register field | Workspace source | Notes |
|---|---|---|
| **Risk source** | Curve-shift driver from scenario card (Cause section) | Map driver category (Income, Tastes, Substitute, Regulation, Cost, Capacity) directly |
| **Event** | Curve-shift event description | "Supply contracts 8–15% due to drought"; "Demand shifts left from substitute entry" |
| **Cause** | Underlying parameter change | The W, Y, T, P_r, etc. that moved |
| **Consequence** | Equilibrium-response section | ΔP*, ΔQ*, surplus deltas, denominated in user units |
| **Likelihood** | Tier from scoring step 4 | Anchored to base-rate calibration in `constraints.md` |
| **Impact / consequence severity** | Tier from scoring step 5 | Mapped from revenue/margin/operational deltas |
| **Existing controls** | Hedges, multi-source contracts, price collars | User-supplied, scenario-card filled-in |
| **Inherent risk** | L × I (or L × I × D) before controls | Composite RPN |
| **Residual risk** | Same composite after controls | Often unfilled — flag for review |
| **Treatment** | Suggested treatment from scoring step 8 | Mapped to ISO terminology: Avoid, Reduce, Transfer, Accept |
| **Owner** | Single named person | Required; flag if missing |
| **Review date** | Default to horizon end | User can override |

ISO 31000 emphasizes risk treatment as a four-option taxonomy:

- **Avoid** — eliminate the activity that exposes the firm to the risk.
- **Reduce** — apply controls (hedges, diversification, contracting) to lower L or I.
- **Transfer** — insurance, supplier risk-shift contracts, financial hedges.
- **Accept** — informed acknowledgment that the residual is within appetite.

The agent always recommends against "Accept" without explicit confirmation that residual sits inside the user's risk appetite tier.

## IEC 31010:2019 — Method Selection

IEC 31010 catalogs ~30 risk-assessment techniques. The workspace's commands map to these techniques:

| Workspace command | IEC 31010 technique | Section |
|---|---|---|
| `/score-supply-shock`, `/score-demand-shock` | Risk matrix + scenario analysis | §B.29, §B.5–B.8 |
| `/equilibrium-stress-test` | Scenario analysis + Monte Carlo (if randomized) | §B.5, §B.18 |
| `/elasticity-risk-matrix`, `/cross-elasticity-screen` | Risk matrix (multi-criteria) | §B.29 |
| `/draft-risk-register` | Risk register | §B.31 |
| `/calibrate-scale` | Risk-criteria definition | §6.3.4 (general) |

IEC 31010 also discusses the **Bow-tie** method (§B.13) for cause–event–consequence decomposition. A scenario card already contains the bow-tie elements; if a stakeholder requests a bow-tie diagram, the agent renders one from the existing fields.

## COSO ERM (2017) Heat-Map and Risk-Appetite Vocabulary

When the user's organization speaks COSO ERM:

- "Risk appetite statement" → the band thresholds in `constraints.md`.
- "Heat map" → the rendered 5×5 matrix from `/elasticity-risk-matrix` or stress-test outputs.
- "Risk profile" → the consolidated register from `/draft-risk-register`.
- "Risk capacity" → not modeled by this workspace; it's the maximum risk the firm can absorb (typically a board-level definition).

COSO emphasizes integration with strategy. The workspace's "Decision This Will Inform" field in `project.md` is the explicit hook — every register row should be traceable back to a strategic decision being supported.

## NIST SP 800-30 Rev. 1 Mapping

NIST 800-30 was written for cybersecurity risk but the qualitative scoring tier definitions are widely re-applied. The workspace uses NIST's Appendix I tier definitions as default anchor language:

- "Very Low" / "Low" / "Moderate" / "High" / "Very High" → maps to tiers 1–5.
- The qualitative-to-semi-quantitative bridge in NIST §3.2 informs how the workspace lets users choose between L+I, L×I, and L×I×D.

## AIAG-VDA FMEA Handbook (2019) — When User Picks L × I × D

If the user chose FMEA-style scoring in `/calibrate-scale`:

- "Severity (S)" = Impact tier.
- "Occurrence (O)" = Likelihood tier.
- "Detection (D)" = Detectability tier.
- AIAG-VDA recommends **Action Priority (AP)** — High/Medium/Low — over the multiplied RPN. The workspace supports both; the user picks.
- The handbook's worked-example cases are operational/manufacturing, not microeconomic. The workspace adapts the *scoring discipline* (always show three components, never just the product), not the AP rubric directly.

## Antitrust Considerations

ISO 31000 and IEC 31010 are silent on antitrust. The workspace adds the following hard constraints (also stated in `context/constraints.md`):

- **Sherman Act §1 (US), Article 101 TFEU (EU), and equivalent regimes** prohibit price coordination among competitors.
- The workspace will refuse to:
  - Recommend matching a competitor's announced (but not yet implemented) price move where the recommendation is conditional on a signal exchange.
  - Score scenarios that require competitive coordination as a "treatment."
  - Produce outputs that could be construed as a price-signaling document if shared externally.
- **Permitted:** observing public competitor pricing, modeling cross-elasticity from observed data, planning unilateral firm responses.

## What This Workspace Does Not Cover

ISO 31000 is broader than microeconomic supply-demand risk. The workspace is *not* a substitute for:

- Cybersecurity risk assessment (use NIST CSF, ISO 27005).
- Operational risk assessment for IT/business continuity (use ISO 22301).
- Health and safety risk (use ISO 45001).
- Project risk management (use ISO 31000 with PMBOK / PRINCE2 integration).
- Climate / ESG transition risk at firm level (use TCFD).

The workspace's outputs slot into a broader enterprise risk register; they are one column, not the whole table.
