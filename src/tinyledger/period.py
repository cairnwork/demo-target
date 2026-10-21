"""Date helpers for reporting periods."""

from __future__ import annotations

from datetime import date


def parse_date(text: str) -> date:
    """Parse an ISO date such as 2026-02-14."""
    return date.fromisoformat(text.strip())


def in_period(day: date, start: date | None, end: date | None) -> bool:
    """Return True when start <= day <= end. A None bound is open."""
    if start is not None and day < start:
        return False
    if end is not None and day > end:
        return False
    return True
