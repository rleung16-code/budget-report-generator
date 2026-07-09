# Budget Report Generator
A Python tool that generates monthly budget reports from CSV transactions data.
This project reads income and expense records from a CSV file,filters transactions by month, calculate totals, summarize expense by category, and saves a text report.
## Features
- Load transactions from a CSV file
- Filter transactions by month
- Calculate total income
- Calculate total expenses
- Calculate monthly balance
- Summarize expenses by category
- Generate a monthly text report
- Save the report to a'.txt'file
- Includes unit tests
## Project files
- 'main.py' - Runs the report generator
- 'report.py' - Contains the core report logic
- 'sample_transacrions.csv' - Sample transaction data
- 'test/test_report.py' - Unit tests
- '.gitignore' - Excludes generated and local files
- 'monthly_report.txt' - Generated report file, not upload to GitHub
## How to run 

```bash
python main.py
```

When promoted, enter a month in this format:

```text
2026-07
```
## Example output

```text
Monthly Budget Report - 2026-07
-----------------------------------
Total income: 27,000.00
Total expenses: 8,203.00
Balance: 18,797.00
 
Expense by category:
- Food:185.00
- Rent:8,000.00
- Transport: 18.00

Report saved to monthly_report.txt
```

## How to run tests

```bash
python -m unittest discover -s tests -p test_*.py -v
```

Expected result:

```text
Ran 7 tests
OK
```

## Notes

'monthly_report.txt' is generated when the program runs and is not uploaded to GitHub

- '