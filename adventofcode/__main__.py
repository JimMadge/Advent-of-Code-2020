from .day1 import expense_report


def main():
    entries = [int(elem) for elem in open("input/day1.txt").read().split()]
    print(f"day 1 - part 1: {expense_report(entries, 2)}")
    print(f"day 1 - part 2: {expense_report(entries, 3)}")


if __name__ == "__main__":
    main()
