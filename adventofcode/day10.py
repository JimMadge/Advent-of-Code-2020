from collections import Counter
from functools import cache


def pick_order(adapters):
    # Add outlet and device
    return sorted(adapters[:] + [0] + [max(adapters) + 3])


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
    adapters = [0] + sorted(adapters)

    @cache
    def routes(index):
        # If we have reached the end this is the only route
        if index == len(adapters) - 1:
            return 1

        return sum(
            routes(i) for i in range(index+1, min(index+4, len(adapters)))
            if adapters[i] - adapters[index] <= 3
        )

    return routes(0)
