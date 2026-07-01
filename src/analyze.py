"""
============================================================
 Module 6: Data Analysis
 Module 7: Sorting
 Module 8: Grouping
 Module 9: Statistical Analysis
============================================================
"""

import pandas as pd

SEP = "=" * 65


def _section(title: str) -> None:
    print(f"\n{SEP}\n  {title}\n{SEP}")


# ════════════════════════════════════════════════════════════════
#  MODULE 6 : DATA ANALYSIS
# ════════════════════════════════════════════════════════════════

def compute_analysis_summary(df: pd.DataFrame) -> dict:
    """
    Compute the core analysis metrics required by Module 6.

    Returns:
        dict: Summary of average/highest/lowest marks, average attendance
              and study hours, pass/fail percentage, and grade distribution.
    """
    total = len(df)
    pass_count = (df["Result"] == "Pass").sum()
    fail_count = (df["Result"] == "Fail").sum()

    summary = {
        "Average Marks": round(df["Marks"].mean(), 2),
        "Highest Marks": df["Marks"].max(),
        "Lowest Marks": df["Marks"].min(),
        "Average Attendance": round(df["Attendance"].mean(), 2),
        "Average Study Hours": round(df["Study_Hours"].mean(), 2),
        "Pass Percentage": round((pass_count / total) * 100, 2) if total else 0,
        "Fail Percentage": round((fail_count / total) * 100, 2) if total else 0,
        "Grade Distribution": df["Grade"].value_counts().sort_index().to_dict(),
    }
    return summary


def display_analysis_summary(summary: dict) -> None:
    """Pretty-print the analysis summary dictionary."""
    _section("DATA ANALYSIS SUMMARY")
    for key, val in summary.items():
        if key == "Grade Distribution":
            print(f"  {key}:")
            for grade, count in val.items():
                print(f"      {grade} : {count}")
        else:
            print(f"  {key:<22}: {val}")


def run_module6(df: pd.DataFrame) -> dict:
    """Execute all Module 6 analysis tasks."""
    print(f"\n{'#'*65}")
    print("  MODULE 6 : DATA ANALYSIS")
    print(f"{'#'*65}")

    summary = compute_analysis_summary(df)
    display_analysis_summary(summary)

    print(f"\n  ✓ Module 6 complete.\n")
    return summary


# ════════════════════════════════════════════════════════════════
#  MODULE 7 : SORTING
# ════════════════════════════════════════════════════════════════

def sort_by_marks(df: pd.DataFrame, ascending: bool = False) -> pd.DataFrame:
    """Return DataFrame sorted by Marks (default: descending)."""
    return df.sort_values("Marks", ascending=ascending).reset_index(drop=True)


def sort_by_attendance(df: pd.DataFrame, ascending: bool = False) -> pd.DataFrame:
    """Return DataFrame sorted by Attendance (default: descending)."""
    return df.sort_values("Attendance", ascending=ascending).reset_index(drop=True)


def sort_by_study_hours(df: pd.DataFrame, ascending: bool = False) -> pd.DataFrame:
    """Return DataFrame sorted by Study_Hours (default: descending)."""
    return df.sort_values("Study_Hours", ascending=ascending).reset_index(drop=True)


def run_module7(df: pd.DataFrame) -> None:
    """Execute all Module 7 sorting tasks and display top rows of each."""
    print(f"\n{'#'*65}")
    print("  MODULE 7 : SORTING")
    print(f"{'#'*65}")

    _section("STUDENTS SORTED BY MARKS (Descending)")
    print(sort_by_marks(df)[["Student_ID", "Student_Name", "Marks"]].head(10).to_string(index=False))

    _section("STUDENTS SORTED BY ATTENDANCE (Descending)")
    print(sort_by_attendance(df)[["Student_ID", "Student_Name", "Attendance"]].head(10).to_string(index=False))

    _section("STUDENTS SORTED BY STUDY HOURS (Descending)")
    print(sort_by_study_hours(df)[["Student_ID", "Student_Name", "Study_Hours"]].head(10).to_string(index=False))

    print(f"\n  ✓ Module 7 complete.\n")


# ════════════════════════════════════════════════════════════════
#  MODULE 8 : GROUPING
# ════════════════════════════════════════════════════════════════

def average_marks_by_grade(df: pd.DataFrame) -> pd.Series:
    """Average Marks grouped by Grade."""
    return df.groupby("Grade")["Marks"].mean().round(2).sort_index()


def students_count_by_grade(df: pd.DataFrame) -> pd.Series:
    """Number of students in each Grade."""
    return df.groupby("Grade")["Student_ID"].count().sort_index()


def average_attendance_by_grade(df: pd.DataFrame) -> pd.Series:
    """Average Attendance grouped by Grade."""
    return df.groupby("Grade")["Attendance"].mean().round(2).sort_index()


def run_module8(df: pd.DataFrame) -> dict:
    """Execute all Module 8 grouping tasks."""
    print(f"\n{'#'*65}")
    print("  MODULE 8 : GROUPING")
    print(f"{'#'*65}")

    _section("AVERAGE MARKS BY GRADE")
    avg_marks = average_marks_by_grade(df)
    print(avg_marks.to_string())

    _section("NUMBER OF STUDENTS IN EACH GRADE")
    count_grade = students_count_by_grade(df)
    print(count_grade.to_string())

    _section("AVERAGE ATTENDANCE BY GRADE")
    avg_att = average_attendance_by_grade(df)
    print(avg_att.to_string())

    print(f"\n  ✓ Module 8 complete.\n")
    return {
        "avg_marks_by_grade": avg_marks,
        "count_by_grade": count_grade,
        "avg_attendance_by_grade": avg_att,
    }


# ════════════════════════════════════════════════════════════════
#  MODULE 9 : STATISTICAL ANALYSIS
# ════════════════════════════════════════════════════════════════

def compute_statistics(df: pd.DataFrame, columns=("Marks", "Attendance", "Study_Hours")) -> pd.DataFrame:
    """
    Compute Mean, Median, Mode, Std Dev, and Variance for given columns.

    Returns:
        pd.DataFrame: Rows = statistic names, Columns = data columns.
    """
    stats = {}
    for col in columns:
        stats[col] = {
            "Mean": round(df[col].mean(), 2),
            "Median": round(df[col].median(), 2),
            "Mode": df[col].mode().iloc[0] if not df[col].mode().empty else None,
            "Std Dev": round(df[col].std(), 2),
            "Variance": round(df[col].var(), 2),
        }
    return pd.DataFrame(stats)


def compute_correlation_matrix(df: pd.DataFrame, columns=("Marks", "Attendance", "Study_Hours")) -> pd.DataFrame:
    """Compute the correlation matrix between the given numeric columns."""
    return df[list(columns)].corr().round(3)


def run_module9(df: pd.DataFrame) -> dict:
    """Execute all Module 9 statistical analysis tasks."""
    print(f"\n{'#'*65}")
    print("  MODULE 9 : STATISTICAL ANALYSIS")
    print(f"{'#'*65}")

    _section("DESCRIPTIVE STATISTICS (Mean / Median / Mode / Std Dev / Variance)")
    stats_df = compute_statistics(df)
    print(stats_df.to_string())

    _section("CORRELATION MATRIX")
    corr_df = compute_correlation_matrix(df)
    print(corr_df.to_string())

    print(f"\n  ✓ Module 9 complete.\n")
    return {"statistics": stats_df, "correlation": corr_df}
