matrix = [[0,1,3,4,1],[3,8,8,3,3],[6,7,8,8,3],[12,2,8,9,1],[12,3,1,3,2]]

def get_neighbors(matrix, i, j):
    num_rows = len(matrix)
    num_cols = len(matrix[0])

    possible_neighbors = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]

    real_neighbors = []
    for neighbor in possible_neighbors:
        nrow, ncol = neighbor
        if nrow >= 0 and nrow <= num_rows-1 and ncol >= 0 and ncol <= num_cols-1:
            real_neighbors.append(neighbor)

    return real_neighbors

# DFS
def flood_fill(r: int, c: int, replacement: int, image: List[List[int]]) -> List[List[int]]:
    stack = [(r, c)]
    seen = set()
    orig_val = image[r][c]
    
    while stack:
        nxt = stack.pop()
        nxtr, nxtc = nxt
        if nxt not in seen:
            seen.add(nxt)
            image[nxtr][nxtc] = replacement
            for neighbor in get_neighbors(image, nxtr, nxtc):
                if image[neighbor[0]][neighbor[1]] == orig_val:
                    stack.append(neighbor)
                
    return image

# BFS
def flood_fill_bfs(r: int, c: int, replacement: int, image: List[List[int]]) -> List[List[int]]:
    queue = [(r, c)]
    seen = set()
    orig_val = image[r][c]
    
    while queue:
        nxt = queue.pop(0)
        nxtr, nxtc = nxt
        if nxt not in seen:
            seen.add(nxt)
            image[nxtr][nxtc] = replacement
            for neighbor in get_neighbors(image, nxtr, nxtc):
                if image[neighbor[0]][neighbor[1]] == orig_val:
                    queue.append(neighbor)
                
    return image
