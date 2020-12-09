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

    for i in range(0, n-1):
        for j in range(i+1, n):
            a = sequence[i:j+1]
            if sum(a) == target:
                return min(a) + max(a)
