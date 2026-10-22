"""Hidden check for demo issue 2: display rounding is half up to the cent."""

from decimal import Decimal

from tinyledger.money import format_amount, quantize_cents


def test_exact_half_cent_rounds_up():
    assert quantize_cents(Decimal("0.125")) == Decimal("0.13"), "0.125 should round up to 0.13"


def test_half_cent_rounds_up_when_previous_cent_is_even():
    assert quantize_cents(Decimal("2.345")) == Decimal("2.35"), "2.345 should round up to 2.35"


def test_half_cent_rounds_up_across_a_whole_unit():
    assert quantize_cents(Decimal("10.005")) == Decimal("10.01"), "10.005 should round up to 10.01"


def test_below_half_cent_rounds_down():
    assert quantize_cents(Decimal("0.124")) == Decimal("0.12"), "0.124 should round down to 0.12"


def test_format_amount_uses_the_same_rule():
    assert format_amount(Decimal("0.145")) == "0.15", "format_amount(0.145) should print 0.15"
