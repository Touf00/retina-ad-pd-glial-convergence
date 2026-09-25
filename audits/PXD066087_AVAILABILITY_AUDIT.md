# PXD066087 availability and inclusion audit

Audit date: 2026-09-25  
Dataset: [PXD066087](https://proteomecentral.proteomexchange.org/cgi/GetDataset?ID=PXD066087-1&test=no)  
Article: [Moon et al., 2026](https://www.nature.com/articles/s41531-026-01261-7)

## Question

Can PXD066087 provide a reproducible, processed protein-level validation dataset for the RETINA-ND journal extension without introducing a new raw-mass-spectrometry pipeline?

## Public-data audit

The official PRIDE Archive v2 project-files endpoint was queried on 2026-09-25:

`https://www.ebi.ac.uk/pride/ws/archive/v2/projects/PXD066087/files`

Returned file categories:

- 26 `RAW` files, all Thermo `.raw` fractions from two TMT sets.
- 4 `SEARCH` files, all very small `.sld` sequence/method files (2,074-7,836 bytes).
- 0 processed protein-abundance tables.
- 0 differential-protein result tables.
- 0 mzIdentML/mzTab/proteinGroups-style result files.

The article reports:

- mouse M83/A53T alpha-synuclein retina, not human PD retina;
- 6- and 16-month groups with age-matched WT controls;
- TMT LC-MS/MS, `n=3/group`;
- 4,135 quantified protein groups at FDR <1%;
- DEPs defined by fold change >=1.3 and nominal `p<0.05`;
- 25 proteins shared between the two age-specific DEP sets (24.8%);
- a single supplementary DOCX containing Supplementary Figure 1, not a machine-readable protein table.

## Decision

**Exclude PXD066087 from quantitative candidate-gene validation and effect-vector convergence testing in the current journal extension.**

Reason: reconstructing protein abundances from the raw TMT files would require a new search, peptide-to-protein inference, reporter-ion correction, normalization, missingness, batch/set handling, and statistical pipeline. That analysis would not be methodologically matched to the authors' unpublished processed table or to PXD040225. It would therefore add analyst degrees of freedom rather than clean validation.

Permitted use:

- cite the paper only as qualitative, cross-species mouse-retina context;
- clearly label it as an A53T transgenic model;
- do not describe it as human PD-retina validation;
- do not claim candidate-gene replication from figure labels or selected narrative proteins.

Revisit only if the authors or PRIDE release a complete processed protein-level table with sample mapping and quantitative values.
