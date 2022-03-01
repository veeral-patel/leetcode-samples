from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

root = TreeNode(3)
root.left = TreeNode(9, TreeNode(5))
root.right = TreeNode(20, left=TreeNode(15), right=TreeNode(7, TreeNode(33)))

def bfs(root):
    queue = deque()
    output = []

    queue.append(root)

    while queue:
        nxt = queue.popleft()
        output.append(nxt.val)

        if nxt.left:
            queue.append(nxt.left)

        if nxt.right:
            queue.append(nxt.right)

    return output

def levelOrder(root):
    if not root:
        return []

    answer = []

    queue = deque()
    queue.append((root, 0))

    while queue:
        node, nodeLevel = queue.popleft()

        if nodeLevel >= len(answer):
            answer.append([])
        answer[nodeLevel].append(node.val)

        if node.left:
            queue.append((node.left, nodeLevel+1))
        if node.right:
            queue.append((node.right, nodeLevel+1))

    return answer
