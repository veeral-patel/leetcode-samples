from typing import List

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def level_order_traversal(root: Node) -> List[List[int]]:
    if not root: return []
    
    queue = [(1, root)]
    ans = []
    
    while queue:
        level, nxt = queue.pop(0)
        
        if len(ans) < level:
            ans.append([nxt.val])
        else:
            ans[level-1].append(nxt.val)
        
        if nxt.left:
            queue.append((level+1, nxt.left))
        
        if nxt.right:
            queue.append((level+1, nxt.right))
    
    return ans
