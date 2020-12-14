from ..day14 import (bits_to_int, int_to_bits, apply_mask, execute_program,
                     apply_mask2, execute_program2)
from textwrap import dedent
import pytest


def expand(bits):
    return [int(i) for i in bits]


@pytest.mark.parametrize(
    "bits,value",
    [
        ([int(i) for i in "000000000000000000000000000000001011"], 11),
        ([int(i) for i in "000000000000000000000000000001100101"], 101),
        ([int(i) for i in "000000000000000000000000000000000000"], 0)
    ]
)
def test_bits_to_int(bits, value):
    assert bits_to_int(bits) == value


@pytest.mark.parametrize(
    "value,bits",
    [
        (11, [int(i) for i in "000000000000000000000000000000001011"]),
        (101, [int(i) for i in "000000000000000000000000000001100101"]),
        (0, [int(i) for i in "000000000000000000000000000000000000"])
    ]
)
def test_int_to_bits(value, bits):
    assert int_to_bits(value) == bits


@pytest.mark.parametrize(
    "bits,mask,expected",
    [
        (expand("000000000000000000000000000000001011"),
         "XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X",
         expand("000000000000000000000000000001001001")),
        (expand("000000000000000000000000000001100101"),
         "XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X",
         expand("000000000000000000000000000001100101")),
        (expand("000000000000000000000000000000000000"),
         "XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X",
         expand("000000000000000000000000000001000000")),
    ]
)
def test_apply_mask(bits, mask, expected):
    assert apply_mask(bits, mask) == expected


test_program = dedent("""\
    mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
    mem[8] = 11
    mem[7] = 101
    mem[8] = 0""")


def test_execute_program():
    mem = execute_program(test_program)

    assert sum(mem.values()) == 165


def test_apply_mask2():
    addresses = apply_mask2(int_to_bits(42),
                            "000000000000000000000000000000X1001X")

    assert len(addresses) == 4
    assert expand("000000000000000000000000000000011010") in addresses
    assert expand("000000000000000000000000000000011011") in addresses
    assert expand("000000000000000000000000000000111010") in addresses
    assert expand("000000000000000000000000000000111011") in addresses
    values = [bits_to_int(address) for address in addresses]
    assert 26 in values
    assert 27 in values
    assert 58 in values
    assert 59 in values


test_program2 = dedent("""\
    mask = 000000000000000000000000000000X1001X
    mem[42] = 100
    mask = 00000000000000000000000000000000X0XX
    mem[26] = 1""")


def test_execute_program2():
    mem = execute_program2(test_program2)
    assert sum(mem.values()) == 208
