from .day1 import expense_report
from .day2 import count_valid_passwords, valid_password1, valid_password2


def main():
    entries = [int(elem) for elem in open("./input/day1.txt").read().split()]
    print(f"day 1 - part 1: {expense_report(entries, 2)}")
    print(f"day 1 - part 2: {expense_report(entries, 3)}")

    password_entries = open("./input/day2.txt").readlines()
    print("day 2 - part 1: "
          f"{count_valid_passwords(valid_password1, password_entries)}")
    print("day 2 - part 1: "
          f"{count_valid_passwords(valid_password2, password_entries)}")


if __name__ == "__main__":
    main()
