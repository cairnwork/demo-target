from datetime import date
from decimal import Decimal

import pytest

from tinyledger.parse import Transaction, parse_csv

SAMPLE = """date,amount,memo
2026-01-02,1000.00,Salary
2026-01-05,-42.50,Groceries
2026-01-09,-1,Coffee
"""


def test_parses_rows():
    assert parse_csv(SAMPLE) == [
        Transaction(date(2026, 1, 2), Decimal("1000.00"), "Salary"),
        Transaction(date(2026, 1, 5), Decimal("-42.50"), "Groceries"),
        Transaction(date(2026, 1, 9), Decimal("-1"), "Coffee"),
    ]


def test_empty_and_header_only_input_yield_no_rows():
    assert parse_csv("") == []
    assert parse_csv("date,amount,memo\n") == []


def test_blank_lines_are_skipped():
    rows = parse_csv("date,amount,memo\n\n2026-01-02,5.00,x\n   \n")
    assert [r.memo for r in rows] == ["x"]


def test_bad_header_and_field_count_are_rejected():
    with pytest.raises(ValueError, match="unexpected header"):
        parse_csv("day,amt\n2026-01-01,1\n")
    with pytest.raises(ValueError, match="line 2"):
        parse_csv("date,amount,memo\n2026-01-01,1\n")
