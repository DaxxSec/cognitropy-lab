# /capture-plan — Generate Optimized RF Capture Plan

Generate a resource-optimized capture plan for a target frequency range or specific device.

## Required Inputs
- Target frequency or frequency range
- Available SDR hardware (from `context/for-agent/environment.md`)
- Time budget for capture session
- Storage budget (GB available for IQ files)

## Procedure

### 1. Assess Constraints
- Calculate instantaneous bandwidth of available SDR
- Determine required sample rate for target signal bandwidth
- Estimate storage: `sample_rate * bytes_per_sample * duration`
- Check if target falls within SDR's frequency range

### 2. Apply Weighted Spectrum Scheduling
If scanning a wide range:
- Divide into bands equal to SDR instantaneous bandwidth
- Assign priority weights (ISM band overlap, user frequencies, historical density)
- Sort by priority/bandwidth ratio
- Generate time-sequenced capture schedule

### 3. Optimize Capture Parameters
For each band: sample rate (Nyquist * 1.2 margin), gain settings, dwell time (2x longest expected frame interval), squelch threshold (noise floor + 6 dB), and decimation factor.

### 4. Generate Capture Commands
Output ready-to-run commands for the user's SDR with file naming: `{date}_{freq_MHz}_{samplerate}_{gain}.raw`

### 5. Resource Estimates
Total capture time, storage required, processing time estimate, and recommended analysis priority order.

Save to `planning/capture-plan-{date}.md` and log in `work-log/`.
