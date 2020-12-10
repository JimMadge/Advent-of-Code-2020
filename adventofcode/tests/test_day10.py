from ..day10 import count_jumps, pick_order, jump_product, count_routes
import pytest

test_adapters = [
    16,
    10,
    15,
    5,
    1,
    11,
    7,
    19,
    6,
    12,
    4,
]

test_adapters2 = [
    28,
    33,
    18,
    42,
    31,
    14,
    46,
    20,
    48,
    47,
    24,
    23,
    49,
    45,
    19,
    38,
    39,
    11,
    1,
    32,
    25,
    35,
    8,
    17,
    7,
    9,
    4,
    2,
    34,
    10,
    3,
]


test_data = [
    (test_adapters, 7, 5),
    (test_adapters2, 22, 10),
]


@pytest.mark.parametrize("adapters,one_jumps,three_jumps", test_data)
def test_count_jumps(adapters, one_jumps, three_jumps):
    adapters = pick_order(adapters)
    jumps = count_jumps(adapters)

    assert jumps[1] == one_jumps
    assert jumps[3] == three_jumps


test_data = [
    (test_adapters, 35),
    (test_adapters2, 220),
]


@pytest.mark.parametrize("adapters,expected_jump_product", test_data)
def test_count_jump_product(adapters, expected_jump_product):
    assert jump_product(pick_order(adapters)) == expected_jump_product


def test_count_routes():
    assert count_routes(test_adapters) == 8
    assert count_routes(test_adapters2) == 19208
