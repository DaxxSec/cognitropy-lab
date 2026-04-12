# Unknown Signal Analysis Prompt

## Purpose
Use this prompt when you've captured an unknown signal and need to systematically identify and decode it.

## Prompt Template

I have captured an unknown wireless signal with the following characteristics:

- **Center frequency:** [e.g., 433.92 MHz]
- **Observed bandwidth:** [e.g., ~50 kHz]
- **Capture sample rate:** [e.g., 2 Msps]
- **Capture format:** [e.g., complex float32, int8]
- **Signal behavior:** [e.g., periodic bursts every 30 seconds, continuous, event-triggered]
- **Known context:** [e.g., captured near IoT device, vehicle, weather station]
- **File location:** [path to .raw or .cf32 file]

Please analyze this signal by:
1. Recommending visual inspection steps (Inspectrum/GRC settings)
2. Identifying likely modulation based on the parameters
3. Suggesting demodulation approach
4. Walking me through frame extraction
5. Comparing against known protocols for this frequency band
6. Documenting the complete frame structure if successfully decoded

Use the resource optimization scoring to prioritize analysis steps if multiple signals are present.

## Expected Output
- Modulation identification with confidence level
- Demodulation parameters (symbol rate, deviation, etc.)
- Frame structure diagram
- CRC/checksum identification
- Match results against known protocols
- Recommended next steps
