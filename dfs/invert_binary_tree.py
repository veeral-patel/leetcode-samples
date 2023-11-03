class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def invert_binary_tree(tree: Node) -> Node:
    if not tree: return tree
    return Node(tree.val, left=invert_binary_tree(tree.right), right=invert_binary_tree(tree.left))
