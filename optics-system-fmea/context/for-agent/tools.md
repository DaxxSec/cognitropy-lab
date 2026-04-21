# Tools Reference

## Python Snippets the Agent Can Reach For

### Airy disk diameter
```python
def airy_diameter(wavelength_um: float, f_number: float) -> float:
    """Returns Airy disk diameter in µm."""
    return 2.44 * wavelength_um * f_number
```

### Strehl from RMS WFE
```python
import math
def strehl_marechal(rms_wfe_waves: float) -> float:
    return math.exp(-(2 * math.pi * rms_wfe_waves) ** 2)
```

### Simple RPN computation
```python
def rpn(severity: int, occurrence: int, detection: int) -> int:
    for s, name in zip([severity, occurrence, detection], ['S','O','D']):
        if not (1 <= s <= 10):
            raise ValueError(f"{name} must be 1..10")
    return severity * occurrence * detection
```

### Gaussian beam waist at distance
```python
import math
def gaussian_w(w0: float, z: float, wavelength: float) -> float:
    zR = math.pi * w0 ** 2 / wavelength
    return w0 * math.sqrt(1 + (z / zR) ** 2)
```

### Monte Carlo tolerance scaffold (prysm)
```python
# See resources/mc-tolerance-template.py — scaffold only, not auto-run.
```

## Tool Selection Guide

| Task | Preferred tool |
|---|---|
| Paraxial / first-order | `rayopt` or pen-and-paper |
| Real-ray tracing | `rayopt` or Zemax/Code V |
| MTF / PSF / Zernike | `prysm` |
| Physical-optics / diffraction | `poppy` |
| Stray light (non-sequential) | FRED / TracePro / LightTools |
| Tolerance Monte Carlo | Zemax Tolerancing + Python post, or pure `prysm` |
| Optomechanical FEA | Ansys / Nastran (out of scope for Claude, but structure inputs) |
| Laser safety (MPE) | `resources/mpe-calc.py` (hand-rolled) |
