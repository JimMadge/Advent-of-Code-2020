import pytest
from ..day1 import expense_report

test_entries = [1721, 979, 366, 299, 675, 1456]
test_data = [
    (test_entries, 2, 514579),
    (test_entries[1:], 2, None),
    (test_entries, 3, 241861950)
]


@pytest.mark.parametrize("entries,number,result", test_data)
def test_expense_report(entries, number, result):
    assert expense_report(entries, number=number) == result
