# Copilot Instructions for Expense Tracker Project

## Project Overview
- **Single-file Python CLI app** for tracking expenses, using a CSV file for persistent storage.
- Main logic is in [Test.py](../Test.py). Data is stored in `expenses.csv`.

## Architecture & Data Flow
- **No external dependencies** beyond Python standard library (`csv`, `os`).
- All user interaction is via command-line prompts.
- Data is loaded from `expenses.csv` at startup and saved after each addition.
- Expense records are dictionaries with fields: `name`, `amount`, `category`.

## Key Functions & Patterns
- `load_expenses()`: Reads all expenses from CSV into a list of dicts.
- `save_expenses(expenses)`: Writes the list of dicts back to CSV.
- `add_expense(expenses)`: Prompts user for details, appends to list, saves.
- `list_expenses(expenses)`: Prints a formatted table of all expenses.
- `main()`: CLI loop for user actions (add, list, exit).

## Developer Workflows
- **Run the app:** `python Test.py`
- **No build step or tests** currently present.
- **Debugging:** Add print statements or use a Python debugger.

## Project Conventions
- All code is in a single file; no modules or packages.
- CSV file is always named `expenses.csv` and must be in the same directory as the script.
- All fields are stored as strings in the CSV.
- Minimal error handling; invalid input may cause exceptions or be ignored.

## Extending the Project
- To add new fields, update `FIELDS`, CSV handling, and prompts.
- For new commands, add to the CLI menu in `main()` and implement as new functions.

## Example: Adding an Expense
```python
add_expense(expenses)  # Prompts for name, amount, category, saves to CSV
```

## Key Files
- [Test.py](../Test.py): All logic and CLI
- [expenses.csv](../expenses.csv): Data storage (created automatically)

---
For questions or improvements, update this file to keep agent guidance current.
