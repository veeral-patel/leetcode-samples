import math

def get_neighbors(matrix, row, col):
    if not matrix:
        return []

    # Can't do a OFFSETS = [-1,0,1] list b/c it will include
    # diagonol elements

    OFFSETS = [(0,-1), (0,1), (-1,0), (1,0)]

    neighbors = []

    numRows = len(matrix)
    numCols = len(matrix[0])

    for rowOffset, colOffset in OFFSETS:
            rowNum = row + rowOffset
            colNum = col + colOffset

            if 0 <= rowNum <= numRows-1 and 0 <= colNum <= numCols-1:
                if matrix[row][col] >= 0: # 0 or INF
                    neighbors.append((rowNum, colNum))

    return neighbors

def get_dist_to_closest_exit(matrix, row, col):
    if not matrix:
        return []

    queue = [(0, (row, col))]
    seen = set()

    while queue:
        nxt = queue.pop(0)

        dist, coord = nxt

        r, c = coord

        if coord in seen:
            continue

        if matrix[r][c] == 0: # hit exit
            return dist

        neighbors = get_neighbors(matrix, r, c)

        for neighbor in neighbors:
            queue.append(((dist + 1), neighbor))

        seen.add(coord)

def walls_and_gates(matrix):
    for i, row in enumerate(matrix):
        for j, col in enumerate(row):
            if matrix[i][j] > 0: # is a INF
                dist = get_dist_to_closest_exit(matrix, i, j)
                matrix[i][j] = dist

    return matrix

INF = math.inf

dungeon_map = [
  [INF, -1, 0, INF],
  [INF, INF, INF, -1],
  [INF, -1, INF, -1],
  [0, -1, INF, INF],
]
