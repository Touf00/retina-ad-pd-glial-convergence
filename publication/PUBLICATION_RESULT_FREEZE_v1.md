# Publication result freeze v1

Branch: reproducibility-audit  
Status: scientific extension results frozen for publication-output reconstruction; main and Zenodo unchanged.

## 1. Original core result retained
The original AD174 x PD243 discovery comparison remains a valid cohort-pair result: positive genome-wide glial concordance in Astro, Micro, OPC and Oligo. It must not be described as universal AD-PD convergence.

## 2. Cross-cohort 2 x 2 glial matrix — include
Run 36142383845.

| AD cohort | PD cohort | Cell type | Matched genes | LFC Spearman | Same-sign fraction | Permutation P |
|---|---|---:|---:|---:|---:|---:|
| GSE174367 | GSE243639 | Astro | 15423 | 0.185301 | 0.577903 | 0.0001 |
| GSE174367 | GSE243639 | Micro | 14975 | 0.054761 | 0.527212 | 0.0001 |
| GSE174367 | GSE243639 | OPC | 14842 | 0.151654 | 0.573305 | 0.0001 |
| GSE174367 | GSE243639 | Oligo | 14241 | 0.253090 | 0.606910 | 0.0001 |
| GSE174367 | GSE329625 | Astro | 12766 | -0.028955 | 0.488485 | 0.0016 |
| GSE174367 | GSE329625 | Micro | 12849 | 0.003342 | 0.496537 | 0.709629 |
| GSE174367 | GSE329625 | OPC | 12342 | 0.075894 | 0.529493 | 0.0001 |
| GSE174367 | GSE329625 | Oligo | 12158 | 0.045172 | 0.521385 | 0.0001 |
| GSE222494 | GSE243639 | Astro | 9803 | 0.315616 | 0.589921 | 0.0001 |
| GSE222494 | GSE243639 | Micro | 5131 | 0.120372 | 0.552719 | 0.0001 |
| GSE222494 | GSE243639 | OPC | 7475 | 0.217484 | 0.568963 | 0.0001 |
| GSE222494 | GSE243639 | Oligo | 11208 | 0.390892 | 0.639722 | 0.0001 |
| GSE222494 | GSE329625 | Astro | 8999 | -0.087160 | 0.481053 | 0.0001 |
| GSE222494 | GSE329625 | Micro | 4931 | 0.040469 | 0.517948 | 0.0047 |
| GSE222494 | GSE329625 | OPC | 6969 | -0.004366 | 0.508538 | 0.722828 |
| GSE222494 | GSE329625 | Oligo | 10045 | -0.040129 | 0.488104 | 0.0001 |

Publication interpretation: cross-disease alignment is cohort/region/context dependent. Do not infer universality from permutation significance when effect magnitude is near zero.

## 3. Independent-pair donor bootstrap — include as robustness
External GSE222494 x GSE329625 donor bootstrap:
- Astro median rho -0.0514, 95% CI [-0.1476, 0.0592].
- Micro median rho 0.0168, 95% CI [-0.0977, 0.1304].
- OPC median rho -0.0037, 95% CI [-0.0608, 0.0524].
- Oligo median rho -0.0285, 95% CI [-0.1457, 0.0875].
Interpretation: the independent pair does not support a universal cross-disease genome-wide effect.

## 4. Vascular analysis — include only as exploratory/sensitivity
AD vascular within-disease replication:
- Endothelial GSE174367 x GSE222494: rho 0.1118, same-sign 0.5140, permutation P 0.007998.
- Pericyte GSE174367 x GSE222494: rho 0.1168, same-sign 0.5428, permutation P 0.001800.

PD endothelial replication:
- GSE243639 x GSE157783: rho -0.0020, same-sign 0.4978, permutation P 0.8834; no replication.

Cross-disease endothelial/pericyte comparisons are mostly positive, but all tested endothelial donor-bootstrap 95% intervals cross zero. GSE243639 has no robust pericyte subgroup. GSE174367 vascular populations are sparse. These results cannot support a strong vascular-convergence claim.

GSE157827 author Endo sensitivity is not donor-pseudobulk equivalent:
- vs AD174 rho 0.0527, P 0.2138.
- vs AD222 rho 0.1663, P 0.0002.
- vs PD243 rho -0.0236, P 0.0968.
- vs PD157 rho 0.1802, P 0.0002.
Use as context-dependent sensitivity only.

## 5. Independent human AD-retina proteomics — include as limited orthogonal support
PXD040225 significant DEP tables contain 844 unique genes. Among the prespecified candidate set, ITGAM is the only overlap: accession P11215, AD mean 79.11, control mean 62.72, source fold change 1.26, P=0.03222, signed log2FC +0.333424.
Interpretation: nominal independent human AD-retina support for ITGAM; not FDR biomarker evidence.

## 6. PXD066087 — exclude from quantitative validation
Public deposition contains raw Thermo files and search/method files but no processed protein-abundance/differential-protein table suitable for the prespecified quantitative validation. It is an A53T/M83 mouse-retina TMT study. Do not describe it as human PD-retina validation. It may be cited only as qualitative cross-species context if useful.

## 7. GSE157827 reproducibility sensitivity — include in methods/supplement
The archival expected partition was 28 clusters, but the original executed cluster assignments are unavailable. Fresh hosted runs can produce different graph partitions.

Donor-level default-versus-exact clustering robustness:
- Astro: LFC rho 0.9649; Wald rho 0.9722; FDR 0 vs 0.
- Micro: LFC rho 0.9376; Wald rho 0.9511; FDR 0 vs 0.
- OPC: LFC rho 0.5380; Wald rho 0.5671; FDR 0 vs 0; donor eligibility 21 vs 19.
- Oligo: LFC rho 0.8963; Wald rho 0.9153; FDR 4 vs 4.

Propagation into GSE174367-to-GSE157827 AD replication:
- Astro LFC rho 0.1822 default / 0.1818 exact.
- Micro 0.0450 / 0.0433.
- OPC 0.0534 / 0.0332.
- Oligo 0.1534 / 0.1635.
All eight corresponding one-sided 10,000-permutation LFC tests were P=0.00009999; Wald tests were also P=0.00009999.
The manuscript-level positive AD discovery-to-replication conclusion survives the tested clustering perturbation, while OPC effect estimates are explicitly less stable.

Do not claim exact reproduction of the archival 28-cluster partition.

## 8. Frozen publication framing
The supported claim is dataset-dependent, constrained cross-disease glial transcriptional alignment with orthogonal ocular support. The data do not support universal AD-PD glial convergence, a universal vascular program, a retinal biomarker claim, or a single causal shared gene.

## 9. Next production step
Build the publication output manifest: map every retained result above and every retained original result to its required notebook/code cell, source-data table, manuscript/supplementary table, and figure/panel. Only after that mapping is checked should figures, Excel supplements and the cleaned publication notebook be regenerated.
