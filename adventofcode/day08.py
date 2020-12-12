def parse_instructions(text):
    return [tuple(line.split()) for line in text.splitlines()]


def flip_instruction(instruction):
    if (arg := instruction[0]) == "nop":
        return ("jmp", instruction[1])
    elif arg == "jmp":
        return ("nop", instruction[1])


def accumulate(accumulator, arg):
    plus_minus = arg[0]
    value = int(arg[1:])

    if plus_minus == "+":
        return accumulator + value
    elif plus_minus == "-":
        return accumulator - value


def execute(instructions):
    index = 0
    max_index = len(instructions)

    count = 0

    visited = set()

    while True:
        if index in visited:
            return "loop", index, count
        else:
            visited.add(index)

        if index == max_index:
            return "end", index, count

        instruction, arg = instructions[index]

        if instruction == "nop":
            index += 1
        elif instruction == "acc":
            count = accumulate(count, arg)
            index += 1
        elif instruction == "jmp":
            index = accumulate(index, arg)


def trial_flips(instructions):
    for i in range(len(instructions)):
        if instructions[i][0] in ["nop", "jmp"]:
            # Flip instruction in place
            instructions[i] = flip_instruction(instructions[i])
            result = execute(instructions)

            if result[0] == "end":
                return result

            instructions[i] = flip_instruction(instructions[i])
