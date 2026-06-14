# Calibration Fitment Review

## Purpose

Decide whether a candidate calibration fits a vehicle's exact hardware "form" before flashing. Use it to avoid the classic phantom-fault trap of mounting a cal built for different injectors, sensors, or transmission.

## Prompt Template

```
You are a PCM calibration conservator verifying hardware-form fitment. Evaluate this candidate cal against the installed hardware.

Candidate calibration:
- **CAL-ID / source:** [VALUE]
- **Assumed hardware (from definition):** [injectors, MAF/MAP range, turbo, trans model]

Installed hardware (the form):
- **Injectors:** [flow rate / part #]
- **MAF/MAP sensor:** [range / part #]
- **Forced induction:** [turbo/supercharger spec, or N/A]
- **Transmission:** [model]
- **Engine:** [displacement / cam / VVT notes]
- **Context:** [stock restoration | replacement module | legitimate non-emissions recalibration]

Please:
1. Compare cal-assumed vs installed hardware axis by axis.
2. Classify each mismatch: benign / correctable (legal, non-emissions) / disqualifying.
3. Give a FIT / FIT-WITH-CORRECTIONS / DOES-NOT-FIT verdict with reasons.
4. List any corrections required and confirm they stay out of emissions-critical scope.
```

## Expected Output

- An axis-by-axis comparison table
- A clear fitment verdict gating the flash
- A list of required (legal, non-emissions) corrections, if any
