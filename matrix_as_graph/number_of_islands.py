def get_neighbors(grid: int, r: int, c: int):
    num_rows, num_cols = len(grid), len(grid[0])
    
    row_offsets = [-1, 1, 0, 0]
    col_offsets = [0, 0, 1, -1]
    
    ans = []
    
    for ro, co in zip(row_offsets, col_offsets):
        if 0 <= r + ro <= num_rows-1 and 0 <= c + co <= num_cols-1:
            ans.append((r + ro, c + co))
                
    return ans

def dfs(grid, i, j):
    stack = [(i, j)]
    seen = set()
    
    while stack:
        nxt = stack.pop()
        if nxt not in seen and grid[nxt[0]][nxt[1]] == 1:
            seen.add(nxt)
            for neighbor in get_neighbors(grid, nxt[0], nxt[1]):
                stack.append(neighbor)
                
    return seen

def count_number_of_islands(grid: List[List[int]]) -> int:
    all_discovered = set()
    num_islands = 0
    
    for i, row in enumerate(grid):
        for j, val in enumerate(row):
            if val == 1 and (i, j) not in all_discovered:
                newly_discovered = dfs(grid, i, j)
                all_discovered = all_discovered.union(newly_discovered)
                num_islands += 1
                
