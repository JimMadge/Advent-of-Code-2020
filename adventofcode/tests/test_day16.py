from ..day16 import create_rule, parse_ticket, completely_invalid
from textwrap import dedent
import pytest


example_rule = "departure location: 45-309 or 320-962"


def test_create_rule():
    rule = create_rule(example_rule)

    assert rule.name == "departure location"
    assert rule.lowera == 45
    assert rule.uppera == 309
    assert rule.lowerb == 320
    assert rule.upperb == 962


@pytest.fixture()
def rule():
    return create_rule(example_rule)


@pytest.mark.parametrize(
    "value,result",
    [
        (45, True),
        (70, True),
        (309, True),
        (42, False),
        (312, False),
        (320, True),
        (962, True),
        (500, True),
        (1000, False),
    ]
)
def test_check(value, result, rule):
    assert rule.check(value) is result


example_rules = dedent("""\
    class: 1-3 or 5-7
    row: 6-11 or 33-44
    seat: 13-40 or 45-50""")


@pytest.fixture()
def rules():
    return [create_rule(line) for line in example_rules.splitlines()]


example_nearby = dedent("""\
    7,3,47
    40,4,50
    55,2,20
    38,6,12""")


def test_parse_ticket():
    assert parse_ticket("7,3,47") == [7, 3, 47]


@pytest.fixture()
def tickets():
    return [parse_ticket(line) for line in example_nearby.splitlines()]


def test_completely_invalid(rules, tickets):
    invalid = completely_invalid(rules, tickets)

    assert len(invalid) == 3
    assert 4 in invalid
    assert 55 in invalid
    assert 12 in invalid
