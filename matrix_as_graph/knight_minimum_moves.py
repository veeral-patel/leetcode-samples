def get_knight_shortest_path(x: int, y: int) -> int:
    queue = [(0, (0, 0))]
    seen = set()
    
    while queue:
        dist, nxt = queue.pop(0)
        
        if nxt == (x, y):
            return dist
        
        if nxt not in seen:
            seen.add(nxt)
            for neighbor in get_neighbors(nxt[0], nxt[1]):
                queue.append((dist+1, neighbor))
                
    return -1
                

def get_neighbors(r, c):
    OFFSETS = [
        (-2, -1),
        (-1, -2),
        (-2, 1),
        (-1, 2),
        (2, -1),
        (1, -2),
        (2, 1),
        (1, 2)
    ]
    
    ans = []
    for ro, co in OFFSETS:
        ans.append((r + ro, c + co))
        
    return ans
