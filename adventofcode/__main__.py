from .day1 import expense_report
from .day2 import count_valid_passwords, valid_password1, valid_password2
from .day3 import count_trees, compare_routes
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


if __name__ == "__main__":
    main()
