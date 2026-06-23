# /spec-capture-profile — Define a standards-conformant capture profile

Produce a complete, citable imaging specification for a given material type pinned to a target standard (FADGI star level, Metamorfoze level, or ISO 19264-1), so capture is right the first time and never needs re-shooting.

## Inputs

- Material type and reflectance/transmission class (reflective: manuscripts, bound volumes, photographs; transmissive: negatives, slides, microfilm).
- Target standard and level (e.g. FADGI 4-star, Metamorfoze Preservation, ISO 19264-1 Level A).
- Largest physical dimension (drives required sensor resolution to hit the target ppi).
- Intended use: preservation master, access, or both.

## Steps

1. **Select the standard and level.** Map the use case to a level using `context/references.md` (FADGI 4★ / Metamorfoze Preservation for irreplaceable originals; lower tiers for high-volume access).
2. **Derive spatial resolution.** Choose ppi so the smallest significant detail is resolved (typ. 400–600 ppi reflective; transmissive scaled to output size, often 2000–4000+ ppi for small negatives). Verify the sensor can deliver true (not interpolated) ppi at the object's largest dimension.
3. **Set tone and color targets.** Bit depth (16-bit/channel for masters), color space (Adobe RGB or ECI-RGB working space, embedded ICC profile), and the standard's aim values for OECF, white balance, and ΔE.
4. **Specify the capture chain.** Light source and CRI, polarization if needed for gloss, copy-stand vs. planetary scanner, target charts to shoot (e.g. an objective/device-level target appropriate to the standard), and capture cadence for target shots.
5. **Define file outputs.** Master format (uncombined TIFF or JPEG2000 lossless), naming convention, embedded technical metadata, and the derivative recipe (handed to `/assemble-aip-package`).
6. **Write the conformance checklist.** Enumerate the measurable pass/fail criteria `/audit-image-quality` will test against, with the standard's tolerance for each.

## Output

`outputs/capture-profile-<material>.md`: the chosen standard/level with citation, resolution + bit depth + color space, light/optics spec, target-chart and cadence plan, master + derivative file spec, and the measurable conformance checklist. This profile is the contract both capture and QA work against.

## Notes

- True optical resolution ≠ marketing dpi. Confirm sampling efficiency / MTF against the standard before trusting a device's stated ppi.
- 16-bit masters are not optional for preservation-grade work — they preserve tonal headroom for future reprocessing you cannot anticipate today.
- One profile per material class. A profile that tries to cover manuscripts and glass-plate negatives at once will satisfy neither.
