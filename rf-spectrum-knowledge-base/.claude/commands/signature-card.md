# /signature-card — Build a Compact KB-Ready Signature Card

Produce a one-screen "signature card" for a single emitter — the dense, scannable summary that sits at the top of its KB entry and feeds quick visual identification.

## Inputs

- A single emitter: an existing KB entry, a draft, or measured parameters
- Optional: a reference waterfall/spectrogram description or a Signal Identification Wiki match to anchor the visual description

## Steps

1. **Pull the core parameters.** Center frequency, occupied bandwidth, modulation/access scheme, channel spacing, duty cycle / burst structure, polarization (if known), typical power/occupancy.
2. **Describe the visual fingerprint.** In words: what the signal looks like on a waterfall (continuous carrier, hopping, bursty, wideband noise-like, FSK "rails", OFDM block, etc.) — the cue an analyst uses to recognize it at a glance.
3. **List discriminators.** The 2–4 features that separate this emitter from its look-alikes (e.g. "same band as X but 12.5 kHz spacing vs. 25 kHz", "hops within 10 ms vs. Y's 400 ms dwell").
4. **Attach identity & provenance.** Identification + confidence, service/allocation, region, and a one-line provenance (last capture, hardware).
5. **Render the card.** Emit a fixed-layout card (table + visual-fingerprint line + discriminators) ready to paste atop the entry.

## Output

A signature-card block (markdown table + fingerprint + discriminators + identity line) written to the top of `outputs/kb/<entry>.md`, or standalone at `outputs/cards/<freq>-<slug>.md` for sharing.

## Notes

- The card is for *recognition*, not completeness — keep it to one screen; depth lives in the full entry.
- Always include at least one discriminator vs. a known look-alike; a card with no discriminators is just a parameter list and won't speed identification.
- Keep the card's numbers in sync with the entry — regenerate the card whenever `/emitter-entry-author` changes a core parameter.
