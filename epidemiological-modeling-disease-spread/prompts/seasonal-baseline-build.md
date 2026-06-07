# Seasonal Baseline Build

## Purpose

Use for a seasonal pathogen (influenza, RSV) when you need to define "above-normal" — building epidemic thresholds from historical seasons so the current season can be read against a principled baseline rather than gut feel.

## Prompt Template

```
Build a seasonal epidemic baseline and thresholds for this pathogen.

- **Pathogen / indicator:** [e.g. influenza ILI %, RSV admissions, positivity]
- **Series & path:** [weekly counts/rates across multiple seasons]
- **Seasons available:** [list seasons; MMWR or ISO week aligned?]
- **Method preference:** [Moving Epidemic Method (MEM) / Serfling cyclic regression / specify]
- **Geography & strata:** [national / region; age groups]
- **Use:** [onset detection, intensity levels, weekly situational reports]

Please:
1. Align the seasons to a common epidemiological-week index (MMWR/ISO) — do not align by naive calendar week.
2. Choose and justify the baseline method (MEM thresholds vs Serfling sinusoidal+trend regression).
3. Derive the pre-epidemic threshold (onset), intensity thresholds (low/medium/high/very-high), and post-epidemic threshold.
4. Overlay the current season and mark threshold crossings (onset week, current intensity level).
5. Report uncertainty in the thresholds and how many seasons underpin them.
6. State caveats (atypical seasons, definition changes, sparse early seasons).
```

## Expected Output

- A baseline figure: historical seasons + threshold bands + the current season overlaid.
- The threshold table (pre-epidemic, intensity levels, post-epidemic) with the method and seasons used.
- The current-season status: onset week (if crossed) and present intensity level.
- A caveat list and a recommendation for routine weekly use.
