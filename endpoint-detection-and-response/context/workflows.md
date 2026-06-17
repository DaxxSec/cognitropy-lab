# Methodology — The Reconstruction Workflow

The canonical engagement is an eleven-phase reconstruction borrowed beat-for-beat from how a textile conservator brings a fragmentary garment back to a documented whole — with **geographic/spatial analysis** woven through every phase. Phases are ordered but iterative: discovery in a later phase routinely sends you back to re-provenance an artifact.

## Phase 0 — Salvage & accession (acquire the fragments)

1. Define scope: which hosts, which time window, which time zone (normalize everything to UTC and record the offset).
2. Acquire telemetry in **order of volatility** (RFC 3227): memory and live process tree first, then volatile EDR cache, then disk artifacts.
3. **Hash on acquisition.** Every artifact gets a SHA-256 at accession; this is the "accession number" that anchors chain of custody.
4. Record the data sources and exact queries. A fragment with no find-context is nearly worthless — note where each came from.

## Phase 1 — Provenance (where did this come from?)

For each artifact of interest, trace lineage backward: parent process → delivery vector → initial access. Establish the *find-context*: first-seen timestamp across Amcache/Prefetch/EDR, the user/session, and the path. Output a provenance chain with a confidence tag per link. → `/artifact-provenance`

## Phase 2 — Authentication (is it what it claims to be?)

Run the anachronism sweep. Compare `$SI` vs `$FN` timestamps, compile time vs first-execution, certificate validity, and OS-build compatibility. Flag every artifact whose chronology is internally inconsistent — these are tampered or planted. → `/anachronism-sweep`

**Decision:** if anachronisms cluster around one toolset → treat that toolset as adversary-controlled and re-baseline its provenance with suspicion. If timestamps are coherent → promote artifacts to the trusted timeline.

## Phase 3 — Stratigraphy (in what order were the layers deposited?)

Order the intrusion's components by *deposition*, not by discovery: initial access → execution → persistence → privilege escalation → defense evasion → the C2 layer on top. Reconstruct the strata even where intermediate layers were deleted (a missing layer leaves a negative impression — a gap in the chronology that other layers reference). → `/layer-stratigraphy`

## Phase 4 — Material analysis (which workshop made the tools?)

Fingerprint the tooling: compiler/linker artifacts, PE Rich header, packer signatures, language/runtime, string and code reuse, infrastructure-naming conventions. Separate **commodity materials** (off-the-shelf, weak attribution signal — like undyed linen anyone could buy) from **bespoke materials** (custom loaders, unique mutexes — strong signal, like a workshop's signature stitch). → `/material-fingerprint`

## Phase 5 — Geospatial mapping (today's technique)

Place the incident in space:

1. **Host layer** — plot affected endpoints on the org's site/subnet topology; identify the spatial cluster and the likely patient-zero.
2. **Diffusion layer** — model lateral movement as a spread process; draw the diffusion frontier and time-order it.
3. **Identity layer** — run geovelocity/impossible-travel on authentication events; flag sessions that cannot share a single human.
4. **Infrastructure layer** — resolve C2 to geolocation + ASN + RIR + hosting provider; map the "supply line." Annotate every geo claim with **resolution and source**.

→ `/geo-spread-map`

## Phase 6 — Timeline reconstruction (assemble the whole)

Merge the trusted artifacts, deposition strata, and geospatial events into one super-timeline. **Tag every entry** `CONFIRMED` (direct telemetry), `INFERRED` (logically forced by surrounding evidence), or `CONJECTURE` (plausible interpolation across a gap). Where the record is missing, state the gap explicitly rather than bridging it silently — the conservator leaves a documented lacuna, not an invented seam. → `/reconstruct-timeline`

## Phase 7 — Comparative typology (which family is this?)

Score the reconstructed TTP set against known campaign families and ATT&CK groups. Require **discriminating** techniques for a match, not shared commodity tooling. Produce ranked hypotheses with a similarity score and the specific TTPs that drive each. → `/campaign-typology`

## Phase 8 — Condition report (assess and stabilize)

Produce the conservator-style assessment of each host: what is intact, what is tampered, what persistence survives a reboot, what data was at risk. Translate directly into containment actions ordered by reversibility and impact. → `/condition-report`

## Phase 9 — Pattern drafting (make it reproducible)

Convert the most durable IOAs into detection rules (Sigma + the native EDR query language). Each rule is the "cutting pattern" that lets the SOC reproduce the detection on the next garment. Note false-positive surface and the telemetry source each rule requires. → `/pattern-draft`

## Phase 10 — Custody dossier (publish the defensible record)

Assemble the evidentiary package: executive summary, confidence-tagged timeline, provenance chains, anachronism findings, geospatial annex, typology hypotheses, detection rules, and a complete chain-of-custody log with acquisition hashes. → `/custody-dossier`

## Triage decision tree (entry point)

```
New alert / suspicious artifact
        │
        ├─ Is the artifact's chronology internally consistent?  ── no ──▶ /anachronism-sweep first (it is tampered/planted)
        │            │ yes
        ├─ Do we know where it came from? ── no ──▶ /artifact-provenance
        │            │ yes
        ├─ More than one host involved? ── yes ──▶ /geo-spread-map (map diffusion before deep dive)
        │            │ no
        ├─ Need actor hypothesis? ── yes ──▶ /material-fingerprint → /campaign-typology
        │            │ no
        └─ Ready to write up ──▶ /reconstruct-timeline → /condition-report → /pattern-draft → /custody-dossier
```

## Confidence-tagging rule (applies to every phase)

- `CONFIRMED` — backed by direct, corroborated telemetry from ≥1 independent source.
- `INFERRED` — not directly observed but logically forced by surrounding confirmed evidence.
- `CONJECTURE` — a plausible interpolation across a gap; must be labelled and must never be cited downstream as if confirmed.

If you cannot tag a claim, you do not yet have the claim — go acquire more fragments.
