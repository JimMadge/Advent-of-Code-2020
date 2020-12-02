from ..day2 import parse_line, valid_password, count_valid_passwords
import pytest

test_lines = [
    "1-3 a: abcde",
    "1-3 b: cdefg",
    "2-9 c: ccccccccc"
]


def test_parse_line():
    assert parse_line("1-3 a: abcde") == (1, 3, "a", "abcde")


test_data = zip(test_lines, [True, False, True])


@pytest.mark.parametrize("test_line,result", test_data)
def test_valid_password(test_line, result):
    assert valid_password(*parse_line(test_line)) == result


def test_count_valid_passwords():
    assert count_valid_passwords(test_lines) == 2
