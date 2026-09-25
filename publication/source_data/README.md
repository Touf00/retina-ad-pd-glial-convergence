# Publication source data

Status: final source-data completeness audit passed on branch `reproducibility-audit`.

All 20 planned publication-workbook sheets now map to durable repository source data. The authoritative mapping is `SOURCE_DATA_COMPLETENESS_AUDIT_v1.csv`; unified run/artifact provenance is in `analysis_provenance.csv`; cohort roles are in `dataset_manifest.csv`.

Durable blocks include:
- original PD replication and frozen AD primary/secondary replication summaries;
- GSE157827 default-vs-exact clustering/effect sensitivity;
- original AD-PD pair, full 2 x 2 cross-cohort matrix, and independent-pair donor bootstrap;
- Reactome pathway and multimodal candidate source data;
- healthy-retina expression gate, PXD073336 AD-retina proteomics, and PD aqueous-humor support;
- exploratory vascular analyses and GSE157827 author-Endo sensitivity;
- independent PXD040225 human AD-retina sensitivity.

Known limitations remain explicit: the original executed GSE157827 28-cluster cell partition is unavailable; the regenerated candidate-pathway map contains 69,296 rows versus the archival assertion of 69,297 although downstream Figure-5 checks passed; PXD066087 is excluded from quantitative human validation; vascular analyses remain exploratory.

`SHA256SUMS.txt` covers the durable source-data tree. Main branch and Zenodo remain unchanged.
