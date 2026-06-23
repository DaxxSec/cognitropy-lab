# Archival Preservation Digital Scanning — Core Concepts

Background the agent reads before acting. Two halves: the **preservation imaging** craft (standards, files, metadata, condition) and the **resource-optimization** framing that schedules it. Optimized for fast recall.

## Imaging Standards and Conformance

Three standards dominate cultural-heritage capture; they overlap but differ in how they express targets:

- **FADGI** (Federal Agencies Digital Guidelines Initiative, US) — a **1–4 star** rating per metric. 4★ = preservation-grade for irreplaceable originals; 1–2★ = access/high-volume. Pragmatic, widely cited in North America.
- **Metamorfoze** (Netherlands) — three tiers: **Preservation** (strictest), **Light**, **Extra Light**. Strong on tone/color aims and very explicit tolerances.
- **ISO 19264-1** — the international standard for **image quality analysis** of heritage capture; defines Levels A/B/C and the metrics/targets used to certify a capture chain. Increasingly the lingua franca for conformance.

The metrics these standards constrain (measured from a target chart): **spatial resolution** (sampling efficiency, SFR/MTF — MTF50 in cycles/mm), **tone reproduction** (OECF — opto-electronic conversion function), **color accuracy** (ΔE against reference patches, mean and max), **white balance / gray balance**, **illumination uniformity**, **noise**, **chromatic aberration**, and **flare**. "Resolution" alone is meaningless without sampling efficiency: a sensor can claim 600 ppi yet resolve far less.

## File Formats and the Master/Derivative Split

- **Preservation master** — captured once to the highest justified standard, **never altered**. Uncompressed **TIFF** (or lossless **JPEG 2000**), **16-bit/channel**, embedded **ICC profile**, working color space (Adobe RGB / ECI-RGB for masters). Tonal headroom in 16-bit preserves the ability to reprocess for needs you cannot anticipate.
- **Derivatives** — regenerable from masters at any time, optimized for delivery: **sRGB JPEG** access copies, **IIIF**-tiled pyramids for deep zoom, **OCR/HTR** text, thumbnails. Because they are disposable, they may be lossy and freely re-optimized.

The cardinal rule: **masters are forever, derivatives are disposable.** Never degrade or discard a master to save space; never publish a master where a derivative belongs.

## Metadata Models

A preservation surrogate is more than pixels. Four metadata types travel with it:

- **Descriptive** — what the item *is* (Dublin Core, MODS, or a finding-aid node): title, creator, date, identifier.
- **Structural** — how parts relate (**METS**): page order, master↔derivative binding, navigable object structure.
- **Technical** — how it was captured (**MIX / NISO Z39.87** for still images): dimensions, bit depth, color space, device, ICC profile.
- **Provenance / preservation** — what happened to it (**PREMIS**): capture, QA, derivative-creation, fixity events, each with agent, timestamp, outcome. This is the machine-readable chain of custody.

## The OAIS Frame

**OAIS** (ISO 14721) is the reference model for trustworthy digital preservation. Key package types:

- **SIP** (Submission) — what arrives for ingest.
- **AIP** (Archival) — the preserved object: master + all metadata + fixity, the thing this workspace builds.
- **DIP** (Dissemination) — what's served to users (the access derivatives).

An isolated TIFF is an *orphan* — without provenance and fixity it is a file no future curator can trust. The AIP, not the loose master, is the preservation object.

## Fixity and Integrity

- **Fixity** = the property that a file has not changed. Verified with cryptographic checksums (**SHA-256** preferred; MD5 legacy/fast but collision-weak).
- **Bit rot / silent corruption** — undetected flips from media decay, transfer error, or hardware fault. Detected only by recomputing checksums against a baseline manifest.
- A "changed" checksum with **no logged preservation event** is the canonical signal of corruption or tampering — an incident, not a glitch.
- **Fixity is useless without replicas** — it tells you the master is bad but gives nothing to restore from. The verification cadence and the replication policy are one decision. See **NDSA Levels of Digital Preservation** for a tiered maturity model.

## Material Condition and Decay Markers

Condition grades route material to capture paths (see `workflows.md`):

| Grade | Meaning | Path |
|---|---|---|
| Pristine / Stable | Safe to handle and capture normally | Standard in-house |
| Fragile | Handleable with care + multiplier | In-house + conservator consult |
| At-risk (unique) | Degraded and irreplaceable | In-house only — **no transit** |
| Unstable | Actively failing | **Conservation-first** — stabilize before imaging |

Format-specific decay markers: **vinegar syndrome** (acetate film off-gassing acetic acid), **nitrate film** (chemically unstable, flammable — safety hazard), **sticky-shed syndrome** (magnetic tape binder breakdown), **flaking emulsion** (glass-plate negatives), **brittle/acidic paper**, **mold** (safety + spreads). Active decay is an **urgency override** that pins a lot to the front of the queue regardless of demand.

## The Resource-Optimization Framing

Capture hours, operators, storage, and budget are scarce; backlogs span decades. The recurring decisions map to operations-research problems:

- **Prioritization → 0/1 knapsack.** Maximize Σ value subject to Σ cost ≤ capacity. Exact via dynamic programming for ≤ a few hundred lots; greedy value-density (`value / cost`) for larger sets, with a stated optimality gap.
- **Station assignment → unrelated-parallel-machines makespan (R||Cmax).** NP-hard; **Longest-Processing-Time-first (LPT)** is the bounded-approximation baseline, improved by local search.
- **Backlog → queueing (M/M/c or M/G/c).** Check stability `ρ = λ / (c·μ) < 1`; if accessions outpace service, no finish date exists — report the stability gap, not a false date.
- **In-house vs. vendor → make-vs-buy** with **hard ethical gates** (no-transit for irreplaceable material) that override the cheaper option.

**Weights are governance, not constants.** Choosing access-demand over preservation-urgency is a policy decision and must be visible in the output, never buried in a coefficient.

## Common Failure Modes

- **Convenience scanning** — digitizing what's easy instead of what's most at-risk or most in demand; the backlog's worst material rots while easy lots get done.
- **Under-specified capture** — discovering years later that masters fail the standard and must be re-shot, often impossible once the original has degraded further.
- **Nameplate throughput** — planning on a device's stated images/hour; real labs run ~60–75% of nameplate after rework, calibration, and staffing reality.
- **Transit loss** — shipping unique originals to a vendor to "save money" and damaging or losing the irreplaceable.
- **Fixity-free storage** — TIFFs with no checksums or provenance; a silent bit-flip a decade later goes undetected and unrecoverable.
- **Ignored QA drift** — slow ΔE creep from an aging lamp or stale profile silently spoils a whole day's captures.

## Operating Constraints

- The object outranks the schedule: condition and conservation always override throughput.
- Rights gate dissemination; provenance and fixity are mandatory for everything captured.
- Reproducibility: capture settings, optimization weights, and cost inputs are recorded so every decision can be re-derived and defended.
