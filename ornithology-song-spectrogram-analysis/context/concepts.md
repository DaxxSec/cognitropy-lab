# Ornithology Song Spectrogram Analysis — Core Concepts

Background to read before classifying. Optimised for fast recall. The organizing idea: **two nested taxonomies** — one of *sound structure*, one of *biological identity* — connected by spectrogram-measurable characters.

## The dual taxonomy

**Acoustic hierarchy** (what the sound is made of, low rank → high rank):

- **Element / note** — the smallest continuous trace on a spectrogram (one unbroken pen-stroke). The atom of classification.
- **Syllable** — one or more elements produced as a unit, typically the smallest repeated thing.
- **Phrase / motif / trill** — a stereotyped run of syllables (a trill is a fast repeated syllable).
- **Song** — a complete, structured vocalization, usually with a function (mate attraction, territory).
- **Song-type** — a discrete variant a bird repeats; many species have a repertoire of several to hundreds.
- **Repertoire** — the full set of song-types an individual (or population, or species) commands.

**Biological hierarchy** (what the sound is evidence for): individual → population → **dialect** → subspecies → species. The acoustic hierarchy is *observed directly*; the biological hierarchy is *inferred* from it. The whole discipline is the disciplined inference from the first to the second.

## Spectrogram physics and the resolution tradeoff

A spectrogram is a short-time Fourier transform: signal sliced into overlapping windows, each FFT'd, magnitude plotted as time (x) × frequency (y) × intensity (color). The **uncertainty principle** governs it: you cannot have fine time *and* fine frequency resolution at once.

- **Short window** (e.g. 256 samples) → good *time* resolution (sharp onsets, fast trills), coarse frequency — "wideband" spectrogram.
- **Long window** (e.g. 2048 samples) → good *frequency* resolution (resolves harmonics, fine pitch), smeared time — "narrowband" spectrogram.
- Always state window length, FFT size, overlap, and window function (Hann is standard) — they change what characters are visible and therefore the classification.

## The acoustic character set

The measurable characters a key splits on (full table in `references.md`):

- **Frequency characters** — peak frequency (max-energy), low/high frequency bounds, bandwidth, dominant-frequency contour shape (rising, falling, V, inverted-V, flat, modulated).
- **Temporal characters** — element duration, inter-element/inter-onset interval, song duration, syllable rate (elements/s), pace trend (accelerating/decelerating trill).
- **Modulation characters** — frequency modulation (FM) depth and slope, amplitude modulation (AM), presence of harmonics vs pure tone vs broadband noise.
- **Structural characters** — number of distinct element types, repetition rule (eventual vs immediate variety), phrase ordering, introductory vs terminal elements.

## Call vs song typology

- **Song** — typically longer, more complex, learned (in oscines), seasonal, male-biased; functions in mate attraction and territory.
- **Call** — short, simpler, often innate; functional categories: contact, flight, alarm (often high and thin to be hard to localize), begging, scolding/mobbing, flush.
- Functional category is itself a classification axis and is frequently more diagnostic than song for non-passerines and for flight identification (nocturnal flight calls / "NFCs").

## Geographic variation and dialects

- **Dialect** — a population-level song variant with a geographic boundary; classic in white-crowned sparrow, chaffinch, corn bunting.
- **Clinal variation** — gradual change across space (no sharp boundary); must be distinguished from true dialects.
- **Song sharing / matched countersinging** — neighbors converging on shared types; a within-population pattern, not a taxonomic one.
- The key risk: mistaking infraspecific variation for a species-level difference (or vice versa).

## Vocal learning and mimicry

- **Oscine passerines learn** their song (culturally transmitted) → high variability, dialects, and mimicry. **Suboscines and most non-passerines have largely innate** vocalizations → more stereotyped and more reliably diagnostic.
- **Mimics** (northern mockingbird, European starling, marsh warbler, lyrebird) embed borrowed elements from model species; classifying their song requires *attributing* elements across taxa rather than to the singer — a cross-taxon classification problem (`/mimicry-trace`).

## Voice in resolving cryptic species

Where morphology fails, voice often succeeds — voice is a recognized taxonomic character in modern checklists:

- `Empidonax` flycatchers (Alder vs Willow split partly on `fee-bee-o` vs `fitz-bew`).
- *Phylloscopus* / leaf warblers; the redpolls; marsh vs willow tit; many *Myiarchus* and tropical antbirds.
- Tobias et al. (2010) quantitative vocal criteria are now used to score species limits.

## Common Failure Modes

- **Over-segmentation** — splitting one frequency-modulated element into several because the spectrogram window is too short or a harmonic is mistaken for a separate note.
- **Recording-quality confounds** — distance, reverberation, and low SNR attenuate high frequencies and blur fine structure, biasing measured bandwidth and peak frequency.
- **Individual variation as taxonomy** — treating one bird's idiolect or a learned dialect as a species character.
- **The Lombard effect & masking** — birds raise pitch/amplitude in noise; urban recordings can shift measured frequency.
- **Mimicry mis-attribution** — scoring a mimic's borrowed phrase as the model species being present.
- **Classifier over-trust** — accepting a BirdNET/automated label as a determination instead of as a hypothesis to key out.

## Operating Constraints

- **Ethics & law** — playback restrictions for protected/breeding birds and in reserves; no nest disturbance; honor archive licenses and suppress sensitive-species localities.
- **Physical** — microphone frequency response and sample rate bound what you can measure (Nyquist: a 48 kHz file resolves to 24 kHz — fine for most birds, marginal for high-frequency species).
- **Reproducibility** — determinations must travel with their spectrogram parameters, clip times, and the diagnostic character cited at each key split.
