def parse_instructions(text):
    return [tuple(line.split()) for line in text.splitlines()]


def accumulate(accumulator, arg):
    plus_minus = arg[0]
    value = int(arg[1:])

    if plus_minus == "+":
        return accumulator + value
    elif plus_minus == "-":
        return accumulator - value


def execute(instructions):
    index = 0
    count = 0

    visited = set()

    while True:
        # print(index, count)
        if index in visited:
            return index, count
        else:
            visited.add(index)

        instruction, arg = instructions[index]

        if instruction == "nop":
            index += 1
        elif instruction == "acc":
            count = accumulate(count, arg)
            index += 1
        elif instruction == "jmp":
            index = accumulate(index, arg)
