from typing import List
import copy

def get_neighbors(board: List[List[int]]):
    zero_r, zero_c = 0, 0
    num_rows, num_cols = len(board), len(board[0])

    # Find zero row
    for i, row in enumerate(board):
        for j, val in enumerate(row):
            if val == 0:
                zero_r, zero_c = i, j

    # Compute all candidates
    all_candidates = [
        (zero_r-1, zero_c),
        (zero_r+1, zero_c),
        (zero_r, zero_c-1),
        (zero_r, zero_c+1),
    ]

    # Filter candidates
    candidates = []
    for row_num, col_num in all_candidates:
        if 0 <= row_num <= num_rows-1 and 0 <= col_num <= num_cols-1:
            candidates.append((row_num, col_num))

    # Generate new boards
    boards = []
    for row_num, col_num in candidates:
        new_board = copy.deepcopy(board)
        new_board[zero_r][zero_c] = board[row_num][col_num]
        new_board[row_num][col_num] = 0 
        boards.append(new_board)

    return boards

def is_end_board(board: List[List[int]]):
    flat = []
    for lst in board:
        for elem in lst:
            flat.append(elem)
    
    failed = False
    for i, elem in enumerate(flat):
        if i == len(flat)-1:
            if elem != 0:
                failed = True
        elif elem != i+1:
            failed = True

    return not failed

def num_steps(init_pos: List[List[int]]) -> int:
    queue = [(0, init_pos)] # (dist, board)
    seen = []

    while queue:
        dist, board = queue.pop(0)

        if is_end_board(board):
            return dist

        if board not in seen:
            seen.append(board)
            for neighbor in get_neighbors(board):
                queue.append((dist + 1, neighbor))

    return -1
