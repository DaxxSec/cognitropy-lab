# Environment

> Populated by `/onboard`.

## User's Simulation Tooling
- [ ] Zemax OpticStudio (version: TBD)
- [ ] Code V
- [ ] FRED (stray light)
- [ ] OSLO
- [ ] LightTools
- [ ] TracePro
- [x] Python (assumed always available)

## Python Libraries Expected
- prysm, rayopt, poppy, opticspy
- numpy, scipy, matplotlib, pandas
- sympy (for symbolic derivations)

## Hardware Available (if any)
- [ ] Interferometer (make/model: TBD)
- [ ] Spectroradiometer
- [ ] Thermal chamber
- [ ] Shake table
- [ ] Cleanroom class: TBD

## Data Storage
- Prescriptions: `outputs/prescription-v{N}.csv` or `.ZMX` if Zemax
- FMEA worksheets: `outputs/fmea-worksheet.csv`
- Reports: `user-docs/`
- Session logs: `work-log/YYYY-MM-DD.md`

## External Tools / MCP
- Filesystem MCP (read/write workspace files)
- GitHub MCP (if versioning needed)
- Python execution MCP (run sanity scripts)
