# FMEA Mode Catalog — Optical Systems

Starter library of failure modes indexed by functional group. Use as a prompt for brainstorming. Not exhaustive.

## Optical Surfaces
| Mode | Effect | Cause | Detection |
|---|---|---|---|
| AR coating delamination | Transmission drop, backscatter | Thermal cycle, humidity, adhesion | Visual, MIL-C-675 tape, witness sample |
| Scratch / dig exceedance | Image artifact, scatter | Mishandling, cleaning | Microscope per MIL-PRF-13830B |
| Abrasion of first surface | Increased stray light | Field exposure, cleaning cycles | Periodic inspection |
| Fogging | Softened contrast | Internal outgassing, humidity ingress | Dew-point test |
| Particulate contamination | Image blobs, scatter | Assembly cleanliness, gasket failure | IEST-STD-CC1246, particle count |

## Optical Materials
| Mode | Effect | Cause | Detection |
|---|---|---|---|
| Stress birefringence | Polarization artifact, WFE | Over-tight mount, molding stress | Polariscope |
| Striae / inclusions | WFE, scatter | Glass quality | Inspection per ISO 10110-3 |
| Solarization | Transmission drop UV/VIS | UV exposure over life | Witness glass, spectrometer |
| Radiation darkening | Transmission drop | Space / medical radiation | Spectroradiometer |

## Mechanical / Mount
| Mode | Effect | Cause | Detection |
|---|---|---|---|
| Element decenter | Coma, astigmatism | Shock, assembly drift, preload loss | Autocollimator, interferometer |
| Element tilt | Coma, boresight shift | Mount tolerance stack-up | Autocollimator |
| Focus drift | MTF loss | Thread creep, shock | Focus check post-shock |
| Preload loss | Free element | Viscoelastic creep, thermal ratchet | Shake + inspect |

## Bonding / Adhesive
| Mode | Effect | Cause | Detection |
|---|---|---|---|
| Bond-line fracture | Catastrophic decenter | CTE mismatch, shock | Thermal cycle + vibe |
| Adhesive creep | Slow decenter | Load + time | Long-duration test |
| Adhesive outgassing | Fogging on cold surfaces | Non-vacuum-rated adhesive | TQCM, residual gas analysis |
| Adhesive absorption | Transmission artifacts | Adhesive in optical path | QA inspection |

## Thermal
| Mode | Effect | Cause | Detection |
|---|---|---|---|
| Focal shift out of DoF | Blurred image | Mismatched CTE / dn/dT | Thermal chamber test |
| Bond stress fracture | See above | CTE mismatch at bond | FEA + thermal cycle |
| Condensation on cold optic | Attenuation, scatter | Humidity + thermal gradient | Dew-point margin |
| Window thermal gradient | Figure distortion | Solar load | FEA, thermal test |

## Vibration / Shock
| Mode | Effect | Cause | Detection |
|---|---|---|---|
| Modal coincidence | Amplified motion | Mount stiffness low | Sine sweep |
| Impact fracture | Catastrophic | Handling, transport drop | Drop test |
| Fastener backing-out | Loss of preload | Vibration + no thread-lock | Post-vibe inspection |

## Stray Light
| Mode | Effect | Cause | Detection |
|---|---|---|---|
| Narcissus (IR) | Self-image of cold detector | Back-reflection from optic | Thermal image background check |
| Ghost reflection | Second image | Two-surface back reflection | Ray trace, bench test |
| Edge diffraction | Halo | Sharp aperture edge | Stray light test |
| Housing scatter | Reduced contrast | Bare metal, oily surface | Housing blackening |

## Laser-Specific
| Mode | Effect | Cause | Detection |
|---|---|---|---|
| LIDT exceedance | Coating burn | Fluence > LIDT | Beam monitor + fuse |
| Interlock bypass | Safety hazard | Tamper, design error | Audit, FMEA |
| Thermal lensing | Beam quality drop | Pump absorption | M² monitor |
| Mode hopping | Power fluctuation | Diode temperature | TEC + stability log |

## Human / Process
| Mode | Effect | Cause | Detection |
|---|---|---|---|
| Mis-orientation | Anamorphic error | Unmarked element | Assembly aid, poka-yoke |
| Cleanroom breach | Contamination | Gowning error | Particle count trend |
| Wrong glass lot | Index drift | Stockroom error | Lot traceability, QA |
