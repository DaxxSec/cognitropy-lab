# Prompt — EMI Root-Cause Postmortem

## Purpose

After `/isolate-emi-culprit` has identified a source / coupling / mitigation chain, write the design-feedback document for engineering. Captures what passed, what failed, what was changed, what we learned for next time.

## Prompt Template

```
Author the EMI root-cause postmortem.

DUT: [name, hardware revision, firmware version]
FAILING TEST: [standard + section, e.g. CISPR 32 30-1000 MHz radiated Class B]
FAILING FREQUENCY/RANGE: [e.g. 117.6 MHz, 12 dB over limit]
DETECTOR: [quasi-peak / average / peak]
SUSPECT LIST (PRE-INVESTIGATION): [from /isolate-emi-culprit ranking]
BISECTION LOG: [the dB drops per power-down step]
NEAR-FIELD MAPS: [paths under outputs/maps/]
COUPLING PATH IDENTIFIED: [cable common-mode | enclosure seam | aperture | ground bounce | other]
MITIGATION(S) APPLIED: [in order, with retest result]
RESIDUAL MARGIN: [final dB vs. limit after mitigation]
RETROFIT vs. DESIGN-CHANGE DECISION: [snap-on for production now / board respin in next rev / both]

Write the postmortem in this structure:

1. SUMMARY — the chain in one paragraph: source → coupling path → emission, with the final margin.
2. DETECTION — how the failure was reproduced; the spectral signature.
3. INVESTIGATION — bisection log table; near-field confirmation; coupling-path evidence (current-clamp readings, aperture tests).
4. MITIGATION ATTEMPTS — table of (mitigation, expected dB, achieved dB, cost). One row per attempt, in chronological order.
5. ROOT CAUSE — the underlying design factor, not just the proximate component (e.g. "DC-DC switching node connected to cable shield via inadequate common-mode choke" rather than "the buck converter").
6. RECOMMENDATIONS — for production retrofit, for next board revision, for the EMC design rule set going forward.
7. LESSONS — what the team learned that should change future pre-compliance protocols.

Cross-reference the artefacts (raw data, maps, photos) by path. The postmortem is the input to next quarter's design-rules review.
```

## Expected Output

A markdown postmortem at `outputs/emi/<date>-<dut>-postmortem.md` that:

- Names the proximate component **and** the underlying design factor — two distinct things, both must be in the report.
- Includes the mitigation table with cost so a product-engineering decision is informed.
- Closes with at least three design-rule lessons phrased as "Going forward, the team will …" — not "Going forward, the team should …".
