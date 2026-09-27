#!/usr/bin/env python3
from pathlib import Path
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import TwoSlopeNorm

ROOT = Path(__file__).resolve().parents[2]
SRC = ROOT / "publication" / "source_data"
OUT_FIG = ROOT / "publication" / "figures" / "main"
OUT_DATA = SRC / "figure_source_data"
OUT_FIG.mkdir(parents=True, exist_ok=True)
OUT_DATA.mkdir(parents=True, exist_ok=True)

matrix_path = SRC / "glial_cross_cohort_matrix.csv"
boot_path = SRC / "independent_pair_donor_bootstrap_summary.csv"

matrix = pd.read_csv(matrix_path)
boot = pd.read_csv(boot_path)

row_order = [
    ("AD174", "PD243"),
    ("AD174", "PD329"),
    ("AD222", "PD243"),
    ("AD222", "PD329"),
]
row_labels = [
    "GSE174367 × GSE243639",
    "GSE174367 × GSE329625",
    "GSE222494 × GSE243639",
    "GSE222494 × GSE329625",
]
cell_order = ["Astro", "Micro", "OPC", "Oligo"]

matrix["pair"] = list(zip(matrix["AD_cohort"], matrix["PD_cohort"]))
missing_pairs = [p for p in row_order if p not in set(matrix["pair"])]
if missing_pairs:
    raise RuntimeError(f"Missing cohort pairs: {missing_pairs}")

rho = np.empty((4, 4), dtype=float)
sign = np.empty((4, 4), dtype=float)
ngenes = np.empty((4, 4), dtype=int)
perm = np.empty((4, 4), dtype=float)

records = []
for i, (ad, pd_) in enumerate(row_order):
    sub = matrix[(matrix["AD_cohort"] == ad) & (matrix["PD_cohort"] == pd_)]
    for j, cell in enumerate(cell_order):
        r = sub[sub["cell_class"] == cell]
        if len(r) != 1:
            raise RuntimeError(f"Expected exactly one row for {ad} {pd_} {cell}, found {len(r)}")
        rr = r.iloc[0]
        rho[i, j] = float(rr["rho"])
        sign[i, j] = float(rr["sign_agreement"])
        ngenes[i, j] = int(rr["n_genes"])
        perm[i, j] = float(rr["perm_p"])
        records.append({
            "panel": "A_B",
            "AD_cohort": ad,
            "PD_cohort": pd_,
            "AD_accession": row_labels[i].split(" × ")[0],
            "PD_accession": row_labels[i].split(" × ")[1],
            "cell_class": cell,
            "matched_genes": int(rr["n_genes"]),
            "spearman_rho": float(rr["rho"]),
            "same_direction_fraction": float(rr["sign_agreement"]),
            "permutation_p": float(rr["perm_p"]),
        })

boot = boot.set_index("cell_class").loc[cell_order].reset_index()
for _, rr in boot.iterrows():
    records.append({
        "panel": "C",
        "AD_cohort": "AD222",
        "PD_cohort": "PD329",
        "AD_accession": "GSE222494",
        "PD_accession": "GSE329625",
        "cell_class": rr["cell_class"],
        "bootstrap_B": int(rr["B"]),
        "median_rho": float(rr["median_rho"]),
        "ci2_5": float(rr["ci2_5"]),
        "ci97_5": float(rr["ci97_5"]),
        "fraction_rho_gt0": float(rr["fraction_rho_gt0"]),
    })

pd.DataFrame(records).to_csv(
    OUT_DATA / "Figure_2_cross_cohort_variability_source_data.csv",
    index=False
)

plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "font.size": 8.5,
    "axes.titlesize": 10,
    "axes.labelsize": 9,
    "xtick.labelsize": 8,
    "ytick.labelsize": 8,
    "pdf.fonttype": 42,
    "ps.fonttype": 42,
})

fig = plt.figure(figsize=(11.0, 4.9))
gs = fig.add_gridspec(1, 3, width_ratios=[1.05, 1.05, 1.0], wspace=0.58)

# Panel A
ax1 = fig.add_subplot(gs[0, 0])
norm = TwoSlopeNorm(vmin=-0.10, vcenter=0.0, vmax=0.40)
im1 = ax1.imshow(rho, cmap="RdBu_r", norm=norm, aspect="auto")
ax1.set_xticks(range(4), cell_order, rotation=35, ha="right")
ax1.set_yticks(range(4), row_labels)
ax1.set_title("Cross-cohort glial effect alignment", pad=9, fontweight="bold")
for i in range(4):
    for j in range(4):
        value = rho[i, j]
        rgba = im1.cmap(im1.norm(value))
        luminance = 0.299*rgba[0] + 0.587*rgba[1] + 0.114*rgba[2]
        color = "black" if luminance > 0.58 else "white"
        ax1.text(j, i, f"{value:.3f}", ha="center", va="center",
                 color=color, fontsize=8, fontweight="bold")
for spine in ax1.spines.values():
    spine.set_visible(False)
cbar1 = fig.colorbar(im1, ax=ax1, fraction=0.046, pad=0.04)
cbar1.set_label("Spearman ρ", rotation=90)
ax1.text(-0.22, 1.08, "A", transform=ax1.transAxes, fontsize=14, fontweight="bold", va="top")

# Panel B
ax2 = fig.add_subplot(gs[0, 1])
im2 = ax2.imshow(sign * 100, cmap="viridis", vmin=47, vmax=65, aspect="auto")
ax2.set_xticks(range(4), cell_order, rotation=35, ha="right")
ax2.set_yticks(range(4), [""]*4)
ax2.set_title("Same-direction genes", pad=9, fontweight="bold")
for i in range(4):
    for j in range(4):
        value = sign[i, j] * 100
        rgba = im2.cmap(im2.norm(value))
        luminance = 0.299*rgba[0] + 0.587*rgba[1] + 0.114*rgba[2]
        color = "black" if luminance > 0.58 else "white"
        ax2.text(j, i, f"{value:.1f}%", ha="center", va="center",
                 color=color, fontsize=8, fontweight="bold")
for spine in ax2.spines.values():
    spine.set_visible(False)
cbar2 = fig.colorbar(im2, ax=ax2, fraction=0.046, pad=0.04)
cbar2.set_label("Genes with matching direction (%)", rotation=90)
ax2.text(-0.18, 1.08, "B", transform=ax2.transAxes, fontsize=14, fontweight="bold", va="top")

# Panel C
ax3 = fig.add_subplot(gs[0, 2])
y = np.arange(len(cell_order))[::-1]
med = boot["median_rho"].to_numpy()
lo = boot["ci2_5"].to_numpy()
hi = boot["ci97_5"].to_numpy()
xerr = np.vstack([med - lo, hi - med])
ax3.errorbar(med, y, xerr=xerr, fmt="o", markersize=6,
             capsize=4, elinewidth=1.6, capthick=1.4)
ax3.axvline(0, color="0.35", linewidth=1, linestyle="--")
ax3.set_yticks(y, cell_order)
ax3.set_xlim(-0.18, 0.16)
ax3.set_xlabel("Bootstrap Spearman ρ")
ax3.set_title("Fully external pair\nGSE222494 × GSE329625", pad=7, fontweight="bold")
ax3.grid(axis="x", linewidth=0.5, alpha=0.25)
for yy, m, l, h in zip(y, med, lo, hi):
    ax3.text(0.165, yy, f"{m:.3f} [{l:.3f}, {h:.3f}]",
             va="center", ha="left", fontsize=7.2, clip_on=False)
ax3.spines["top"].set_visible(False)
ax3.spines["right"].set_visible(False)
ax3.text(-0.23, 1.08, "C", transform=ax3.transAxes, fontsize=14, fontweight="bold", va="top")

fig.suptitle(
    "Cohort-dependent variability of AD–PD glial transcriptomic alignment",
    fontsize=12.5, fontweight="bold", y=1.01
)
fig.text(
    0.5, -0.02,
    "Panels A–B use frozen cross-cohort gene-effect summaries. Panel C shows donor-bootstrap medians and 95% intervals (B=500) for the fully external cohort pair.",
    ha="center", va="top", fontsize=7.5
)

png = OUT_FIG / "Figure_2_cross_cohort_variability.png"
pdf = OUT_FIG / "Figure_2_cross_cohort_variability.pdf"
fig.savefig(png, dpi=600, bbox_inches="tight")
fig.savefig(pdf, bbox_inches="tight")
plt.close(fig)

# Basic assertions
assert np.all((lo < 0) & (hi > 0)), "Not all external-pair bootstrap intervals cross zero."
assert png.exists() and png.stat().st_size > 0
assert pdf.exists() and pdf.stat().st_size > 0

print("Created:")
print(png)
print(pdf)
print(OUT_DATA / "Figure_2_cross_cohort_variability_source_data.csv")
print("Verified: all four fully external bootstrap 95% intervals cross zero.")
