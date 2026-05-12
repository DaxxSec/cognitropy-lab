# Environment Setup

> Populated by `/onboard`. The agent uses this to know what storage, audit, and case-management context the analyst is operating in.

## Workspace Classification Level
<!-- Default unclassified / CUI. If higher, the workspace must be deployed on a system rated for that level. The agent will refuse to ingest material above the workspace's stated classification. -->

## System of Record
<!-- The case-management system the workspace's outputs ultimately feed: CIIS, FBI Sentinel, NCIS CLEOC, agency equivalent, or a sanctioned private-sector platform. This workspace is the analytic layer; system of record is separate. -->

## Audit Logging
<!-- How session activity is preserved. At minimum: the work-log/ folder is appended to per session. If the host environment provides additional auditing (HBSS, Splunk, agency audit framework), document it here. -->

## Storage Disposition
<!-- Retention policy for analytic working files. Many CI authorities mandate retention rules; document what applies here so the agent does not propose deletion outside policy. -->

## Source-System Access
<!-- Which raw source systems the analyst can query: defense-vetting databases, financial reporting systems, badge-log systems, DLP/UEBA dashboards, OSINT-vetted feeds. The agent will not propose pulling from a system the analyst cannot lawfully access. -->

## Connectivity
<!-- Are external lookups (open-source research, lawful court records) available from this system? Many CI environments are air-gapped — note constraints so the agent does not propose unreachable steps. -->

## Tooling Available
<!-- What structured-analytic-technique tooling is in reach: ACH spreadsheets, Excel, Palantir Gotham (if authorized), specialized CI workflow tools, or just markdown. The agent matches its outputs to tool availability. -->

## Subject Population Size (if a hub-level program)
<!-- For insider-threat hubs running this workspace across many subjects, document the population size and how this case fits into the broader prioritization. -->

## Backup and Recovery
<!-- How analytic work is preserved across system events. -->

## End-of-Session Hygiene
<!-- Steps the analyst takes at end-of-session: clear scratch, rotate credentials, log out of source systems. The agent will remind at session close. -->
