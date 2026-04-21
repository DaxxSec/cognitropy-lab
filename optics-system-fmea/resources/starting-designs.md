# Starting-Point Designs

Curated starting points for each common optical system type. Use these to bootstrap `/design-optical-system`.

## Visible Imaging
| f/# | FOV | Starting form | Reference |
|---|---|---|---|
| f/5+ wide | <30° | Cooke triplet | Smith §13 |
| f/2–4 | <30° | Double-Gauss | Smith §16 |
| f/1.0–2.0 | <15° | Petzval / Zeiss Planar | Smith §17 |
| f/1.4 wide | 60°+ | Retrofocus / Distagon | Smith §18 |
| Long focal | small | Telephoto | Smith §19 |

## LWIR (8–14 µm)
| Form | Notes |
|---|---|
| Ge doublet | Simple, achromatic in LWIR |
| Ge-ZnSe triplet | Wider FOV, better correction |
| Diffractive Ge singlet | Athermal, mass-saving |

## MWIR (3–5 µm)
| Form | Notes |
|---|---|
| Si-Ge doublet | Cheap, common |
| BaF₂ / CaF₂ / ZnSe triplet | Cold-stop efficient |

## Spectrometers
| Form | Wavelength | Notes |
|---|---|---|
| Czerny-Turner | UV-VIS-NIR | Stigmatic with toroidal mirror |
| Littrow | Any | Compact, double-pass grating |
| Echelle | Broad + high resolution | 2D format, cross-disperser |
| Offner relay | UV-VIS | Low distortion |

## Laser
| Scenario | Starting point |
|---|---|
| Fiber-coupled pump | Aspheric collimator + focus lens |
| Beam expander | Galilean (-/+) or Keplerian (+/+) |
| Beam shaper | Powell lens or integrator rod |

## Metrology
| Scenario | Starting point |
|---|---|
| Fizeau interferometer | Transmission flat + reference |
| Michelson | Beam splitter + two arms |
| Twyman-Green | Collimated Michelson variant |

## References
- Warren J. Smith, *Modern Lens Design* (2nd ed.)
- Robert E. Fischer, *Optical System Design* (2nd ed.)
- Pantazis Mouroulis, *Geometrical Optics and Optical Design*
