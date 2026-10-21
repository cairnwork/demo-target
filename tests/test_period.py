from datetime import date

from tinyledger.period import in_period, parse_date


def test_parse_date_and_day_inside_period():
    assert parse_date(" 2026-02-14 ") == date(2026, 2, 14)
    assert in_period(date(2026, 2, 15), date(2026, 2, 1), date(2026, 2, 28))


def test_open_bounds_and_days_well_outside_period():
    assert in_period(date(1999, 1, 1), None, None)
    assert not in_period(date(2026, 1, 31), date(2026, 2, 1), date(2026, 2, 28))
    assert not in_period(date(2026, 3, 15), date(2026, 2, 1), date(2026, 2, 28))
