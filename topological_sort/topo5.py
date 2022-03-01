def topological_sort(graph):
    zeroIndegreeNodes = []
    result = []

    # Build in-degree for each node
    indegree = {node: 0 for node in graph}

    for node in graph:
        for child in graph[node]:
            indegree[child] += 1

    # Find nodes with 0 in-degree
    zeroIndegreeNodes = [node for node in graph if indegree[node] == 0]

    # Process nodes with in-degree 0
    while zeroIndegreeNodes:
        # Remove from our list of zero indegree nodes
        znode = zeroIndegreeNodes.pop(0)

        # Add to our sorted list
        result.append(znode)

        # Update in-degree for children
        for child in graph[znode]:
            indegree[child] -= 1
            if indegree[child] == 0:
                zeroIndegreeNodes.append(child)

    return result

def has_cycles(graph):
    ts = topological_sort(graph)
    return not len(ts) == len(graph)
