from collections import defaultdict
import re


def bits_to_int(bits):
    return sum(2**i * bit for i, bit in enumerate(reversed(bits)))


def int_to_bits(value):
    bits = [0]*36
    for i in reversed(range(36)):
        if (remainder := value % 2**i) != value:
            bits[i] = 1
            value = remainder
    return list(reversed(bits))


def apply_mask(bits, mask):
    return [
        1 if imask == "1" else 0 if imask == "0" else ibit
        for ibit, imask in zip(bits, mask)
    ]


mem_parser = re.compile(r"mem\[(\d+)\] = (\d+)")


def execute_program(program):
    program = program.splitlines()

    mask = ""
    mem = defaultdict(lambda: 0)

    for line in program:
        if line.startswith("mask"):
            # Copy new mask
            mask = line.split(" = ")[1]
        elif line.startswith("mem"):
            # Get memory address and value
            result = mem_parser.match(line)
            address = int(result.group(1))
            value = int(result.group(2))

            # Apply mask
            bits = int_to_bits(value)
            bits = apply_mask(bits, mask)

            # Store value
            value = bits_to_int(bits)
            mem[address] = value

    return mem
