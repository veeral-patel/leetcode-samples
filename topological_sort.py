def topological_sort(nodes, edges):
    if not nodes:
        return []

    sort_order = []

    # While there are more nodes:
    while nodes:
        out_degrees = compute_out_degrees(nodes, edges)
        node = get_last_node(out_degrees)

        if not node:
            if len(nodes) >= 2:
                # have a cycle
                return []
            else:
                sort_order.append(nodes[0])
                nodes.remove(nodes[0])
        else:
            sort_order.append(node)
            nodes.remove(node)

    return sort_order

def compute_out_degrees(nodes, edges):
    out_degrees = {}
    for node in nodes:
        out_degrees[node] = 0

    for node in nodes:
        for edge in edges:
            if edge[0] == node:
                out_degrees[node] += 1

    return out_degrees

def get_last_node(out_degrees):
    # Get the first node with a out-degree of 0
    for node, degree in out_degrees.items():
        if degree == 0:
            return node
    return None
