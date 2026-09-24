# Glial transcriptomic convergence in Alzheimer’s and Parkinson’s disease

Code accompanying the manuscript **“Glial transcriptomic convergence in Alzheimer’s and Parkinson’s disease with independent retinal and aqueous-humor evidence.”**

**Author:** Mohamed Tawfik, PhD  
**ORCID:** https://orcid.org/0000-0002-5028-7463  
**Software release:** v1.0.0

## Overview

This repository contains the submission-facing analysis code and reproducibility helpers for a cross-disease study of Alzheimer’s disease (AD) and Parkinson’s disease (PD). The analysis uses donor-level pseudobulk models in four harmonized human glial classes—astrocytes, microglia, oligodendrocyte precursor cells (OPCs), and oligodendrocytes—followed by within-disease replication, AD–PD effect-vector convergence, Reactome pathway analysis, healthy-retina expression assessment, AD retinal proteomics, PD aqueous-humor proteomics, and rule-based multimodal candidate prioritization.

The ocular analyses are independent supportive evidence layers for candidate prioritization. They are **not** presented as clinical biomarker validation.

## Repository contents

- `RETINA_ND_bioRxiv_release.ipynb` — primary public analysis notebook.
- `RETINA_ND_bioRxiv_release_FRESH_TEST.ipynb` — optional clean-run helper that builds into a new `RETINA_ND_RELEASE_TEST` folder and guards against reuse of prior outputs.
- `RETINA_ND_pre_submission_test.ipynb` — quick artifact check against a completed project folder; it does not rerun differential expression.
- `requirements.txt` — recorded package versions plus packages whose exact historical versions were not captured.
- `release_manifest.json` — provenance and static release-audit metadata.
- `CITATION.cff` — software citation metadata.
- `LICENSE` — MIT license for the original code in this repository.

The historical recovery/master notebook is intentionally not included. It contained recovery cells, duplicated figure versions, embedded outputs, repeated Drive mounting, and older project-root assumptions.

## Public datasets used

Brain single-nucleus RNA-sequencing datasets:

- PD discovery: `GSE243639`
- PD replication: `GSE157783`
- AD discovery: `GSE174367`
- AD primary same-region replication: `GSE157827`
- AD secondary cross-region replication: `GSE138852`

Additional datasets:

- Healthy human retinal single-cell reference: `GSE148077`
- AD retinal proteomics: `PXD073336`
- PD aqueous-humor proteomics: supplementary SomaScan measurements from Wolf et al., *Cell* (2023)

Large public source datasets are not redistributed here. Obtain them from their original repositories/publication supplements.

## Manual/frozen resources

For an exact rerun, the project expects the following resources at these locations below the selected project root:

```text
resources/pathways/ReactomePathways_V97.gmt
ocular_validation/Wolf_Cell_2023/NIHMS1931846-supplement-8.xlsx
```

The AD retinal proteomics workbook is expected at:

```text
ocular_validation/PXD073336/Retinaxhippocampus_Proteomics.xlsx
```

The primary release notebook can download the PXD073336 workbook when it is absent. The exact frozen Reactome V97 GMT and Wolf Table S7 are not bundled in this repository and must be supplied by the user from their original sources.

## Running the primary notebook

The notebook was written for Google Colab/Google Drive but centralizes the project root through the `RETINA_ND_ROOT` environment variable. If `RETINA_ND_ROOT` is not set, the setup cell checks the author’s historical Colab project locations and otherwise falls back to:

```text
/content/drive/MyDrive/RETINA_ND_V2
```

For a different environment, set `RETINA_ND_ROOT` before the setup cell or adapt the project-root configuration to your filesystem.

Install the recorded dependencies with:

```bash
pip install -r requirements.txt
```

Ten package versions were explicitly recorded in the executed analysis and are pinned. Six additional packages used by the pipeline were not version-recorded in the historical executed notebook and are therefore intentionally left unpinned rather than assigned invented versions.

## Reproducibility status

This repository is an **archival release of the analysis code** accompanying the manuscript.

For this public archive, the notebooks were checked statically without executing analysis cells. The release audit verified:

- valid notebook JSON;
- 75 code cells in the primary release notebook;
- zero embedded code-cell outputs;
- zero non-null execution counts;
- successful Python compilation of every code cell in all three notebooks;
- no obvious API keys, passwords, bearer tokens, GitHub tokens, or OpenAI-style secret keys detected by the static credential scan.

The complete pipeline was **not re-executed end-to-end from the raw public datasets in a new clean runtime immediately before this archival release**. Code availability should therefore not be interpreted as an independently demonstrated fresh end-to-end reproduction.

`RETINA_ND_bioRxiv_release_FRESH_TEST.ipynb` is included specifically to facilitate a clean-runtime verification. It creates `/content/drive/MyDrive/RETINA_ND_RELEASE_TEST`, refuses to reuse a non-empty test folder, and copies only the frozen/manual source resources from a completed project before rebuilding the pipeline.

## Analysis scope and interpretation

The analysis keeps several evidence layers separate:

1. within-disease AD and PD replication;
2. genome-wide cross-disease effect-vector concordance;
3. conservative same-direction gene-level conjunction testing;
4. cell-class-resolved Reactome convergence and recurrent pathway directionality;
5. healthy-retina expression support;
6. AD retinal and PD aqueous-humor proteomic support;
7. rule-based multimodal candidate prioritization.

The multimodal evidence classes are prioritization categories, not probabilities or new significance tests. Cross-tissue support does not establish retinal origin for aqueous-humor proteins and does not establish clinically validated ocular biomarkers.

## Citation

Please cite the software release using the metadata in `CITATION.cff`. A Zenodo DOI will be added to this README after the GitHub release is archived by Zenodo.

Manuscript title:

> Tawfik M. *Glial transcriptomic convergence in Alzheimer’s and Parkinson’s disease with independent retinal and aqueous-humor evidence.*

## License

The original code in this repository is released under the MIT License. Third-party datasets, supplementary files, pathway resources, and other source materials are **not** relicensed by this repository and remain subject to their original terms and licenses.