# Prompt: FMEA Mode Brainstorm

Use when you need to seed an FMEA with a broad mode list.

---

For the optical system described in `context/project.md`, brainstorm failure modes across these eight categories. Aim for 3–5 modes per category. Do not score yet — just enumerate.

Categories:
1. **Optical surface** (coating, damage, contamination, scratch-dig)
2. **Optical material** (stress birefringence, striae, bubble/inclusion, absorption)
3. **Mechanical mount** (decenter, tilt, axial shift, preload loss)
4. **Bonding / adhesive** (fracture, creep, outgassing, bubble)
5. **Thermal** (focal shift, bond-line stress, condensation, dn/dT drift)
6. **Vibration / shock** (modal, impact, settled decenter)
7. **Stray light / scatter** (ghost, diffraction off edges, scatter off mounts)
8. **Human factors / assembly** (cleanliness, mis-assembly, handling damage)

Output: a markdown table with columns `Category | Mode | Effect | Typical Cause`.
