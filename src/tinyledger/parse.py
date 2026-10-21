"""CSV reader for transactions. Expected header: date,amount,memo."""

from __future__ import annotations

import csv
import io
from dataclasses import dataclass
from datetime import date
from decimal import Decimal

from .money import parse_amount
from .period import parse_date

HEADER = ["date", "amount", "memo"]


@dataclass(frozen=True)
class Transaction:
    day: date
    amount: Decimal
    memo: str


def parse_csv(text: str) -> list[Transaction]:
    reader = csv.reader(io.StringIO(text))
    header = next(reader, None)
    if header is None:
        return []
    if [column.strip().lower() for column in header] != HEADER:
        raise ValueError(f"unexpected header: {header!r}")
    transactions = []
    for lineno, row in enumerate(reader, start=2):
        if not row or all(not cell.strip() for cell in row):
            continue
        if len(row) != 3:
            raise ValueError(f"line {lineno}: expected 3 fields, got {len(row)}")
        day_text, amount_text, memo = row
        transactions.append(
            Transaction(parse_date(day_text), parse_amount(amount_text), memo.strip())
        )
    return transactions
