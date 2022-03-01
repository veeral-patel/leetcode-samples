from collections import deque

def count_parents(graph):
    numParents = { node: 0 for node in graph }
    for node in graph:
        for child in graph[node]:
            numParents[child] += 1
    return numParents

def topo_sort(graph):
    q = deque()
    results = []

    # add all nodes without any parents to the queue
    numParents = count_parents(graph)

    for node in graph:
        if numParents[node] == 0:
            q.append(node)

    while q:
        nxt = q.popleft()
        results.append(nxt)

        for child in graph[nxt]:
            numParents[child] = max(0, numParents[child]-1)
            if numParents[child] == 0:
                q.append(child)

    return results
