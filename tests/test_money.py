from decimal import Decimal

import pytest

from tinyledger.money import format_amount, parse_amount, quantize_cents


def test_parse_amount_accepts_commas_and_rejects_garbage():
    assert parse_amount(" 1,234.50 ") == Decimal("1234.50")
    with pytest.raises(ValueError, match="invalid amount"):
        parse_amount("12.3.4")


def test_quantize_drops_sub_cent_digits():
    assert quantize_cents(Decimal("1.234")) == Decimal("1.23")
    assert quantize_cents(Decimal("1.236")) == Decimal("1.24")


def test_format_groups_thousands_and_keeps_sign():
    assert format_amount(Decimal("1234.5")) == "1,234.50"
    assert format_amount(Decimal("-42.5")) == "-42.50"
