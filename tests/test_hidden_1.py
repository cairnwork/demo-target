"""Hidden check for demo issue 1: the period end date is inclusive."""

from datetime import date
from decimal import Decimal

from tinyledger.ledger import Ledger
from tinyledger.parse import Transaction
from tinyledger.period import in_period
from tinyledger.report import render_report

END = date(2026, 3, 31)


def test_last_day_of_period_is_included():
    assert in_period(END, date(2026, 3, 1), END), "a day equal to the period end must be included"


def test_first_day_of_period_is_included():
    assert in_period(date(2026, 3, 1), date(2026, 3, 1), END), "a day equal to the period start must be included"


def test_day_after_period_end_is_excluded():
    assert not in_period(date(2026, 4, 1), date(2026, 3, 1), END), "a day after the period end must be excluded"


def test_ledger_between_includes_transaction_on_end_date():
    ledger = Ledger([Transaction(END, Decimal("12.00"), "Last day")])
    memos = [t.memo for t in ledger.between(date(2026, 3, 1), END)]
    assert memos == ["Last day"], f"transaction dated on the period end is missing, got {memos!r}"


def test_report_includes_end_date_row():
    ledger = Ledger([Transaction(END, Decimal("12.00"), "Last day")])
    text = render_report(ledger, date(2026, 3, 1), END)
    assert "Last day" in text, "report omits the transaction dated on the period end"
    assert "Count: 1" in text, "report count omits the transaction dated on the period end"
