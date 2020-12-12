from ..day03 import count_trees, compare_routes
from textwrap import dedent

test_map = dedent(
    """\
    ..##.......
    #...#...#..
    .#....#..#.
    ..#.#...#.#
    .#...##..#.
    ..#.##.....
    .#.#.#....#
    .#........#
    #.##...#...
    #...##....#
    .#..#...#.#
    """).splitlines()


def test_count_trees():
    assert count_trees(test_map, (1, 3)) == 7


def test_compare_routes():
    assert compare_routes(
        test_map,
        [(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)]
    ) == [2, 7, 3, 4, 2]
