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
