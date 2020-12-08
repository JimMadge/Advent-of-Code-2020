from ..day8 import parse_instructions, execute
from textwrap import dedent

test_data = dedent("""\
    nop +0
    acc +1
    jmp +4
    acc +3
    jmp -3
    acc -99
    acc +1
    jmp -4
    acc +6""")


def test_parse_instructions():
    instructions = parse_instructions(test_data)

    assert instructions[0] == ("nop", "+0")
    assert instructions[6] == ("acc", "+1")


def test_execute():
    assert execute(parse_instructions(test_data)) == (1, 5)
