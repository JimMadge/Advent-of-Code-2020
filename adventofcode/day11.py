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
                    seats[i][j].neighbours.append(neighbour)


def create_neighbours2(seats):
    height = len(seats)
    width = len(seats[0])

    for i in range(height):
        for j in range(width):
            # Skip empty space
            if seats[i][j] is None:
                continue

            # Try each direction
            for displacement in displacements:
                # Look further until a neighbour is found
                multiplier = 1
                while True:
                    ni = i + displacement[0]*multiplier
                    nj = j + displacement[1]*multiplier

                    # End if neighbouring tile is out of bounds
                    if ni >= height:
                        break
                    if ni < 0:
                        break
                    if nj >= width:
                        break
                    if nj < 0:
                        break

                    # Only add if neighbouring tile is a seat (not None)
                    if (neighbour := seats[ni][nj]):
                        seats[i][j].neighbours.append(neighbour)
                        break

                    multiplier += 1


def step(seats, visible=4):
    flipped = 0

    for seat in chain.from_iterable(seats):
        if seat is None:
            continue

        if seat.occupied:
            if seat.occupied_neighbours() >= visible:
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


def optimise(seats, visible=4):
    flipped = 1
    while flipped != 0:
        flipped = step(seats, visible)


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


def settle2(plan):
    seats = read_plan(plan)
    create_neighbours2(seats)
    optimise(seats, 5)

    return count_occupied(seats)
