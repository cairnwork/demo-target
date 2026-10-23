from datetime import date
from decimal import Decimal

from tinyledger.parse import Transaction, parse_csv


def test_header_with_utf8_bom_is_accepted():
    text = "﻿date,amount,memo\n2026-01-02,1000.00,Salary\n"
    assert parse_csv(text) == [Transaction(date(2026, 1, 2), Decimal("1000.00"), "Salary")]


def test_bom_only_affects_the_header():
    text = "﻿date,amount,memo\n2026-01-05,-42.50,Groceries\n"
    assert [t.memo for t in parse_csv(text)] == ["Groceries"]
