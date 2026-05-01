# Puppet Mechanism Failure Modes — Tactic × Technique Catalog

> The puppetry analogue of the [MITRE ATT&CK matrix](https://attack.mitre.org/). Every detection rule must tag at least one tactic and one technique from this catalog. Additions go through `/peer-review`.

## How to Read This Catalog

- **Tactic** = the *why* of a failure: the high-level operational class (e.g. *string-system-drift* — strings are no longer at their intended tuning).
- **Technique** = the *how*: the specific mechanism by which the tactic manifests (e.g. *gradual-stretch* — string material slowly creeps under sustained load).

Rules tag with `tactic.<id>` and `technique.<id>`. Reports aggregate by tactic to surface company-wide trends.

## Catalog v1.0

### Tactic: string-system-drift
String tuning has drifted from baseline; the marionette / rod-puppet is no longer where the rigger left it.

| Technique ID | Name | Notes |
|---|---|---|
| ssd-001 | gradual-stretch | Spectra creep, polyester relaxation; cumulative over weeks |
| ssd-002 | hygroscopic-shrink | Polyester strings absorbing humidity; reverses on dry-out |
| ssd-003 | knot-slippage | Single-step tuning loss at a knot or anchor |
| ssd-004 | anchor-detachment | String partially detached from puppet anchor; usually a precursor to break |
| ssd-005 | airplane-twist | Airplane control bar rotated off-axis on the rigger's hand |

### Tactic: servo-axis-drift
Animatronic axis no longer at commanded position.

| Technique ID | Name | Notes |
|---|---|---|
| sad-001 | zero-point-creep | Hobby servo zero drift; ~1–3°/12-hour day |
| sad-002 | temperature-offset | Servo offset shifts with ambient temperature |
| sad-003 | bearing-wear-jitter | Broadband noise above 30 Hz in current spectrum |
| sad-004 | end-stop-overshoot | Servo overshooting commanded end position |
| sad-005 | encoder-quantization-drift | Encoder rounding errors accumulating; industrial axes |

### Tactic: foam-latex-fatigue
Foam-latex skin or mechanism has lost elasticity or shape memory.

| Technique ID | Name | Notes |
|---|---|---|
| flf-001 | mouth-mech-hysteresis | Mouth doesn't fully close after sustained cycling |
| flf-002 | brow-mech-permanent-set | Brow position drifted from baseline; recovery slower than 30s |
| flf-003 | jaw-skin-tear | Latex tear at the jaw hinge |
| flf-004 | foam-compaction | Foam lost loft; mechanism feels under-driven |
| flf-005 | adhesive-creep | Skin separating from armature at glued seams |

### Tactic: ensemble-sync-loss
Two or more performers are no longer in coordination.

| Technique ID | Name | Notes |
|---|---|---|
| esl-001 | handoff-lag | One performer arrives late on a handoff cue |
| esl-002 | breath-cue-miss | Breath-cue not caught by partner |
| esl-003 | weight-cue-miss | Weight-cue through the puppet not caught |
| esl-004 | omozukai-hidari-phase-lag | Bunraku-specific: head and left-arm phase mismatch |
| esl-005 | ashizukai-floor-drift | Bunraku-specific: feet drifting from staging mark |

### Tactic: screen-geometry-drift
Wayang-kulit / shadow-puppet geometry on the kelir has drifted.

| Technique ID | Name | Notes |
|---|---|---|
| sgd-001 | screen-distance-shift | Puppet-to-screen distance off baseline |
| sgd-002 | backlight-flicker | Backlight intensity unstable; affects silhouette read |
| sgd-003 | hide-warp | Buffalo hide curling away from screen plane |
| sgd-004 | rod-anchor-loosening | Articulated arm rod slipping at body anchor |

### Tactic: arc-of-motion-failure
Stop-motion / animatronic motion violating arc-of-motion principle.

| Technique ID | Name | Notes |
|---|---|---|
| amf-001 | linear-interpolation-leak | Stop-motion: a joint moved on a straight line, not an arc |
| amf-002 | follow-through-clipped | Animation: end of gesture cut short of natural follow-through |
| amf-003 | anticipation-skipped | Animation: action without setup motion |
| amf-004 | ease-out-collapsed | Animation: deceleration too sharp |

### Tactic: performer-fatigue
Performer-side degradation; not a puppet failure but presents as one.

| Technique ID | Name | Notes |
|---|---|---|
| pf-001 | grip-tremor | High-frequency tremor in joint trace; performer-fatigue indicator |
| pf-002 | off-axis-loading | Performer holding rig at non-baseline angle |
| pf-003 | calibration-skip | Pre-show calibration shortened or omitted |
| pf-004 | new-performer-bound | New performer's Effort drifts toward Bound |

### Tactic: environment-induced
External conditions are the proximate cause.

| Technique ID | Name | Notes |
|---|---|---|
| ei-001 | thermal-shift | Temperature change moved a mechanism off baseline |
| ei-002 | humidity-shift | Humidity change affected hide / latex / strings |
| ei-003 | travel-shock-misalignment | Touring travel shock misaligned a rig |
| ei-004 | venue-geometry-mismatch | New venue's wing space, fly height, or sightlines incompatible with home rehearsal |

## Tactic-by-Tradition Heat Map

Not every tactic applies to every tradition. The heat map helps onboarding decide which tactics are worth caring about for their puppets:

| Tradition | string-system-drift | servo-axis-drift | foam-latex-fatigue | ensemble-sync-loss | screen-geometry-drift | arc-of-motion-failure | performer-fatigue | environment-induced |
|---|---|---|---|---|---|---|---|---|
| String marionette | ★★★ | — | — | ★ | — | — | ★★ | ★★ |
| Bunraku / ningyō jōruri | ★★ | — | — | ★★★ | — | — | ★★★ | ★ |
| Wayang kulit | ★ | — | — | ★ | ★★★ | — | ★★ | ★★ |
| Hand / rod (Henson-school) | ★ | — | ★★★ | ★ | — | — | ★★ | ★ |
| Animatronic | — | ★★★ | ★★ | — | — | — | — | ★★★ |
| Stop-motion | — | — | ★ | — | — | ★★★ | — | ★★ |

★★★ — primary concern; ★★ — secondary; ★ — occasional; — not applicable

## Adding Catalog Entries

Catalog additions are made via `/peer-review` with target `outputs/reviews/<date>-taxonomy-proposal.md`. Two distinct-role reviewers, plus the catalog maintainer (typically a senior tradition-bearer or company lead). Approved additions bump the catalog version (semver: minor for new techniques, major for new tactics or restructuring).

## References

- MITRE ATT&CK Framework — [attack.mitre.org](https://attack.mitre.org/) — the structural model.
- Bell, John — *American Puppet Modernism* (2008) — for many of the named failure modes.
- Adachi, Barbara — *The Voices and Hands of Bunraku* (1978) — for ensemble-sync-loss techniques.
- Mrázek, Jan — *Phenomenology of a Puppet Theatre* (2005) — for wayang screen-geometry drift cases.
