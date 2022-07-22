def task_scheduling(tasks, requirements):
    graph = {node: [] for node in tasks}

    for prereq, task in requirements:
        graph[prereq].append(task)

    return topological_sort(graph)

def topological_sort(graph):
    order = []

    # populate indegrees map
    indegrees = {node: 0 for node in graph}

    for node in graph:
        for child in graph[node]:
            indegrees[child] += 1

    zeroIndegreeNodes = [node for node in indegrees if indegrees[node] == 0]

    while zeroIndegreeNodes:
        nxt = zeroIndegreeNodes.pop(0)

        order.append(nxt)

        children = graph[nxt]

        for child in children:
            indegrees[child] -= 1
            if indegrees[child] == 0:
                zeroIndegreeNodes.append(child)

    return order
