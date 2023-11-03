class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def valid_bst(root: Node) -> bool:
    if not root: return True
    return root.val > max_descendant(root.left) and root.val < max_descendant(root.right)

def max_descendant(root: Node) -> int:
    if not root: return float("-inf")
    max_left = max_descendant(root.left) if root.left else float("-inf")
    max_right = max_descendant(root.right) if root.right else float("-inf")
    return max(max_left, max_right, root.val)
