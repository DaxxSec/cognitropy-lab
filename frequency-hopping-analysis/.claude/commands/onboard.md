# /onboard — Initialize Frequency Hopping Analysis Workspace

Welcome. I'll gather your SDR setup, target system, hop hypotheses, and legal authorisation, then write the workspace context files.

## Inputs

None — interview-driven.

## Steps

### 1. Hardware Profile
Ask:
- Which SDR are you using? (HackRF One, USRP B210/X310, BladeRF 2.0, LimeSDR, Pluto, RTL-SDR — exact model)
- What's the maximum instantaneous bandwidth?
- Do you have a GPSDO or external 10 MHz reference?
- What antennas are available, and which is best matched to today's target band?

Save to `context/for-agent/environment.md`.

### 2. Target System
Ask:
- What system are you trying to analyse? (Bluetooth, BLE, WMBus, LoRa channel-hopping, proprietary IoT, range-authorised tactical, unknown signal labelled with FCC ID, etc.)
- What's the suspected hop band?
- Have you found regulator filings (FCC ID lookup, ETSI test reports, vendor datasheets)?
- Any prior reverse-engineering work on this system you can cite?

Save to `context/project.md`. Drop links into `context/project.md` "Public information available" section.

### 3. Bayesian Hop Hypotheses
Ask:
- What hop rate do you expect, order-of-magnitude? (10/s? 100/s? 1000/s? unknown?)
- What channel count K do you expect?
- Pseudo-random, table-driven, or AFH? Or is this what we're trying to figure out?

Translate the answers into prior parameters and save them to `planning/plan.md` as the analysis plan's prior section. If the user says "unknown", use the default uninformative priors from `domain-knowledge.md` §3.3.

### 4. Legal & Ethical Clearance
**Mandatory.** Ask:
- What jurisdiction are you in?
- What's your authorisation to receive this signal? (Personal device → consumer ISM is OK in most jurisdictions; tactical/public-safety/cellular requires explicit authorisation)
- Is the authorisation document on file? What's the path?
- Receive-only, or are you authorised for active/transmit work?

Save to `context/constraints.md`. **If receive authorisation is unclear, halt and tell the user to resolve before proceeding.**

### 5. Calibration Plan
Recommend:
- A Bluetooth Classic calibration capture at 2.441 GHz, 80 MS/s, 1 s, gain 40 dB
- Validation: gr-bluetooth ground truth + Bayesian dehopper agreement
- Save calibration evidence in `outputs/calibration-<date>/`

Write the calibration plan to `planning/plan.md`.

### 6. Goals & Reporting
Ask:
- What does success look like? (Hop characterisation, sequence recovery, dehop for downstream demod, jammer triage, calibration only)
- What's the time budget?
- What's the reporting format? (Numeric posteriors, narrative writeup, court-admissible chain-of-custody)

Save to `context/project.md` "Goals" and `context/role.md` "Output preferences".

### 7. First Capture Recommendation
Based on the gathered info, output:
- Center frequency
- Sample rate (≥ Nyquist for the hop set)
- Duration (≥ 2× expected sequence period)
- Recommended SDR command (from `context/for-agent/tools.md`)
- Storage estimate

Write to `planning/plan.md` and log the onboarding session in `work-log/<YYYY-MM-DD>-onboard.md`.

## Output

- `context/project.md` populated
- `context/role.md` populated
- `context/constraints.md` populated
- `context/for-agent/environment.md` populated
- `planning/plan.md` created with calibration plan + first capture parameters
- `work-log/<date>-onboard.md` written

After running `/onboard`, the user should run the calibration capture (Workflow C) before any unknown-signal analysis.
