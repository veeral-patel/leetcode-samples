"""
See Algomonster

Given an (unweighted) connected graph, return the length of the shortest path between two nodes A and B, in terms of the number of edges.

Assume there always exists a path between nodes A and B.

Input:

graph = [[1, 2], [0, 2, 3], [0, 1], [1]]
A = 0
B = 3
"""

# Common mistakes
# - Not storing, checking or inserting into seen List
# - Doing pop() instead of pop(0)
def shortest_path(graph: List[List[int]], a: int, b: int) -> int:
    queue = [(0, a)]
    seen = set()
    
    while queue:
        dist, nxt = queue.pop(0)
        
        if nxt == b:
            return dist
        
        if nxt not in seen:
            seen.add(nxt)
            for neighbor in graph[nxt]:
                queue.append((dist+1, neighbor))
                
    return -1
