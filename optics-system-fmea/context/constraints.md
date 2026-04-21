# Constraints & Preferences

> Populated by `/onboard`.

## Technical Constraints
- **Size envelope:** TBD
- **Mass budget:** TBD
- **Cost ceiling (BOM):** TBD
- **Volume / packaging:** TBD
- **Assembly constraints:** TBD

## Regulatory / Standards
- [ ] ISO 10110 drawing compliance required
- [ ] MIL-STD-1472 human-factors scoping
- [ ] IEC 60825 laser safety (if Class 1+)
- [ ] ISO 9022 environmental test compliance
- [ ] Export control (ITAR / EAR) applies — flag dual-use
- [ ] Medical (FDA / CE MDR / IEC 60601) applies
- [ ] Space / aerospace (NASA, ESA, AS9100) applies

## Workflow Preferences
- **Preferred units:** SI (metric) unless the user overrides
- **Design software available:** TBD (Zemax OpticStudio / Code V / FRED / OSLO / Python-only)
- **FMEA framework:** AIAG-VDA (2019) by default; switch to MIL-STD-1629 if user requests
- **RPN action threshold:** 100 (any Sev=10 actioned regardless)
- **Risk appetite:** TBD (conservative / balanced / aggressive)

## Hard Rules
1. No laser design above Class 2 without a safety paragraph here.
2. No optimization of a detector-saturating condition without explicit user sign-off.
3. Every quantitative claim must cite an equation or standard.
4. Every design candidate must come with ≥3 failure modes BEFORE tolerance work begins.
