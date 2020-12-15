from .day01 import expense_report
from .day02 import count_valid_passwords, valid_password1, valid_password2
from .day03 import count_trees, compare_routes
from .day04 import (process_passports, count_valid_passports,
                    count_valid_passports2)
from .day05 import seat_number, seat_id,  my_seat
from .day06 import count_any_affirmative, count_all_affirmative
from .day07 import build_tree, build_nodes, count_contains_shiny_gold
from .day08 import parse_instructions, execute, trial_flips
from .day09 import first_invalid, weakness
from .day10 import pick_order, jump_product, count_routes
from .day11 import settle, settle2
from .day12 import manhattan_distance, follow_route, follow_route2
from .day13 import parse_bus_info, earliest_bus
from .day14 import execute_program, execute_program2
from .day15 import memory_game
from functools import reduce


def main():
    entries = [int(elem) for elem in open("./input/day1.txt").read().split()]
    print(f"day 01 - part 1: {expense_report(entries, 2)}")
    print(f"day 01 - part 2: {expense_report(entries, 3)}")

    password_entries = open("./input/day2.txt").readlines()
    print("day 02 - part 1: "
          f"{count_valid_passwords(valid_password1, password_entries)}")
    print("day 02 - part 1: "
          f"{count_valid_passwords(valid_password2, password_entries)}")

    toboggan_map = open("./input/day3.txt").read().splitlines()
    print(f"day 03 - part 1: {count_trees(toboggan_map, (1, 3))}")
    day3_part2 = reduce(
        lambda x, y: x*y,
        compare_routes(toboggan_map, [(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)])
    )
    print(f"day 03 - part 2: {day3_part2}")

    passports = process_passports(open("./input/day4.txt").read())
    print(f"day 04 - part 1: {count_valid_passports(passports)}")
    print(f"day 04 - part 2: {count_valid_passports2(passports)}")

    boarding_passes = open("./input/day5.txt").read().splitlines()
    print("day 05 - part 1: "
          f"{max([seat_id(*seat_number(seat)) for seat in boarding_passes])}")
    print(f"day 05 - part 2: {my_seat(boarding_passes)}")

    groups_answers = open("./input/day6.txt").read().split("\n\n")
    print(f"day 06 - part 1: {count_any_affirmative(groups_answers)}")
    print(f"day 06 - part 2: {count_all_affirmative(groups_answers)}")

    bags = open("./input/day7.txt").read()
    nodes = build_tree(bags, build_nodes(bags))
    print(f"day 07 - part 1: {count_contains_shiny_gold(nodes)}")
    print(f"day 07 - part 2: {nodes['shiny gold'].total_children()}")

    instructions = parse_instructions(open("./input/day8.txt").read())
    print(f"day 08 - part 1: {execute(instructions)[2]}")
    print(f"day 08 - part 2: {trial_flips(instructions)[2]}")

    sequence = [int(line) for line in open("./input/day9.txt").readlines()]
    print(f"day 09 - part 1: {first_invalid(sequence)}")
    print(f"day 09 - part 2: {weakness(first_invalid(sequence), sequence)}")

    adapters = [int(line) for line in open("./input/day10.txt").readlines()]
    print(f"day 10 - part 1: {jump_product(pick_order(adapters))}")
    print(f"day 10 - part 2: {count_routes(adapters)}")

    plan = open("./input/day11.txt").read()
    print(f"day 11 - part 1: {settle(plan)}")
    print(f"day 11 - part 2: {settle2(plan)}")

    route = open("./input/day12.txt").read()
    print(f"day 12 - part 1: {manhattan_distance(follow_route(route)[0])}")
    print(f"day 12 - part 2: {manhattan_distance(follow_route2(route))}")

    start_time, bus_ids = parse_bus_info(open("./input/day13.txt").read())
    time, bus = earliest_bus(start_time, bus_ids)
    print(f"day 13 - part 1: {(time - start_time) * bus}")

    program = open("./input/day14.txt").read()
    print(f"day 14 - part 1: {sum(execute_program(program).values())}")
    print(f"day 14 - part 2: {sum(execute_program2(program).values())}")

    print(f"day 15 - part 1: {memory_game([1, 2, 16, 19, 18, 0])}")
    print("day 15 - part 2: "
          f"{memory_game([1, 2, 16, 19, 18, 0], end_turn=30_000_000)}")


if __name__ == "__main__":
    main()
