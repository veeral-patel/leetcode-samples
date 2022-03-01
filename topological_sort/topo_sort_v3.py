from collections import deque

def count_parents(graph):
    counts = { node: 0 for node in graph }
    for parent in graph:
        for node in graph[parent]:
            counts[node] += 1
    return counts


def topo_sort(graph):
    res = []
    q = deque()
    counts = count_parents(graph)
    for node in counts:
        if counts[node] == 0:
            q.append(node)
    while len(q) > 0:
        node = q.popleft()
        res.append(node)
        for child in graph[node]:
            counts[child] -= 1
            if counts[child] == 0:
                q.append(child)
    return res

