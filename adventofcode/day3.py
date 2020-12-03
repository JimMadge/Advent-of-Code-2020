def count_trees(grid, route):
    pos = [0, 0]

    height = len(grid)
    width = len(grid[0])

    trees = 0

    # Top left never has a tree so no need to check initial position
    while pos[0] < height-1:
        pos[0] += route[0]
        pos[1] = (pos[1] + route[1]) % width  # Allow wrapping

        # Inspect current position
        if grid[pos[0]][pos[1]] == "#":
            trees += 1

    return trees


def compare_routes(grid, routes):
    return [count_trees(grid, route) for route in routes]
