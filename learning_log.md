# Python + Data Engineering + AWS Learning Log

## Environment
- OS: macOS (M1)
- Python: 3.11.7
- Virtual Env: venv
- Editor: VS Code

## Progress Completed
- Day 1: Computer basics, Terminal, print()
- Day 2: Files, folders, running .py files
- Day 3: Variables, assignment, case sensitivity
- Day 4: Data types (pending practical)

## Key Rules Learned
- Always activate venv before work
- `=` is assignment, `==` is comparison
- Python is case-sensitive

## Current File
- day_2_basics.py

## Next Topic
- Numbers vs Strings

## Progress Update (Latest Session)
- Learned conditionals (`if / elif / else`)
- Learned `try / except` for safe input handling
- Understood silent bugs vs crashes
- Learned how to design functions properly
- Implemented:
  - `convert_to_int` / `to_int_or_none`
  - `pipeline_status`
  - `pipeline_status_v2`
- Learned why functions take parameters like `raw`
- Learned separation of raw vs processed data
- Solved multiple real-world pipeline validation problems

## Current Status
- Functions: completed (basic + real-world validation

## Latest Update
- Introduced data structures concept
- Understood what lists solve vs single variables
- Learned real-world use cases: batch processing, looping, data cleanup
- Ready to start Python lists (coding)


- Refactored batch-cleaning logic into a reusable function
- Learned correct placement of return statements
- Understood why return must be outside loops
- Built real-world list processing logic

## Latest Update
- Consolidated loops, functions, try/except, continue
- Built real-world batch validation logic
- Implemented pipeline decision logic with thresholds
- Practiced debugger-style tracing of code execution
- Ready to start dictionaries (records & structured data)

Factorial (iterative, accumulator pattern)

Palindrome (reverse + compare, index logic)

First non-repeating character (nested loops, counting logic)

Reverse a number ( % 10, // 10, accumulator)

Add this (copy/paste):

CSV Step 1: Created raw_sales.csv and read it using csv.DictReader

Understood: CSV → list of dicts, each loop variable r is one row dict

Step 2: Inspected real data problems: empty strings, non-numeric values, missing email

Step 3: Built cleaning function with:

validation first (isdigit, missing email)

continue to skip invalid rows

normalization: convert numeric strings to int

counted invalid rows (got invalid = 3, clean rows = 3)

Learned CSV writing concepts:

DictWriter(fieldnames=...) defines schema

missing key → blank cell

extra key → crash (schema enforcement)

“silent ignore” can cause data corruption\



date: feb 17 2026

🔄 Latest Session Update — Datetime + Reporting Pipeline
CSV + Datetime Integration (Major Milestone)

Step 1 — Structured CSV Processing

Read sales_with_data.csv using csv.DictReader

Understood difference between:

Raw text (f.read())

Structured rows (list of dictionaries)

Learned that CSV values are always strings

Practiced accessing row fields using r["column_name"]

Step 2 — Datetime Fundamentals

Learned datetime.strptime() (string → datetime object)

Understood difference between:

strptime (parse string)

strftime (format datetime to string)

Learned .weekday() and weekday numbering (Mon=0, Sun=6)

Practiced:

Date comparison (>=, <=)

Date subtraction using timedelta(days=n)

Difference between rolling window vs calendar month

Step 3 — Rolling Window Revenue (Last 30 Days)

Implemented:

cutoff = today - timedelta(days=30)

Filtered rows using:

sale_date >= cutoff

Learned accumulator pattern correctly:

Initialize total BEFORE loop

Update inside loop

Built working revenue calculation for last 30 days

Step 4 — Previous Calendar Month Logic (Advanced Date Handling)

Understood difference:

Last 30 days ≠ Previous calendar month

Implemented automatic month boundary detection:

first_day_of_month = today.replace(day=1)

previous_month_end = first_day_of_month - timedelta(days=1)

previous_month_start = previous_month_end.replace(day=1)

Learned inclusive range filtering:

start <= sale_date <= end

Successfully computed February revenue (1250)

Step 5 — Report Generation (Professional Output)

Created derived column: revenue

Built filtered dataset report_rows

Used csv.DictWriter to generate:

sales_report.csv

Learned:

"w" mode auto-creates file

writeheader() required

Fieldnames define schema

Successfully exported structured monthly report

Core Concepts Reinforced

Accumulator pattern (never reset inside loop)

Date range filtering logic

Data pipeline structure:

Ingest → Transform → Filter → Aggregate → Output

Importance of schema enforcement in CSV writing

Why month boundaries must be computed, not hardcoded

Handling leap years automatically

Architectural Thinking Gained

Difference between:

Rolling window analytics

Calendar-based reporting (finance logic)

Understood how real systems compute:

Monthly reports

Revenue dashboards

Time-based KPIs

Refactoring Phase (Started)

Introduced function-based pipeline structure:

load_sales()

prev_month_range()

build_prev_month_report_rows()

write_report()

Introduced main() execution pattern

Began moving toward reusable, production-style code

Status Now

Comfortable with CSV ingestion

Comfortable with datetime arithmetic

Able to build filtered reporting pipelines

Ready to:

Parameterize reports (CLI arguments)

Add analytics (Top N products/customers)

Move toward automation-ready workflows

Tomorrow Focus:

Finalize function-based refactor

Add parameter support (dynamic month selection)

Begin automation design thinking