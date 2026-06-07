# /nowcast

Correct recent counts for reporting delay and right-truncation so the present edge of the series can be read as a trend rather than an artifact.

## Inputs

- The series **plus** a reporting structure: ideally a **reporting triangle** (event date × reporting delay) or a fitted/known **delay distribution** (onset → report).
- Number of recent time points to nowcast `k` (≥ max plausible delay).
- Method preference (multiplier / Bayesian / hierarchical) and whether the delay is stationary.

## Steps

1. Read `context/workflows.md` "Workflow 3: Nowcasting the truncated present".
2. Build the empirical delay distribution from the reporting triangle, or import a known one.
3. Test for **non-stationary delay** (has the delay distribution drifted over the epidemic?). If yes, use a time-varying delay model.
4. Choose the method:
   - **Inverse-CDF multiplier** — quick, assumes stationary delay.
   - **Bayesian generative** (`surveillance::nowcast`, `epinowcast`, EpiNow2) — proper intervals, handles non-stationarity.
5. Produce nowcast counts for the last `k` points with prediction intervals.
6. Annotate which points are observed vs nowcast; never silently overwrite.
7. Write the nowcast series + figure to `outputs/`.

## Output

`outputs/nowcast-<stream>-<snapshot-date>.md` + figure: observed series, nowcast tail with intervals (distinct styling), the delay distribution used, stationarity verdict, and a corrected trend read for the recent window.

## Notes

- The raw tail **always** looks like a decline because of right-truncation — this command is the antidote; run it before any peak/decline call.
- If no delay data exist, the honest move is to **exclude** the truncated window from trend calls, not to invent a multiplier.
- A non-stationary delay (e.g. lab backlog clearing) will make a fixed multiplier over- or under-shoot — check first.
