"""
================================================================================
 Student Performance Data Handling and Analysis System
 -------------------------------------------------------------------------------
 Main entry point. Orchestrates Modules 1-11 in sequence, and offers an
 optional interactive menu (BONUS) for re-running individual modules or
 loading a different CSV dynamically (BONUS).

 Run:
     python main.py              -> runs the full pipeline automatically
     python main.py --menu       -> launches the interactive menu instead
================================================================================
"""

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "src"))

from src.load_data import run_module1
from src.clean_data import run_module2, run_module3
from src.transform import run_module4, run_module5
from src.analyze import run_module6, run_module7, run_module8, run_module9
from src.report import run_module10, verify_exports
from src.visualize import run_visualizations

# ── Paths ─────────────────────────────────────────────────────────
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, "data", "student_dataset_v2.csv")
OUTPUT_DIR = os.path.join(BASE_DIR, "output")
CHARTS_DIR = os.path.join(BASE_DIR, "charts")


def run_full_pipeline(data_path: str = DATA_PATH) -> None:
    """Run the complete Module 1 → Module 11 pipeline end to end."""
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    os.makedirs(CHARTS_DIR, exist_ok=True)

    print("\n" + "█" * 65)
    print("  STUDENT PERFORMANCE DATA HANDLING & ANALYSIS SYSTEM")
    print("█" * 65)

    # Module 1: Load
    df_raw = run_module1(data_path)

    # Module 2: Inspect
    run_module2(df_raw)

    # Module 3: Clean
    df_clean = run_module3(df_raw, os.path.join(OUTPUT_DIR, "cleaned_data.csv"))

    # Module 4: Transform
    df_transformed = run_module4(df_clean)

    # Module 5: Filter
    run_module5(df_transformed, OUTPUT_DIR)

    # Module 6: Analyze
    run_module6(df_transformed)

    # Module 7: Sort
    run_module7(df_transformed)

    # Module 8: Group
    run_module8(df_transformed)

    # Module 9: Statistics
    run_module9(df_transformed)

    # Module 10: Report
    run_module10(df_transformed, OUTPUT_DIR)

    # Module 11: Export verification
    verify_exports(OUTPUT_DIR)

    # BONUS: Visualizations
    run_visualizations(df_transformed, CHARTS_DIR)

    print("█" * 65)
    print("  ✓ PIPELINE COMPLETE — all outputs saved to /output and /charts")
    print("█" * 65 + "\n")


# ════════════════════════════════════════════════════════════════
#  BONUS: Interactive Menu-Driven Application
# ════════════════════════════════════════════════════════════════

def interactive_menu() -> None:
    """
    BONUS feature: a simple menu-driven interface that lets the user
    run the full pipeline, or load a different CSV file dynamically (BONUS).
    """
    print("\n" + "=" * 65)
    print("  STUDENT PERFORMANCE SYSTEM — INTERACTIVE MENU")
    print("=" * 65)
    print("""
  1. Run full pipeline (default dataset)
  2. Load a different CSV file and run full pipeline
  3. Exit
""")
    choice = input("  Enter your choice (1-3): ").strip()

    if choice == "1":
        run_full_pipeline(DATA_PATH)
    elif choice == "2":
        custom_path = input("  Enter path to your CSV file: ").strip()
        if os.path.exists(custom_path):
            run_full_pipeline(custom_path)
        else:
            print(f"  ✗ File not found: {custom_path}")
    elif choice == "3":
        print("  Exiting. Goodbye!")
    else:
        print("  Invalid choice. Please run again.")


if __name__ == "__main__":
    if "--menu" in sys.argv:
        interactive_menu()
    else:
        run_full_pipeline()
