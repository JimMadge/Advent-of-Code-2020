from ..day15 import memory_game
import pytest


@pytest.mark.parametrize(
    "starting_numbers,rounds,expected",
    [
        ([0, 3, 6], 10, 0),
        ([0, 3, 6], None, 436),
        ([1, 3, 2], None, 1),
        ([2, 1, 3], None, 10),
        ([1, 2, 3], None, 27),
        ([2, 3, 1], None, 78),
        ([3, 2, 1], None, 438),
        ([3, 1, 2], None, 1836),
        pytest.param([0, 3, 6], 30_000_000, 175594, marks=pytest.mark.skip),
        pytest.param([1, 3, 2], 30_000_000, 2578, marks=pytest.mark.skip),
        pytest.param([2, 1, 3], 30_000_000, 3544142, marks=pytest.mark.skip),
        pytest.param([1, 2, 3], 30_000_000, 261214, marks=pytest.mark.skip),
        pytest.param([2, 3, 1], 30_000_000, 6895259, marks=pytest.mark.skip),
        pytest.param([3, 2, 1], 30_000_000, 18, marks=pytest.mark.skip),
        pytest.param([3, 1, 2], 30_000_000, 362, marks=pytest.mark.skip),
    ]
)
def test_memory_game(starting_numbers, rounds, expected):
    if rounds:
        assert memory_game(starting_numbers, end_turn=rounds) == expected
    else:
        assert memory_game(starting_numbers) == expected
