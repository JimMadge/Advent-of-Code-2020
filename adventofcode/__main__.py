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
from .day16 import completely_invalid, parse_ticket, create_rule, part2
import argparse
from functools import reduce


def print_result(day, part, result):
    print(f"day {day:02d} - part {part}: {result}")


def day01():
    entries = [int(elem) for elem in open("./input/day1.txt").read().split()]
    print_result(1, 1, expense_report(entries, 2))
    print_result(1, 2, expense_report(entries, 3))


def day02():
    password_entries = open("./input/day2.txt").readlines()
    print_result(2, 1,
                 count_valid_passwords(valid_password1, password_entries))
    print_result(2, 2,
                 count_valid_passwords(valid_password2, password_entries))


def day03():
    toboggan_map = open("./input/day3.txt").read().splitlines()
    print_result(3, 1, count_trees(toboggan_map, (1, 3)))
    print_result(
        3,
        2,
        reduce(
            lambda x, y: x*y,
            compare_routes(toboggan_map,
                           [(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)])
        )
    )


def day04():
    passports = process_passports(open("./input/day4.txt").read())
    print_result(4, 1, count_valid_passports(passports))
    print_result(4, 2, count_valid_passports2(passports))


def day05():
    boarding_passes = open("./input/day5.txt").read().splitlines()
    print_result(
        5,
        1,
        max([seat_id(*seat_number(seat)) for seat in boarding_passes])
    )
    print_result(5, 2, my_seat(boarding_passes))


def day06():
    groups_answers = open("./input/day6.txt").read().split("\n\n")
    print_result(6, 1, count_any_affirmative(groups_answers))
    print_result(6, 2, count_all_affirmative(groups_answers))


def day07():
    bags = open("./input/day7.txt").read()
    nodes = build_tree(bags, build_nodes(bags))
    print_result(7, 1, count_contains_shiny_gold(nodes))
    print_result(7, 2, nodes['shiny gold'].total_children())


def day08():
    instructions = parse_instructions(open("./input/day8.txt").read())
    print_result(8, 1, execute(instructions)[2])
    print_result(8, 2, trial_flips(instructions)[2])


def day09():
    sequence = [int(line) for line in open("./input/day9.txt").readlines()]
    print_result(9, 1, first_invalid(sequence))
    print_result(9, 2, weakness(first_invalid(sequence), sequence))


def day10():
    adapters = [int(line) for line in open("./input/day10.txt").readlines()]
    print_result(10, 1, jump_product(pick_order(adapters)))
    print_result(10, 2, count_routes(adapters))


def day11():
    plan = open("./input/day11.txt").read()
    print_result(11, 1, settle(plan))
    print_result(11, 2, settle2(plan))


def day12():
    route = open("./input/day12.txt").read()
    print_result(12, 1, manhattan_distance(follow_route(route)[0]))
    print_result(12, 2, manhattan_distance(follow_route2(route)))


def day13():
    start_time, bus_ids = parse_bus_info(open("./input/day13.txt").read())
    time, bus = earliest_bus(start_time, bus_ids)
    print_result(13, 1, (time - start_time) * bus)


def day14():
    program = open("./input/day14.txt").read()
    print_result(14, 1, sum(execute_program(program).values()))
    print_result(14, 2, sum(execute_program2(program).values()))


def day15():
    print_result(15, 1, memory_game([1, 2, 16, 19, 18, 0]))
    print_result(15, 2,
                 memory_game([1, 2, 16, 19, 18, 0], end_turn=30_000_000))


def day16():
    rules = [create_rule(line) for line in
             open("./input/day16_rules.txt").readlines()]
    tickets = [parse_ticket(line) for line in
               open("./input/day16_tickets.txt").readlines()]
    my_ticket = tickets[0]
    nearby_tickets = tickets[1:]
    print_result(16, 1, sum(completely_invalid(rules, nearby_tickets)))
    print_result(16, 1, part2(rules, nearby_tickets, my_ticket))


def main():
    parser = argparse.ArgumentParser(description="Advent of Code 2020")
    parser.add_argument("--last", action="store_true")

    args = parser.parse_args()

    days = [
        day01,
        day02,
        day03,
        day04,
        day05,
        day06,
        day07,
        day10,
        day11,
        day12,
        day13,
        day14,
        day15,
        day16,
    ]

    if args.last:
        days[-1]()
        return

    for day in days:
        day()


if __name__ == "__main__":
    main()
