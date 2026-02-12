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

“silent ignore” can cause data corruption