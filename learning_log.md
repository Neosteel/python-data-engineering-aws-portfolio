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

build_report_for_range_rows()

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

## Latest Update – CSV Pipeline & CLI Tool

### Data Pipeline Built
Implemented a complete structured Python data pipeline:

sales_with_data.csv
↓
convert_csv_to_list()
↓
previous_month_range()
↓
build_report_for_range()
↓
write_report()
↓
sales_report.csv

### Key Concepts Learned

- Reading CSV files using `csv.DictReader`
- Converting CSV rows into `list[dict]`
- Date handling using `datetime` and `timedelta`
- Calculating previous calendar month range dynamically
- Filtering rows using datetime comparisons
- Computing derived values (revenue = price × quantity)
- Writing CSV reports using `csv.DictWriter`

### Code Architecture Improvements

Refactored script into reusable functions:

- `convert_csv_to_list()`
- `previous_month_range()`
- `build_report_for_range()`
- `write_report()`
- `main()`

Learned professional Python script structure:

## Latest Update (CSV + Datetime Pipeline - Advanced)

- Built dynamic CSV reporting pipeline using CLI arguments (`sys.argv`)
- Implemented multiple reporting modes:
  - `prev_month`
  - `last_30_days`
- Learned how to design flexible pipelines using mode-based logic

- Created reusable function:
  - `build_report_for_range` (generic date-range processing)

- Implemented robust error handling:
  - Used `try/except` for date parsing
  - Used `try/except` for numeric conversion (quantity, price)
  - Skipped invalid rows safely instead of crashing

- Added data quality tracking:
  - `invalid_count` to track bad rows
  - Printed invalid row summary in output

- Learned real-world pipeline design concepts:
  - Happy path vs difficult path handling
  - Defensive programming for messy data
  - Importance of not breaking pipeline due to bad records

- Improved CLI design:
  - Mode-based execution
  - Input/output file arguments
  - Safe exit using `sys.exit(1)`

- Practiced real-world testing:
  - Injected invalid data into CSV
  - Verified pipeline robustness

## Current Status
- Strong foundation in:
  - CSV processing
  - datetime handling
  - function-based pipelines
  - CLI tools
  - error handling

## Next Topics
- argparse (professional CLI handling)
- Data validation patterns (advanced)
- Introduction to pandas (structured data processing)
- SQL integration with Python


# Learning Log

## Current Project
Sales Reporting Tool (CLI + Data Pipeline)

## Current File
sales_reporting_tool.py

## Dataset
sales_project_data.csv

## What I completed
- Built CSV pipeline using Python
- Added argparse CLI
- Handled invalid data using try/except
- Started learning pandas basics
- Created numeric cleaning using pd.to_numeric

## Current Topic
Pandas fundamentals (DataFrame, cleaning, filtering)

## Next Step
- Build project from scratch using new dataset
- Start with loading CSV and basic structure

## Key Learnings
- DataFrame is like a table (Excel in Python)
- df["col"] vs df[["col1","col2"]]
- errors="coerce" converts bad values to NaN

## Questions / Confusions
- pandas syntax still confusing
- need more clarity on filtering and transformations

## Latest Session
- Created project folder structure for sales_reporting_tool
- Added input/sales_project_data.csv
- Built load_sales_data(file_path) using csv.DictReader
- Confirmed CSV loads as a list of dictionaries
- Built clean_sales_data(rows)
- Converted:
  - order_id -> int
  - quantity -> int
  - price -> float
  - date -> datetime using datetime.strptime(...)
- Used try/except ValueError to skip bad rows instead of crashing
- Verified invalid row count = 2
- Understood that try/except here mainly protects conversion errors
- Next step: write filter_sales_data(rows, mode, reference_date)

## Current File
sales_reporting_tool.py

## Next Topic
Build filter_sales_data(rows, mode, reference_date)

## Resume From
Start by writing filter_sales_data() for:
- prev_month
- last_30_days
Then test filtered output before moving to revenue calculations.

## Latest Session
- Created sales_reporting_tool project folder with input and output folders
- Added sales_project_data.csv into input/
- Built load_sales_data(file_path) using csv.DictReader
- Confirmed CSV loads as list of dictionaries
- Built clean_sales_data(rows)
- Converted:
  - order_id -> int
  - quantity -> int
  - price -> float
  - date -> datetime using datetime.strptime()
- Used try/except ValueError to skip bad rows without crashing
- Verified invalid row count = 2
- Pushed current sales_reporting_tool progress to GitHub
- Next step is to write filter_sales_data(rows, mode, reference_date)

## Current File
sales_reporting_tool/sales_reporting_tool.py

## Next Topic
Build filter_sales_data(rows, mode, reference_date)

## Resume From
Start with filter_sales_data() for:
- prev_month
- last_30_days
Then test filtered rows before moving to revenue calculations.

## Latest Session
- Refactored sales_reporting_tool.py into a cleaner structure
- Kept all function definitions at the top
- Kept execution logic at the bottom
- Removed noisy row-by-row debug printing
- Renamed unclear variable names for cleaner readability
- Confirmed final summary output:
  - Invalid row count = 2
  - Previous month total revenue = 1900.0
  - Last 30 days total revenue = 3975.0
- Confirmed revenue by product and revenue by customer outputs are correct
- Confirmed output/prev_month_report.csv and output/last_30_days_report.csv are written correctly

## Current File
sales_reporting_tool/sales_reporting_tool.py

## Next Topic
Add simple user mode selection or refactor further for portfolio quality

## Resume From
Decide next improvement:
- option 1: add user input for mode selection
- option 2: refactor into class-based version for learning OOP
- option 3: push current version to GitHub first

