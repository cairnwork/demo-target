"""Plain-text period report."""

from __future__ import annotations

from datetime import date

from .ledger import Ledger
from .money import format_amount


def render_report(ledger: Ledger, start: date, end: date) -> str:
    rows = ledger.between(start, end)
    rule = "-" * 44
    lines = [f"Report {start.isoformat()} .. {end.isoformat()}", rule]
    for txn in rows:
        lines.append(f"{txn.day.isoformat()}  {format_amount(txn.amount):>12}  {txn.memo}")
    lines.append(rule)
    total = ledger.total_between(start, end)
    lines.append(f"Total {format_amount(total):>12}")
    lines.append(f"Count: {len(rows)}")
    return "\n".join(lines) + "\n"
