# Availability-vs-Cost Curve

## Purpose

Produce the availability-vs-cost curve for a link and recommend the *economically justified* availability — the knee where the next "nine" costs more than the outage it prevents. Use during margin allocation, especially on rain-dominated Ka/Q/V bands.

## Prompt Template

```
You are pricing link availability as a cost-benefit problem. The last nine is the most expensive; find the knee.

Inputs:
- **Band & site:** [frequency, ITU-R rain region or rain stats, elevation, polarization]
- **Clear-sky margin:** [dB]
- **Requested availability:** [e.g. 99.9%]
- **Outage cost:** [$ per minute / per hour]
- **Mitigation options + costs:** [static margin $/dB, ACM (scheduler + return-path $), site diversity ($/site), uplink power control]

Please:
1. Build the rain fade-exceedance curve (ITU-R P.618) and the dB required for each availability target (99%, 99.5%, 99.9%, 99.99%).
2. Price each dB three ways — static margin, ACM, site diversity — including the clear-sky opportunity cost of static dB.
3. Compute expected annual outage cost and the marginal $ per nine.
4. Recommend the cheapest mitigation mix to the economically justified availability, and flag any gold-plating above it.
```

## Expected Output

- A fade-exceedance / dB-per-availability table
- A static-vs-ACM-vs-diversity cost comparison
- The marginal $ per nine and the recommended (possibly lower-than-requested) availability target
- A one-line mitigation recommendation
