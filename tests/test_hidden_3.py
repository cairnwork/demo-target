"""Hidden check for demo issue 3: the balance before the first transaction is zero."""

from datetime import date
from decimal import Decimal

from tinyledger.ledger import Ledger
from tinyledger.parse import Transaction


def _ledger():
    return Ledger([
        Transaction(date(2026, 1, 2), Decimal("1000.00"), "Salary"),
        Transaction(date(2026, 1, 5), Decimal("-42.50"), "Groceries"),
    ])


def test_day_before_first_transaction_is_zero():
    got = _ledger().balance_as_of(date(2025, 12, 31))
    assert got == Decimal("0.00"), f"no transactions yet, expected 0.00 but got {got}"


def test_empty_ledger_is_zero_on_any_day():
    got = Ledger([]).balance_as_of(date(2026, 1, 1))
    assert got == Decimal("0"), f"empty ledger, expected 0 but got {got}"


def test_first_transaction_day_includes_it():
    assert _ledger().balance_as_of(date(2026, 1, 2)) == Decimal("1000.00")


def test_later_day_is_the_running_balance():
    assert _ledger().balance_as_of(date(2026, 1, 31)) == Decimal("957.50")
