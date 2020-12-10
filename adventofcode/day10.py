from collections import Counter
from functools import cache


def pick_order(adapters):
    # Add outlet
    adapters = adapters[:] + [0]
    # Add device
    adapters += [max(adapters) + 3]
    return sorted(adapters)


def count_jumps(adapters):
    jumps = Counter()

    for i in range(len(adapters)-1):
        difference = abs(adapters[i] - adapters[i+1])
        jumps[difference] += 1

    return jumps


def jump_product(adapters):
    jumps = count_jumps(adapters)

    return jumps[1] * jumps[3]


def count_routes(adapters):
    adapters = pick_order(adapters)

    @cache
    def routes(index):
        if index == len(adapters) - 1:
            return 1

        count = 0
        for i in range(index+1, min(index+4, len(adapters))):
            if adapters[i] - adapters[index] <= 3:
                count += routes(i)
        return count

    return routes(0)
