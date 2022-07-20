def flood_fill(r, c, replacement, image):
    # get all pixels connected to the pixel at (r, c)
    # with the same color
    connected = get_connected(image, r, c)

    # set all those pixels to be REPLACEMENT color
    for row, col in connected:
        image[row][col] = replacement

    return image

# Run DFS to get all pixels connected to the pixel at (r, c)
# with the same color as the pixel at (r, c).
def get_connected(image, r, c):
    if not image:
        return []

    color = image[r][c]

    stack = [(r, c)]
    seen = set()

    while stack:
        nxt = stack.pop()

        if nxt in seen:
            continue

        r, c = nxt

        for neighbor in get_neighbors(image, r, c):
            row, col = neighbor
            if image[row][col] == color:
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
