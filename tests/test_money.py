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


def test_non_finite_amounts_are_rejected():
    import pytest

    from tinyledger.money import parse_amount

    for text in ["NaN", "nan", " NaN ", "-NaN", "sNaN", "Infinity", "inf", "-Infinity", "+INF"]:
        with pytest.raises(ValueError, match="invalid amount"):
            parse_amount(text)


def test_finite_amounts_still_parse_after_the_check():
    from decimal import Decimal

    from tinyledger.money import parse_amount

    assert parse_amount("1,234.00") == Decimal("1234.00")
    assert parse_amount(" -3 ") == Decimal("-3")
    assert parse_amount("12.5") == Decimal("12.5")
    assert parse_amount("0") == Decimal("0")
    assert parse_amount("-0.01") == Decimal("-0.01")


def test_csv_row_with_non_finite_amount_is_rejected():
    import pytest

    from tinyledger.parse import parse_csv

    with pytest.raises(ValueError, match="invalid amount"):
        parse_csv("date,amount,memo\n2026-01-02,5.00,ok\n2026-01-03,Infinity,bad\n")
