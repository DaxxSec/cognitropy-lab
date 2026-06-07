# /build-epicurve

Construct and quality-check an epidemic curve from a line list or aggregate counts, surfacing the reporting artifacts that would otherwise be read as epidemiology.

## Inputs

- Path to a **line list** (one row per case, with onset/specimen/report/death dates) or **aggregate counts** (`date`, `count`, optional strata).
- Which **date** to bin on (onset > specimen > report; state which and why).
- Aggregation grain (daily / weekly-MMWR) and any strata to facet (region, age, variant).
- Data **snapshot date** (for the truncation note).

## Steps

1. Read `context/workflows.md` "Workflow 0: Series intake and triage".
2. Parse dates; convert weekly bins to MMWR weeks if applicable; reconcile time zones / locales.
3. Bin counts on the chosen date axis; build the curve with `incidence2` (R) or pandas resample (Py).
4. Run QC sweep: detect day-of-week periodicity (autocorrelation at lag 7), holiday cliffs, zero-runs, negative/late corrections (data revisions), and level shifts (case-definition changes).
5. Mark the **right-truncated tail** (last ~max-reporting-delay points) explicitly — shade or flag, do not interpret.
6. Overlay a 7-day trailing mean for visual de-noising (annotate that it is not the trend estimate).
7. Plot the curve (+ facets); write the figure and a QC note to `outputs/`.

## Output

`outputs/epicurve-<stream>-<snapshot-date>.md` + figure: the curve, the QC findings table (artifact → location → recommended handling), the marked truncated window, and a one-line readiness verdict ("clean for Rt after nowcast" / "exclude tail" / "definition shift at <date> — split series").

## Notes

- An epicurve is the *input* to every other command — get the date axis and truncation right here or everything downstream inherits the error.
- A run of exact zeros mid-series is almost always missing data, not zero incidence.
- Report-date and onset-date curves of the same outbreak differ by the reporting delay; never compare them as if equivalent.
