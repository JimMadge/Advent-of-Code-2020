from enum import Enum, auto


class Direction(Enum):
    EAST = auto()
    NORTH = auto()
    WEST = auto()
    SOUTH = auto()


def translate(pos, direction, distance):
    if direction == "N":
        pos = (pos[0]+distance, pos[1])
    elif direction == "S":
        pos = (pos[0]-distance, pos[1])
    elif direction == "E":
        pos = (pos[0], pos[1]+distance)
    elif direction == "W":
        pos = (pos[0], pos[1]-distance)

    return pos


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
        pos = (pos[0], pos[1]+distance)
    elif heading == Direction.NORTH:
        pos = (pos[0]+distance, pos[1])
    elif heading == Direction.WEST:
        pos = (pos[0], pos[1]-distance)
    elif heading == Direction.SOUTH:
        pos = (pos[0]-distance, pos[1])

    return pos


def update_position(instruction, pos, heading):
    action, arg = instruction[0], int(instruction[1:])

    if action in ["N", "S", "E", "W"]:
        pos = translate(pos, action, arg)
    elif action in ["L", "R"]:
        heading = turn(heading, action, arg)
    elif action == "F":
        pos = forward(pos, heading, arg)

    return pos, heading


def follow_route(route):
    pos = (0, 0)
    heading = Direction.EAST
    for instruction in route.splitlines():
        pos, heading = update_position(instruction, pos, heading)

    return pos, heading


def manhattan_distance(pos):
    return abs(pos[0]) + abs(pos[1])


def rotate(waypoint, direction, degrees):
    n_turns = degrees // 90

    for i in range(n_turns):
        if direction == "L":
            waypoint = (waypoint[1], -waypoint[0])
        if direction == "R":
            waypoint = (-waypoint[1], waypoint[0])

    return waypoint


def forward2(pos, waypoint, distance):
    return (pos[0]+waypoint[0]*distance, pos[1]+waypoint[1]*distance)


def update_position2(instruction, pos, waypoint):
    action, arg = instruction[0], int(instruction[1:])

    if action in ["N", "S", "E", "W"]:
        waypoint = translate(waypoint, action, arg)
    elif action in ["L", "R"]:
        waypoint = rotate(waypoint, action, arg)
    elif action == "F":
        pos = forward2(pos, waypoint, arg)

    return pos, waypoint


def follow_route2(route):
    pos = (0, 0)
    waypoint = (1, 10)
    for instruction in route.splitlines():
        pos, waypoint = update_position2(instruction, pos, waypoint)

    return pos
