"""
============================================================
 Module 4: Data Transformation
 Module 5: Data Filtering
============================================================
 Module 4 engineers new columns: Grade, Result, Performance_Score
 Module 5 filters subsets of students and saves them as CSVs
============================================================
"""

import pandas as pd

SEP = "=" * 65


def _section(title: str) -> None:
    print(f"\n{SEP}\n  {title}\n{SEP}")


# ════════════════════════════════════════════════════════════════
#  MODULE 4 : DATA TRANSFORMATION
# ════════════════════════════════════════════════════════════════

def assign_grade(marks: float) -> str:
    """
    Map a marks value to a letter grade.

        90-100 -> A
        75-89  -> B
        60-74  -> C
        45-59  -> D
        0-44   -> F
    """
    if marks >= 90:
        return "A"
    elif marks >= 75:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 45:
        return "D"
    else:
        return "F"


def add_grade_column(df: pd.DataFrame) -> pd.DataFrame:
    """Add a 'Grade' column based on Marks."""
    df["Grade"] = df["Marks"].apply(assign_grade)
    print("  ✓ 'Grade' column created.")
    print(df[["Student_ID", "Marks", "Grade"]].head().to_string(index=False))
    return df


def add_result_column(df: pd.DataFrame, pass_mark: float = 40) -> pd.DataFrame:
    """Add a 'Result' column: Pass if Marks >= pass_mark, else Fail."""
    df["Result"] = df["Marks"].apply(lambda m: "Pass" if m >= pass_mark else "Fail")
    print(f"\n  ✓ 'Result' column created (pass mark = {pass_mark}).")
    print(df[["Student_ID", "Marks", "Result"]].head().to_string(index=False))
    return df


def add_performance_score(
    df: pd.DataFrame,
    w_marks: float = 0.5,
    w_attendance: float = 0.3,
    w_study: float = 0.2,
) -> pd.DataFrame:
    """
    Add a 'Performance_Score' column — a weighted composite of:
        Marks (50%) + Attendance (30%) + normalized Study_Hours (20%)

    Study_Hours is normalized against a cap of 12 hrs/day -> 0-100 scale,
    so it can be combined fairly with Marks and Attendance (both 0-100).
    """
    study_normalized = (df["Study_Hours"] / 12) * 100
    study_normalized = study_normalized.clip(upper=100)

    df["Performance_Score"] = (
        df["Marks"] * w_marks
        + df["Attendance"] * w_attendance
        + study_normalized * w_study
    ).round(2)

    print(f"\n  ✓ 'Performance_Score' column created "
          f"(weights → Marks:{w_marks}, Attendance:{w_attendance}, Study:{w_study}).")
    print(df[["Student_ID", "Marks", "Attendance", "Study_Hours", "Performance_Score"]]
          .head().to_string(index=False))
    return df


def run_module4(df: pd.DataFrame) -> pd.DataFrame:
    """Execute all Module 4 transformation tasks."""
    print(f"\n{'#'*65}")
    print("  MODULE 4 : DATA TRANSFORMATION")
    print(f"{'#'*65}")

    df = add_grade_column(df)
    df = add_result_column(df)
    df = add_performance_score(df)

    print(f"\n  ✓ Module 4 complete.\n")
    return df


# ════════════════════════════════════════════════════════════════
#  MODULE 5 : DATA FILTERING
# ════════════════════════════════════════════════════════════════

def get_top_performers(df: pd.DataFrame, top_n: int = 10) -> pd.DataFrame:
    """Return the top_n students ranked by Performance_Score."""
    return df.sort_values("Performance_Score", ascending=False).head(top_n).reset_index(drop=True)


def get_failed_students(df: pd.DataFrame) -> pd.DataFrame:
    """Return all students whose Result is 'Fail'."""
    return df[df["Result"] == "Fail"].reset_index(drop=True)


def get_low_attendance_students(df: pd.DataFrame, threshold: float = 75) -> pd.DataFrame:
    """Return students with Attendance below the given threshold."""
    return df[df["Attendance"] < threshold].reset_index(drop=True)


def get_high_study_hours_students(df: pd.DataFrame, threshold: float = 8) -> pd.DataFrame:
    """Return students who study more than the given threshold of hours."""
    return df[df["Study_Hours"] > threshold].reset_index(drop=True)


def run_module5(df: pd.DataFrame, output_dir: str) -> dict:
    """
    Execute all Module 5 filtering tasks and save each subset as CSV.

    Returns:
        dict: {subset_name: DataFrame} for use in later modules/reporting.
    """
    print(f"\n{'#'*65}")
    print("  MODULE 5 : DATA FILTERING")
    print(f"{'#'*65}")

    _section("TOP-PERFORMING STUDENTS")
    toppers = get_top_performers(df)
    print(toppers[["Student_ID", "Student_Name", "Marks", "Performance_Score"]].to_string(index=False))
    toppers.to_csv(f"{output_dir}/toppers.csv", index=False)
    print(f"  ✓ Saved → {output_dir}/toppers.csv ({len(toppers)} rows)")

    _section("FAILED STUDENTS")
    failed = get_failed_students(df)
    print(failed[["Student_ID", "Student_Name", "Marks", "Result"]].to_string(index=False)
          if not failed.empty else "  No failed students found.")
    failed.to_csv(f"{output_dir}/failed_students.csv", index=False)
    print(f"  ✓ Saved → {output_dir}/failed_students.csv ({len(failed)} rows)")

    _section("STUDENTS WITH ATTENDANCE BELOW 75%")
    low_att = get_low_attendance_students(df)
    print(f"  Count: {len(low_att)}")
    low_att.to_csv(f"{output_dir}/low_attendance_students.csv", index=False)
    print(f"  ✓ Saved → {output_dir}/low_attendance_students.csv")

    _section("STUDENTS STUDYING MORE THAN 8 HOURS")
    high_study = get_high_study_hours_students(df)
    print(f"  Count: {len(high_study)}")
    high_study.to_csv(f"{output_dir}/high_study_hours_students.csv", index=False)
    print(f"  ✓ Saved → {output_dir}/high_study_hours_students.csv")

    print(f"\n  ✓ Module 5 complete.\n")

    return {
        "toppers": toppers,
        "failed": failed,
        "low_attendance": low_att,
        "high_study_hours": high_study,
    }
