# /ingest-recording

First touch on any new clip: render its spectrogram and bind it to provenance so everything downstream is reproducible and citable. A recording without provenance is a sound, not a specimen.

## Inputs

- Audio file path (WAV/FLAC preferred; note codec if lossy)
- Locality (place, coordinates if available), date, time
- Recordist, equipment (mic, recorder), and whether playback was used
- Any field-determined taxon ("as-recorded" label — treated as a hypothesis, not truth)

## Steps

1. Read the file; record sample rate, bit depth, duration, channels, and compute the Nyquist ceiling (sample_rate / 2).
2. Render **two** spectrograms — wideband (short window, e.g. 256 samples) and narrowband (long window, e.g. 2048) — with window/FFT/overlap recorded.
3. Note SNR qualitatively (clean / moderate / poor), reverberation, and background species audible in the cut.
4. Assign an accession ID (`<taxon-or-unk>-<YYYYMMDD>-<seq>`) and create `outputs/specimens/<accession-id>/`.
5. Write `provenance.md` capturing every field above plus spectrogram parameters and any playback/disturbance.

## Output

`outputs/specimens/<accession-id>/provenance.md` plus the two spectrogram exports. The accession ID is the handle every later command references.

## Notes

- If high frequencies look attenuated and the species is high-pitched, flag it — distance and low sample rate both bias frequency measurements.
- Keep the "as-recorded" taxon clearly marked as unverified; the workspace's job is to confirm or overturn it by character.
