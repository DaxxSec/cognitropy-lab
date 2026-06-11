# Eco Material Substitution

## Purpose

Evaluate replacing a conventional mechanism with an SMA solution (or vice versa) on a combined performance-plus-life-cycle basis, producing a defensible recommendation rather than a marketing claim.

## Prompt Template

```
You are evaluating a material/mechanism substitution for both functional performance and
environmental impact. Be even-handed; an honest "don't substitute" is a valid answer.

The substitution under consideration is:

- **Incumbent:** [solenoid / DC motor + gearbox / wax actuator / bimetal / spring]
- **Proposed SMA solution:** [alloy, form factor, actuation method]
- **Function & duty cycle:** [stroke, force, actuations/day, on-time, lifetime]
- **Use location grid intensity:** [gCO₂/kWh, or region]
- **Decision drivers, ranked:** [e.g. weight > reliability > energy > cost]

Please:
1. Compare functional performance: stroke, force, bandwidth, mass, part count, reliability, NVH.
2. Compare full life cycle: cradle-to-gate embodied GWP, use-phase energy/GWP, end-of-life recyclability, and Ni-release risk if relevant.
3. Find the break-even (if any) where the SMA option's total footprint beats the incumbent's.
4. Recommend substitute / don't substitute, against the ranked decision drivers, with the decisive factor named and the weighting made explicit.
```

## Expected Output

- A side-by-side functional comparison (incumbent vs. SMA).
- A full life-cycle comparison covering embodied, use-phase, and end-of-life.
- The break-even point or an explicit "no break-even."
- A recommendation aligned to the stated decision drivers, with the weighting visible and challengeable.
