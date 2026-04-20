# Environment

<\!-- Populated by /onboard. Defaults below. -->

## User environment defaults
- OS: unspecified (the workflows are OS-agnostic).
- Editor: Claude Code in Cowork mode.
- Storage: local filesystem within this workspace.
- Network: air-gapped assumption for any real case material; integrations optional and external only.

## Paths
- Subject folders: `outputs/subjects/<SUBJ-ID>/`
- CE alert folders: `outputs/ce-alerts/<alert-id>/`
- Deliverables: `user-docs/subjects/<SUBJ-ID>/`

## Naming conventions
- Subject IDs: `SUBJ-NNNN` (zero-padded 4 digits).
- Scan filenames: `scan-YYYYMMDD.md`.
- Alert IDs: `CE-YYYYMMDD-NN`.
- Deliverable filenames: `<type>-YYYYMMDD.md` (adjudicative-memo, reinvest-plan, etc.).
