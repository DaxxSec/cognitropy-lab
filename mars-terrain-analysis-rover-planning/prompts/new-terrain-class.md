# New Terrain Class Documentation Prompt

## Purpose
Use this prompt when downlinked imagery reveals a terrain class that doesn't fit the existing categories (bedrock / regolith-rocky / regolith-fines / aeolian / conglomerate / mixed). New classes need to be added to the workspace's domain knowledge so future hazard maps can classify them; doing this poorly is how planners stop trusting their own hazard maps.

## Prompt Template

We've encountered a terrain feature in the latest downlink that doesn't classify cleanly under our existing scheme. I need to formalize it as a new terrain class.

**What was observed:**
- **Sol of observation:** <N>
- **Imagery source:** <hazcam / navcam / mast camera / orbital follow-up>
- **Rover position:** <coords>
- **Description:** <verbatim observer description — what does it look like?>
- **Comparison to existing classes:** <what's similar / what's different from the canonical 6 classes?>
- **Inferred origin:** <impact ejecta? Aeolian induration? Hydrothermal alteration? Frozen volatile?>

Please help me produce:

1. A **proposed class name** (lower-snake-case, fits the existing naming scheme).

2. A **definition paragraph** suitable for `context/for-agent/domain-knowledge.md`: 3–6 sentences, defines the class by observable features (texture, scale, slope tendency, rock distribution), distinguishes it from the closest existing class.

3. A **chord-framework treatment**:
   - What `class_penalty` weight does this terrain warrant in the hazard formula? (Compare to existing weights: bedrock 0.0, regolith-rocky 0.3, regolith-fines 0.5, aeolian 0.8, conglomerate 0.2, mixed 0.5)
   - What chord *flavors* does this terrain typically produce? (e.g., a class that's always at extreme slope tends to produce only fully-diminished chords — i.e., is mostly forbidden ground.)
   - Are there voice-leading penalties specific to entering or exiting this terrain class?

4. A **detection rubric** for `/terrain-assess`: how should the hazard pipeline recognize this class from a DEM + orthoimage? What slope range, roughness range, brightness range?

5. A **flight-rule recommendation** for `resources/flight-rules-quickref.md`: should this class be forbidden, restricted, or routine? Cite the rover-platform-specific reasoning.

6. A **dissent-friendly framing**: what concerns would each reviewer role (driver / science / mech-safety / autonomy / comms) raise the first time this terrain class appears in a candidate traverse?

## Expected Output

A self-contained classification proposal that can be merged into `context/for-agent/domain-knowledge.md` after a brief peer review. The proposal must include the dissent-friendly framing — adding a terrain class without thinking about reviewer concerns is how new classes silently bias hazard scoring.
