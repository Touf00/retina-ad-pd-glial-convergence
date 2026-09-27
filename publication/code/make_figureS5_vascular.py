#!/usr/bin/env python3
from pathlib import Path
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[2]
SRC = ROOT / "publication" / "source_data" / "vascular"
OUT_FIG = ROOT / "publication" / "figures" / "supplementary"
OUT_DATA = ROOT / "publication" / "source_data" / "figure_source_data"
OUT_FIG.mkdir(parents=True, exist_ok=True)
OUT_DATA.mkdir(parents=True, exist_ok=True)

comp = pd.read_csv(SRC / "vascular_comparison_summary.csv")
boot = pd.read_csv(SRC / "vascular_endothelial_bootstrap_summary.csv")

within_order = [
    "AD_replication_Endothelial",
    "AD_replication_Pericyte",
    "PD_replication_Endothelial",
]
within_labels = {
    "AD_replication_Endothelial": "AD endothelial\nGSE174367 x GSE222494",
    "AD_replication_Pericyte": "AD pericyte\nGSE174367 x GSE222494",
    "PD_replication_Endothelial": "PD endothelial\nGSE243639 x GSE157783",
}

cross_order = [
    "Cross_Endo_AD174_PD243",
    "Cross_Endo_AD174_PD157",
    "Cross_Endo_AD222_PD243",
    "Cross_Endo_AD222_PD157",
    "Cross_Pericyte_AD174_PD157",
    "Cross_Pericyte_AD222_PD157",
]
cross_labels = {
    "Cross_Endo_AD174_PD243": "Endo: AD174 x PD243",
    "Cross_Endo_AD174_PD157": "Endo: AD174 x PD157",
    "Cross_Endo_AD222_PD243": "Endo: AD222 x PD243",
    "Cross_Endo_AD222_PD157": "Endo: AD222 x PD157",
    "Cross_Pericyte_AD174_PD157": "Pericyte: AD174 x PD157",
    "Cross_Pericyte_AD222_PD157": "Pericyte: AD222 x PD157",
}

boot_order = [
    "Cross_Endo_AD174_PD243",
    "Cross_Endo_AD174_PD157",
    "Cross_Endo_AD222_PD243",
    "Cross_Endo_AD222_PD157",
]
boot_labels = {
    "Cross_Endo_AD174_PD243": "AD174 x PD243",
    "Cross_Endo_AD174_PD157": "AD174 x PD157",
    "Cross_Endo_AD222_PD243": "AD222 x PD243",
    "Cross_Endo_AD222_PD157": "AD222 x PD157",
}

# Freeze a compact publication-facing source table.
rows = []
for _, r in comp.iterrows():
    rows.append({
        "section": "comparison_summary",
        "comparison": r["comparison"],
        "cell_class": r["cell_class"],
        "n_genes": int(r["n_genes"]),
        "rho": float(r["rho"]),
        "sign_agreement": float(r["sign_agreement"]),
        "permutation_p": float(r["perm_p"]),
        "bootstrap_B": np.nan,
        "bootstrap_median_rho": np.nan,
        "bootstrap_ci2_5": np.nan,
        "bootstrap_ci97_5": np.nan,
    })
for _, r in boot.iterrows():
    rows.append({
        "section": "endothelial_bootstrap",
        "comparison": r["comparison"],
        "cell_class": "Endothelial",
        "n_genes": np.nan,
        "rho": np.nan,
        "sign_agreement": np.nan,
        "permutation_p": np.nan,
        "bootstrap_B": int(r["B"]),
        "bootstrap_median_rho": float(r["median_rho"]),
        "bootstrap_ci2_5": float(r["ci2_5"]),
        "bootstrap_ci97_5": float(r["ci97_5"]),
    })

pd.DataFrame(rows).to_csv(
    OUT_DATA / "Figure_S5_exploratory_vascular_source_data.csv",
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

fig = plt.figure(figsize=(12.2, 4.9))
gs = fig.add_gridspec(1, 3, width_ratios=[1.05, 1.12, 1.05], wspace=0.62)

# Panel A: within-disease vascular replication
ax1 = fig.add_subplot(gs[0, 0])
w = comp.set_index("comparison").loc[within_order].reset_index()
y = np.arange(len(w))[::-1]
ax1.axvline(0, color="0.45", linewidth=1, linestyle="--")
ax1.scatter(w["rho"], y, s=52, zorder=3)
ax1.set_yticks(y, [within_labels[x] for x in w["comparison"]])
ax1.set_xlim(-0.04, 0.145)
ax1.set_xlabel("Spearman rho")
ax1.set_title("Within-disease vascular replication", fontweight="bold", pad=9)
ax1.grid(axis="x", linewidth=0.5, alpha=0.25)
for yy, (_, r) in zip(y, w.iterrows()):
    ax1.text(
        0.148, yy,
        f"rho={r['rho']:.3f}\nsame dir.={100*r['sign_agreement']:.1f}%\nperm. P={r['perm_p']:.3g}",
        va="center", ha="left", fontsize=7.1, clip_on=False
    )
ax1.spines["top"].set_visible(False)
ax1.spines["right"].set_visible(False)

# Panel B: cross-disease vascular point estimates
ax2 = fig.add_subplot(gs[0, 1])
c = comp.set_index("comparison").loc[cross_order].reset_index()
y2 = np.arange(len(c))[::-1]
ax2.axvline(0, color="0.45", linewidth=1, linestyle="--")
markers = ["o" if cls == "Endothelial" else "s" for cls in c["cell_class"]]
for xx, yy, mk in zip(c["rho"], y2, markers):
    ax2.scatter(xx, yy, s=42, marker=mk, zorder=3)
ax2.set_yticks(y2, [cross_labels[x] for x in c["comparison"]])
ax2.set_xlim(-0.02, 0.23)
ax2.set_xlabel("Spearman rho")
ax2.set_title("Cross-disease vascular comparisons", fontweight="bold", pad=9)
ax2.grid(axis="x", linewidth=0.5, alpha=0.25)
for yy, (_, r) in zip(y2, c.iterrows()):
    ax2.text(
        0.233, yy,
        f"{r['rho']:.3f} ({100*r['sign_agreement']:.1f}%)",
        va="center", ha="left", fontsize=7.2, clip_on=False
    )
ax2.spines["top"].set_visible(False)
ax2.spines["right"].set_visible(False)

# Panel C: donor-bootstrap uncertainty for cross-disease endothelial comparisons
ax3 = fig.add_subplot(gs[0, 2])
b = boot.set_index("comparison").loc[boot_order].reset_index()
y3 = np.arange(len(b))[::-1]
med = b["median_rho"].to_numpy()
lo = b["ci2_5"].to_numpy()
hi = b["ci97_5"].to_numpy()
xerr = np.vstack([med - lo, hi - med])
ax3.errorbar(med, y3, xerr=xerr, fmt="o", markersize=6,
             capsize=4, elinewidth=1.6, capthick=1.4)
ax3.axvline(0, color="0.35", linewidth=1, linestyle="--")
ax3.set_yticks(y3, [boot_labels[x] for x in b["comparison"]])
ax3.set_xlim(-0.22, 0.30)
ax3.set_xlabel("Bootstrap Spearman rho")
ax3.set_title("Endothelial donor-bootstrap uncertainty", fontweight="bold", pad=9)
ax3.grid(axis="x", linewidth=0.5, alpha=0.25)
for yy, m, l, h in zip(y3, med, lo, hi):
    ax3.text(
        1.02, yy, f"{m:.3f} [{l:.3f}, {h:.3f}]",
        transform=ax3.get_yaxis_transform(),
        va="center", ha="left", fontsize=7.1, clip_on=False
    )
ax3.spines["top"].set_visible(False)
ax3.spines["right"].set_visible(False)

# Panel letters in figure coordinates
fig.subplots_adjust(left=0.14, right=0.91, top=0.79, bottom=0.18)
fig.canvas.draw()
for label, ax in zip(["A", "B", "C"], [ax1, ax2, ax3]):
    pos = ax.get_position()
    fig.text(pos.x0 - 0.025, pos.y1 + 0.065, label,
             fontsize=14, fontweight="bold", ha="right", va="center")

fig.suptitle(
    "Exploratory vascular replication and cross-disease sensitivity analyses",
    fontsize=12.5, fontweight="bold", y=0.98
)
fig.text(
    0.5, 0.04,
    "Pericyte PD replication was unavailable; all tested cross-disease endothelial donor-bootstrap 95% intervals include zero.",
    ha="center", va="bottom", fontsize=8
)

png = OUT_FIG / "Figure_S5_exploratory_vascular_analysis.png"
pdf = OUT_FIG / "Figure_S5_exploratory_vascular_analysis.pdf"
fig.savefig(png, dpi=600, bbox_inches="tight")
fig.savefig(pdf, bbox_inches="tight")
plt.close(fig)

# QA
assert np.all((lo < 0) & (hi > 0)), "Expected all endothelial bootstrap intervals to cross zero."
assert "PD_replication_Pericyte" not in set(comp["comparison"]), "Unexpected PD pericyte replication appeared."
assert png.exists() and png.stat().st_size > 0
assert pdf.exists() and pdf.stat().st_size > 0

print("Created:")
print(png)
print(pdf)
print(OUT_DATA / "Figure_S5_exploratory_vascular_source_data.csv")
print("QA passed: all endothelial bootstrap intervals cross zero; no PD pericyte replication is claimed.")
