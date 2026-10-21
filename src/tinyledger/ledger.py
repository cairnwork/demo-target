"""In-memory ledger: ordering, running balances and period queries."""

from __future__ import annotations

import bisect
from datetime import date
from decimal import Decimal

from .money import ZERO
from .parse import Transaction
from .period import in_period


class Ledger:
    def __init__(self, transactions=()) -> None:
        self._txns: list[Transaction] = sorted(transactions, key=lambda t: t.day)
        self._dates = [t.day for t in self._txns]
        # _running[i] is the balance after the first i transactions.
        self._running: list[Decimal] = [ZERO]
        for txn in self._txns:
            self._running.append(self._running[-1] + txn.amount)

    def __len__(self) -> int:
        return len(self._txns)

    def __iter__(self):
        return iter(self._txns)

    def balance(self) -> Decimal:
        return self._running[-1]

    def balance_as_of(self, day: date) -> Decimal:
        """Balance after every transaction dated on or before `day`."""
        count = bisect.bisect_right(self._dates, day)
        if count == 0:
            return self._running[-1]
        return self._running[count]

    def between(self, start: date, end: date) -> list[Transaction]:
        return [t for t in self._txns if in_period(t.day, start, end)]

    def total_between(self, start: date, end: date) -> Decimal:
        return sum((t.amount for t in self.between(start, end)), ZERO)
