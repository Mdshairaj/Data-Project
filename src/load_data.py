"""
============================================================
 Module 1: Data Loading
============================================================
 Handles all data-loading operations:
   - Reading CSV files
   - Displaying head / tail records
   - Printing shape, column names, and data types
============================================================
"""

import os
import pandas as pd

SEP = "=" * 65


# ── Helper ────────────────────────────────────────────────────────

def _section(title: str) -> None:
    print(f"\n{SEP}\n  {title}\n{SEP}")


# ── Core functions ────────────────────────────────────────────────

def load_dataset(filepath: str) -> pd.DataFrame:
    """
    Read a CSV file and return a DataFrame.

    Args:
        filepath (str): Relative or absolute path to the CSV file.

    Returns:
        pd.DataFrame: The loaded dataset.

    Raises:
        FileNotFoundError: If the file does not exist at the given path.
    """
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"Dataset not found at: {filepath}")

    df = pd.read_csv(filepath)
    print(f"\n  ✓ Dataset loaded  →  {filepath}")
    print(f"    Rows: {df.shape[0]}   |   Columns: {df.shape[1]}")
    return df


def display_first_records(df: pd.DataFrame, n: int = 5) -> None:
    """Display the first *n* records of the DataFrame."""
    _section(f"FIRST {n} RECORDS")
    print(df.head(n).to_string(index=True))


def display_last_records(df: pd.DataFrame, n: int = 5) -> None:
    """Display the last *n* records of the DataFrame."""
    _section(f"LAST {n} RECORDS")
    print(df.tail(n).to_string(index=True))


def display_shape(df: pd.DataFrame) -> None:
    """Print the dimensions (rows × columns) of the dataset."""
    _section("DATASET SHAPE")
    print(f"  Rows    : {df.shape[0]}")
    print(f"  Columns : {df.shape[1]}")


def display_columns(df: pd.DataFrame) -> None:
    """Print all column names with their index numbers."""
    _section("COLUMN NAMES")
    for i, col in enumerate(df.columns, 1):
        print(f"  {i}. {col}")


def display_dtypes(df: pd.DataFrame) -> None:
    """Display the data type of each column."""
    _section("DATA TYPES")
    for col, dtype in df.dtypes.items():
        print(f"  {col:<25} :  {dtype}")


# ── Module runner ─────────────────────────────────────────────────

def run_module1(filepath: str) -> pd.DataFrame:
    """
    Execute all Module 1 tasks in sequence.

    Args:
        filepath (str): Path to the raw CSV file.

    Returns:
        pd.DataFrame: The loaded raw DataFrame.
    """
    print(f"\n{'#'*65}")
    print("  MODULE 1 : DATA LOADING")
    print(f"{'#'*65}")

    df = load_dataset(filepath)
    display_first_records(df)
    display_last_records(df)
    display_shape(df)
    display_columns(df)
    display_dtypes(df)

    print(f"\n  ✓ Module 1 complete.\n")
    return df
