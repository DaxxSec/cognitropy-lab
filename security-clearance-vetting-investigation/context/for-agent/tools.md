# Tools

## Tools the agent CAN and SHOULD use

- **Filesystem / Write / Edit** — primary memory is this repo.
- **Bash (where available)** — for generating calendar files, SHA-256 hashes of inputs, or aggregating JSON indexes.
- **Calendar MCP (optional)** — to push `reinvest.ics` into the user's calendar.
- **SQLite MCP (optional)** — if the user wants a local scan history database in `outputs/history.db`.

## Tools the agent MUST NOT use

- **No HTTP calls to authoritative systems.** DISS, NBIS, Scattered Castles, e-QIP/NBIS application portals — do not attempt to integrate.
- **No queries to commercial data brokers** (LexisNexis Accurint, TransUnion, CLEAR, Thomson Reuters CLEAR). These are used in real investigations, but only via agency contracts and not through an LLM.
- **No web scraping of personal social media.** Open-source intelligence on subjects is governed by agency policy (SEAD 5) and not something this workspace executes.
- **No PII exfiltration.** Never write real subject identifiers to any committed file.

## Integration suggestions (the user wires these up, not the agent)

- Obsidian / local notes for case context.
- Calendar (Google / Outlook / iCal) for scheduled scan dates.
- A redaction pre-processor (pdfredact, redactor.py) to sanitize inputs before paste.
