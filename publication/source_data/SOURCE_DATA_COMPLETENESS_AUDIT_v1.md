# Final source-data completeness audit v1

Status: COMPLETE for workbook/figure construction on branch reproducibility-audit.

All 20 planned supplementary-workbook sheets now map to durable repository source data. No planned sheet remains source-data-missing.

Three items carry explicit limitations rather than silent normalization:
1. AD primary replication: exact frozen publication summary is retained, but the original executed GSE157827 28-cluster cell assignment is unavailable; fresh default-vs-exact sensitivity is preserved separately.
2. Candidate-pathway map: regenerated global map has 69,296 rows versus the archival assertion of 69,297; downstream Figure-5 publication checks passed and the discrepancy remains documented.
3. GSE157827 clustering/effect sensitivity: OPC is materially less stable than the other glial classes, although the AD discovery-to-replication conclusion survives both tested variants.

PXD066087 remains excluded from quantitative human validation. Vascular results remain exploratory. PXD040225 remains limited independent AD-retina support, not biomarker validation.

Main branch and Zenodo are unchanged.
