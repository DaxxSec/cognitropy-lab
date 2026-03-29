# Environment

## Typical Operating Setup

The user operates on a Linux workstation (Ubuntu/Debian preferred) or macOS with Linux VMs. They have hands-on experience with RTL-SDR and HackRF hardware and are comfortable with CLI tools.

**Hardware available (assumed):**
- RTL-SDR v3 or similar (RTL2832U) for 315/433 MHz capture
- HackRF One for wideband sweeps and characterization
- Appropriate antennas: 1/4 wave monopole or dipole for 315/433 MHz (~23 cm for 315, ~17 cm for 433)

**Software environment:**
- Linux (Ubuntu 22.04+ recommended) or macOS with Homebrew
- `rtl_433` — installed via package manager or built from source (github.com/merbanan/rtl_433)
- `inspectrum` — IQ file visualization
- `Universal Radio Hacker (URH)` — protocol RE platform
- `GNU Radio` with `gr-osmosdr` — custom flowgraphs
- `SigDigger` — signal characterization and analysis
- Python 3 with `numpy`, `scipy`, `matplotlib`, `bitstring`
- SDR# (Windows) or GQRX (Linux/Mac) for visual waterfall and initial characterization

## File Formats in Use

- `.cu8` / `.cs16` — RTL-SDR raw IQ files (8-bit unsigned / 16-bit signed complex)
- `.sigmf` — SigMF annotated IQ recording format (preferred for documented captures)
- `.cfile` — GNU Radio complex float32 IQ
- `.json` / `.jsonl` — rtl_433 decoded output
- `.md` — Session logs, protocol notes, and analysis reports

## Working Directory Structure

```
wireless-tpms-analyzer/
├── outputs/          # Decoded packet logs, protocol maps, reports
├── planning/         # Capture plans, frequency surveys, test notes
├── work-log/         # Session journals
├── prompts/          # Reusable analysis prompt templates
├── resources/        # Reference docs, cheatsheets
└── context/          # Agent context (this directory)
```

## Network / External Resources

The agent may reference:
- FCC ID database (fccid.io) for sensor documentation
- rtl_433 GitHub issues and device_discussions for known protocols
- OpenTireData community wiki
- Academic papers on TPMS security (Rouf et al. 2010 is foundational)
