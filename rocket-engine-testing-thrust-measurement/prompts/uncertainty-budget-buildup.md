# Uncertainty Budget Buildup (New Stand / New Transducer)

## Purpose

Use when commissioning a new thrust stand, swapping a load cell, or qualifying a new amplifier / DAQ in the measurement chain. Builds the thrust uncertainty budget from scratch (rather than incrementally on an established stand), with every term sourced and every assumption documented. Output is the baseline budget that subsequent `/thrust-uncertainty-budget` runs adjust off.

## Prompt Template

```
You are a metrology engineer building the thrust uncertainty budget from scratch for a new
or significantly-modified thrust stand. Walk every term in the load-cell measurement chain
through JCGM 100 (the GUM) and produce a baseline budget that can be referenced for the next
campaign of fires.

Stand and transducer details:
- **Stand name / id:** [e.g. "Stand 4B — vertical, 50 klbf"]
- **Topology:** [vertical / horizontal]
- **Load cell(s):** [serials, models, FS rating, manufacturer's combined-error spec]
- **Calibration plan:** [in-situ proving ring / deadweight / hydraulic calibration cylinder; cert path if available]
- **Amplifier / signal conditioner:** [model, gain, noise floor measurement]
- **DAQ:** [bits, sample rate, range, anti-alias filtering]
- **Alignment survey results:** [axial-tilt budget in degrees, side-load cell presence]
- **Thermal environment:** [expected ambient range during fire, thermal-protection scheme]
- **Side-load / gimbal coupling:** [yes / no; gimbal sweep envelope if yes]
- **Tare measurement plan:** [pre-fire tare protocol, thermal-stabilization period, tare repeatability spec]
- **Measurement objective(s) the stand must support:** [list, e.g. development at 2%, qualification at 0.5% k=2]

Please:
1. For each term in `context/concepts.md` §"Typical Inputs to a Thrust Uncertainty Budget", determine applicability for this stand. Document why a term is excluded if it is.
2. For each applicable term, assign type-A or type-B and the basis for the standard uncertainty value. Cite source (cert, datasheet, in-house measurement, manufacturer's stated spec).
3. Derive the sensitivity coefficient for each term against thrust. Document the math.
4. Identify correlation between terms. Multi-cell stands sharing excitation, tare and reading from same cell, etc.
5. Compute the combined standard uncertainty `u_c` and expanded uncertainty `U_95 = 2·u_c` (or k from Welch-Satterthwaite if `ν_eff < 30`).
6. Compare to each named measurement objective. For any objective that the budget fails to meet, identify the dominant terms and the proposed mitigations (better thermal compensation, tighter alignment, re-calibration cadence, etc.).
7. Produce a baseline budget document with sign-off block for the responsible metrology engineer.
```

## Expected Output

- A complete JCGM-100-format uncertainty budget table: term, type (A/B), distribution, raw value, source citation, standard uncertainty, sensitivity coefficient, contribution to `u_c²`, percent of total.
- Correlation notes with explicit covariance terms applied where relevant.
- `u_c` and `U_95` in both N (or lbf) and % of expected reading at multiple representative thrust values across the FS range (so the % varies appropriately at low thrust).
- Comparison against each measurement objective with PASS / REWORK and dominant-term ranking.
- Mitigation roadmap for any failed objective with cost / schedule rough order of magnitude.
- Recommended re-evaluation triggers: cal cycle, environment change, side-load events, etc.
- Sign-off block for the responsible metrology engineer + reproducibility footer.
