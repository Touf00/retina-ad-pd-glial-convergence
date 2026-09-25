### GSE157827 historical-like Python 3.13 environment — 29/31 CROSS-RUN DRIFT CONFIRMED
- Run 36169236711 completed the focused STEP26A1 notebook successfully under Python 3.13.15, numpy 2.1.3, pandas 2.3.3, scipy 1.16.3, anndata 0.13.3.post0, scanpy 1.12.4, scikit-learn 1.6.1, harmonypy 2.0.0, igraph 1.0.0, and leidenalg 0.12.0.
- The workflow failed only in the result-extraction step because it looked for the STEP26A1 lock in `annotation_provisional`; the notebook writes that lock to the top-level `locks` directory.
- Artifact 10879377749 was uploaded despite the extraction failure. Direct inspection of its cluster assignments recovered 169,506 cells and 29 clusters, with labels 0 through 28.
- The workflow was patched only to read and collect the lock from its actual path; no analysis parameters were changed. Verification run 36172862812 completed successfully but produced 31 clusters with HVG LOESS span 0.5. Artifact: 10881183724, expires 2026-10-02 18:26:05 UTC.
- Therefore the historical-like Python 3.13 environment does NOT restore the archival 28-cluster result. More importantly, the same code, explicit package versions, seed, and nominal GitHub runner produced 29 and then 31 clusters across two fresh runs.
- The earlier 31-cluster and 29-cluster Python 3.12 focused workflows also installed the same complete dependency set. Package drift is therefore ruled out as the explanation for the 29-vs-31 split.
- This localizes the remaining instability to lower-level numerical/runtime state before the already-fixed Harmony-to-Leiden comparison, with parallel BLAS/OpenMP scheduling the shortest remaining falsifiable hypothesis.
- The relaunch artifact is privacy-minimized: it publishes only the aggregate result JSON and non-cell-level lock metadata, not cell-level assignments, the HVG list, or execution logs.
- Next controlled test: two independent exact reruns with all common numerical thread pools capped at one, recording only aggregate counts and SHA-256 hashes. If both match, compare their hashes with the default-thread locks; if they diverge, document an irreducible hosted-runner numerical-state limitation.

### GSE157827 HVG / normalization / PCA localization — COMPLETED
- Run 36166577734 completed successfully.
- Focused rebuild unexpectedly produced 29 clusters (not the prior 31), despite the same nominal clean-room package stack. This demonstrates that the full upstream PCA/Harmony reconstruction is not perfectly invariant across independent fresh runs.
- HVG selection was identical between current and sklearn-1.6.1 alternate environments: 1000/1000 overlap, Jaccard 1.0; LOESS span 0.5 after span 0.3 numerical failure.
- With identical raw data and identical HVGs, normalization/log1p/scale matrices were bit-identical: exact_equal=true, max_abs_diff=0.
- PCA from the identical scaled matrix was effectively identical between sklearn 1.9.1 and 1.6.1 (absolute PC correlations ~1.0); both propagated to 29 clusters.
- Therefore HVG selection and normalization are ruled out for this run, and sklearn 1.9.1 vs 1.6.1 alone is not sufficient to explain 28 vs 29/31.
- Important historical evidence recovered from original GSE157827 locks: immediately before STEP26A1, the analysis environment had Python 3.13.15, numpy 2.1.3, pandas 2.2.3, scipy 1.16.3, scikit-learn 1.6.1, anndata 0.12.6, scanpy 1.11.5, harmonypy 2.0.0, igraph 1.0.0, leidenalg 0.12.0, scikit-misc 0.5.2. STEP26A1 itself upgraded/verified scanpy 1.12.4, harmonypy 2.0.0, leidenalg 0.12.0, igraph 1.0.0, scikit-misc 0.5.2 but did not pin pandas/anndata/scikit-learn.
- Next targeted test: rerun STEP26A1 in the likely historical hybrid environment: Python 3.13.15, numpy 2.1.3, pandas 2.2.3, scipy 1.16.3, anndata 0.12.6, scanpy 1.12.4, scikit-learn 1.6.1, harmonypy 2.0.0, igraph 1.0.0, leidenalg 0.12.0, scikit-misc 0.5.2. Test whether this restores the archival 28 clusters.

### GSE157827 PCA/Harmony drift localization — COMPLETED
- Run: 36161845545; completed successfully.
- Rebuilt GSE157827 through PCA and Harmony in the current clean-room environment.
- PCA50 shape: 169,506 x 50; Harmony20 shape: 169,506 x 20.
- Current pipeline produced 31 clusters.
- Current PCA SHA256: 6b207f3855b88d5d70b5f899ab12e8b55b21a5c33ac2c2f75fdf106011684b89.
- Current Harmony20 SHA256: 5fa4adc58581ab864546f274507e2010641d672dde3dda0e8d51e6e8b2553d95.
- Recomputed Harmony from the exact same PCA50 matrix in a Colab-like environment (numpy 2.0.2, scikit-learn 1.6.1, harmonypy 2.0.0).
- Colab-like Harmony produced the same SHA256 as the current Harmony20 matrix and the same 31-cluster partition.
- Conclusion: the 31-vs-28 drift does NOT originate in Harmony or the downstream neighbors/Leiden stage. The drift must arise at or before PCA generation, most plausibly HVG selection / normalization / PCA numerical state or an earlier preprocessing difference.
- Next step: isolate PCA/HVG by comparing the exact current HVG1000 set and PCA state against the archival/original run if available, then reproduce PCA under the historical/Colab-like stack while keeping the same cells and HVGs fixed.

# RETINA-ND PROJECT CHECKPOINT

Updated: 2026-09-25
Branch: `chatgpt-repro-audit`
Checkpoint commit inspected: `4a98ef9`

## Verified workflow state at handoff

- GitHub Actions checked directly on 2026-09-25 after the checkpoint commit.
- Active/queued workflows: `36144781563` — clean-room reproducibility audit, launched from commit `15d4c28`; currently in progress. It preserves the Harmony20 embedding, cluster assignments, HVG list, clustering lock, full `pip freeze`, and numerical-runtime details even if the downstream archival assertion fails again.
- Latest successful milestone runs:
  - `36142383845` — full glial cross-cohort matrix; completed successfully.
  - `36142316148` — corrected vascular convergence extension; completed successfully.
  - `36136473933` — PXD040225 DEP extraction; completed successfully.
  - `36087596027` — external-cohort pseudobulk; completed successfully.
- Latest resolved feasibility milestone:
  - `36145217468` — GSE157827 endothelial feasibility audit completed successfully using the official PMC Open Access object; artifact `10869243247`, expires 2026-10-02 14:06:13 UTC.
- Relevant unresolved failed run:
  - `36131301979` — clean-room audit failed during notebook execution at the GSE157827 31-vs-28 clustering assertion; audit artifact was still uploaded.

## Purpose

Durable checkpoint so the RETINA-ND manuscript audit/extension can be resumed in ordinary ChatGPT if Work mode credits run out.

## Current manuscript/project

Project: AD/PD glial transcriptomic convergence with retinal/ocular support.
Public repo: `Touf00/retina-ad-pd-glial-convergence`
Original manuscript is already on bioRxiv; journal-version strengthening is in progress.

## Completed today

### Independent human AD retina proteomics — PXD040225
- Source parsed successfully.
- 423 upregulated retinal proteins.
- 422 downregulated retinal proteins.
- 844 unique gene symbols recovered.
- Source FC convention verified:
  - Table 4 = AD/NC for upregulated proteins.
  - Table 5 = NC/AD for downregulated proteins, so signed AD/NC log2FC requires sign inversion.
- Current manuscript candidate overlap:
  - ITGAM independently detected as upregulated in AD retina.
  - ITGAM AD mean 79.11, NC mean 62.72, FC 1.26, p ~0.03222.
- Latest successful run: 36136473933.
- Artifact: 10865201485; expires 2026-10-02 12:43:55 UTC.

### PXD066087 mouse PD retina availability decision
- Official PRIDE API returned 26 Thermo `.raw` files plus four small `.sld` search/method files; no processed protein-abundance or differential-protein table is public.
- The paper reports an A53T/M83 mouse-retina TMT experiment (`n=3/group`, 4,135 quantified protein groups, DEP threshold FC >=1.3 and nominal p<0.05), but its only supplementary file is Supplementary Figure 1.
- Decision: exclude PXD066087 from quantitative candidate-gene validation and convergence testing. Raw-MS reprocessing would create a new, unmatched pipeline with substantial analyst degrees of freedom.
- Permitted use is qualitative, explicitly cross-species mouse-model context only; never call it human PD-retina validation.
- Durable audit: [`audits/PXD066087_AVAILABILITY_AUDIT.md`](audits/PXD066087_AVAILABILITY_AUDIT.md).

### Extra brain cohorts
Completed donor-level pseudobulk/effect-vector analysis for:
- GSE222494: sporadic AD vs controls; Astro, Micro, OPC, Oligo, Endothelial, Pericyte.
- GSE329625: PD vs controls; Astro, Micro, OPC, Oligo.
- Run: 36087596027.
- Artifact from external-cohort analysis: 10843939879; expires 2026-10-02 03:12:00 UTC.

### Full 2x2 glial cross-cohort matrix
Completed 16 AD x PD comparisons:
- AD174 = original AD discovery GSE174367.
- AD222 = external AD GSE222494.
- PD243 = original PD discovery GSE243639.
- PD329 = external PD GSE329625.

Key results:
AD174 x PD243:
- Astro rho 0.185301
- Micro rho 0.054761
- OPC rho 0.151654
- Oligo rho 0.253090

AD174 x PD329:
- Astro rho -0.028955
- Micro rho 0.003342
- OPC rho 0.075894
- Oligo rho 0.045172

AD222 x PD243:
- Astro rho 0.315616
- Micro rho 0.120372
- OPC rho 0.217484
- Oligo rho 0.390892

AD222 x PD329:
- Astro rho -0.087160
- Micro rho 0.040469
- OPC rho -0.004366
- Oligo rho -0.040129

Consistency summaries across four pairings:
- Astro: 2/4 positive, median rho 0.078173, range -0.087160 to 0.315616.
- Micro: 4/4 positive, median rho 0.047615, range 0.003342 to 0.120372.
- OPC: 3/4 positive, median rho 0.113774, range -0.004366 to 0.217484.
- Oligo: 3/4 positive, median rho 0.149131, range -0.040129 to 0.390892.

Interpretation:
- Original AD174 x PD243 convergence is reproduced exactly by this matrix.
- Convergence is not universal across arbitrary cohort pairs.
- PD329 attenuates/reverses several effects.
- The journal version should frame convergence as cohort/region/context-dependent rather than universal.
- Successful run: 36142383845.
- Artifact: 10868790506; expires 2026-10-02 13:48:32 UTC.

### Vascular extension
Corrected GSE157783 Ensembl release 93 mapping to unambiguous gene symbols and reran.

Coverage:
- GSE174367 AD Endothelial: 580 genes, 6 AD / 5 control.
- GSE174367 AD Pericyte: 790 genes, 7 AD / 6 control.
- GSE243639 PD Endothelial: 7,965 genes, 11 PD / 11 control.
- GSE157783 PD Endothelial: 6,131 genes, 5 PD / 6 control.
- GSE157783 PD Pericyte: 6,354 genes, 5 PD / 6 control.
- GSE222494 AD Endothelial: 6,746 genes, 8 AD / 8 control.
- GSE222494 AD Pericyte: 1,469 genes, 8 AD / 8 control.

Within-disease replication:
- AD endothelial replication: rho 0.11181, permutation p ~0.0080.
- AD pericyte replication: rho 0.11679, permutation p ~0.0018.
- PD endothelial replication (PD243 vs PD157): rho -0.00197, p ~0.88; no replication.

Cross-disease endothelial:
- AD174 x PD243: rho 0.09657, perm p ~0.0226.
- AD174 x PD157: rho 0.05429, perm p ~0.200.
- AD222 x PD243: rho 0.17203, perm p ~0.0002.
- AD222 x PD157: rho 0.20067, perm p ~0.0002.

Cross-disease pericyte:
- AD174 x PD157: rho 0.07377, perm p ~0.0430.
- AD222 x PD157: rho 0.20392, perm p ~0.0002.

Endothelial donor bootstrap:
- AD174 x PD243 median rho 0.0495, 95% CI -0.125 to 0.209, fraction >0 = 0.777.
- AD174 x PD157 median rho 0.0322, 95% CI -0.180 to 0.263, fraction >0 = 0.633.
- AD222 x PD243 median rho 0.1181, 95% CI -0.0538 to 0.265, fraction >0 = 0.900.
- AD222 x PD157 median rho 0.1307, 95% CI -0.0286 to 0.265, fraction >0 = 0.953.

Interpretation:
- AD vascular effects replicate modestly across AD cohorts.
- PD endothelial effects do NOT replicate between PD243 and PD157.
- Cross-disease endothelial/pericyte correlations are mostly positive but donor-bootstrap intervals cross zero.
- Treat vascular convergence as suggestive/context-dependent, not definitive.
- Successful run: 36142316148.
- Artifact: 10867267704; expires 2026-10-02 13:44:06 UTC.
- Upstream corrected PD-vascular pseudobulk run: 36140417739.
- Upstream artifact: 10865839087; expires 2026-10-02 13:22:10 UTC.

### GSE157827 author-Endo sensitivity — COMPLETED
- Run: 36147039005; completed successfully.
- Published GSE157827 Endo AD-vs-NC effect vector contains 5,346 unique non-mitochondrial genes.
- Comparison to vascular effect vectors:
  - vs GSE174367 AD Endo: n=568, rho=0.05270, sign agreement=0.5194, permutation p=0.2138.
  - vs GSE222494 AD Endo: n=4,942, rho=0.16633, sign agreement=0.5546, permutation p=0.00020.
  - vs GSE243639 PD Endo: n=5,150, rho=-0.02356, sign agreement=0.4777, permutation p=0.0968.
  - vs GSE157783 PD Endo: n=4,585, rho=0.18017, sign agreement=0.5568, permutation p=0.00020.
- Interpretation: GSE157827 provides useful endothelial sensitivity evidence, but it is not a donor-level pseudobulk effect vector. It supports context-dependent endothelial concordance (stronger with AD222 and PD157; absent with AD174 and PD243), not universal vascular convergence.
- Keep as sensitivity/context unless a defensible donor-level GSE157827 endothelial pseudobulk is later reconstructed.

### GSE157827 endothelial feasibility
- Official author supplement recovered deterministically from PMC Open Access and verified by SHA-256 `a7cf9493b99e5cb904e8dcc764349a331fda701509ebbe5a9e1ad868b18bc344`.
- AD: 12 donors, estimated 1,729.8 author-labelled Endo nuclei total; all 12 donors >=20, 10/12 >=50; median 96, range 23-645.
- NC: 9 donors, estimated 714 Endo nuclei total; all 9 donors >=50; median 70, range 51-159.
- This establishes donor-level endothelial coverage feasibility, not an AD effect result.
- The author QC table does not separate pericytes, so this cohort cannot support an author-labelled pericyte arm without a defensible independent reannotation.
- Successful run: `36145217468`.
- Artifact: `10869243247`; expires 2026-10-02 14:06:13 UTC.

### GSE157827 published Endo effect-vector sensitivity
- Official author supplement `pnas.2008762117.sd03.xlsx` contains an `Endo` sheet with published AD-vs-NC log2FC and adjusted p-values.
- Non-mitochondrial unique-gene effect vector: 5,346 genes.
- This is the authors' published cell-level Endo effect vector, NOT donor-level pseudobulk, so it is sensitivity/context only.
- Comparisons against our donor-level vascular effect vectors:
  - vs GSE174367 AD Endothelial: n=568 genes, rho 0.05270, sign agreement 51.94%, permutation p ~0.214 (not supportive).
  - vs GSE222494 sporadic-AD Endothelial: n=4,942, rho 0.16633, sign agreement 55.46%, permutation p ~0.0002 (supportive).
  - vs GSE243639 PD Endothelial: n=5,150, rho -0.02356, sign agreement 47.77%, permutation p ~0.0968 (not supportive).
  - vs GSE157783 PD Endothelial: n=4,585, rho 0.18017, sign agreement 55.68%, permutation p ~0.0002 (supportive).
- Interpretation: GSE157827 author-reported Endo biology is heterogeneous across comparator cohorts; it supports context-dependent rather than universal vascular convergence.
- Successful run: 36147039005.
- Artifact: 10869811622; expires 2026-10-02 14:23:00 UTC.

### GSE157827 supplementary-data audit
- Official supplements sd01-sd05 were inspected.
- sd01 contains donor clinical/QC information including donor-specific Endo proportions.
- sd02 contains author cell-type marker statistics.
- sd03 contains published AD-vs-NC effect tables for Astro, Endo, Excit, Inhit, Mic, Oligo.
- sd05 contains within-cell-type state/subcluster contrasts, including Endo `Up_vs_No_change_log2fc`.
- Successful run: 36146729500.

### GSE243639 vascular identity
- Author `VC` population was audited diagnosis-blind.
- It behaves as endothelial-like rather than a clear endothelial/pericyte mixture.
- Do not force a pericyte subgroup from this dataset.

### Clean-room reproducibility audit
Not fully passed.
What did pass:
- fresh environment setup;
- exact resource retrieval and hash checks;
- reconstruction progressed far enough to regenerate major original effect files, including:
  - GSE174367_AD_DISCOVERY_ALL_EFFECTS_LONG_v1.csv.gz
  - GSE243639_PD_DISCOVERY_ALL_EFFECTS_LONG_v1.csv.gz
  - GSE157783_PD_REPLICATION_ALL_EFFECTS_LONG_v1.csv.gz

Blocking issue:
- GSE157827 disease-blind clustering gives 31 clusters in the fresh environment vs archival expected 28.
- Subsequent frozen exact-count / low-margin mapping assertions stop the clean-room notebook.
- This is an environment/version reproducibility drift, not a storage problem and not evidence that all code is broken.
- Do NOT simply remove biological assertions to manufacture a pass.
- Clean-room artifact: 10864609217; expires 2026-10-02 13:02:32 UTC.
- Most recent clean-room run: 36131301979.

### Independent-pair donor bootstrap artifact
- Successful run: 36135599890.
- Artifact: 10863442549; expires 2026-10-02 12:35:54 UTC.

## Still unresolved / next actions

1. Resolve GSE157827 31-vs-28 clustering drift.
   - Identify package/version or algorithm behavior responsible.
   - Compare archival environment snapshot against fresh environment.
   - Reproduce archival 28-cluster solution if possible.
   - Then continue full clean-room notebook to the end.

2. Complete GSE157827 endothelial disease-effect analysis or explicitly defer it.
   - Supplement retrieval and donor coverage feasibility are now resolved.
   - Endothelial coverage is adequate for a donor-level AD-vs-NC analysis, but coverage counts alone are not an effect estimate.
   - Generate a donor-level endothelial pseudobulk/effect vector under a frozen, diagnosis-blind mapping, then compare it with GSE174367 and GSE222494; if the unresolved 31-vs-28 drift prevents a defensible mapping, record that limitation and defer the effect analysis.
   - Pericytes are not author-separated and should not be forced from this cohort.

3. Robustness/final synthesis.
   - Use completed 2x2 glial matrix + existing donor bootstrap.
   - Decide whether more pairwise bootstraps are needed for the 16 comparisons.
   - Freeze language around heterogeneity/context dependence.
   - Do not force a universal convergence claim.

4. Final journal-version inclusion decisions.
   Likely include:
   - PXD040225 independent AD-retina support.
   - 2x2 glial cross-cohort sensitivity matrix.
   - Vascular extension as exploratory/sensitivity unless stronger replication emerges.
   - Exact clean-room reproducibility status.

5. Only after analysis freeze:
   - update manuscript;
   - update figures/supplement;
   - update Code Availability;
   - create a new reproducibility release / Zenodo version if justified.

## Important scientific caveats

- Original glial convergence remains valid for the original discovery pairing.
- New external analyses show that convergence is not universal across every cohort combination.
- PD329 is the main source of attenuation/reversal in the 2x2 matrix.
- Vascular cross-disease signal is positive in several pairings but PD endothelial within-disease replication is absent and donor-bootstrap CIs cross zero.
- Do not upgrade candidate genes to biomarkers.
- PXD040225 ITGAM support is nominal p<0.05 in an independent AD retinal proteomic dataset, not FDR-validated biomarker evidence by itself.

## Resume instruction for ordinary ChatGPT

Copy/paste this if Work mode stops or credits run out:

> Continue the RETINA-ND project from the durable checkpoint file `PROJECT_CHECKPOINT.md` on GitHub branch `chatgpt-repro-audit` in repository `Touf00/retina-ad-pd-glial-convergence`. Do not restart from scratch. First read the checkpoint, inspect the latest workflow runs/artifacts, then continue the unresolved actions in order. Preserve negative/null findings. Do not rewrite the manuscript until the analysis freeze is complete.

## Rule for future Work sessions

After every major milestone, update this file with:
- run ID;
- artifact ID and expiry if relevant;
- exact result;
- exact failure if any;
- next action.


