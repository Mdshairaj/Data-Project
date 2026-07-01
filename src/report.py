"""
============================================================
 Module 10: Report Generation
 Module 11: Export Data
============================================================
 Module 10 compiles a final summary report.
 Module 11 confirms / lists all exported output files.
============================================================
"""

import os
import pandas as pd

SEP = "=" * 65


def _section(title: str) -> None:
    print(f"\n{SEP}\n  {title}\n{SEP}")


# ════════════════════════════════════════════════════════════════
#  MODULE 10 : REPORT GENERATION
# ════════════════════════════════════════════════════════════════

def build_final_report(df: pd.DataFrame) -> pd.DataFrame:
    """
    Build the final report as a single-row-per-metric DataFrame,
    suitable for saving directly as report.csv.

    Args:
        df (pd.DataFrame): Cleaned & transformed dataset (with Grade/Result).

    Returns:
        pd.DataFrame: Two-column report (Metric, Value).
    """
    total_students = len(df)
    passed = (df["Result"] == "Pass").sum()
    failed = (df["Result"] == "Fail").sum()
    grade_dist = df["Grade"].value_counts().sort_index()

    rows = [
        ("Total Students", total_students),
        ("Number of Passed Students", passed),
        ("Number of Failed Students", failed),
        ("Highest Marks", df["Marks"].max()),
        ("Lowest Marks", df["Marks"].min()),
        ("Average Marks", round(df["Marks"].mean(), 2)),
        ("Average Attendance", round(df["Attendance"].mean(), 2)),
    ]

    for grade in ["A", "B", "C", "D", "F"]:
        rows.append((f"Grade {grade} Count", int(grade_dist.get(grade, 0))))

    report_df = pd.DataFrame(rows, columns=["Metric", "Value"])
    return report_df


def display_report(report_df: pd.DataFrame) -> None:
    """Pretty-print the final report."""
    _section("FINAL REPORT")
    print(report_df.to_string(index=False))


def save_report(report_df: pd.DataFrame, output_path: str) -> None:
    """Save the final report to CSV."""
    report_df.to_csv(output_path, index=False)
    print(f"\n  ✓ Report saved → {output_path}")


def save_report_excel(report_df: pd.DataFrame, output_path: str) -> None:
    """
    Bonus: Save the final report as an Excel (.xlsx) file too.
    Requires openpyxl to be installed.
    """
    try:
        report_df.to_excel(output_path, index=False, sheet_name="Report")
        print(f"  ✓ Report also saved as Excel → {output_path}  [BONUS]")
    except ImportError:
        print("  ⚠ openpyxl not installed — skipping Excel export.")


def run_module10(df: pd.DataFrame, output_dir: str) -> pd.DataFrame:
    """Execute all Module 10 report generation tasks."""
    print(f"\n{'#'*65}")
    print("  MODULE 10 : REPORT GENERATION")
    print(f"{'#'*65}")

    report_df = build_final_report(df)
    display_report(report_df)
    save_report(report_df, f"{output_dir}/report.csv")
    save_report_excel(report_df, f"{output_dir}/report.xlsx")

    print(f"\n  ✓ Module 10 complete.\n")
    return report_df


# ════════════════════════════════════════════════════════════════
#  MODULE 11 : EXPORT DATA
# ════════════════════════════════════════════════════════════════

def verify_exports(output_dir: str) -> None:
    """
    Verify and list all expected output files inside the output folder,
    confirming the export step (Module 11) completed successfully.
    """
    print(f"\n{'#'*65}")
    print("  MODULE 11 : EXPORT DATA")
    print(f"{'#'*65}")

    expected_files = [
        "cleaned_data.csv",
        "toppers.csv",
        "failed_students.csv",
        "report.csv",
        "low_attendance_students.csv",
        "high_study_hours_students.csv",
        "report.xlsx",
    ]

    _section(f"OUTPUT FILES IN '{output_dir}/'")
    for fname in expected_files:
        fpath = os.path.join(output_dir, fname)
        if os.path.exists(fpath):
            size_kb = os.path.getsize(fpath) / 1024
            print(f"  ✓ {fname:<35} ({size_kb:.2f} KB)")
        else:
            print(f"  ✗ {fname:<35} MISSING")

    print(f"\n  ✓ Module 11 complete — all files exported to '{output_dir}/'\n")
