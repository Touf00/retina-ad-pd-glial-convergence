#!/usr/bin/env python3
from pathlib import Path
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import spearmanr

ROOT = Path(__file__).resolve().parents[2]
SRC = ROOT / "publication" / "source_data" / "cross_cohort_gene_effects"
SUMMARY = ROOT / "publication" / "source_data" / "glial_cross_cohort_matrix.csv"
OUT_FIG = ROOT / "publication" / "figures" / "supplementary"
OUT_DATA = ROOT / "publication" / "source_data" / "figure_source_data"
OUT_FIG.mkdir(parents=True, exist_ok=True)
OUT_DATA.mkdir(parents=True, exist_ok=True)

cell_order = ["Astro", "Micro", "OPC", "Oligo"]
panel_letters = ["A", "B", "C", "D"]
panel_titles = {
    "Astro": "Astrocytes",
    "Micro": "Microglia",
    "OPC": "OPCs",
    "Oligo": "Oligodendrocytes",
}

summary = pd.read_csv(SUMMARY)
summary = summary[(summary["AD_cohort"]=="AD174") & (summary["PD_cohort"]=="PD243")].copy()
summary = summary.set_index("cell_class").loc[cell_order].reset_index()

fig, axes = plt.subplots(2, 2, figsize=(8.8, 7.8), constrained_layout=False)
axes = axes.ravel()

plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "pdf.fonttype": 42,
    "ps.fonttype": 42,
})

source_manifest = []

for ax, cell, letter in zip(axes, cell_order, panel_letters):
    path = SRC / f"AD174__PD243__{cell}.csv.gz"
    df = pd.read_csv(path)

    # Historical files store gene IDs either in the first unnamed/index column or a named gene column.
    cols = list(df.columns)
    gene_col = cols[0]
    if gene_col.startswith("Unnamed"):
        df = df.rename(columns={gene_col: "gene"})
        gene_col = "gene"
    elif gene_col not in ("gene", "gene_symbol"):
        df = df.rename(columns={gene_col: "gene"})
        gene_col = "gene"

    if not {"AD", "PD"}.issubset(df.columns):
        raise RuntimeError(f"{path.name}: expected AD and PD columns, found {list(df.columns)}")

    x = pd.to_numeric(df["AD"], errors="coerce")
    y = pd.to_numeric(df["PD"], errors="coerce")
    ok = np.isfinite(x) & np.isfinite(y)
    x = x[ok].to_numpy()
    y = y[ok].to_numpy()

    if len(x) == 0:
        raise RuntimeError(f"No finite points in {path}")

    # Validate figure inputs against the frozen summary.
    row = summary[summary["cell_class"] == cell].iloc[0]
    rho = float(spearmanr(x, y).statistic)
    same = float(np.mean(np.sign(x) == np.sign(y)))
    if not np.isclose(rho, float(row["rho"]), atol=5e-7):
        raise RuntimeError(f"{cell}: rho mismatch {rho} vs {row['rho']}")
    if not np.isclose(same, float(row["sign_agreement"]), atol=5e-7):
        raise RuntimeError(f"{cell}: same-direction mismatch {same} vs {row['sign_agreement']}")
    if len(x) != int(row["n_genes"]):
        raise RuntimeError(f"{cell}: matched-gene count mismatch {len(x)} vs {int(row['n_genes'])}")

    # Symmetric plotting window based on the central 99.5% of absolute effects.
    lim = float(np.quantile(np.abs(np.concatenate([x, y])), 0.995))
    lim = max(lim, 0.25)

    ax.scatter(x, y, s=5, alpha=0.18, linewidths=0, rasterized=True)
    ax.axhline(0, color="0.55", linewidth=0.8, zorder=0)
    ax.axvline(0, color="0.55", linewidth=0.8, zorder=0)

    # Simple least-squares trend shown only as a visual guide.
    slope, intercept = np.polyfit(x, y, 1)
    xx = np.linspace(-lim, lim, 200)
    ax.plot(xx, intercept + slope * xx, color="black", linewidth=1.25)

    ax.set_xlim(-lim, lim)
    ax.set_ylim(-lim, lim)
    ax.set_aspect("equal", adjustable="box")
    ax.set_title(panel_titles[cell], fontsize=11, fontweight="bold", pad=8)
    ax.set_xlabel("AD effect (GSE174367)")
    ax.set_ylabel("PD effect (GSE243639)")

    ax.text(
        0.04, 0.96,
        f"n = {len(x):,}\nSpearman rho = {rho:.3f}\nSame direction = {same*100:.1f}%",
        transform=ax.transAxes, ha="left", va="top", fontsize=8.5,
        bbox=dict(boxstyle="round,pad=0.35", facecolor="white", edgecolor="0.75", alpha=0.9)
    )
    ax.text(-0.18, 1.07, letter, transform=ax.transAxes,
            fontsize=14, fontweight="bold", va="top", ha="left")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    source_manifest.append({
        "panel": letter,
        "cell_class": cell,
        "input_file": str(path.relative_to(ROOT)),
        "n_genes": len(x),
        "spearman_rho": rho,
        "same_direction_fraction": same,
        "permutation_p": float(row["perm_p"]),
        "plot_limit_abs_effect": lim,
        "trend_slope": float(slope),
        "trend_intercept": float(intercept),
    })

fig.suptitle(
    "Discovery-pair AD-PD glial gene-effect concordance",
    fontsize=13, fontweight="bold", y=0.985
)
fig.text(
    0.5, 0.015,
    "Each point is one matched gene. Black line: least-squares visual guide; statistics are based on Spearman correlation and sign agreement.",
    ha="center", va="bottom", fontsize=8
)
fig.subplots_adjust(left=0.11, right=0.98, top=0.91, bottom=0.09, wspace=0.25, hspace=0.30)

png = OUT_FIG / "Figure_S4_discovery_pair_gene_effect_concordance.png"
pdf = OUT_FIG / "Figure_S4_discovery_pair_gene_effect_concordance.pdf"
fig.savefig(png, dpi=600, bbox_inches="tight")
fig.savefig(pdf, bbox_inches="tight")
plt.close(fig)

manifest = pd.DataFrame(source_manifest)
manifest.to_csv(
    OUT_DATA / "Figure_S4_discovery_pair_gene_effect_concordance_manifest.csv",
    index=False
)

assert png.exists() and png.stat().st_size > 0
assert pdf.exists() and pdf.stat().st_size > 0
assert len(manifest) == 4

print("Created:")
print(png)
print(pdf)
print(OUT_DATA / "Figure_S4_discovery_pair_gene_effect_concordance_manifest.csv")
print(manifest[["cell_class","n_genes","spearman_rho","same_direction_fraction"]].to_string(index=False))
