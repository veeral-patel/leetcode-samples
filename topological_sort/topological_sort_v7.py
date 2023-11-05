def topological_sort(graph):
    # First, compute indegree for each node in the graph
    indegree = {node: 0 for node in graph}
    for node in graph:
        for outgoing_node in graph[node]:
            indegree[outgoing_node] += 1

    zeroIndegreeQueue = [node for node in indegree if indegree[node] == 0]

    ans = []
    while zeroIndegreeQueue:
        nxt = zeroIndegreeQueue.pop(0)
        ans.append(nxt)

        for neighbor in graph[nxt]:
            indegree[neighbor] -= 1

        for neighbor in graph[nxt]:
            if indegree[neighbor] == 0:
                zeroIndegreeQueue.append(neighbor)

        del graph[nxt]

    if len(ans) != len(graph):
        print("Cycle detected")
        return []

    return ans
