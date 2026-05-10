# Soil Microbiome Management Workspace

A Claude Code workspace for longitudinal management of agricultural soil microbiomes — built around **time-series trend analysis** of community composition, functional-gene abundance, and soil-health proxies across cropping cycles, amendments, and disturbances.

Provisioned via the [`workspace-foundational`](https://github.com/danielrosehill/Claude-Workspace-Foundational-Plugin) plugin model (`generic-workspace` variant). Drop sample tables (16S/ITS ASV counts, shotgun taxonomies, qPCR results, soil-health sensors) into `context/`; save reusable prompts in `prompts/`; write trend reports, change-point summaries, and recovery indices to `outputs/`.

## Why time-series trend analysis here

Microbiomes are noisy, seasonal, and compositional — a one-shot test reveals nothing about whether the soil is improving, holding, or degrading. Pairing repeated sampling with classical (Mann-Kendall, Sen's slope, STL decomposition, SARIMA) and ecology-aware (ALDEx2 / MaAsLin2 with random effects, change-point detection on Aitchison distances, generalized Lotka-Volterra) trend tools lets the agent separate management signal from rotation noise and flag deviations early.

See `context/concepts.md` for the working domain reference and `context/references.md` for sequencing pipelines, public datasets, and the canonical literature.
