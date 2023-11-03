class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def insert_bst(bst: Node, val: int) -> Node:
    if not bst: return Node(val)
    
    if val < bst.val:
        if bst.left:
            new_left = insert_bst(bst.left, val)
            return Node(bst.val, new_left, bst.right)
        else:
            new_left = Node(val)
            return Node(bst.val, new_left, bst.right)
    
    if val > bst.val:
        if bst.right:
            new_right = insert_bst(bst.right, val)
            return Node(bst.val, bst.left, new_right)
        else:
            new_right = Node(val)
            return Node(bst.val, bst.left, new_right)
        
    return bst
