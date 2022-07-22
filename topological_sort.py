def topological_sort(graph):
    order = []

    # initialize indegrees map
    indegrees = {node: 0 for node in graph}

    # and populate it
    for node in graph: # remember to do this!
        for child in graph[node]:
            indegrees[child] += 1

    zeroIndegreeQueue = []

    for node, indegree in indegrees.items():
        if indegree == 0:
            zeroIndegreeQueue.append(node)

    while zeroIndegreeQueue:
        nxt = zeroIndegreeQueue.pop(0)

        order.append(nxt)

        children = graph[nxt]

        for child in children:
            indegrees[child] -= 1

            if indegrees[child] == 0:
                zeroIndegreeQueue.append(child)

    return order

def has_cycle(graph):
    ts = topological_sort(graph)
    return len(ts) < len(graph)

g1 = {4: [2], 2: [1], 3: [1], 1: []}

# has cycle
g2 = {4: [2], 2: [5], 5: [4]}
