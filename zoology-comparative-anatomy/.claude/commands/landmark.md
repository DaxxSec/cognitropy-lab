# /landmark — Catalog anatomical landmarks for a body region

Foundation for geometric morphometrics. Produces a landmark list with definitions, Bookstein-classification, and (if image-derived) coordinates.

## Inputs

Required:
- **Specimen ID**.
- **Body region** — precisely defined. "Skull lateral view" is acceptable; "skull" alone is not (specify view or 3D vs. 2D).
- **Image / mesh source** — path to image file, or 3D mesh file, or "I'll provide as we go".

Optional:
- Reference scheme (e.g. Klingenberg 2011 mouse cranium scheme; Adams & Otárola-Castillo 2013).

## Pre-flight

- Image scale calibrated? Scale bar present and length stated, OR pixel-to-mm calibration provided. If neither, halt and ask.
- For 3D meshes: units of the mesh (mm? voxels?), and origin/orientation convention.

## Procedure

For each landmark:

1. **Name** — unambiguous, ideally tied to a published landmark scheme.
2. **Definition** — anatomical position in words, replicable by another worker without seeing this output.
3. **Type** (Bookstein 1991):
   - **Type I** — discrete juxtaposition of tissues (suture intersection, tooth-tooth contact, foramen center). Highest replicability.
   - **Type II** — local geometric property (point of maximum curvature, deepest point of a fossa). Medium.
   - **Type III** — extremal point relative to another landmark (point on margin most distant from landmark X, point at end of an axis through two other landmarks). Lowest replicability — flag.
4. **Coordinates** if image- or mesh-derived: with image/mesh reference and units.
5. **Notes** — replicability concerns, alternative definitions in literature, missing-data status (e.g. "absent due to specimen damage", flag distinct from "absent due to anatomy").

End with a **Replicability summary**: count of Type I, II, III; expected inter-observer error class.

## Output

`outputs/landmarks/<specimen-id>__<region>.md`

If multiple specimens are landmarked with the same scheme, also produce a TPS file `outputs/landmarks/<scheme>.tps` aggregating them — TPS is the standard input format for tpsRelw, geomorph, etc.

## Validation

- Landmark list is non-empty and each has a name.
- Each landmark's definition is replicable by another worker (test: imagine you're a colleague with no context — does the definition uniquely identify the point?).
- Type assignment is justified.
- Missing-data is flagged distinctly from anatomical absence.

## Common pitfalls

- Calling a landmark "Type II" when it's actually a Type III (defined relative to another landmark, not by local geometry).
- Vague definitions: "anterior tip of the nasal" — anterior in which view? Define the reference view.
- Mixing 2D and 3D landmarks in the same output without flagging.
