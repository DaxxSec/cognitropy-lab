# Ornithology Song Spectrogram Analysis — Reference Tables

Compact lookup data. Defer to the upstream catalogues for full specs.

## Acoustic element-type glossary

| Term | Definition | Spectrogram appearance |
|------|-----------|------------------------|
| Element / note | Smallest continuous trace | One unbroken stroke |
| Syllable | One+ elements as a repeated unit | Recurring small cluster |
| Phrase / motif | Stereotyped run of syllables | Repeated block |
| Trill | Fast repetition of one syllable | Dense vertical comb |
| Whistle | Pure-tone, slow FM | Thin clean line |
| Buzz | Broadband, fast unresolved modulation | Vertical smear / hatching |
| Warble | Continuously varying complex | Tangled multi-shape run |

## Standardized acoustic measurements

| Character | Definition | Unit | Classification use |
|-----------|-----------|------|--------------------|
| Peak frequency | Frequency of maximum energy | Hz / kHz | Coarse pitch class |
| Low / high frequency | −X dB band edges | Hz | Bandwidth, range |
| Bandwidth | High − low frequency | Hz | Tonal vs broadband |
| Element duration | Onset → offset | ms | Temporal character |
| Inter-onset interval | Onset → next onset | ms | Pace / rhythm |
| Syllable rate | Elements per second | /s | Trill speed |
| FM slope | Δfrequency / Δtime | Hz/ms | Contour shape |
| Element-type count | Distinct types per song | n | Complexity / repertoire |

## Spectrogram parameter cheat-sheet (Hann window, ~48 kHz audio)

| Window length | Time resolution | Frequency resolution | Best for |
|---------------|-----------------|----------------------|----------|
| 256 samples | Fine (~5 ms) | Coarse (~190 Hz) | Fast trills, sharp onsets (wideband) |
| 512 samples | ~11 ms | ~95 Hz | General-purpose default |
| 1024 samples | ~21 ms | ~47 Hz | Tonal pitch, contour |
| 2048 samples | Coarse (~43 ms) | Fine (~23 Hz) | Harmonics, fine pitch (narrowband) |

Overlap 50–75%; always report window length, FFT size, overlap, and window function with any measurement.

## Call-function categories

| Function | Typical form | Notes |
|----------|-------------|-------|
| Advertising song | Long, complex, loud | Mate attraction / territory; often male, seasonal |
| Contact call | Short, simple, repeated | Flock cohesion |
| Flight call (NFC) | Very short, often high | Diagnostic for nocturnal migration ID |
| Alarm call | High, thin, ventriloquial | Hard to localize by design |
| Mobbing / scold | Harsh, broadband, repeated | Recruits other birds |
| Begging | Rapid, rising, persistent | Nestlings/fledglings |

## Upstream catalogues and tools

- **Xeno-canto** — https://xeno-canto.org/ — open global bird-sound archive with spectrograms; API for fetching comparison cuts.
- **Macaulay Library (Cornell)** — https://www.macaulaylibrary.org/ — largest curated wildlife audio archive.
- **Raven Pro / Lite** — https://www.ravensoundsoftware.com/ — spectrogram viewing, selection tables, measurements.
- **warbleR (R)** — https://cran.r-project.org/package=warbleR — reproducible measurement, spectrographic cross-correlation, signal detection.
- **seewave (R)** — https://cran.r-project.org/package=seewave — acoustic analysis primitives.
- **BirdNET** — https://birdnet.cornell.edu/ — neural classifier; use as a hypothesis generator, not an authority.
- **IOC World Bird List** — https://www.worldbirdnames.org/ — canonical global taxonomy.
- **eBird/Clements taxonomy** — https://www.birds.cornell.edu/clementschecklist/ — checklist used by Macaulay/eBird.
- **Avibase** — https://avibase.bsc-eoc.org/ — taxonomic concordance across checklists.

## Operating cheat-sheet

- Render wideband **and** narrowband before measuring; they reveal different characters.
- Nyquist = sample_rate / 2; confirm the file resolves the species' frequency range before trusting high-frequency bounds.
- Tobias et al. (2010) vocal scoring criteria underpin many modern species-limit decisions — cite when arguing splits/lumps.
