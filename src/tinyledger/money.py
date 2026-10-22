"""Money helpers: parsing, cent rounding and display."""

from __future__ import annotations

from decimal import ROUND_HALF_UP, Decimal, InvalidOperation

ZERO = Decimal("0.00")
CENT = Decimal("0.01")


def parse_amount(text: str) -> Decimal:
    """Parse an amount such as '12.5', '-3' or '1,234.00'."""
    cleaned = text.strip().replace(",", "")
    if not cleaned:
        raise ValueError("empty amount")
    try:
        return Decimal(cleaned)
    except InvalidOperation as exc:
        raise ValueError(f"invalid amount: {text!r}") from exc


def quantize_cents(value: Decimal) -> Decimal:
    """Round a value to whole cents using the statement rule (half up)."""
    return value.quantize(CENT, rounding=ROUND_HALF_UP)


def format_amount(value: Decimal) -> str:
    """Format with thousands separators and exactly two decimal places."""
    return f"{quantize_cents(value):,.2f}"
