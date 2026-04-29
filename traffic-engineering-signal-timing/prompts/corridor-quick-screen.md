# Corridor Quick-Screen Prompt

## Purpose
Decide in 30 minutes whether a corridor is a viable retiming candidate for an environmental-co-benefits engagement, before committing to the full pipeline.

## Prompt Template

I'm evaluating whether to undertake a retiming + environmental impact assessment on the following corridor:

- **Corridor:** [route, jurisdiction, from-cross-street to to-cross-street]
- **Length:** [miles]
- **Number of signalized intersections:** [N]
- **Last retimed:** [year, agency]
- **Average ADT:** [vehicles/day if known]
- **Existing coordination:** [yes/no/partial; common cycle if known]
- **Air-quality basin:** [non-attainment status by pollutant if known]
- **CMAQ-eligible:** [yes/no]
- **Funding source on the table:** [CMAQ / TSMO / Capital / unknown]
- **Recent complaints / drivers:** [delay, queueing, emissions, transit OTP, ped service]

Please screen this corridor by:

1. **Retiming benefit potential.** Based on signal count, time since last retiming, and coordination status, what's the rough delay-reduction headroom (high / medium / low)?
2. **Emissions benefit potential.** Given the air-quality basin status and ADT, is the corridor likely to yield meaningful CO2/NOx benefits (high / medium / low)?
3. **Funding fit.** Does the combined delay + emissions story qualify for CMAQ? What other funding programs might fit?
4. **Risk flags.** Any reason to expect this corridor to be a retiming dead-end? (downstream bottleneck, geometric issue masquerading as timing, irregular detection, controller obsolescence, jurisdictional split)
5. **Recommended next step.** Proceed to `/onboard` and full pipeline, or escalate a different intervention?

## Expected Output
- Three rough benefit/potential ratings with one-sentence rationale each
- Funding-program fit assessment
- 2–4 risk flags
- Single-sentence go/no-go recommendation with confidence level
