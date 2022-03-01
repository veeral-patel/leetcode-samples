# from algomonster
def bfs(root):
    queue = deque([root])
    while len(queue) > 0:
        node = queue.popleft()
        for child in node.children:
            if OK(child):
                return FOUND(child)
            queue.append(child)
    return NOT_FOUND
