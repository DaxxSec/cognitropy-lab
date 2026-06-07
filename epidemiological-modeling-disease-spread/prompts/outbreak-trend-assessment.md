# Outbreak Trend Assessment

## Purpose

Use this when you have a surveillance time series for an active or suspected outbreak and need a defensible read on whether transmission is growing, plateauing, or declining — with the reporting artifacts properly handled before any conclusion.

## Prompt Template

```
You are an infectious-disease modeller doing time-series trend analysis on surveillance data.

I have a disease-spread surveillance series:

- **Pathogen / syndrome:** [e.g. influenza A, novel respiratory pathogen, mpox]
- **Stream(s):** [cases / hospitalisations / deaths / ED visits / test positivity / wastewater]
- **Date axis:** [onset / specimen / report / death]
- **Grain & geography:** [daily or weekly; national / region / facility]
- **Span & snapshot date:** [series start–end; data vintage]
- **Reporting delay info:** [delay distribution or reporting triangle available? typical lag?]
- **Serial / generation interval:** [mean, SD, source — or "please suggest from references"]
- **Files:** [paths to the series / line list]
- **Context:** [interventions, testing-policy changes, holidays, known data revisions]

Please:
1. Triage the series (stream behaviour, date axis, day-of-week and holiday artifacts, truncated tail).
2. Nowcast or explicitly exclude the right-truncated window before any trend call.
3. Estimate the time-varying Rt (Cori/EpiEstim) with the stated serial interval and credible intervals.
4. Cross-check with the growth rate r → doubling/halving time and r→Rt conversion.
5. Give the current epidemic phase and any change-points.
6. State the trend verdict with explicit caveats (ascertainment, delay model, interval choice, power).
```

## Expected Output

- A triage note listing the artifacts found and how each was handled.
- Rt time series with CrI and the date it last crossed 1, plus the growth-rate cross-check.
- A phase classification with change-point timeline.
- An explicit "what's growing / plateaued / declining, and how confident" verdict.
- A caveat list (data vintage, serial interval, ascertainment, truncation) and recommended next data pulls.
