"""
Laser Maximum Permissible Exposure (MPE) calculator — rough first-cut.

Follows IEC 60825-1:2014 Table 3/4 simplifications. NOT a replacement for a
qualified laser safety officer. Use only for initial design classification.
"""
from __future__ import annotations

import math


def mpe_eye_visible(wavelength_nm: float, exposure_time_s: float) -> float:
    """MPE in J/m² for eye, visible (400–700 nm)."""
    if not (400 <= wavelength_nm <= 700):
        raise ValueError("Only visible range supported in this stub.")
    if exposure_time_s <= 0.25:
        return 5e-3 * exposure_time_s ** 0.75 * 1e4  # convert J/cm² to J/m²
    elif exposure_time_s <= 10:
        return 1.8e-3 * exposure_time_s ** 0.75 * 1e4
    else:
        return 1e-2  # W/m² × time approx


def nohd(power_w: float, beam_dia_m: float, divergence_rad: float, mpe_wm2: float) -> float:
    """Nominal Ocular Hazard Distance (m)."""
    return (1 / divergence_rad) * math.sqrt(
        4 * power_w / (math.pi * mpe_wm2)
    ) - beam_dia_m / divergence_rad


def classify_cw(power_w: float, wavelength_nm: float) -> str:
    """Return IEC 60825 class for a CW visible laser."""
    if 400 <= wavelength_nm <= 700:
        if power_w < 0.39e-3:
            return "Class 1"
        if power_w < 1e-3:
            return "Class 2"
        if power_w < 5e-3:
            return "Class 3R"
        if power_w < 0.5:
            return "Class 3B"
        return "Class 4"
    return "out-of-scope: use full IEC 60825-1"


if __name__ == "__main__":
    # Example: 5 mW green pointer, 1 mm beam, 1 mrad divergence
    print("Class:", classify_cw(5e-3, 532))
    mpe = mpe_eye_visible(532, 0.25)
    print(f"MPE (0.25 s aversion): {mpe:.3f} W/m²")
    d = nohd(5e-3, 1e-3, 1e-3, mpe)
    print(f"NOHD: {d:.1f} m")
