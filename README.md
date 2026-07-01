# Student Performance Data Handling and Analysis System

A complete data-handling pipeline built with **Pandas** that loads, inspects,
cleans, transforms, filters, analyzes, and reports on student performance
data — covering the full data lifecycle end-to-end.

## Project Structure

```
Student_Data_Project/
├── data/
│   └── student_dataset_v2.csv        # Raw input dataset (100 records)
├── output/
│   ├── cleaned_data.csv              # Cleaned dataset
│   ├── toppers.csv                   # Top 10 performers
│   ├── failed_students.csv           # Students who failed
│   ├── low_attendance_students.csv   # Attendance < 75%
│   ├── high_study_hours_students.csv # Study hours > 8
│   ├── report.csv                    # Final summary report
│   └── report.xlsx                   # Final report (Excel, bonus)
├── charts/                           # Bonus Matplotlib visualizations
│   ├── grade_distribution.png
│   ├── marks_histogram.png
│   ├── attendance_vs_marks.png
│   ├── top10_performance.png
│   └── correlation_heatmap.png
├── src/
│   ├── load_data.py                  # Module 1
│   ├── clean_data.py                 # Modules 2 & 3
│   ├── transform.py                  # Modules 4 & 5
│   ├── analyze.py                    # Modules 6, 7, 8, 9
│   ├── report.py                     # Modules 10 & 11
│   └── visualize.py                  # Bonus: charts
├── main.py                           # Orchestrates the full pipeline
└── README.md
```

## How to Run

**Run the full pipeline (recommended):**
```bash
cd Student_Data_Project
python main.py
```

**Run the interactive menu (bonus feature):**
```bash
python main.py --menu
```
This lets you choose to run the default dataset or load any CSV file
dynamically.

## Dataset

`student_dataset_v2.csv` contains 100 records with the following columns:

| Column        | Description                          |
|---------------|---------------------------------------|
| Student_ID    | Unique student identifier             |
| Student_Name  | Full name                             |
| Study_Hours   | Average daily study hours             |
| Attendance    | Attendance percentage                 |
| Marks         | Final examination marks (0-100)       |

The raw dataset intentionally contains realistic data-quality issues —
**5 duplicate rows**, **8 missing values**, and **6 invalid entries**
(negative or out-of-range values) — so that the cleaning logic in Module 3
has real problems to solve and demonstrate.

## Module Summary

| Module | Description |
|--------|-------------|
| 1. Data Loading | Read CSV, preview head/tail, shape, columns, dtypes |
| 2. Data Inspection | Missing values, duplicates, descriptive stats, memory, info |
| 3. Data Cleaning | Remove duplicates, handle missing values, validate ranges → `cleaned_data.csv` |
| 4. Data Transformation | Add `Grade`, `Result`, `Performance_Score` columns |
| 5. Data Filtering | Toppers, failed students, low attendance, high study hours → CSVs |
| 6. Data Analysis | Average/highest/lowest marks, pass/fail %, grade distribution |
| 7. Sorting | By Marks, Attendance, Study Hours |
| 8. Grouping | Average marks/attendance & counts by Grade (`groupby`) |
| 9. Statistical Analysis | Mean, median, mode, std dev, variance, correlation matrix |
| 10. Report Generation | Final consolidated report → `report.csv` (+ `.xlsx` bonus) |
| 11. Export Data | Verifies and lists all generated output files |

## Design Decisions

- **Missing value handling**: numeric columns (`Study_Hours`, `Attendance`,
  `Marks`) are imputed with the column **median** (robust to outliers);
  rows missing `Student_Name` are dropped since identity cannot be imputed.
- **Validation ranges**: `Marks` and `Attendance` must be within `0-100`;
  `Study_Hours` must be within `0-24` (a realistic daily cap).
- **Grading scale**: A (90-100), B (75-89), C (60-74), D (45-59), F (<45).
- **Pass mark**: 40 — students scoring 40 or above are marked `Pass`.
- **Performance Score**: a weighted composite —
  `0.5×Marks + 0.3×Attendance + 0.2×(normalized Study_Hours)`,
  where Study_Hours is normalized to a 0-100 scale against a 12-hour cap
  so it can be fairly combined with the other two metrics.

## Bonus Tasks Completed

- ✅ Visualizations using Matplotlib (5 charts: grade distribution, marks
  histogram, attendance-vs-marks scatter, top-10 performance bar chart,
  correlation heatmap)
- ✅ Interactive menu-driven application (`python main.py --menu`)
- ✅ Dynamic CSV loading (choose any file path via the menu)
- ✅ Reports exported in both CSV and Excel (`.xlsx`) formats
- ✅ Top 10 students by Performance Score displayed and charted

## Requirements

```
pandas
matplotlib
openpyxl
```

Install with:
```bash
pip install pandas matplotlib openpyxl
```

## Author Notes

This project follows a modular structure with each pipeline stage isolated
into its own file under `src/`, all orchestrated from `main.py`. Every
function includes a docstring describing its purpose, parameters, and
return value, in line with good code-documentation practice.
