from collections import deque

def task_scheduling(tasks, requirements):
    graph = {}
    for task in tasks:
        graph[task] = []

    for prereq, task in requirements:
        graph[prereq].append(task)

    return topological_sort(graph)

def topological_sort(graph):
    results = []

    # Compute the in-degree for each node
    indegrees = {node: 0 for node in graph}
    for node in graph:
        for child in graph[node]:
            indegrees[child] += 1

    # Build a queue of nodes with zero indegree
    haveZeroIndegree = deque([node for node in indegrees if indegrees[node] == 0])

    # While our queue is not empty...
    while haveZeroIndegree:

        # Take the next node from the queue
        # And move it from the queue
        nxt = haveZeroIndegree.popleft()

        # Add it to our result list
        results.append(nxt)

        # Go through the list of nodes this node points to
        # And update their indegree
        for child in graph[nxt]:
            indegrees[child] -= 1

            # Add check if we can add them to the zero indegree list
            if indegrees[child] == 0:
                haveZeroIndegree.append(child)

    # Return our result list
    return results

def has_cycles(graph):
    return len(topological_sort(graph)) < len(graph)
