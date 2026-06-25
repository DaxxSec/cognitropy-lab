# Ornithology Song Spectrogram Analysis Workspace

> Identify and classify bird vocalizations from spectrograms the way a systematist keys a specimen — by diagnostic characters, measured and vouchered, across two nested taxonomies (acoustic structure and biological identity).

## What This Workspace Does

This workspace turns Claude into an **avian bioacoustician** that reads spectrograms and produces defensible classifications. It frames every recording as a *specimen*: it is ingested with provenance, decomposed into the acoustic taxonomy (elements → syllables → phrases → songs → repertoire), measured against a standardized character set, and then keyed upward through the biological taxonomy to a species (or, where the voice can't resolve it, to the tightest taxon the characters support).

Today's organizing technique is **taxonomy and classification systems**, and the domain rewards it: birdsong is one of the few places where sound *is* a taxonomic character. Sister species that are visually identical — the `Empidonax` flycatchers, the *Phylloscopus* leaf warblers, the marsh/willow tit pair — are routinely separated by voice alone. So the workspace doesn't just label clips; it builds and applies **keys**: dichotomous decision trees whose every branch names the acoustic character it splits on, polythetic class definitions for variable singers, and confusion matrices that make cryptic-species and mimicry errors explicit instead of silent.

The product is a growing reference collection in `outputs/`: vouchered specimens, a repertoire catalog per taxon, and a maintained acoustic key. Each entry is reproducible — same audio, same spectrogram settings, same key yields the same determination.

## Why This Workspace Exists

Field recordings accumulate far faster than they get identified, and ad-hoc identification ("sounds like a thrush") is unreproducible and unfalsifiable. Bioacoustic monitoring — for breeding surveys, migration tracking, and biodiversity assessment — needs determinations that another analyst can check and that hold up when a record is rare or contested. This workspace codifies the systematist's discipline (measure, key, voucher) for sound, so an identification carries its evidence with it.

## Getting Started

### Prerequisites

- Audio files (WAV/FLAC preferred; lossy formats acceptable with provenance noting the codec)
- A spectrogram tool — [Raven Lite/Pro](https://www.ravensoundsoftware.com/) (Cornell), [Audacity](https://www.audacityteam.org/), or the R package [`warbleR`](https://cran.r-project.org/package=warbleR)/[`seewave`](https://cran.r-project.org/package=seewave)
- A working taxonomy reference (IOC World Bird List or eBird/Clements) for canonical names
- Optional: a [BirdNET](https://birdnet.cornell.edu/) baseline to triage candidates before keying (treat as a hypothesis generator, not an authority)

### Quick Start

1. Clone this workspace
2. Drop a recording in and run `/ingest-recording` — it renders a spectrogram and captures provenance
3. Run `/segment-syllables` then `/measure-acoustic-features` to build the labeled, measured element inventory
4. Run `/key-out-species` to descend the acoustic key to a determination, character by character
5. Run `/voucher-specimen` to commit the classified recording with its diagnostic characters to `outputs/specimens/`

## Command Reference

| Command | Description | When to Use |
|---------|-------------|-------------|
| `/ingest-recording` | Render spectrogram + capture provenance | First touch on any new clip |
| `/segment-syllables` | Decompose into elements/syllables/phrases | After ingest, before measuring |
| `/measure-acoustic-features` | Extract the standardized character set | Once segmentation is stable |
| `/key-out-species` | Descend a dichotomous acoustic key to a determination | When you have measurements and need an ID |
| `/build-repertoire` | Catalog an individual's/species' song-types | Multi-song individuals; species reference building |
| `/dialect-cluster` | Cluster recordings into dialects with a tested boundary | Geographic-variation studies |
| `/mimicry-trace` | Attribute borrowed elements to model species | Mockingbirds, lyrebirds, starlings, marsh warblers |
| `/confusion-audit` | Build a confusion matrix between similar taxa | Cryptic pairs; contested determinations |
| `/voucher-specimen` | Commit a classified reference voucher | Closing out any confident determination |

## Directory Structure

```
ornithology-song-spectrogram-analysis/
├── CLAUDE.md                 # Agent role, context refs, command list
├── README.md                 # This file
├── .claude/commands/         # Bespoke domain commands
├── context/
│   ├── concepts.md           # The dual taxonomy, spectrogram physics, acoustic characters
│   ├── workflows.md          # Specimen→classification pipeline, key building, dialect clustering
│   └── references.md         # Element glossary, measurement table, catalogues
├── prompts/                  # Reusable prompt templates
└── outputs/                  # Vouchered specimens, repertoire catalogs, the acoustic key
```

## Example Use Cases

### Resolving a cryptic flycatcher
A silent `Empidonax` is unidentifiable; a recorded `fitz-bew` vs `che-bek` is diagnostic. Ingest, measure the phrase structure and frequency contour, and key it out with the character cited.

### Building a species reference repertoire
A repeatedly recorded individual sings several song-types. `/build-repertoire` deduplicates and catalogs them, giving a reference any future recording can be matched against.

### Mapping a dialect boundary
Recordings of one species across a region cluster into song variants. `/dialect-cluster` proposes dialect classes and tests whether the boundary is real or a sampling artifact.

## Recommended MCP Servers

- **Filesystem** — read audio and spectrogram exports, write specimen dossiers to `outputs/`
- **Fetch / HTTP** — pull comparison recordings and taxonomy from Xeno-canto and the Macaulay Library APIs

## Legal & Ethical Considerations

- **Playback discipline.** Eliciting song with playback stresses territorial birds and disrupts breeding; it is restricted or banned for protected species, during breeding season, and in many reserves. Minimize it, log it, and never use it where prohibited.
- **Disturbance and access.** Don't trespass or approach nests for a recording. Record disturbance context in provenance.
- **Data sharing.** Honor the licenses of recordings pulled from public archives, and suppress precise localities for sensitive or persecuted species.

## Technical References

- [Raven Sound Analysis Software](https://www.ravensoundsoftware.com/) — the de-facto spectrogram + measurement tool (Cornell Lab)
- [Xeno-canto](https://xeno-canto.org/) — open archive of bird sounds with spectrograms, searchable by taxon and region
- [Macaulay Library](https://www.macaulaylibrary.org/) — the world's largest archive of wildlife audio/video (Cornell)
- [warbleR (R package)](https://cran.r-project.org/package=warbleR) — reproducible acoustic measurement and spectrographic cross-correlation
- [IOC World Bird List](https://www.worldbirdnames.org/) — a maintained global avian taxonomy for canonical names

## Optional plugin

If you have the [`workspace-foundational`](https://github.com/danielrosehill/Claude-Workspace-Foundational-Plugin) plugin installed, additional global commands (`/workspace-foundational:context-sweep`, `/workspace-foundational:find-template`) are available; the workspace works without it.
