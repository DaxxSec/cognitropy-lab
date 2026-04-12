# ISM Band Device Survey Prompt

## Purpose
Use this prompt to perform a systematic survey of all wireless devices operating in a specific ISM band within your environment.

## Prompt Template

I want to survey all wireless devices operating in the [315/433/868/915/2400] MHz ISM band in my [home/office/lab/vehicle].

**My hardware:**
- SDR: [e.g., HackRF One]
- Antenna: [e.g., telescopic whip]
- Environment: [e.g., suburban home, no Faraday cage]

**Goals:**
- Catalog all active devices and their transmission patterns
- Identify which protocols are in use (known vs. unknown)
- Map the spectrum occupancy over a [1 hour / 24 hour] period
- Flag any unexpected or suspicious transmissions

Please:
1. Generate an optimized sweep schedule using the weighted spectrum scheduling algorithm
2. Provide exact capture commands for my hardware
3. After I provide the sweep data, analyze and catalog all signals found
4. For each signal, attempt identification against known protocol databases
5. Produce a device survey report sorted by priority score

## Expected Output
- Sweep schedule with timing
- Ready-to-run capture commands
- Device catalog with protocol IDs
- Spectrum occupancy summary
- Flags for unknown/suspicious signals
