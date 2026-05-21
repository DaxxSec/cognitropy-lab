# new-patient-fitting-intake

## Purpose

Use when a new patient enters the practice for an initial prosthetic fitting consultation. Establishes the structured baseline that all subsequent SPC, PROM tracking, and component-selection work will reference.

## Prompt Template

```
Acting as the biomechanical engineer working alongside the CPO for a new initial fitting consult.

Patient context:

- **Age:** [VALUE]
- **Amputation level:** [transtibial / transfemoral / etc.]
- **Amputation side:** [L / R / bilateral]
- **Etiology:** [vascular / traumatic / congenital / oncologic / infectious]
- **Time since amputation:** [VALUE]
- **Anticipated K-level:** [K1 / K2 / K3 / K4]
- **Weight (kg):** [VALUE]
- **Activity goals (verbatim from patient):** [VALUE]
- **Comorbidities:** [diabetes / PVD / cardiac / neuropathy / etc.]
- **Prior prosthesis (if any):** [model + duration of use + reason for new fitting]
- **Insurance / payer:** [VALUE — affects component formulary access]

Please:
1. Propose an initial component selection rationale (foot, knee if applicable, liner, suspension) tied to K-level + activity goals + payer constraints; cite Medicare L-code formulary where applicable.
2. Define the baseline measurement plan: what gait variables, pressure-map regions, and PROMs will be collected at day-0, day-30, day-60, day-90 for the SPC baseline lock.
3. Identify upfront risks specific to this patient (component fit risks, expected limb volume trajectory, training requirements, comorbidity considerations).
4. Recommend the test-socket strategy (number of iterations expected, alignment session cadence).
5. Flag any regulatory / consent considerations specific to the proposed components.
```

## Expected Output

- A structured intake memo with component-selection rationale + rationale citation
- A baseline measurement plan with specific instruments, variables, and visit cadence
- A risk register specific to this patient
- A test-socket and alignment strategy
- Regulatory + consent checklist for the proposed fitting

## Notes

- Always defer final clinical decisions to the licensed CPO + prescribing physician; this prompt produces a structured *proposal*, not a clinical order.
- For Medicare patients, K-level documentation must be present in the prescribing physician's notes — the prosthetist cannot upgrade K-level without medical documentation.
- The output of this prompt becomes the seed file for `/gait-lab-spc-baseline` at the 90-day mark; structure the intake so the baseline can be locked cleanly later.
