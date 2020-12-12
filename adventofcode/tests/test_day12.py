from ..day12 import (Direction, turn, follow_route, manhattan_distance, rotate,
                     follow_route2)
from textwrap import dedent
import pytest


@pytest.mark.parametrize(
    "heading,direction,degrees,expected",
    [
        (Direction.EAST, "L", 90, Direction.NORTH),
        (Direction.NORTH, "R", 180, Direction.SOUTH),
        (Direction.SOUTH, "R", 270, Direction.EAST),
    ]
)
def test_turn(heading, direction, degrees, expected):
    assert turn(heading, direction, degrees) == expected


test_route = dedent("""\
    F10
    N3
    F7
    R90
    F11""")


def test_follow_route():
    pos, _ = follow_route(test_route)

    assert pos == (-8, 17)
    assert manhattan_distance(pos) == 25


@pytest.mark.parametrize(
    "waypoint,direction,degrees,expected",
    [
        ((4, 10), "R", 90, (-10, 4)),
    ]
)
def test_rotate(waypoint, direction, degrees, expected):
    assert rotate(waypoint, direction, degrees) == expected


def test_follow_route2():
    pos = follow_route2(test_route)

    assert pos == (-72, 214)
    assert manhattan_distance(pos) == 286
