from enum import Enum, auto


class Direction(Enum):
    EAST = auto()
    NORTH = auto()
    WEST = auto()
    SOUTH = auto()


def turn(heading, direction, degrees):
    turns = {
        "L": {
            Direction.EAST: Direction.NORTH,
            Direction.NORTH: Direction.WEST,
            Direction.WEST: Direction.SOUTH,
            Direction.SOUTH: Direction.EAST
        },
        "R": {
            Direction.EAST: Direction.SOUTH,
            Direction.SOUTH: Direction.WEST,
            Direction.WEST: Direction.NORTH,
            Direction.NORTH: Direction.EAST
        }
    }

    n_turns = degrees // 90

    for turn in range(n_turns):
        heading = turns[direction][heading]
    return heading


def forward(pos, heading, distance):
    if heading == Direction.EAST:
        return (pos[0], pos[1]+distance)
    elif heading == Direction.NORTH:
        return (pos[0]+distance, pos[1])
    elif heading == Direction.WEST:
        return (pos[0], pos[1]-distance)
    elif heading == Direction.SOUTH:
        return (pos[0]-distance, pos[1])


def update_position(instruction, pos, heading):
    action, arg = instruction[0], int(instruction[1:])

    if action == "N":
        return (pos[0]+arg, pos[1]), heading
    elif action == "S":
        return (pos[0]-arg, pos[1]), heading
    elif action == "E":
        return (pos[0], pos[1]+arg), heading
    elif action == "W":
        return (pos[0], pos[1]-arg), heading
    elif action == "L":
        return pos, turn(heading, "L", arg)
    elif action == "R":
        return pos, turn(heading, "R", arg)
    elif action == "F":
        return forward(pos, heading, arg), heading


def follow_route(route):
    pos = (0, 0)
    heading = Direction.EAST
    for instruction in route.splitlines():
        pos, heading = update_position(instruction, pos, heading)

    return pos, heading


def manhatten_distance(pos):
    return abs(pos[0]) + abs(pos[1])
