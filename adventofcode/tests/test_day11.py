from ..day11 import (read_plan, create_neighbours, Seat, step, optimise,
                     count_occupied, create_neighbours2)
from textwrap import dedent


test_plan = dedent("""\
    L.LL.LL.LL
    LLLLLLL.LL
    L.L.L..L..
    LLLL.LL.LL
    L.LL.LL.LL
    L.LLLLL.LL
    ..L.L.....
    LLLLLLLLLL
    L.LLLLLL.L
    L.LLLLL.LL""")


def test_read_plan():
    seats = read_plan(test_plan)

    assert isinstance(seats[0][0], Seat)
    assert not seats[0][0].occupied
    assert seats[0][1] is None
    assert seats[2][1] is None


def test_create_neighbours():
    seats = read_plan(test_plan)
    create_neighbours(seats)

    assert len(seats[0][0].neighbours) == 2
    assert len(seats[7][3].neighbours) == 7


def test_step():
    seats = read_plan(test_plan)
    create_neighbours(seats)
    step(seats)

    assert seats[0][0].occupied
    assert seats[1][0].occupied


def test_optimise():
    seats = read_plan(test_plan)
    create_neighbours(seats)
    optimise(seats)

    assert count_occupied(seats) == 37


def test_optimise2():
    seats = read_plan(test_plan)
    create_neighbours2(seats)
    optimise(seats, 5)

    assert count_occupied(seats) == 26
