from datetime import date

from tinyledger.ledger import Ledger
from tinyledger.parse import parse_csv
from tinyledger.report import render_report

SAMPLE = """date,amount,memo
2026-01-02,1000.00,Salary
2026-01-05,-42.50,Groceries
2026-01-09,-1,Coffee
2026-02-03,-300.00,Rent
"""


def test_report_lists_january_rows_total_and_count():
    text = render_report(Ledger(parse_csv(SAMPLE)), date(2026, 1, 1), date(2026, 1, 31))
    assert "Salary" in text and "Groceries" in text and "Coffee" in text
    assert "Rent" not in text
    assert "Total       956.50" in text
    assert "Count: 3" in text
