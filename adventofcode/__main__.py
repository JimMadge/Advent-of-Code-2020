from .day1 import expense_report
from .day2 import count_valid_passwords, valid_password1, valid_password2
from .day3 import count_trees, compare_routes
from .day4 import (process_passports, count_valid_passports,
                   count_valid_passports2)
from .day5 import seat_number, seat_id,  my_seat
from .day6 import count_any_affirmative, count_all_affirmative
from .day7 import build_tree, build_nodes, count_contains_shiny_gold
from .day8 import parse_instructions, execute, trial_flips
from .day9 import first_invalid, weakness
from .day10 import pick_order, jump_product, count_routes
from .day11 import settle, settle2
from functools import reduce


def main():
    entries = [int(elem) for elem in open("./input/day1.txt").read().split()]
    print(f"day 1 - part 1: {expense_report(entries, 2)}")
    print(f"day 1 - part 2: {expense_report(entries, 3)}")

    password_entries = open("./input/day2.txt").readlines()
    print("day 2 - part 1: "
          f"{count_valid_passwords(valid_password1, password_entries)}")
    print("day 2 - part 1: "
          f"{count_valid_passwords(valid_password2, password_entries)}")

    toboggan_map = open("./input/day3.txt").read().splitlines()
    print(f"day 3 - part 1: {count_trees(toboggan_map, (1, 3))}")
    day3_part2 = reduce(
        lambda x, y: x*y,
        compare_routes(toboggan_map, [(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)])
    )
    print(f"day 3 - part 2: {day3_part2}")

    passports = process_passports(open("./input/day4.txt").read())
    print(f"day 4 - part 1: {count_valid_passports(passports)}")
    print(f"day 4 - part 2: {count_valid_passports2(passports)}")

    boarding_passes = open("./input/day5.txt").read().splitlines()
    print("day 5 - part 1: "
          f"{max([seat_id(*seat_number(seat)) for seat in boarding_passes])}")
    print(f"day 5 - part 2: {my_seat(boarding_passes)}")

    groups_answers = open("./input/day6.txt").read().split("\n\n")
    print(f"day 6 - part 1: {count_any_affirmative(groups_answers)}")
    print(f"day 6 - part 2: {count_all_affirmative(groups_answers)}")

    bags = open("./input/day7.txt").read()
    nodes = build_tree(bags, build_nodes(bags))
    print(f"day 7 - part 1: {count_contains_shiny_gold(nodes)}")
    print(f"day 7 - part 2: {nodes['shiny gold'].total_children()}")

    instructions = parse_instructions(open("./input/day8.txt").read())
    print(f"day 8 - part 1: {execute(instructions)[2]}")
    print(f"day 8 - part 2: {trial_flips(instructions)[2]}")

    sequence = [int(line) for line in open("./input/day9.txt").readlines()]
    print(f"day 9 - part 1: {first_invalid(sequence)}")
    print(f"day 9 - part 2: {weakness(first_invalid(sequence), sequence)}")

    adapters = [int(line) for line in open("./input/day10.txt").readlines()]
    print(f"day 10 - part 1: {jump_product(pick_order(adapters))}")
    print(f"day 10 - part 2: {count_routes(adapters)}")

    plan = open("./input/day11.txt").read()
    print(f"day 11 - part 1: {settle(plan)}")
    print(f"day 11 - part 1: {settle2(plan)}")


if __name__ == "__main__":
    main()
