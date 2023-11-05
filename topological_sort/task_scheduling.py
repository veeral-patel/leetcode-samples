from typing import List

def task_scheduling(tasks: List[str], requirements: List[List[str]]) -> List[str]:
    # Build adjacency list
    graph = {task: [] for task in tasks}
    for prereq, task in requirements:
        graph[prereq].append(task)

    # Compute indegrees
    indegrees = {node: 0 for node in graph}
    for node in graph:
        for out_node in graph[node]:
            if out_node in indegrees:
                indegrees[out_node] += 1
            else:
                indegrees[out_node] = 1
                
    # Run topological sort
    zeroIndegreeQueue = [node for node in graph if indegrees[node] == 0]
    ans = []
    while zeroIndegreeQueue:
        nxt = zeroIndegreeQueue.pop(0)

        ans.append(nxt)

        for neighbor in graph[nxt]:
            indegrees[neighbor] -= 1
            if indegrees[neighbor] == 0:
                zeroIndegreeQueue.append(neighbor)

        del graph[nxt]

    if len(tasks) != len(ans):
        # Cycle detected
        return []

    return ans
