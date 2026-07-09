import tempfile 
import unittest
from pathlib import Path
from report import (
    load_transactions,
    filter_by_month,
    calculate_total,
    summarize_expense_by_category,
    generate_monthly_report,
    save_report,
)
class TestReport(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.file_path = str(Path(self.temp_dir.name)/"transaction.csv")
        with open(self.file_path, "w", encoding="utf-8") as file:
            file.write(
                "date,type,category,description,amount\n"
                "2026-07-01,income,Salary,Monthly salary,25000\n"
                "2026-07-02,expense,Food,Lunch,65\n"
                "2026-07-03,expense,Transport,MTR,18\n"
                "2026-07-05,expense,Rent,Apartment rent,8000\n"
                "2026-07-06,expense,Food,Dinner,120\n"
                "2026-07-08,income,Freelance,Side project,2000\n"
                "2026-08-01,income,Salary,Monthly salary,25000\n"
                "2026-08-02,expense,Food,Lunch,70\n"
                "2026-08-05,expense,Rent,Apartment rent,8000\n"
            )
    def tearDown(self):
        self.temp_dir.cleanup()
    def test_load_transactions(self):
        transactions = load_transactions(self.file_path)
        self.assertEqual(len(transactions), 9)
        self.assertEqual(transactions[0]["category"], "Salary")
        self.assertEqual(transactions[0]["amount"], 25000.0)
    def test_filter_by_month(self):
        transactions = load_transactions(self.file_path)
        july_transactions = filter_by_month(transactions, "2026-07")
        self.assertEqual(len(july_transactions), 6)
    def test_calculate_total_income(self):
        transactions = load_transactions(self.file_path)
        july_transactions = filter_by_month(transactions, "2026-07")
        result = calculate_total(july_transactions, "income")
        self.assertEqual(result, 27000.0)
    def test_calculate_total_expense(self):
        transactions = load_transactions(self.file_path)
        july_transactions = filter_by_month(transactions, "2026-07")
        result = calculate_total(july_transactions, "expense")
        self.assertEqual(result, 8203.0)
    def test_summarize_expense_by_category(self):
        transactions = load_transactions(self.file_path)
        july_transactions = filter_by_month(transactions, "2026-07")
        result = summarize_expense_by_category(july_transactions)
        expected = {
            "Food": 185.0,
            "Rent": 8000.0,
            "Transport": 18.0
        }
        self.assertEqual(result, expected)
    def test_generate_monthly_report(self):
        transactions = load_transactions(self.file_path)
        report_text = generate_monthly_report(transactions, "2026-07")
        self.assertIn("Monthly Budget Report - 2026-07", report_text)
        self.assertIn("Total income: 27,000.00", report_text)
        self.assertIn("Total expenses: 8,203.00", report_text)
        self.assertIn("Balance: 18,797.00", report_text)
    def test_save_report(self):
        output_file = str(Path(self.temp_dir.name)/"monthly_report.txt")
        save_report("Test report", output_file)
        with open(output_file, "r", encoding="utf-8") as file:
            content = file.read()
        self.assertEqual(content, "Test report")
if __name__ == "__main__":
    unittest.main()