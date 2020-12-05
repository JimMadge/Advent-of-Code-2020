from ..day5 import seat_number, seat_id
import pytest


test_data = [
    ("FBFBBFFRLR", 357),
    ("BFFFBBFRRR", 567),
    ("FFFBBBFRRR", 119),
    ("BBFFBBFRLL", 820)
]


def test_seat_number():
    assert seat_number("FBFBBFFRLR") == (44, 5)


@pytest.mark.parametrize("seat_string,expected_id", test_data)
def test_seat_id(seat_string, expected_id):
    assert seat_id(*seat_number(seat_string)) == expected_id
