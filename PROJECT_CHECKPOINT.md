# RETINA-ND PROJECT CHECKPOINT

Updated: 2026-09-25
Branch: `chatgpt-repro-audit`
Checkpoint commit inspected: `4a98ef9`

## Verified workflow state at handoff

- GitHub Actions checked directly on 2026-09-25 after the checkpoint commit.
- Active/queued workflows: **none**. The two jobs previously described as live have completed successfully.
- Latest successful milestone runs:
  - `36142383845` — full glial cross-cohort matrix; completed successfully.
  - `36142316148` — corrected vascular convergence extension; completed successfully.
  - `36136473933` — PXD040225 DEP extraction; completed successfully.
  - `36087596027` — external-cohort pseudobulk; completed successfully.
- Relevant unresolved failed runs:
  - `36131301979` — clean-room audit failed during notebook execution at the GSE157827 31-vs-28 clustering assertion; audit artifact was still uploaded.
  - `36135706446` — GSE157827 endothelial feasibility audit failed before producing an artifact. PNAS supplement URLs returned HTTP 403 or HTML, and the Europe PMC supplementary bundle request timed out. This is a source-retrieval failure, not a biological exclusion.

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

2. Complete GSE157827 vascular decision.
   - First make supplement retrieval deterministic (vendor/Europe PMC URLs currently fail or time out in Actions), or recover the same author QC table from a verified alternate public source.
   - Establish whether author Endo cells are sufficiently represented for donor-level AD endothelial analysis.
   - Pericytes are not clearly author-annotated in the available GSE157827 QC.
   - If robust extraction is not possible, explicitly exclude this cohort from the vascular extension.

3. PXD066087 mouse PD retina.
   - PRIDE currently exposes raw TMT MS files, no obvious processed protein-level table.
   - Recover processed differential-protein results from article/supplement if available.
   - Otherwise formally exclude it from the journal extension rather than doing an unmatched de novo raw-proteomics pipeline.
   - It is cross-species support only, never human PD-retina validation.

4. Robustness/final synthesis.
   - Use completed 2x2 glial matrix + existing donor bootstrap.
   - Decide whether more pairwise bootstraps are needed for the 16 comparisons.
   - Freeze language around heterogeneity/context dependence.
   - Do not force a universal convergence claim.

5. Final journal-version inclusion decisions.
   Likely include:
   - PXD040225 independent AD-retina support.
   - 2x2 glial cross-cohort sensitivity matrix.
   - Vascular extension as exploratory/sensitivity unless stronger replication emerges.
   - Exact clean-room reproducibility status.

6. Only after analysis freeze:
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

