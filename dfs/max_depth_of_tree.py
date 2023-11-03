class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def tree_max_depth(root: Node) -> int:
    if not root: return 0
    max_left = 1 + tree_max_depth(root.left) if root.left else 0
    max_right = 1 + tree_max_depth(root.right) if root.right else 0
    return max(max_left, max_right)
