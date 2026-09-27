# Archived extension-analysis workflows

These files preserve the exact GitHub Actions workflow code used for later RETINA-ND robustness and extension analyses that were originally executed on the historical `chatgpt-repro-audit` branch.

They are stored outside `.github/workflows/` so they remain provenance records and are not triggered automatically on the current `reproducibility-audit` branch.

| Analysis | Archived workflow | Historical source commit | Workflow run |
|---|---|---|---|
| Fully external AD-PD donor bootstrap | chatgpt-external-pair-robustness.yml | d011d11e95932c9d73b1d4fafeebeb53d4b6f0f7 | 36135599890 |
| 2 x 2 AD-PD glial cross-cohort matrix | chatgpt-glial-cross-cohort-matrix.yml | c65a7f873364e814d6da0b130e87c3c3e0f54d19 | 36142383845 |
| Exploratory vascular analysis | chatgpt-vascular-convergence.yml | 9fc7ec21dd0ded653bcf08595d44512f501230cd | 36142316148 |
| GSE157827 author-defined endothelial sensitivity | chatgpt-gse157827-author-endo-sensitivity.yml | 7ca0a06a2dcc08e3e4356f6f3d2bce686f6459b3 | 36147039005 |

Frozen outputs from these analyses are stored under `publication/source_data/` and mapped in `publication/source_data/analysis_provenance.csv`.
