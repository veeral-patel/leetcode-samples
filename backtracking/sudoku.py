def sudoku(board):
    dfs(board)

def printBoard(board):
    for row in board:
        print(" ".join(row))

def dfs(board):
    if isValid(board):
        return board

    rowNum, colNum = getFirstMissingPiece(board)
    if rowNum == -1 and colNum == -1:
        # board is full but not valid => exit
        print("board is full but not valid")
        return None

    candidates = getCandidates(board, rowNum, colNum)

    for candidate in candidates:
        # modify board
        board[rowNum][colNum] = candidate

        # check if this board can lead to a valid state
        result = dfs(board)
        
        # if so, return this board
        if result:
            return board
        else:
            # if not revert this board back so the
            # next iteration will work
            board[rowNum][colNum] = "."

def isValid(board):
    for rowNum in range(len(board)):
        row = board[rowNum]
        if len(set(row)) != 9:
            return False

    for colNum in range(len(board[0])):
        numsInCol = [row[colNum] for row in board if row[colNum] != "."]
        if len(set(numsInCol)) != 9:
            return False

    for rowNum in range(0, 2+1):
        for colNum in range(0, 2+1):
            numsInBox = getNumsInBox(board, rowNum, colNum)
            if len(set(numsInBox)) != 9:
                return False

    return True

def getFirstMissingPiece(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == ".":
                return i, j
    return -1, -1

def getCandidates(board, rowNum, colNum):
    allowed = set(str(digit) for digit in range(1,9+1))
    numsInBox = getNumsInBox(board, rowNum, colNum)
    numsInRow = [num for num in board[rowNum] if num != "."]
    numsInCol = [row[colNum] for row in board if row[colNum] != "."]
    diff = allowed-set(numsInBox)-set(numsInRow)-set(numsInCol)
    return diff

def getNumsInBox(board, rowNum, colNum):
    res = []
    for i in range(len(board)):
        for j in range(len(board[0])):
            if i // 3 == rowNum // 3 and j // 3 == colNum // 3 and board[i][j] != ".":
                res.append(board[i][j])
    return res

board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]

solution = [["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]]

almostDone = [[".",".",".",".","7",".",".","1","2"],["6",".","2",".",".","5",".","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]]

grid01 = '''
003020600
900305001
001806400
008102900
700000008
006708200
002609500
800203009
005010300
'''

def parseGrid(grid):
    parsed = [list(s) for s in grid.split()]
    for row in parsed:
        for i in range(len(row)):
            if row[i] == '0':
                row[i] = "."
    return parsed

grid08 = '''
480006902
002008001
900370060
840010200
003704100
001060049
020085007
700900600
609200018
'''

grid09 = '''
000900002
050123400
030000160
908000000
070000090
000000205
091000050
007439020
400007000
'''

parsed = parseGrid(grid09)
sudoku(parsed)