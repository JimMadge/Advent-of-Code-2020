from itertools import chain


class Seat(object):
    def __init__(self, occupied=False):
        self.occupied = occupied
        self.neighbours = []
        self.pending_flip = False

    def flip(self):
        self.occupied = not self.occupied
        self.pending_flip = False

    def occupied_neighbours(self):
        return sum(neighbour.occupied for neighbour in self.neighbours)


def read_plan(plan):
    d = {
        'L': Seat,
        '.': lambda: None,
    }

    seats = []
    for line in plan.splitlines():
        seats.append(
            [d[char]() for char in line]
        )

    return seats


displacements = [
    (0, 1),
    (1, 1),
    (1, 0),
    (1, -1),
    (0, -1),
    (-1, -1),
    (-1, 0),
    (-1, 1),
]


def create_neighbours(seats):
    height = len(seats)
    width = len(seats[0])

    for i in range(height):
        for j in range(width):
            # print(i, j)
            # Skip empty space
            if seats[i][j] is None:
                continue

            # Try each neighbour
            for displacement in displacements:
                ni = i + displacement[0]
                nj = j + displacement[1]

                # Skip if neighbouring tile is out of bounds
                if ni >= height:
                    continue
                if ni < 0:
                    continue
                if nj >= width:
                    continue
                if nj < 0:
                    continue

                # Only add if neighbouring tile is a seat (not None)
                if (neighbour := seats[ni][nj]):
                    # print(neighbour)
                    seats[i][j].neighbours.append(neighbour)


def step(seats):
    flipped = 0

    for seat in chain.from_iterable(seats):
        if seat is None:
            continue

        if seat.occupied:
            if seat.occupied_neighbours() >= 4:
                seat.pending_flip = True
        else:
            if seat.occupied_neighbours() == 0:
                seat.pending_flip = True

    for seat in chain.from_iterable(seats):
        if seat is None:
            continue

        if seat.pending_flip:
            seat.flip()
            flipped += 1

    return flipped


def optimise(seats):
    flipped = 1
    while flipped != 0:
        flipped = step(seats)


def count_occupied(seats):
    count = 0
    for seat in chain.from_iterable(seats):
        if seat is None:
            continue

        if seat.occupied:
            count += 1
    return count


def settle(plan):
    seats = read_plan(plan)
    create_neighbours(seats)
    optimise(seats)

    return count_occupied(seats)
