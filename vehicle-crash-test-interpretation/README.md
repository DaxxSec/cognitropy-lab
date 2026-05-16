# Vehicle Crash Test Interpretation Workspace

> Turn raw crash-test instrumentation into Bayesian probability statements about injury, restraint performance, and regulatory compliance.

## What This Workspace Does

This workspace equips a Claude agent to interpret full-vehicle crash tests — frontal rigid barrier, offset deformable barrier, moving deformable barrier, small-overlap, oblique, side pole, and rollover — by treating every channel of crash-test instrumentation as **evidence in a Bayesian update**, not as a verdict in itself. The agent ingests SAE J211 / ISO 6487 conforming time histories from Anthropomorphic Test Devices (ATDs), vehicle accelerometers, intrusion measurements, and high-speed kinematics markers, then produces posterior distributions over (a) occupant injury probability per AIS body region, (b) restraint-system contribution to those probabilities, and (c) compliance probability against the relevant regulation (FMVSS 208/214/301, UNECE R94/R95/R137, Euro NCAP / IIHS / US NCAP protocol series).

The "using Bayesian probability assessment" framing is what differentiates this workspace from a generic crash-data pipeline. Industry practice typically reports a single Head Injury Criterion (HIC15), a single chest deflection, a single Nij — then traffic-lights it against a threshold. This workspace refuses the point estimate. It encodes the canonical injury-risk curves (Mertz, Eppinger, Kuppa) as **likelihood functions**, elicits priors from the lab's calibration history and prior fleet data, and outputs **posterior credibility intervals** that quantify how much of the apparent margin to a regulatory threshold is real and how much is sensor / dummy / pulse-shape noise.

## Why This Workspace Exists

Crash testing is irreducibly low-N. A single full-scale test costs USD 100k-500k, dummies drift between certifications, channels saturate without notice, and high-speed cameras lose markers behind airbag deployments. The temptation to report point-estimate metrics — "HIC = 612, passes threshold of 700" — masks the fact that the same vehicle re-tested next week may yield 740 from sensor variation alone. The Bayesian frame is what protects star ratings, NHTSA submissions, and consumer publications from being repeatedly embarrassed by replication tests. This workspace codifies that frame so a single analyst can apply it consistently across every test in a model-year batch.

## Getting Started

### Prerequisites

- Python 3.11+ with NumPy, SciPy, PyMC (for Bayesian sampling) and Matplotlib.
- Access to test recordings in ISO/MME or DIAdem TDMS format (or CSV exports thereof).
- The lab's dummy certification log (covering at least the last 12 calibration cycles).
- A copy of the relevant regulation revision PDF in `outputs/_regulation-refs/`.
- Optional: the public Euro NCAP / IIHS test database mirror for comparator runs.

### Quick Start

1. Clone this workspace and place test channel data under `outputs/raw/<test-id>/`.
2. Run `/pulse-anomaly-check` to confirm the vehicle crash pulse falls within the expected family for the test mode — if not, stop and investigate before any injury analysis.
3. Run `/dummy-bias-prior` once per dummy serial to establish (or refresh) the calibration prior for this test campaign.
4. Run `/injury-posterior` for each occupant position; review the posterior plots written under `outputs/posteriors/`.
5. Run `/restraint-likelihood` to interpret what the kinematics imply about belt / airbag / pretensioner performance.
6. Run `/regulation-compare` to convert posterior injury distributions into a posterior probability of regulatory compliance.
7. Run `/star-rating-confidence` to convert per-test posteriors into a confidence interval around the consumer rating.

## Command Reference

| Command | Description | When to Use |
|---------|-------------|-------------|
| `/injury-posterior` | Posterior injury-risk distribution per AIS body region, conditioned on ATD channels. | After channel validation, once per occupant per test. |
| `/restraint-likelihood` | Posterior likelihood ratio for normal vs. degraded restraint-system performance. | When occupant kinematics deviate from belted-and-airbagged norm. |
| `/pulse-anomaly-check` | Bayesian anomaly screening on the vehicle accelerometer pulse vs. expected mode-specific family. | Before any injury analysis on a fresh test. |
| `/star-rating-confidence` | Credibility interval on predicted NCAP / IIHS rating before publication. | Once the per-occupant posteriors are computed, before any rating is published. |
| `/dummy-bias-prior` | Elicit / update a per-dummy-serial calibration prior. | Start of a test campaign, or after any re-certification. |
| `/regulation-compare` | Compare measured posteriors against FMVSS / UNECE thresholds; return P(compliant \| data). | Whenever an explicit regulatory compliance claim is to be made. |

## Directory Structure

```
vehicle-crash-test-interpretation/
├── CLAUDE.md                 # Agent role, context refs, command list
├── README.md                 # This file
├── .claude/commands/         # Six bespoke Bayesian-crash commands
├── context/
│   ├── concepts.md           # Injury criteria, ATD families, test modes, regulations
│   ├── workflows.md          # Bayesian update procedure, prior-elicitation, channel validation
│   └── references.md         # IARV tables, CFC classes, regulation citations, public datasets
├── prompts/                  # Analyst-facing prompt templates
└── outputs/                  # Posteriors, plots, compliance memos, raw test data
```

## Example Use Cases

### A vehicle scores HIC15 = 612 in one test and HIC15 = 698 in a repeat. Both "pass." Which result should the consumer publication trust?
Use `/dummy-bias-prior` + `/injury-posterior` to derive a single posterior across both tests; the credibility interval typically straddles the 700 threshold even though both point estimates "pass." That is the truthful headline.

### A small-overlap test shows occupant head excursion approaching the A-pillar but the HIC is "fine."
Use `/restraint-likelihood` to estimate the posterior probability that the airbag positioned the occupant inadequately even though the head injury criterion stayed in spec — restraint performance and HIC are correlated but not identical.

### NHTSA proposes a new FMVSS amendment that tightens the chest deflection threshold from 63 mm to 52 mm.
Run `/regulation-compare` with the new threshold across the lab's historical test database to estimate the posterior probability that each model-year would have passed under the proposed rule — a defensible regulatory-impact analysis instead of a binary recount.

### A new ATD generation (e.g. THOR-50M replacing Hybrid III) is introduced mid-campaign.
Use `/dummy-bias-prior` to estimate the offset and re-derive priors so historical Hybrid III data and new THOR data are commensurable in a single Bayesian model.

### A rating publication is days from going public and one channel on one test shows possible signal clipping.
Use `/pulse-anomaly-check` to quantify the posterior probability that the channel was clipped vs. noisy; if non-trivial, the rating is held until the test is re-run rather than published with hidden risk.

## Recommended MCP Servers

- **filesystem** — read TDMS / ISO-MME / CSV exports out of `outputs/raw/`.
- **fetch** — pull regulation revisions and public NCAP database entries.
- **memory** — persist per-dummy and per-vehicle priors across sessions so they accumulate evidence across a campaign.

## Legal & Ethical Considerations

- **Consumer publications carry liability.** Star ratings influence purchasing decisions; over-claiming margin is litigable. Posterior credibility intervals are how the lab defends its conclusions.
- **Anthropomorphic Test Devices are imperfect proxies for human injury.** A passing HIC posterior does not imply a passing human — it implies the regulation's surrogate-injury criterion is satisfied.
- **Regulatory compliance is not safety.** A vehicle that probabilistically passes FMVSS 208 may still injure real occupants in modes not captured by the test matrix. Communicate the gap explicitly.
- **Cite the agency.** Reference FMVSS / UNECE / Euro NCAP / IIHS protocol text directly; do not paraphrase regulation in a deliverable.

## Technical References

- [SAE J211 — Instrumentation for Impact Test](https://www.sae.org/standards/content/j211/1_202203/) — channel filter classes, polarity conventions.
- [ISO 6487 — Road vehicles, measurement techniques in impact tests](https://www.iso.org/standard/72356.html) — instrumentation standard.
- [Euro NCAP Test Protocols](https://www.euroncap.com/en/for-engineers/protocols/) — adult/child occupant, vulnerable road user, safety-assist series.
- [IIHS Vehicle Research Test Protocols](https://www.iihs.org/ratings/about-our-tests) — small-overlap, moderate-overlap, side, roof-strength.
- [NHTSA FMVSS](https://www.nhtsa.gov/laws-regulations/fmvss) — FMVSS 208 (occupant crash protection), 214 (side impact), 301 (fuel system integrity).
- [Mertz et al. — Hybrid III injury-risk curves](https://www.sae.org/publications/technical-papers/content/2003-22-0009/) — canonical HIC, Nij, chest deflection risk functions used as likelihoods.
- [NHTSA Vehicle Crash Test Database](https://www.nhtsa.gov/research-data/research-testing-databases) — public test channel data for prior elicitation.

## Optional plugin

If you have the [`workspace-foundational`](https://github.com/danielrosehill/Claude-Workspace-Foundational-Plugin) plugin installed, additional global commands (`/workspace-foundational:context-sweep`, `/workspace-foundational:find-template`) are available; the workspace works without it.
