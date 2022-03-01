def get_neighbors(matrix, i, j):
    neighbors = []

    if i > 0:
        neighbors.append((i-1, j))

    if j > 0:
        neighbors.append((i, j-1))

    if i < len(matrix)-1:
        neighbors.append((i+1, j))

    if j < len(matrix[0])-1:
        neighbors.append((i, j+1))

    return neighbors

def get_neighbor_values(matrix, val):
    for i, row in enumerate(matrix):
        for j, col in enumerate(row):
            if matrix[i][j] == val:
                neighbors = get_neighbors(matrix, i, j)
                for i2, j2 in neighbors:
                    print(matrix[i2][j2])

matrix=[[0,1,2],[3,4,5],[6,7,8]]
