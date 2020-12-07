from ..day7 import build_tree, build_nodes, count_contains_shiny_gold
import pytest
from textwrap import dedent

test_data = dedent("""\
   light red bags contain 1 bright white bag, 2 muted yellow bags.
   dark orange bags contain 3 bright white bags, 4 muted yellow bags.
   bright white bags contain 1 shiny gold bag.
   muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
   shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
   dark olive bags contain 3 faded blue bags, 4 dotted black bags.
   vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
   faded blue bags contain no other bags.
   dotted black bags contain no other bags.""")


def test_build_nodes():
    nodes = build_nodes(test_data)

    keys = nodes.keys()

    assert "light red" in keys
    assert "shiny gold" in keys
    assert "dotted black" in keys


def test_build_tree():
    nodes = build_nodes(test_data)
    nodes = build_tree(test_data, nodes)

    assert nodes["dotted black"].children == []
    assert nodes["bright white"].children == [nodes["shiny gold"]]


@pytest.fixture
def test_tree():
    nodes = build_nodes(test_data)
    nodes = build_tree(test_data, nodes)

    return nodes


def test_contains_shiny_gold(test_tree):
    assert test_tree["bright white"].contains_shiny_gold() is True
    assert test_tree["dark olive"].contains_shiny_gold() is False


def test_count_contains_shiny_gold(test_tree):
    assert count_contains_shiny_gold(test_tree) == 4


def test_total_children(test_tree):
    assert test_tree["shiny gold"].total_children() == 32
