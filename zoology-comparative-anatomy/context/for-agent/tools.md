# Tools — Recommended Software for Comparative Anatomy

*Reference for the agent. When recommending an analytical step, prefer these established tools over reinventing.*

## Imaging & Measurement

- **Fiji / ImageJ** — open-source image analysis. Calibrate scale via known scale bar, then measure linear distances, areas, angles. Plugins: BioFormats (microscopy), ROI Manager (batch annotation), TrakEM2 (serial sections).
- **3D Slicer** — open-source DICOM-capable 3D viewer; segments CT and MRI volumes.
- **Avizo / Amira** — commercial 3D segmentation/visualization, common for high-end museum CT workflows.
- **Dragonfly** — free for academic use, capable 3D visualization and segmentation.

## Landmark Digitization

- **TPS series** (Rohlf): tpsUtil → tpsDig → tpsRelw / tpsSplin / tpsSuper. Standard for 2D landmark workflows. Free.
- **Stratovan Checkpoint** — 3D landmark digitization.
- **MorphoDig** — open-source 3D landmark and curve placement.
- **IDAV Landmark Editor** — 3D landmark digitization (older, still functional).

## Geometric Morphometrics

- **R: geomorph** (Adams et al.) — Procrustes superimposition, PCA, regression, allometry, modularity, integration. Active development.
- **R: Morpho** — geometric morphometrics with semilandmarks support.
- **MorphoJ** — GUI alternative for Procrustes + multivariate analysis.
- **PAST** — multivariate stats with morphometrics support.

## Phylogenetic Tooling

- **Mesquite** — character matrix authoring, NEXUS file management, character evolution visualization. Front-end for trait-matrix work.
- **FigTree** — tree visualization.
- **R: ape** — comparative methods foundation. Tree handling, plotting, ancestral state reconstruction.
- **R: phytools** — phylogenetic comparative methods (PCM): PIC, PGLS, evolutionary rate estimation.
- **R: caper** — PGLS specifically.
- **IQ-TREE / RAxML / MrBayes / BEAST2** — tree inference. Out of scope for comparative-anatomy workflow but commonly chained.

## Specimen / Collection Management

- **OpenSpecimen** — biospecimen management.
- **Specify** — natural history collection management.
- **Symbiota** — biodiversity data network.
- **iDigBio API** — programmatic access to US biodiversity collection metadata.
- **VertNet** — vertebrate-specific specimen records.
- **GBIF API** — global biodiversity records.

## 3D Repositories

- **MorphoSource** — 3D media (CT, surface scans). Free upload, DOI assignment, embargo support.
- **Dryad** — generalist data repository, accepts trait matrices and supplementary tables.
- **MorphoBank** — character-matrix-focused; widely used for phylogenetic supplementary data.

## Reference Texts (citations to keep handy)

| Topic | Reference |
|---|---|
| Vertebrate comparative (intro) | Kardong 2018 |
| Functional vertebrate anatomy | Liem et al. 2001 |
| Classic descriptive | Romer & Parsons 1986 |
| Homology theory | Hall 1994; Wagner 2014 |
| Landmarks | Bookstein 1991; Zelditch et al. 2012 |
| Vertebrate nomenclature | TA2 (FIPAT 2019); NAV 6th ed.; NAA 2nd ed. |
| Invertebrate | Brusca & Brusca 2003; Ruppert et al. 2004; phylum-specific monographs |

## CLI / API Notes

- **iDigBio API:** `https://search.idigbio.org/v2/search/records/` accepts JSON queries for specimen records.
- **GBIF API:** `https://api.gbif.org/v1/occurrence/search` for occurrence data.
- **MorphoSource API:** `https://www.morphosource.org/api/v1/` for 3D media metadata.

If MCP servers exist for any of these, register in `.mcp.json` after `/onboard`.
