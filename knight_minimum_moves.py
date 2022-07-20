def get_knight_shortest_path(x, y):
    # Run BFS
    queue = []

    queue.append((0, (0, 0)))

    seen = set()

    while queue:
        dist, coord = queue.pop(0)

        row, col = coord

        if coord == (x, y):
            return dist

        if coord in seen:
            continue

        for neighbor in get_neighbors(row, col):
            queue.append((dist + 1, neighbor))

        seen.add(coord)

    return -1

def get_neighbors(row, col):
    OFFSETS = [
        (-2, -1),
        (-1, -2),
        (1, -2),
        (2, -1),
        (-2, -1),
        (-1, 2),
        (1, 2),
        (2, 1)
    ]

    neighbors = []

    for rowOffset, colOffset in OFFSETS:
        neighbors.append((row + rowOffset, col + colOffset))

    return neighbors
