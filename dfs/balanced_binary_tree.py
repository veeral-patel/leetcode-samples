class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def is_balanced(tree: Node) -> bool:
    if not tree: return True
    return is_balanced(tree.left) and is_balanced(tree.right) and abs(height(tree.left) - height(tree.right)) <= 1

def height(tree: Node) -> int:
    if not tree: return 0
    return 1 + max(height(tree.left), height(tree.right))
