"""
Monte Carlo tolerance scaffold for optics-system-fmea workspace.

This is a STARTING POINT, not an auto-run script. Adapt to your specific
prescription. Requires: numpy, pandas, prysm (pip install prysm).
"""
from __future__ import annotations

import numpy as np
import pandas as pd


# -------- 1) Load prescription --------
# Replace with your actual reader (CSV, Zemax, etc.)
def load_prescription(path: str) -> pd.DataFrame:
    return pd.read_csv(path)


# -------- 2) Define tolerances --------
# Values are (distribution, scale). 'n' = normal, 'u' = uniform ±scale.
DEFAULT_TOLS = {
    "radius_pct":   ("n", 0.1),    # fraction
    "thickness_mm": ("n", 0.05),
    "decenter_mm":  ("n", 0.025),
    "tilt_arcmin":  ("n", 1.0),
    "wedge_arcmin": ("n", 0.5),
    "index_dn":     ("n", 0.0005),
    "abbe_dV":      ("n", 0.3),
}


def sample_perturbations(n_trials: int, rng: np.random.Generator, tols: dict = DEFAULT_TOLS):
    out = {}
    for key, (dist, scale) in tols.items():
        if dist == "n":
            out[key] = rng.normal(0.0, scale / 3, size=n_trials)  # 3σ = tol
        elif dist == "u":
            out[key] = rng.uniform(-scale, scale, size=n_trials)
    return pd.DataFrame(out)


# -------- 3) Surrogate performance model --------
# Replace with your real MTF/WFE evaluator. This stub assumes WFE is a weighted
# RSS of perturbations, which is a reasonable first-cut surrogate.
PERF_WEIGHTS = {
    "radius_pct":   30.0,
    "thickness_mm": 10.0,
    "decenter_mm":  40.0,
    "tilt_arcmin":  8.0,
    "wedge_arcmin": 12.0,
    "index_dn":     1000.0,
    "abbe_dV":      2.0,
}


def evaluate_rms_wfe(perturbs: pd.DataFrame) -> pd.Series:
    contributions = sum(
        (perturbs[k] * w) ** 2 for k, w in PERF_WEIGHTS.items()
    )
    return np.sqrt(contributions) / 1000.0  # arbitrary units → waves


# -------- 4) Run Monte Carlo --------
def run_monte_carlo(n_trials: int = 1000, seed: int = 42) -> pd.DataFrame:
    rng = np.random.default_rng(seed)
    perturbs = sample_perturbations(n_trials, rng)
    perturbs["rms_wfe_waves"] = evaluate_rms_wfe(perturbs)
    return perturbs


# -------- 5) Report --------
def summarize(df: pd.DataFrame) -> None:
    wfe = df["rms_wfe_waves"]
    print(f"Trials:       {len(df)}")
    print(f"Mean WFE:     {wfe.mean():.4f} waves")
    print(f"p50 / p90:    {wfe.quantile(0.5):.4f} / {wfe.quantile(0.9):.4f}")
    print(f"p95 / p99:    {wfe.quantile(0.95):.4f} / {wfe.quantile(0.99):.4f}")
    print("\nSensitivities (|Pearson r| vs WFE):")
    for col in DEFAULT_TOLS:
        r = df[col].corr(wfe)
        print(f"  {col:16s} {r:+.3f}")


if __name__ == "__main__":
    df = run_monte_carlo(n_trials=2000)
    summarize(df)
    df.to_csv("outputs/tolerance-mc.csv", index=False)
