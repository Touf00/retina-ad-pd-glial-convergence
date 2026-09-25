### Publication source-data preservation — cross-cohort matrix + independent bootstrap COMPLETE
- Run 36191824900 completed successfully and committed exact durable source data at commit daf7db2d885066122fc8976452abeb6d91ba951b.
- Preserved publication/source_data/glial_cross_cohort_matrix.csv (16 comparisons) and glial_cross_cohort_consistency_summary.csv.
- Preserved all 16 matched gene-level compressed effect tables underlying the 2 x 2 matrix.
- Preserved independent_pair_donor_bootstrap_summary.csv, independent_AD_PD_pair_summary.csv, all four B=500 bootstrap draw tables, all four merged independent-pair gene-effect tables, and summary.json.
- Added publication/source_data/SHA256SUMS.txt and README.md with workflow/artifact provenance.
- Automated verification passed exactly: 16 matrix rows, 4 bootstrap draw files with 500 draws each, and 16 cross-cohort gene-effect files. Frozen matrix and bootstrap-summary values matched PUBLICATION_RESULT_FREEZE_v1.md; no publication-value mismatch was found.
- Important provenance distinction: the separately executed independent-pair pair-summary has its own permutation realization; its permutation P values are retained but must not overwrite the corresponding 2 x 2 matrix-run P values.
- These publication source data no longer depend on the workflow artifacts expiring on 2026-10-02.
- Main and Zenodo remain unchanged.
- Stop point: this source-data preservation step is complete. Do not start workbook/figure/notebook generation until the next explicit step.

### GSE157827 clustering sensitivity propagated to AD replication — COMPLETE
- Run 36186876350 completed successfully.
- Both default-neighbor and exact-neighbor GSE157827 variants retained positive GSE174367 discovery-to-replication genome-wide concordance in all four glial classes; all LFC and Wald permutation tests were P=0.00009999.
- Default / exact LFC Spearman: Astro 0.1822 / 0.1818; Micro 0.0450 / 0.0433; OPC 0.0534 / 0.0332; Oligo 0.1534 / 0.1635.
- Default / exact all-gene direction concordance: Astro 57.27% / 57.14%; Micro 51.55% / 51.09%; OPC 51.65% / 51.77%; Oligo 55.90% / 56.59%.
- Discovery-FDR gene-level replication was also essentially unchanged: Astro 0/1 measurable hit replicated in both; Micro 1/3 in both; OPC had no measurable discovery-FDR hits in either; Oligo 2 replicated genes in both, with 19/29 versus 20/30 same-direction measurable discovery hits.
- Conclusion for reproducibility audit: the GSE157827 graph partition is not bitwise portable across hosted numerical environments and OPC assignment is particularly sensitive, but the manuscript-level AD discovery-to-replication conclusion is robust to the tested default-versus-exact clustering perturbation. Do not claim exact archival partition reproduction.
- Clustering forensic work is CLOSED unless a later consistency check reveals a downstream dependency. Next step is to freeze the expanded scientific result set and decide the exact publication-facing analyses/tables/figures before regenerating deliverables.

### GSE157827 donor-level effect robustness — COMPLETE
- Run 36184453396 completed successfully after the sensitivity workflow was debugged through the archival-count assertions without changing the biological mapping rules.
- Default-vs-exact donor-level effect concordance:
  - Astro: 17,247 overlapping genes; LFC Spearman 0.9649; Wald Spearman 0.9722; sign agreement 93.74%; top-5%-effect sign agreement 99.54%; primary FDR 0 vs 0; PMD FDR 0 vs 0.
  - Micro: 16,622 genes; LFC Spearman 0.9376; Wald 0.9511; sign agreement 91.91%; top-5% 99.16%; primary FDR 0 vs 0; PMD FDR 0 vs 0.
  - OPC: 15,648 genes; LFC Spearman 0.5380; Wald 0.5671; sign agreement 70.46%; top-5% 85.82%; primary FDR 0 vs 0; PMD FDR 0 vs 0. Donor eligibility changed 21 vs 19.
  - Oligo: 16,055 genes; LFC Spearman 0.8963; Wald 0.9153; sign agreement 87.91%; top-5% 99.13%; primary FDR 4 vs 4; PMD FDR 2 vs 2.
- Cell partitioning can vary substantially across hosted runs, especially OPC/oligodendrocyte lineage assignment, yet the primary FDR-level conclusion is unchanged in all four classes. Astro/Micro/Oligo effect vectors are highly stable; OPC effect magnitudes are only moderately stable and must be carried into the AD discovery-to-replication sensitivity analysis.
- Next required test: compare the frozen GSE174367 AD discovery effects against BOTH GSE157827 clustering variants using the original Step-30 metrics. This determines whether the manuscript's AD replication/concordance claim survives the OPC partition instability.

### GSE157827 deterministic annotation robustness — TARGET COMPOSITION MOSTLY STABLE EXCEPT OPC
- Run 36180304636 completed successfully through disease-blind provisional annotation and application of the original rule-based final target mapping, with archival cluster-ID/count assertions removed only for sensitivity testing.
- This hosted run produced 29 clusters and 5 low-margin clusters.
- Final rule-based nuclei: Astro 17,829; Micro 8,173; OPC 2,009; Oligo 41,092; Other 100,403.
- Versus archival expected counts: Astro -4.60%; Micro +3.34%; OPC +54.18%; Oligo -0.03%; Other -0.10%.
- Versus the earlier fresh default 31-cluster mapping: Astro -5.00%; Micro +2.32%; OPC +331.12%; Oligo -1.62%; Other -0.11%.
- Oligodendrocytes and the non-target pool are highly stable, astrocytes/microglia shift modestly, but OPC assignment is materially unstable because a small lineage population is sensitive to graph partitioning.
- Donor-level expression robustness is therefore REQUIRED, especially for OPC. The next test will run two GSE157827 variants on the same hosted runner (default approximate neighbors versus exact brute-force neighbors), apply the same disease-blind mapping rules, regenerate Step27 donor pseudobulk and Step28 AD-vs-Control effects, and compare effect vectors/FDR summaries directly.

### GSE157827 within-run exact-neighbor repeatability — DETERMINISTIC WITHIN ONE HOST
- Run 36178603337 completed successfully on one AMD EPYC 9V74 hosted runner using Python 3.13.15, numpy 2.1.3, scikit-learn 1.6.1, single-thread OpenBLAS/OpenMP, and the frozen Harmony20 input.
- Two sequential exact brute-force neighbor + Leiden calculations in the same process were bit-identical: distance SHA-256 138d8724a28e15272d95573901f8a2863919c94c6090974ed1529a1859100856; connectivity SHA-256 03c6ea6250c6b97ea2e549e0fcd665a77eb778e24bf371d9ee88c657b19e9cfe; partition SHA-256 4862f1cafd6b550623b0c2980ede105374581b1c485e95dbd9e38c7ea71f46b6; 28 clusters in both repeats.
- This establishes that the tested exact-neighbor + Leiden calculation is deterministic within a fixed host/process. The remaining cross-run differences are host/numerical-state dependent.
- The 28-cluster count is numerically equal to the archival expected count, but this is not evidence that the cell partition matches the archival partition because archival cell assignments are unavailable.
- Stop trying to recover the archival count by environment tweaking. Next priority is biological robustness: propagate a deterministic 28-cluster exact-neighbor partition through the frozen annotation logic and compare its cell-type calls / downstream donor-level effects against the fresh default-clustering result. The scientific question is whether conclusions are robust to the clustering instability, not whether a particular integer cluster count can be forced.

### GSE157827 exact brute-force neighbors — CROSS-RUN DRIFT PERSISTS
- Run 36177674976 completed successfully. Both jobs used the exact same frozen Harmony20 file, scikit-learn KNeighborsTransformer with algorithm=brute, Euclidean distance, n_jobs=1, and single-thread environment limits.
- Replicate 1: distance SHA-256 1345c06daf735c66cf82af5a222dcb9fde22241c5be2f9dd5c3661dd53ca06a5; connectivity SHA-256 5c57d8a729630e7612a368718e71e9febbd896fed174d12d42c701fe1501e210; 30 clusters.
- Replicate 2: distance SHA-256 138d8724a28e15272d95573901f8a2863919c94c6090974ed1529a1859100856; connectivity SHA-256 03c6ea6250c6b97ea2e549e0fcd665a77eb778e24bf371d9ee88c657b19e9cfe; 28 clusters.
- Matching the archival cluster count in replicate 2 does NOT establish reproduction of the archival partition because the original 28-cluster cell assignments are not preserved for direct comparison.
- Approximate-neighbor randomness is therefore not the whole explanation: even exact brute-force kNN differs across independent hosted runners.
- Next controlled test: execute the exact brute-force neighbor+Leiden calculation twice sequentially inside one runner/process and record CPU/runtime information. If the two within-run hashes match, the remaining difference is cross-run host/numerical implementation state rather than algorithmic randomness within one process.

### GSE157827 explicit single-job PyNNDescent — STILL NONDETERMINISTIC
- Run 36177321311 completed successfully using the exact same frozen Harmony20 file in two independent jobs, PyNNDescent random_state=20260914, n_jobs=1, and all common numerical/Numba thread pools capped at one.
- Replicate 1: distance SHA-256 c46604dbccd3f31885c66626ae59e8c52ba2fbd30ca95fb37af5f7b3196d57ce; connectivity SHA-256 9e239ade64e8ff49fadb423b5eb3d63b34ce324571692ed2b2479238928966e0; 31 clusters.
- Replicate 2: distance SHA-256 7134e307d0bda5ebba8b723c618eb37a26e4b7da6f148292b0ff7def50ec8938; connectivity SHA-256 9cd84f68538fca07ee25bbdf32cdb962c7b09c498be2e2625bfe0a829ac84976; 27 clusters.
- Therefore explicit PyNNDescent seeding plus n_jobs=1 is insufficient to make the neighbor graph cross-run deterministic on hosted runners.
- Next controlled test: replace approximate PyNNDescent with scikit-learn KNeighborsTransformer using exact brute-force Euclidean search and n_jobs=1, still on the identical frozen Harmony matrix. Run two independent jobs and compare graph hashes and Leiden partitions.

### GSE157827 fixed-Harmony downstream repeatability — kNN SEARCH IS THE FIRST DIVERGENCE
- Run 36175179052 completed successfully with two independent jobs using the exact same frozen Harmony20 file (SHA-256 5fa4adc58581ab864546f274507e2010641d672dde3dda0e8d51e6e8b2553d95).
- Replicate 1: distance-graph SHA-256 b9582c75ac35b2362a3cf711630e7a2c4b28f8626a5f3ab4d2b6aa3d8a169ee4; connectivity SHA-256 dba620f90fcf87a5037f39feb17e0c5d21bf900d92cda47ced64bb5fd311826d; 31 clusters.
- Replicate 2: distance-graph SHA-256 087cf3a0bcb93aa2157d3fcd318419fad815eb73176785387444c74b7000cff8; connectivity SHA-256 897ce290316b060a25c703397de29f78d40632fea9e4b4b8c6336979d51e4257; 30 clusters.
- Because the distance matrices already differ before Leiden, the first demonstrated source of cross-run nondeterminism is approximate k-nearest-neighbor graph construction, not PCA or Harmony.
- All common numerical thread variables including NUMBA_NUM_THREADS were capped at one, but the default large-dataset Scanpy path still delegates to PyNNDescent without an explicitly supplied n_jobs=1 transformer.
- Next controlled test: use the same frozen Harmony matrix and an explicit PyNNDescentTransformer with random_state=20260914 and n_jobs=1 in two independent jobs. If graph hashes match, the missing explicit PyNNDescent job cap explains the downstream drift. If they do not, treat PyNNDescent cross-process behavior as the unresolved source and freeze the neighbor graph or use a deterministic exact-neighbor backend for the reproducibility release.

# RETINA-ND PROJECT CHECKPOINT

Updated: 2026-09-25
Branch: `reproducibility-audit`

## Reproducibility status

Run 36175179052 used the exact same frozen GSE157827 Harmony20 matrix in two independent jobs (SHA-256 `5fa4adc58581ab864546f274507e2010641d672dde3dda0e8d51e6e8b2553d95`) with common numerical and Numba thread pools capped at one.

Replicate 1 produced connectivities SHA-256 `dba620f90fcf87a5037f39feb17e0c5d21bf900d92cda47ced64bb5fd311826d`, distances SHA-256 `b9582c75ac35b2362a3cf711630e7a2c4b28f8626a5f3ab4d2b6aa3d8a169ee4`, 31 clusters, and partition SHA-256 `972057bd3981ed2bde373121ea69fb34565a66c15e5b522caa4cf363eec15763`.

Replicate 2 produced connectivities SHA-256 `897ce290316b060a25c703397de29f78d40632fea9e4b4b8c6336979d51e4257`, distances SHA-256 `087cf3a0bcb93aa2157d3fcd318419fad815eb73176785387444c74b7000cff8`, 30 clusters, and partition SHA-256 `fb0f88be88b0370848da801e2593228fb9a6fbdd80630d231bfd0b89faf370b6`.

Conclusion: the neighbor graph differs before Leiden despite byte-identical Harmony input. Approximate neighbor construction is cross-run nondeterministic on the hosted runner under these controls. This supersedes the earlier provisional statement that downstream neighbors/Leiden had been ruled out.

Previous evidence:
- Run 36173634884: byte-identical HVGs and Harmony20 followed by 29 versus 31 clusters.
- Run 36174283860: full-pipeline replicas with Numba capped still produced 29 versus 31; those replicas also developed upstream byte differences.
- Historical clean-room target: 28 clusters.

Next controlled test: use the same frozen Harmony20 matrix and force Scanpy's exact scikit-learn neighbor transformer in two independent jobs. Compare graph hashes first, then Leiden partition hashes. This separates approximate-neighbor nondeterminism from Leiden nondeterminism.

## Journal-extension results already established

- PXD040225 human AD retina proteomics: 423 upregulated and 422 downregulated proteins; 844 unique gene symbols. ITGAM is independently upregulated (AD mean 79.11, NC mean 62.72, FC 1.26, nominal p ~0.03222). Treat as independent support, not biomarker proof.
- PXD066087 mouse PD retina: public release lacks a processed quantitative protein table. Exclude from quantitative validation; use only as qualitative cross-species context. See `audits/PXD066087_AVAILABILITY_AUDIT.md`.
- Glial 2x2 matrix across GSE174367/GSE222494 AD and GSE243639/GSE329625 PD: original pairing reproduces, but convergence is cohort/region/context-dependent rather than universal.
- Vascular extension: AD endothelial/pericyte effects replicate modestly; PD endothelial replication fails between PD243 and PD157; cross-disease vascular effects are exploratory because donor-bootstrap intervals cross zero.
- GSE157827 published Endo vector contains 5,346 non-mitochondrial unique genes and supports context-dependent sensitivity evidence. It is not donor-level pseudobulk replication.

## Remaining work

1. Complete exact-neighbor fixed-Harmony test and localize residual Leiden behavior.
2. Determine whether the archival 28-cluster reconstruction is recoverable; otherwise document the reproducibility limitation precisely.
3. Complete GSE157827 donor-level endothelial disease-effect analysis only if diagnosis-blind mapping remains defensible; otherwise defer it explicitly.
4. Freeze robustness language around cohort/context heterogeneity.
5. After analysis freeze, update manuscript, figures/supplement, Code Availability, and reproducibility release if justified.

## Scientific guardrails

Preserve negative/null findings. Do not claim universal AD/PD convergence. Do not upgrade candidate genes to biomarkers. Do not force unsupported pericyte subgroups. Keep the main branch and original source data unchanged during the audit.
