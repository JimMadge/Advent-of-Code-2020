from .day1 import expense_report
from .day2 import count_valid_passwords


def main():
    entries = [int(elem) for elem in open("./input/day1.txt").read().split()]
    print(f"day 1 - part 1: {expense_report(entries, 2)}")
    print(f"day 1 - part 2: {expense_report(entries, 3)}")

    password_entries = open("./input/day2.txt").readlines()
    print(f"day 2 - part 1: {count_valid_passwords(password_entries)}")


if __name__ == "__main__":
    main()
