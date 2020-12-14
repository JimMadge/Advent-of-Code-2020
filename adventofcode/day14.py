from collections import defaultdict
import re


def bits_to_int(bits):
    return sum(2**i * bit for i, bit in enumerate(reversed(bits)))


def int_to_bits(value, depth=36):
    bits = [0]*depth
    for i in reversed(range(depth)):
        if (remainder := value % 2**i) != value:
            bits[i] = 1
            value = remainder
    return list(reversed(bits))


def apply_mask(bits, mask):
    return [
        1 if imask == "1" else 0 if imask == "0" else ibit
        for ibit, imask in zip(bits, mask)
    ]


def apply_mask2(bits, mask):
    # Apply 1s and 0s, ignoring Xs
    bits = [
        1 if imask == "1" else ibit if imask == "0" else "X"
        for ibit, imask in zip(bits, mask)
    ]

    floating_bits = bits.count("X")
    combinations = [
        int_to_bits(value, depth=floating_bits)
        for value in range(2**floating_bits)
    ]

    results = []
    for combination in combinations:
        results.append(
            [ibit if ibit in [0, 1] else combination.pop() for ibit in bits]
        )

    return results


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


def execute_program2(program):
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
            addresses = apply_mask2(int_to_bits(address), mask)

            # Store value
            for address in addresses:
                mem[bits_to_int(address)] = value

    return mem
