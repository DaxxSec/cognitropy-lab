# Endpoint Detection & Response — Core Concepts

Background to read before acting. The premise of this workspace: an EDR investigation is an act of **reconstruction from fragmentary, layered, partly-tampered physical evidence** — structurally identical to reconstructing a historical garment from extant pieces, portraits, and inventories. The disciplines that keep costume reconstruction honest (provenance, anachronism detection, material analysis, stratigraphy, typology, and the evidence/conjecture boundary) port directly onto endpoint forensics, and the geographic lens that costume historians use for regional dress and trade routes ports onto the spatial spread of an intrusion.

## EDR fundamentals

**What EDR is.** Endpoint Detection & Response is continuous recording of host-level activity (a sensor/agent streaming telemetry to a backend) plus detection logic and response tooling. It sits between EPP (preventive antivirus), XDR (correlation across endpoint + network + identity + cloud), and SIEM (log aggregation across the enterprise). EDR's distinctive value is the *time-ordered behavioral record* — the equivalent of stitch-by-stitch construction notes on a garment.

**Telemetry types (the "fragments").** Process creation with full command line and parent lineage; file create/modify/delete; registry key/value changes; network connections (5-tuple + DNS); module/DLL loads; driver loads; AMSI script content; named pipes; WMI activity; authentication events; scheduled-task and service creation. On Windows these surface via the EDR sensor, Sysmon, and the Windows Event Log; on Linux via auditd/eBPF; on macOS via the Endpoint Security framework.

**Indicators, by altitude.**
- **IOC** (Indicator of Compromise) — atomic, brittle artifacts: a hash, an IP, a domain, a mutex. The "torn-off button" of evidence.
- **IOA** (Indicator of Attack) — behavioral: "office app spawned a script interpreter that made an outbound connection." Survives cosmetic change.
- **TTP** (Tactic, Technique, Procedure) — the actor's method, mapped to MITRE ATT&CK. The "construction style of the workshop" — hardest to fake, best for attribution.

**MITRE ATT&CK** is the field's shared typology: 14 tactics (Reconnaissance → Impact) decomposed into techniques and sub-techniques, each with detection and mitigation notes. Use it as the canonical vocabulary in every reconstruction so findings compose across cases.

## The reconstruction mapping (the crossover)

| Historical costume reconstruction discipline | EDR analogue in this workspace |
|---|---|
| **Provenance research** — sourcing an extant garment, tracing ownership and find-context | **Artifact provenance** — where a binary/process/key originated, how it was delivered, its lineage (`/artifact-provenance`) |
| **Anachronism detection** — a metal zipper on a "1600s" gown, aniline dye before 1856 | **Temporal-inconsistency hunting** — timestomping, backdated MFT records, version/build mismatches (`/anachronism-sweep`) |
| **Material analysis** — fiber under microscopy, dye by HPLC, weave & stitch type → workshop | **Tooling fingerprint** — compiler/linker artifacts, packer, Rich header, code reuse, language → actor (`/material-fingerprint`) |
| **Stratigraphy** — documented layering of a garment (shift → kirtle → gown → accessories) | **Intrusion strata** — dropper → loader → implant → persistence → C2, in deposition order (`/layer-stratigraphy`) |
| **Evidence vs. informed conjecture** — what the source documents vs. what the reconstructor interpolates | **Confidence tagging** — `CONFIRMED` telemetry vs. `INFERRED` vs. `CONJECTURE` (every command enforces it) |
| **Comparative typology** — regional dress families, period style typologies | **Campaign/TTP family matching** — ATT&CK groups, known intrusion sets (`/campaign-typology`) |
| **Condition report** — conservation assessment: losses, damage, prior interventions | **Compromise assessment** — what is intact, tampered, persistent + containment (`/condition-report`) |
| **Pattern drafting** — the cutting pattern that lets you reproduce the garment | **Detection rule** — the Sigma/EDR query that lets you re-detect the behavior (`/pattern-draft`) |
| **Geographic distribution & trade routes** — regional styles, dye/silk supply lines | **Geospatial spread** — host geography, lateral diffusion, geovelocity, C2 geolocation/ASN (`/geo-spread-map`) |

The mapping is not decorative. Each discipline carries a *failure mode it was invented to prevent*, and that failure mode also exists in EDR — which is exactly why the import is useful.

## Anachronism detection — the deepest analogue

Costume authentication lives or dies on spotting materials and techniques that could not have existed in the claimed period. EDR's equivalent is **temporal forensics**, and the richest tell is the NTFS timestamp pair:

- Every file has `$STANDARD_INFORMATION` (`$SI`) timestamps — the ones Explorer shows and the ones malware alters with `SetFileTime` (ATT&CK **T1070.006 Timestomp**) — and `$FILE_NAME` (`$FN`) timestamps held in the parent directory's MFT index, which most timestomping tools do *not* touch. When `$SI` predates `$FN`, or `$SI` has zeroed sub-seconds while neighbors don't, you have caught a "zipper on the Tudor gown."
- Corroborating chronologies: Prefetch, Amcache, ShimCache/AppCompatCache, SRUM, USN journal, $LogFile, and event-log sequence numbers. A binary whose Amcache first-execution predates its own compile timestamp is an anachronism.
- **PE compile timestamp vs. observed-on-host time, certificate validity windows, and OS build compatibility** are the cyber equivalent of dye chronology and sewing-machine-stitch dating.

## Geographic / spatial analysis (today's technique)

Costume historians map *where* a style or material belongs — regional folk-dress typologies, and the trade routes that carried cochineal from the New World, indigo from India, silk along the Silk Road. The intrusion has the same spatial structure:

- **Host geography** — physical/site placement of affected endpoints; cluster the incident on the org's spatial topology (sites, subnets, business units).
- **Lateral movement as diffusion** — model spread as a spatial/graph process; the "patient-zero" host and the diffusion frontier are the analogues of a fashion's place of origin and its spread.
- **Geovelocity / impossible travel** — successive authentications from locations farther apart than travel time allows (ATT&CK **T1078 Valid Accounts** abuse); the cyber tell that two "garments" cannot share one wearer.
- **C2 topology** — geolocation, ASN, RIR allocation, and hosting-provider of command-and-control infrastructure; the "supply line." Always state GeoIP **resolution and source** — country-level is usually reliable, city-level often is not.

## Common failure modes

- **Conjecture hardening into fact** — an analyst's plausible inference is repeated until it is treated as confirmed. The conservator's evidence/conjecture rule exists precisely to stop this; enforce confidence tags.
- **Single-timestamp trust** — believing `$SI` alone; always corroborate against `$FN` and independent chronologies.
- **GeoIP over-attribution** — concluding actor nationality from C2 geolocation. C2 is rented; geography is a lead, not a verdict.
- **Stratigraphic inversion** — assuming the first artifact *found* is the first *deposited*. Order discovery ≠ order of events; rebuild deposition order from corroborated time, not from query order.
- **Typology forcing** — pattern-matching to a famous campaign because it is famous. Score the match; require discriminating TTPs, not just shared commodity tooling.
- **Chain-of-custody breaks** — analyzing originals, losing the order of volatility, or failing to hash before/after. Destroys evidentiary value the way handling destroys a fragile textile.

## Operating constraints

- Authorized scope only; respect data-protection law for any PII in telemetry (usernames, IPs, geolocation are personal data under GDPR/CCPA).
- Preserve order of volatility (RFC 3227) and chain of custody; hash artifacts on acquisition and document every transfer.
- Treat GeoIP/ASN as probabilistic; never make an irreversible decision (attribution, legal referral) on geolocation alone.
