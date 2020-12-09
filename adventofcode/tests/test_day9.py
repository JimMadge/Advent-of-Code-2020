from ..day9 import find_sum, first_invalid, weakness
import pytest

test_sequence = [
    35,
    20,
    15,
    25,
    47,
    40,
    62,
    55,
    65,
    95,
    102,
    117,
    150,
    182,
    127,
    219,
    299,
    277,
    309,
    576,
]

test_data = [
    (26, range(1, 26), True),
    (49, range(1, 26), True),
    (100, range(1, 26), False),
    (50, range(1, 26), False)
]


@pytest.mark.parametrize("target,pool,result", test_data)
def test_find_sum(target, pool, result):
    assert find_sum(target, pool) == result


def test_first_invalid():
    assert first_invalid(test_sequence, preamble=5) == 127


def test_weakness():
    assert weakness(127, test_sequence) == 62
