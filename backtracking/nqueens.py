import copy

def nQueens(n):
    # build the board
    board = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(".")
        board.append(row)

    # trigger DFS
    res = []
    dfs(board, n, res)
    return res

def printBoard(board):
    for row in board:
        print(" ".join(row))

def dfs(board, n, res):
    placed = getPlaced(board)

    if placed == n:
        if board not in res:
            res.append(copy.deepcopy(board))
        return

    possibleSpots = findNextSpots(board)

    for spot in possibleSpots:
        rowNum, colNum = spot

        board[rowNum][colNum] = "Q"

        dfs(board, n, res)

        # revert board back for next iteration
        board[rowNum][colNum] = "."

def getPlaced(board):
    count = 0
    for row in board:
        for c in row:
            if c == "Q":
                count += 1
    return count

def findNextSpots(board):
    badRows = set()
    badCols = set()
    badDiags = set()
    badNegativeDiags = set()

    # blacklist spots blocked by queens
    for i, row in enumerate(board):
        for j, val in enumerate(row):
            if board[i][j] == "Q":
                badRows.add(i)
                badCols.add(j)
                badDiags.add(i-j)
                badNegativeDiags.add(i+j)

    # build list of eligible next spots
    nextSpots = []
    for i, row in enumerate(board):
        for j, val in enumerate(row):
            cond1 = i not in badRows and j not in badCols
            cond2 = i-j not in badDiags
            cond3 = i+j not in badNegativeDiags
            if cond1 and cond2 and cond3:
                nextSpots.append((i,j))

    return nextSpots

nQueens(4)
