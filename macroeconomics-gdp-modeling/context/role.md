# User Role

> Populated by `/onboard`.

## Typical Personas This Workspace Serves

- **Sell-side macro strategist** publishing a quarterly GDP nowcast and short-term outlook for clients.
- **Central bank or policy institution researcher** running real-time forecasting horseraces and writing methodology papers.
- **Sovereign analyst** at a multilateral or rating agency covering a single country's growth outlook.
- **Quantitative macro PM** running real-time forecasts as part of a discretionary or systematic macro book.
- **Academic researcher** working on real-time data methodology, MIDAS, DFMs, or revision behaviour.

## Defaults Until `/onboard`

- Assume the user is **technically fluent in Python** and comfortable with `pandas`/`statsmodels`.
- Assume **professional-grade rigour** — they want reproducibility, not just point forecasts.
- Assume they understand the difference between **real-time and revised** data and care about it.
- Assume **publication consequences** — a bad number costs reputation, money, or both.

## What the Agent Should Do With This

- Always speak in real-time terms: "as of vintage v2026-04-30..." rather than "the value is..."
- Recommend procedures, not just answers: "the right next step is `/audit-revision` because the BEA released this morning."
- Flag reproducibility gaps loudly. If the user is about to publish without sealing inputs, refuse and explain.
- Match the user's seniority — do not over-explain GDP measurement to a central bank researcher.
