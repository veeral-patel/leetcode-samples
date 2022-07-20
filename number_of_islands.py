def number_of_islands(grid):
    if not grid:
        return 0

    numberOfRows = len(grid)
    numberOfCols = len(grid[0])

    seen = set()
    numIslands = 0

    for row in range(0, numberOfRows):
        for col in range(0, numberOfCols):
            if grid[row][col] != 1:
                continue
            elif (row, col) in seen:
                continue
            else:
                used = get_connected(grid, row, col)
                seen = seen.union(used)
                numIslands += 1

    return numIslands

# Run DFS to get all pixels connected to the pixel at (r, c)
# with value 1.
def get_connected(grid, r, c):
    if not grid:
        return []

    stack = [(r, c)]
    seen = set()

    while stack:
        nxt = stack.pop()

        if nxt in seen:
            continue

        r, c = nxt

        for neighbor in get_neighbors(grid, r, c):
            row, col = neighbor
            if grid[row][col] == 1:
                stack.append((row, col))

        seen.add(nxt)

    return list(seen)

def get_neighbors(matrix, r, c):
    if not matrix:
        return []

    neighbors = []

    numRows = len(matrix)
    numCols = len(matrix[0])

    OFFSETS = [(-1,0), (1,0), (0,1), (0,-1)]

    for rowOffset, colOffset in OFFSETS:
        if 0 <= r + rowOffset <= numRows-1:
            if 0 <= c + colOffset <= numCols-1:
                neighbors.append((r + rowOffset, c + colOffset))

    return neighbors
