# tinyledger

A small ledger written with the Python standard library only. It parses CSV
transactions, computes running balances, totals transactions for an inclusive
date period, and renders a plain-text report.

This repository is the **demo target** for Cairnwork's five-minute demonstration.
It is an ordinary Python project. Known problems are tracked as GitHub Issues,
not documented here.

## Layout

- `src/tinyledger/money.py`: amount parsing, cent rounding, display formatting
- `src/tinyledger/period.py`: ISO date parsing and period membership
- `src/tinyledger/parse.py`: CSV reader (`date,amount,memo`)
- `src/tinyledger/ledger.py`: ordering, balances, period queries
- `src/tinyledger/report.py`: plain-text period report
- `tests/`: public unit tests

## Usage

```python
from datetime import date
from tinyledger import Ledger, parse_csv, render_report

text = "date,amount,memo\n2026-01-02,1000.00,Salary\n2026-01-05,-42.50,Groceries\n"
ledger = Ledger(parse_csv(text))
print(render_report(ledger, date(2026, 1, 1), date(2026, 1, 31)))
```

## Conventions

- Amounts are `decimal.Decimal` values and are displayed with two decimal places.
- Reporting periods include both their start and end dates.
- Money is never stored as a float.

## Development

```
python3 -m pip install pytest
python3 -m pytest -q tests
```

No runtime dependencies are needed. `pytest` is only needed to run the tests.
