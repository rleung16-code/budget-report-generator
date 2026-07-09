from report import load_transactions, generate_monthly_report, save_report
DATA_FILE = "sample_transactions.csv"
OUTPUT_FILE = "monthly_report.txt"
def main():
    """Run the monthly budget report generator."""
    year_month = input("Enter month, for example 2026-07: ").strip()
    transactions = load_transactions(DATA_FILE)
    report_text = generate_monthly_report(transactions, year_month)
    print()
    print(report_text)
    save_report(report_text, OUTPUT_FILE)
    print(f"\nReport saved to {OUTPUT_FILE}")
if __name__ == "__main__":
    main()
    