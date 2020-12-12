from collections import deque
from itertools import combinations


def find_sum(target, pool):
    for a, b in combinations(pool, 2):
        if a + b == target:
            return True
    return False


def first_invalid(sequence, preamble=25):
    pool = deque(sequence[:preamble], maxlen=preamble)

    index = preamble
    while True:
        target = sequence[index]

        if find_sum(target, pool):
            index += 1
            pool.append(target)
        else:
            return target


def weakness(target, sequence):
    n = len(sequence)

    for (lower, upper) in combinations(range(n), 2):
        sub_sequence = sequence[lower:upper+1]
        if sum(sub_sequence) == target:
            return min(sub_sequence) + max(sub_sequence)
