"""
============================================================
 BONUS MODULE: Visualizations (Matplotlib)
============================================================
 Generates charts to visually support the analysis:
   1. Grade distribution bar chart
   2. Marks distribution histogram
   3. Attendance vs Marks scatter plot
   4. Top 10 students by Performance Score (bar chart)
   5. Correlation heatmap
============================================================
"""

import matplotlib
matplotlib.use("Agg")  # non-interactive backend, safe for headless runs
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

plt.rcParams["figure.facecolor"] = "white"
plt.rcParams["axes.facecolor"] = "white"

GRADE_COLORS = {"A": "#2E7D32", "B": "#558B2F", "C": "#F9A825", "D": "#EF6C00", "F": "#C62828"}


def plot_grade_distribution(df: pd.DataFrame, save_path: str) -> None:
    """Bar chart of student counts per grade."""
    counts = df["Grade"].value_counts().reindex(["A", "B", "C", "D", "F"]).fillna(0)
    colors = [GRADE_COLORS[g] for g in counts.index]

    fig, ax = plt.subplots(figsize=(7, 5))
    bars = ax.bar(counts.index, counts.values, color=colors, edgecolor="black", linewidth=0.6)
    ax.set_title("Grade Distribution", fontsize=14, fontweight="bold")
    ax.set_xlabel("Grade")
    ax.set_ylabel("Number of Students")
    for bar, val in zip(bars, counts.values):
        ax.text(bar.get_x() + bar.get_width()/2, val + 0.3, int(val), ha="center", fontsize=10)
    ax.spines[["top", "right"]].set_visible(False)
    plt.tight_layout()
    plt.savefig(save_path, dpi=150)
    plt.close()
    print(f"  ✓ Saved chart → {save_path}")


def plot_marks_histogram(df: pd.DataFrame, save_path: str) -> None:
    """Histogram of Marks distribution."""
    fig, ax = plt.subplots(figsize=(7, 5))
    ax.hist(df["Marks"], bins=10, color="#1565C0", edgecolor="black", alpha=0.85)
    ax.axvline(df["Marks"].mean(), color="red", linestyle="--", linewidth=1.5,
               label=f"Mean = {df['Marks'].mean():.1f}")
    ax.set_title("Marks Distribution", fontsize=14, fontweight="bold")
    ax.set_xlabel("Marks")
    ax.set_ylabel("Frequency")
    ax.legend()
    ax.spines[["top", "right"]].set_visible(False)
    plt.tight_layout()
    plt.savefig(save_path, dpi=150)
    plt.close()
    print(f"  ✓ Saved chart → {save_path}")


def plot_attendance_vs_marks(df: pd.DataFrame, save_path: str) -> None:
    """Scatter plot showing relationship between Attendance and Marks."""
    fig, ax = plt.subplots(figsize=(7, 5))
    colors = df["Result"].map({"Pass": "#2E7D32", "Fail": "#C62828"})
    ax.scatter(df["Attendance"], df["Marks"], c=colors, alpha=0.75, edgecolor="black", linewidth=0.4)
    ax.set_title("Attendance vs Marks", fontsize=14, fontweight="bold")
    ax.set_xlabel("Attendance (%)")
    ax.set_ylabel("Marks")
    from matplotlib.patches import Patch
    legend_elems = [Patch(facecolor="#2E7D32", label="Pass"), Patch(facecolor="#C62828", label="Fail")]
    ax.legend(handles=legend_elems)
    ax.spines[["top", "right"]].set_visible(False)
    plt.tight_layout()
    plt.savefig(save_path, dpi=150)
    plt.close()
    print(f"  ✓ Saved chart → {save_path}")


def plot_top10_performance(df: pd.DataFrame, save_path: str) -> None:
    """Horizontal bar chart of Top 10 students by Performance Score."""
    top10 = df.sort_values("Performance_Score", ascending=False).head(10)
    fig, ax = plt.subplots(figsize=(8, 6))
    bars = ax.barh(top10["Student_Name"], top10["Performance_Score"], color="#6A1B9A", edgecolor="black")
    ax.invert_yaxis()
    ax.set_title("Top 10 Students — Performance Score", fontsize=14, fontweight="bold")
    ax.set_xlabel("Performance Score")
    for bar, val in zip(bars, top10["Performance_Score"]):
        ax.text(val + 0.5, bar.get_y() + bar.get_height()/2, f"{val:.1f}", va="center", fontsize=9)
    ax.spines[["top", "right"]].set_visible(False)
    plt.tight_layout()
    plt.savefig(save_path, dpi=150)
    plt.close()
    print(f"  ✓ Saved chart → {save_path}")


def plot_correlation_heatmap(df: pd.DataFrame, save_path: str) -> None:
    """Heatmap of correlation matrix between Marks, Attendance, Study_Hours."""
    cols = ["Marks", "Attendance", "Study_Hours"]
    corr = df[cols].corr()

    fig, ax = plt.subplots(figsize=(6, 5))
    im = ax.imshow(corr, cmap="coolwarm", vmin=-1, vmax=1)
    ax.set_xticks(range(len(cols)))
    ax.set_yticks(range(len(cols)))
    ax.set_xticklabels(cols, rotation=30, ha="right")
    ax.set_yticklabels(cols)
    for i in range(len(cols)):
        for j in range(len(cols)):
            ax.text(j, i, f"{corr.iloc[i, j]:.2f}", ha="center", va="center",
                     color="white" if abs(corr.iloc[i, j]) > 0.5 else "black", fontsize=10)
    ax.set_title("Correlation Heatmap", fontsize=14, fontweight="bold")
    fig.colorbar(im, ax=ax, shrink=0.8)
    plt.tight_layout()
    plt.savefig(save_path, dpi=150)
    plt.close()
    print(f"  ✓ Saved chart → {save_path}")


def run_visualizations(df: pd.DataFrame, charts_dir: str) -> None:
    """Generate and save all bonus visualizations."""
    print(f"\n{'#'*65}")
    print("  BONUS MODULE : VISUALIZATIONS")
    print(f"{'#'*65}\n")

    plot_grade_distribution(df, f"{charts_dir}/grade_distribution.png")
    plot_marks_histogram(df, f"{charts_dir}/marks_histogram.png")
    plot_attendance_vs_marks(df, f"{charts_dir}/attendance_vs_marks.png")
    plot_top10_performance(df, f"{charts_dir}/top10_performance.png")
    plot_correlation_heatmap(df, f"{charts_dir}/correlation_heatmap.png")

    print(f"\n  ✓ Bonus visualizations complete.\n")
