import csv
from datetime import datetime

def load_transactions(file_path: str) -> list[dict]:
    """Load transactions from a CSV file."""
    transactions = []
    with open(file_path, "r",newline="", encoding="utf-8") as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            row["amount"] = float(row["amount"])
            transactions.append(row)
    return transactions
def filter_by_month(transactions: list[dict], year_month: str) -> list[dict]:
    """Filter transactions by month, using YYYY-MM format."""
    filtered = []
    for transaction in transactions:
        transaction_date = datetime.strptime(transaction["date"], "%Y-%m-%d")
        if transaction_date.strftime("%Y-%m") == year_month:
            filtered.append(transaction)
    return filtered
def calculate_total(transactions: list[dict], transaction_type: str) -> float:
    """Calculate total income or expense."""
    return sum(
        transaction["amount"]
        for transaction in transactions
        if transaction["type"] == transaction_type
    )
def summarize_expense_by_category(transactions: list[dict]) -> dict[str, float]:
    """Summarize expense by category."""
    summary = {}
    for transaction in transactions:
        if transaction["type"] == "expense":
            category = transaction["category"]
            summary[category] = summary.get(category, 0) + transaction["amount"]
    return summary
def generate_monthly_report(transactions: list[dict], year_month: str) -> str:
    """Generate a monthly budget report."""
    monthly_transactions = filter_by_month(transactions, year_month)
    total_income = calculate_total(monthly_transactions, "income")
    total_expense = calculate_total(monthly_transactions, "expense")
    balance = total_income - total_expense
    expense_summary = summarize_expense_by_category(monthly_transactions)
    lines = [
        f"Monthly Budget Report - {year_month}",
        "-"* 35,
        f"Total income: {total_income:,.2f}",
        f"Total expenses: {total_expense:,.2f}",
        f"Balance: {balance:,.2f}",
        "",
        "Expense by category:",
    ]
    if expense_summary:
        for category, amount in sorted(expense_summary.items()):
            lines.append(f"- {category}: {amount:,.2f}")
    else:
        lines.append("-No expenses found")
    return"\n".join(lines)
def save_report(report_text: str, output_file: str) -> None:
    """Save report text to a file."""
    with open(output_file, "w", encoding="utf-8") as file:
        file.write(report_text)

        