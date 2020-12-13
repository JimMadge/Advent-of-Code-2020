from ..day13 import parse_bus_info, earliest_bus
from textwrap import dedent


test_bus_info = dedent("""\
    939
    7,13,x,x,59,x,31,19""")


def test_parse_bus_info():
    time, bus_ids = parse_bus_info(test_bus_info)

    assert time == 939
    assert bus_ids == [7, 13, 59, 31, 19]


def test_earliest_bus():
    start_time, bus_ids = parse_bus_info(test_bus_info)
    time, bus = earliest_bus(start_time, bus_ids)

    assert time == 944
    assert bus == 59
    assert (time - start_time) * bus == 295
