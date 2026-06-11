# DSC Curve Interpretation

## Purpose

Hand an agent a raw or described DSC thermogram and get back a clean transformation fingerprint — transformation temperatures, hysteresis, enthalpy, and a read on what the curve shape implies about composition, aging, or oxidation.

## Prompt Template

```
You are a shape-memory-alloy characterization specialist. Interpret this DSC thermogram.

I have a DSC measurement of an SMA sample:

- **Alloy (nominal):** [e.g. Ni-50.8 at% Ti, or "unknown NiTi"]
- **Scan rate / sample mass:** [e.g. 10 °C/min, 12 mg]
- **Cooling segment peaks (exothermic):** [peak positions, shoulders, twin peaks]
- **Heating segment peaks (endothermic):** [peak positions, shoulders]
- **Sample history:** [as-received / annealed / aged at X°C / cycled N times / unknown]

Please:
1. Read off Ms, Mf, As, Af using the ASTM F2004 tangent construction, and Rs/Rf if an R-phase is present.
2. Report thermal hysteresis (Af − Ms) and the transformation enthalpy for each direction.
3. Diagnose the curve shape: single vs. multistage, peak broadening, suppressed peaks — and what each implies (aging/Ni₄Ti₃, oxidation, off-stoichiometry, functional fatigue).
4. Flag anything that looks inconsistent with the nominal composition and recommend a confirmation test.
```

## Expected Output

- A transformation-temperature table (Ms/Mf/As/Af, + R-phase if present) with the construction method stated.
- Hysteresis and enthalpy values with units.
- A short diagnosis of composition/aging/oxidation/fatigue signatures from the peak shape.
- A recommended follow-up measurement when the curve conflicts with the nominal alloy.
