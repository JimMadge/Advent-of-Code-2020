from functools import reduce
from itertools import combinations


def expense_report(entries, number=2):
    for items in combinations(entries, number):
        if sum(items) == 2020:
            return reduce(lambda x, y: x*y, items)
    return None
