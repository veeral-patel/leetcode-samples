def get_neighbors(grid: int, r: int, c: int) -> List[(int, int)]:
    num_rows, num_cols = len(grid), len(grid[0])
    
    row_offsets = [-1, 0, 1]
    col_offsets = [-1, 0, 1]
    
    ans = []
    
    for ro in row_offsets:
        for co in col_offsets:
            if 0 <= r + ro <= num_rows-1 and 0 <= c + co <= num_cols-1:
                ans.append((r + ro, c + co))
                
    return ans

