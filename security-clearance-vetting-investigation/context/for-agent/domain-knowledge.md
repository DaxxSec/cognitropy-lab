# Domain Knowledge

## 1. Governing authorities
- **EO 12968 (1995)** — Access to Classified Information; established baseline standards and process.
- **EO 13467 (2008)** — Reformed suitability / security clearance / credentialing processes; established the Security, Suitability, and Credentialing Performance Accountability Council.
- **EO 13764 (2017)** — Amended and strengthened 13467; directed the move to continuous vetting.
- **SEAD 4 (2017)** — Security Executive Agent Directive 4: 13 adjudicative guidelines, whole-person concept.
- **32 CFR Part 117 (2021)** — Current NISPOM for industrial security.
- **TW 2.0** — Trusted Workforce 2.0 policy framework for ending periodic reinvestigations in favor of continuous vetting.

## 2. The 13 SEAD 4 adjudicative guidelines

| # | Guideline | Short |
|---|---|---|
| A | Allegiance to the United States | Allegiance |
| B | Foreign Influence | Foreign |
| C | Foreign Preference | Preference |
| D | Sexual Behavior | Sexual |
| E | Personal Conduct | Conduct |
| F | Financial Considerations | Financial |
| G | Alcohol Consumption | Alcohol |
| H | Drug Involvement and Substance Misuse | Drugs |
| I | Psychological Conditions | Psych |
| J | Criminal Conduct | Criminal |
| K | Handling Protected Information | Handling |
| L | Outside Activities | Outside |
| M | Use of Information Technology | IT-use |

Each guideline has enumerated **Conditions that could raise a security concern and may be disqualifying** and **Conditions that could mitigate security concerns**. The **whole-person concept** requires the adjudicator to consider all available, reliable information about the person, past and present, favorable and unfavorable.

Key adjudicative factors under whole-person:
1. Nature, extent, and seriousness of the conduct
2. Circumstances surrounding the conduct
3. Frequency and recency
4. Individual's age and maturity at the time of conduct
5. Extent of voluntary participation
6. Presence or absence of rehabilitation
7. Motivation for the conduct
8. Potential for pressure, coercion, exploitation, or duress
9. Likelihood of continuation or recurrence

## 3. Investigation tiers (baseline)
- **Tier 1** — Low risk non-sensitive / HSPD-12
- **Tier 2** — Moderate risk public trust
- **Tier 3 / T3R** — Non-critical sensitive / Secret (was NACLC/ANACI)
- **Tier 4** — High risk public trust
- **Tier 5 / T5R** — Critical sensitive / Top Secret (was SSBI/SSBI-PR)

Under TW 2.0 the tier structure is being collapsed toward continuous vetting enrollment with event-driven expansions.

## 4. Continuous Vetting signal sources
- **Criminal** — FBI rap sheet updates, local arrest records, warrants.
- **Financial** — credit score drops, bankruptcies, tax liens, significant new debt.
- **Terrorism / foreign** — watchlist matches, suspicious activity reports.
- **Public records** — civil litigation, divorce filings with financial stress, news adverse.
- **Self-reported** — under SEAD 3, subjects must self-report incidents.
- **Employer / facility** — security violations, spillage, policy violations.

## 5. The predictive-maintenance analogy (expanded)

Reliability engineering distinguishes four maintenance regimes:
1. **Reactive** — run to failure.
2. **Preventive** — time/usage-based intervals.
3. **Condition-based (CBM)** — act on sensor readings.
4. **Prescriptive / predictive (PdM)** — model-driven recommendation of *when* and *what*.

Vetting analogs:
1. **Reactive** — Discovering a compromise after the fact.
2. **Preventive** — 5-year / 10-year periodic reinvestigation.
3. **Condition-based** — Continuous vetting alert-driven inquiry.
4. **Predictive** — Risk-model-driven expansion (what TW 2.0 *aspires* to do well).

The **P-F interval** is the window between the first detectable indicator of an emerging problem (P) and the actual functional failure (F). In PdM you want your sampling interval to be shorter than P-F. In vetting you want your CE alert latency + triage time to be shorter than the time between "first signal of a risk condition" and "disqualifying event or compromise."

A well-run drift scan produces:
- A current health index per guideline.
- A trend (improving, stable, degrading) over the last N scans.
- A recommended next action and next scan date.

## 6. Risk scoring (overview)

A simple rubric:
- Each guideline → score 0-5 (0 = no concern; 5 = disqualifying conditions observed and not mitigated).
- Weight each guideline by mission risk (e.g., Guideline K may be higher weighted in an IC SCIF context; Guideline F may be higher for a finance-adjacent role).
- Compute a weighted composite.
- Track deltas across scans; a positive delta > threshold triggers an action.

Exact weights and thresholds live in `resources/risk-scoring-rubric.md` so they can be tuned per agency mission.

## 7. Reinvestigation modes

| Mode | Trigger | Typical scope |
|---|---|---|
| **Calendar PR** | Time since last investigation | Full Tier 3 or Tier 5 |
| **Out-of-cycle** | Incident, CE hit, or commander request | Focused on the issue |
| **Focused inquiry** | Single guideline concern | Guideline-specific interview + records |
| **SOI (Statement of Intent)** | Guideline F / Guideline G context | Subject commits to remediation |
| **LOI (Letter of Intent to Deny/Revoke)** | Serious disqualifying conditions | Full SOR process follows |
| **Continuous vetting re-check** | Scheduled sensor read | Automated, minimal human time |

This workspace biases toward **focused inquiry** and **out-of-cycle** actions, because that's where the predictive-maintenance analogy adds the most value.
