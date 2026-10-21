from datetime import date
from decimal import Decimal

from tinyledger.ledger import Ledger
from tinyledger.parse import Transaction


def make_ledger():
    return Ledger([
        Transaction(date(2026, 1, 9), Decimal("-1.00"), "Coffee"),
        Transaction(date(2026, 1, 2), Decimal("1000.00"), "Salary"),
        Transaction(date(2026, 1, 5), Decimal("-42.50"), "Groceries"),
        Transaction(date(2026, 2, 3), Decimal("-300.00"), "Rent"),
    ])


def test_sorts_by_date_and_sums_balance():
    ledger = make_ledger()
    days = [t.day for t in ledger]
    assert days == sorted(days)
    assert ledger.balance() == Decimal("656.50")


def test_balance_as_of_on_and_between_transaction_days():
    ledger = make_ledger()
    assert ledger.balance_as_of(date(2026, 1, 5)) == Decimal("957.50")
    assert ledger.balance_as_of(date(2026, 1, 6)) == Decimal("957.50")
    assert ledger.balance_as_of(date(2026, 12, 31)) == Decimal("656.50")


def test_between_and_total_for_mid_range_period():
    ledger = make_ledger()
    txns = ledger.between(date(2026, 1, 3), date(2026, 1, 31))
    assert [t.memo for t in txns] == ["Groceries", "Coffee"]
    assert ledger.total_between(date(2026, 1, 1), date(2026, 1, 31)) == Decimal("956.50")
