# quality-complaint-root-cause

## Purpose

Use when a patient quality complaint comes in — pain at an unexpected ROI, sudden fit deterioration, premature component wear, repeat refit need — and the question is structured root-cause analysis tied back to measurable process state. Outputs a 5-Whys / Fishbone-style root-cause memo that supports either patient-level remediation OR a candidate for `/dmaic-fit-improvement`.

## Prompt Template

```
Acting as the biomechanical engineer performing root-cause analysis on a quality complaint.

Complaint context:

- **Complaint received date:** [VALUE]
- **Patient ID / pseudonym:** [VALUE]
- **Complaint summary (verbatim from patient):** [VALUE]
- **Complaint category:** [pain / fit / fall / component break / cosmetic / functional regression]
- **Time since fit:** [VALUE]
- **Recent component changes:** [VALUE]
- **Last in-control SPC session date:** [VALUE]
- **Most recent SPC chart signals (if any):** [VALUE]
- **Most recent PROMs:** [VALUE]
- **Fitter who delivered the fitting:** [VALUE]
- **Manufacturing batch / lot for definitive socket:** [VALUE if available]
- **Component lot / serial for affected components:** [VALUE]

Please:
1. Construct a fishbone (Ishikawa) cause-and-effect diagram across the 6 M's: Material, Method, Machine, Man, Measurement, Environment.
2. For each populated bone, name the specific candidate cause and the evidence required to confirm or refute it.
3. Cross-reference the SPC chart history — was there a pre-complaint signal that should have been investigated? (If yes, flag this as a process gap.)
4. Cross-reference the manufacturing data — was the relevant build batch within Cp/Cpk bounds?
5. Cross-reference the Gauge R&R status of the measurement systems involved — could measurement noise have masked an earlier signal?
6. Run a 5-Whys on the most likely candidate cause to surface a deeper systemic root.
7. Propose:
   a. Immediate patient-level remediation (clinical action by CPO).
   b. Process-level recommendations (if the root cause indicates a systemic gap — feed candidate into `/dmaic-fit-improvement`).
   c. Regulatory considerations (does this need MDR-style adverse-event reporting per FDA 21 CFR 806 / EU MDR Article 87?).
8. Document the analysis at `outputs/complaints/<patient-id>/<YYYY-MM-DD>-rca.md`.
```

## Expected Output

- Fishbone diagram (text description) with populated bones
- Per-bone candidate cause + evidence requirement
- SPC + manufacturing + R&R cross-reference findings
- 5-Whys for the top candidate
- Patient-level + process-level + regulatory recommendations
- Documented analysis memo ready for QMS filing

## Notes

- Complaints often surface process gaps that single-patient remediation won't fix; the value of structured RCA is the bridge to DMAIC.
- Regulatory reporting obligations apply when the complaint involves serious patient injury or device malfunction — when in doubt, escalate to the practice's Regulatory Coordinator / Quality Manager.
- Some "complaints" are actually patient expectation mismatch (e.g. expecting microprocessor knee to compensate for unsteady gait when it requires user-side training). RCA should distinguish device failure from expectation misalignment.
- Document EVERY complaint, even resolved-amicably ones — the pattern across complaints is more informative than any individual incident.
