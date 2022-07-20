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
                neighbors.append((rowNum, colNum))

    return neighbors

matrix = [[1,2,3],[4,5,6],[7,8,9]]
