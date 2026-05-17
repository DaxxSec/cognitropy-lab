# /check-exposure-compliance — Compare Measurements Against Exposure Limits

Compare a survey's measurements against the applicable RF / LF exposure limit and produce a defensible compliance statement. Cites the standard verbatim; never paraphrases the limit formula.

## Inputs

- Survey output (CSV / table) with: position, frequency, magnitude in field units (V/m, A/m, W/m², µT, mT), detector mode, dwell, polarization.
- Applicable standard: ICNIRP 2020, IEEE C95.1-2019, FCC OET-65, IEC 62232, IEC 60601-2-33, or local equivalent.
- Exposure classification: occupational vs. general public (the limit formula differs).
- Averaging time (the standard's mandated window — usually 6 minutes for thermal-zone RF, 30 minutes for some LF cases).
- Body-zone designation if using IEEE C95.1's restricted vs. unrestricted environment partition.

## Steps

1. **Confirm the standard edition and pull the limit table** from `context/references.md`. Record the table citation in the report; do not retype values from memory.
2. **For each row, identify the frequency-dependent limit.** ICNIRP 2020 RF (general public) example shapes: `E = 27.7 V/m`, `H = 0.0735 A/m`, `S = 2 W/m²` for 400 MHz – 2 GHz, with `f/200` scaling above; below 400 MHz scale as `1.375·√f` (V/m). IEEE C95.1 differs in transition points and uses MPE for restricted vs. unrestricted. Use the formula from the standard, computed per-frequency.
3. **Apply the averaging rule.** For thermal-zone RF, the limit applies to the 6-minute (or 30-minute, depending on standard / frequency / classification) time-averaged exposure — convert peak / RMS samples to time-averaged where the survey design supports it. Where it does not, mark the reading as "instantaneous, conservative" and explain.
4. **Compute the exposure quotient** `EQ_i = measured_i / limit_i` per row. For multi-frequency exposures, sum the quotients per ICNIRP §3 and IEEE §4 multi-tone rule: `Σ (E_i² / E_limit_i²) ≤ 1` and `Σ (S_i / S_limit_i) ≤ 1`. The aggregate must satisfy the rule, not just any single line.
5. **Classify each measurement zone** as Compliant (EQ < 0.5), Watch (0.5 ≤ EQ < 1.0), Non-Compliant (EQ ≥ 1.0). Adjust the boundary if the survey scope specifies a tighter safety factor.
6. **Compute uncertainty** per the standard's recommended method (IEC 62232 Annex D for RF base-station compliance, NIST TN 1297 for general metrology). The uncertainty interval must straddle the limit before declaring "compliant within uncertainty".
7. **Generate the compliance report.** Output a Markdown report `outputs/compliance/<date>-<site>-compliance.md` and a CSV of per-row EQs. Include: standard cited, formula used per band, averaging applied, aggregate sum-quotient verdict, uncertainty discussion, photographs / map references, sign-off line.
8. **Flag the highest-EQ rows** for re-measurement before sign-off if any EQ ≥ 0.8.

## Output

- `outputs/compliance/<date>-<site>-compliance.md` — narrative report citing the exact limit formula per frequency band.
- `outputs/compliance/<date>-<site>-eq.csv` — per-row exposure quotients with classification.
- Optional: a heat map of EQ over the site (calls `/interpolate-isofield` with EQ as the field).

## Notes

- Never round limit values down for comfort or up for conservatism — quote the standard exactly. Adjust the verdict using uncertainty, not the limit itself.
- Pulsed / peak-limited fields (e.g. radar) have a separate "peak-power" criterion in IEEE C95.1; the time-averaged check is not sufficient.
- FCC OET-65 uses MPE (Maximum Permissible Exposure) values tabulated per band — they are not the same as ICNIRP "reference levels" although they agree on order of magnitude in most bands.
- Below 100 kHz, the limits switch from thermal to nerve-stimulation criteria; ICNIRP 2010 (LF) and IEEE C95.6 (basic restriction) apply — different formulas, different averaging.
