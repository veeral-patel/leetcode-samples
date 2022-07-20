def shortest_path(graph, a, b):
    queue = [(a, 0)]
    seen = set()

    while queue:
        nxt, dist = queue.pop(0)

        if nxt == b:
            return dist

        if nxt in seen:
            continue

        for neighbor in graph[nxt]:
            queue.append((neighbor, dist+1))

        seen.add(nxt)

    return -1
