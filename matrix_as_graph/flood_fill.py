def get_neighbors(matrix, i, j):
    neighbors = []

    delta_row = [-1, 0, 1]
    delta_col = [-1, 0, 1]

    for drow in delta_row:
        for dcol in delta_col:
            rrow, rcol = i+drow, j+dcol
            if rrow >= 0 and rrow <= len(matrix)-1 and rcol >= 0 and rcol <= len(matrix[0])-1:
                neighbors.append((rrow, rcol))

    return neighbors

# This is not correct; it does not update neighbors 
# of neighbors of the target which have the same color
def flood_fill(r, c, replacement, image):
    val = image[r][c]
    image[r][c] = replacement

    neighbors = get_neighbors(image, r, c)
    for i2, j2 in neighbors:
        if image[i2][j2] == val:
            image[i2][j2] = replacement

    return image

def bfs(graph, a):
    queue = deque()
    seen = set()

    order = []

    queue.append((a, 0))

    while queue:
        nxt, nextLevel = queue.popleft()
        if nxt not in seen:
            seen.add(nxt)
            order.append((nxt, nextLevel))
            for neighbor in graph[nxt]:
                queue.append((neighbor, nextLevel+1))

    return order

image = [[0,1,3,4,1],[3,8,8,3,3],[6,7,8,8,3],[12,2,8,9,1],[12,3,1,3,2]]

