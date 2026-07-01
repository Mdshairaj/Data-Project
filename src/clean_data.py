"""
============================================================
 Module 2: Data Inspection
 Module 3: Data Cleaning
============================================================
 Module 2 inspects the raw dataset for quality issues.
 Module 3 fixes those issues and saves cleaned_data.csv
============================================================
"""

import pandas as pd

SEP = "=" * 65


def _section(title: str) -> None:
    print(f"\n{SEP}\n  {title}\n{SEP}")


# ════════════════════════════════════════════════════════════════
#  MODULE 2 : DATA INSPECTION
# ════════════════════════════════════════════════════════════════

def find_missing_values(df: pd.DataFrame) -> pd.Series:
    """Return and display count of missing values per column."""
    _section("MISSING VALUES PER COLUMN")
    missing = df.isnull().sum()
    print(missing.to_string())
    print(f"\n  Total missing cells: {missing.sum()}")
    return missing


def find_duplicate_records(df: pd.DataFrame) -> int:
    """Return and display the count of fully duplicated rows."""
    _section("DUPLICATE RECORDS")
    dup_count = df.duplicated().sum()
    print(f"  Total duplicate rows: {dup_count}")
    if dup_count > 0:
        print("\n  Duplicate rows preview:")
        print(df[df.duplicated()].to_string(index=True))
    return dup_count


def display_statistics(df: pd.DataFrame) -> None:
    """Display descriptive statistics for numeric columns."""
    _section("DESCRIPTIVE STATISTICS")
    print(df.describe().to_string())


def check_memory_usage(df: pd.DataFrame) -> None:
    """Display memory usage of the DataFrame."""
    _section("MEMORY USAGE")
    mem = df.memory_usage(deep=True)
    print(mem.to_string())
    print(f"\n  Total memory: {mem.sum() / 1024:.2f} KB")


def display_summary_info(df: pd.DataFrame) -> None:
    """Display df.info() style summary."""
    _section("SUMMARY INFO")
    df.info()


def run_module2(df: pd.DataFrame) -> None:
    """Execute all Module 2 inspection tasks."""
    print(f"\n{'#'*65}")
    print("  MODULE 2 : DATA INSPECTION")
    print(f"{'#'*65}")

    find_missing_values(df)
    find_duplicate_records(df)
    display_statistics(df)
    check_memory_usage(df)
    display_summary_info(df)

    print(f"\n  ✓ Module 2 complete.\n")


# ════════════════════════════════════════════════════════════════
#  MODULE 3 : DATA CLEANING
# ════════════════════════════════════════════════════════════════

def remove_duplicates(df: pd.DataFrame) -> pd.DataFrame:
    """Remove fully duplicated rows."""
    before = len(df)
    df = df.drop_duplicates().reset_index(drop=True)
    print(f"  ✓ Removed {before - len(df)} duplicate row(s). Remaining: {len(df)}")
    return df


def handle_missing_values(df: pd.DataFrame) -> pd.DataFrame:
    """
    Handle missing values per column:
      - Student_Name : drop row (cannot impute an identity field)
      - Study_Hours, Attendance, Marks : fill with column median
    """
    before = len(df)

    # Drop rows where the student's name itself is missing
    df = df.dropna(subset=["Student_Name"]).reset_index(drop=True)

    # Impute numeric columns with median (robust to outliers)
    for col in ["Study_Hours", "Attendance", "Marks"]:
        if df[col].isnull().sum() > 0:
            median_val = df[col].median()
            n_filled = df[col].isnull().sum()
            df[col] = df[col].fillna(median_val)
            print(f"  ✓ Filled {n_filled} missing value(s) in '{col}' with median = {median_val}")

    dropped = before - len(df)
    if dropped:
        print(f"  ✓ Dropped {dropped} row(s) with missing Student_Name.")
    return df


def validate_attendance(df: pd.DataFrame) -> pd.DataFrame:
    """Keep only rows where Attendance is within the valid 0-100 range."""
    before = len(df)
    df = df[(df["Attendance"] >= 0) & (df["Attendance"] <= 100)].reset_index(drop=True)
    print(f"  ✓ Removed {before - len(df)} row(s) with invalid Attendance (outside 0-100).")
    return df


def validate_study_hours(df: pd.DataFrame) -> pd.DataFrame:
    """Keep only rows where Study_Hours is within a realistic 0-24 range."""
    before = len(df)
    df = df[(df["Study_Hours"] >= 0) & (df["Study_Hours"] <= 24)].reset_index(drop=True)
    print(f"  ✓ Removed {before - len(df)} row(s) with invalid Study_Hours (outside 0-24).")
    return df


def validate_marks(df: pd.DataFrame) -> pd.DataFrame:
    """Keep only rows where Marks is within the valid 0-100 range."""
    before = len(df)
    df = df[(df["Marks"] >= 0) & (df["Marks"] <= 100)].reset_index(drop=True)
    print(f"  ✓ Removed {before - len(df)} row(s) with invalid Marks (outside 0-100).")
    return df


def remove_invalid_entries(df: pd.DataFrame) -> pd.DataFrame:
    """
    Apply all field-level validations in sequence.
    Wraps validate_attendance / validate_study_hours / validate_marks.
    """
    df = validate_attendance(df)
    df = validate_study_hours(df)
    df = validate_marks(df)
    return df


def save_cleaned_data(df: pd.DataFrame, output_path: str) -> None:
    """Save the cleaned DataFrame to CSV."""
    df.to_csv(output_path, index=False)
    print(f"\n  ✓ Cleaned dataset saved → {output_path}  ({len(df)} rows)")


def run_module3(df: pd.DataFrame, output_path: str) -> pd.DataFrame:
    """
    Execute all Module 3 cleaning tasks in sequence.

    Args:
        df (pd.DataFrame): Raw dataset (from Module 1).
        output_path (str): Where to save cleaned_data.csv

    Returns:
        pd.DataFrame: The cleaned dataset.
    """
    print(f"\n{'#'*65}")
    print("  MODULE 3 : DATA CLEANING")
    print(f"{'#'*65}\n")

    df = remove_duplicates(df)
    df = handle_missing_values(df)
    df = remove_invalid_entries(df)
    save_cleaned_data(df, output_path)

    print(f"\n  ✓ Module 3 complete.\n")
    return df
