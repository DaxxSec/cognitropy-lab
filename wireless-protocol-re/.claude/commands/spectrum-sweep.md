# /spectrum-sweep — Optimized Spectrum Sweep

Plan an optimized spectrum sweep using resource allocation algorithms.

## Required Inputs
- Frequency range (start-end MHz)
- Time budget
- SDR hardware
- Priority frequencies/bands

## Steps

### 1. Segment
Divide range into SDR-bandwidth segments. Tag with ISM overlap bonus, user priority, historical activity.

### 2. Optimize Schedule
Weighted interval scheduling with adaptive dwell:
- priority = base + ism_bonus + user_priority + history
- dwell = min_dwell * (1 + priority / max_priority)
- Sort descending, generate schedule

### 3. Commands
Generate hackrf_sweep / rtl_power commands with parameters.

### 4. Analyze Results
Parse CSV, find peaks (mean + 3 sigma), cluster into candidates, score: novelty*3 + strength*1 + duty_cycle*2 + complexity*2.

### 5. Discovery Report
Output to `outputs/sweep-report-{date}.md` with activity summary, ranked candidates, next steps.
