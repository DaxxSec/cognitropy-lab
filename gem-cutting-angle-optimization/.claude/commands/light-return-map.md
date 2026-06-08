# /light-return-map — Brilliance / Fire / Scintillation Trade-off Map

Build a map of optical performance across a grid of crown and pavilion angles so you can pick the crown that balances fire against brilliance for the material in hand.

## Inputs

- Material RI and dispersion (from `context/references.md`).
- Pavilion main band from `/optimize-pavilion-angle`.
- Crown-angle range to explore (typically 30–45°).
- Intended table % (default 56%).

## Steps

1. Lay out a grid: pavilion main (a few values across its safe band) × crown main (across the explored range).
2. For each cell, reason qualitatively about the three effects: brilliance (TIR completeness, driven by pavilion + table), fire (crown steepness × material dispersion), scintillation (facet count/precision — roughly constant across the grid for a fixed design).
3. Mark the windowing edge (pavilion too shallow) and the nailhead edge (pavilion too steep) on the map.
4. Identify the **balance ridge** — the crown angle where added fire stops being worth the brilliance it costs, given this material's dispersion. High-dispersion stones (diamond, zircon, sphalerite) justify steeper crowns; low-dispersion stones (quartz, beryl) do not.
5. Recommend a crown/pavilion pair and explain the trade made.

## Output

A grid/table with each cell rated for brilliance/fire and annotated with the window and nailhead edges, plus a one-line recommendation. Save to `outputs/<material>-light-map.md`.

## Notes

- Low-dispersion material: don't chase fire with a steep crown — you only lose brilliance. Keep the crown moderate.
- For a true ray-trace, export the chosen design to GemRay; this command is the fast bench-side approximation.
