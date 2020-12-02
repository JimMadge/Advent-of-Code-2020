from ..day2 import (parse_line, valid_password1, valid_password2,
                    count_valid_passwords)
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
def test_valid_password1(test_line, result):
    assert valid_password1(*parse_line(test_line)) == result


test_data = zip(test_lines, [True, False, False])


@pytest.mark.parametrize("test_line,result", test_data)
def test_valid_password2(test_line, result):
    assert valid_password2(*parse_line(test_line)) == result


def test_count_valid_passwords():
    assert count_valid_passwords(valid_password1, test_lines) == 2


def test_count_valid_passwords2():
    assert count_valid_passwords(valid_password2, test_lines) == 1
