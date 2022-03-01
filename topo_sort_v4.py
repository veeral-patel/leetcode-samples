from collections import deque

def count_parents(nodes, edges):
    num_parents = {node: 0 for node in nodes}
    for node in nodes:
        for edge in edges:
            if edge[1] == node:
                num_parents[node] += 1
    return num_parents

def topo_sort(nodes, edges):
    if not nodes:
        return []

    num_parents = count_parents(nodes, edges)
    results = []
    queue = deque()

    for node in num_parents:
        if num_parents[node] == 0:
            queue.append(node)

    while queue:
        nxt = queue.popleft()
        results.append(nxt)

        # remove the node from our hashmap
        if nxt in num_parents:
            del num_parents[nxt]

        # decrement number of parents for children
        # of this node
        for edge in edges:
            start, end = edge
            if start == nxt:
                num_parents[end] -= 1

        # add any newly orphaned nodes
        for node in num_parents:
            if num_parents[node] == 0:
                queue.append(node)

    return results

# TODO: handle cycles
