# Prompt: Laser Safety Classification (IEC 60825)

Use when any laser is present in the design.

---

For the laser described below, determine the IEC 60825-1 class and compute the MPE (maximum permissible exposure) for a 100 mm skin and 0.25 s eye accommodation:

Inputs I need from you:
- Wavelength
- CW power OR pulse energy + PRF + pulse width
- Beam diameter at aperture
- Beam divergence
- Whether the beam is expanded, collimated, or diverging

Compute:
1. AEL (accessible emission limit) per IEC 60825-1 Table 3/4
2. Class: 1, 1M, 2, 2M, 3R, 3B, or 4
3. NOHD (nominal ocular hazard distance)
4. MPE @ 100 mm, 0.25 s
5. Required enclosure / interlock level
6. Labels required

Output an FMEA-ready safety paragraph for `context/constraints.md`.
