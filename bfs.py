from collections import deque

def bfs(graph, a):
    queue = deque()
    seen = set()

    order = []

    queue.append((a, 0))

    while queue:
        nxt, nextLevel = queue.popleft()
        if nxt not in seen:
            seen.add(nxt)
            order.append((nxt, nextLevel))
            for neighbor in graph[nxt]:
                queue.append((neighbor, nextLevel+1))

    return order

def getDistance(graph, a, b):
    bfsOrder = bfs(graph, a)
    for node, level in bfsOrder:
        if node == b:
            return level

graph = { 0: [1, 2], 1: [0, 2, 3], 2: [0, 1], 3: [1] }
