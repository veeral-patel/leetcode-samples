from typing import List

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def zig_zag_traversal(root: Node) -> List[List[int]]:
    # Idea: Do a level order traversal then flip every other row
    queue = [(1, root)]
    ans = []
    
    while queue:
        level, nxt = queue.pop(0)
        
        if len(ans) < level:
            ans.append([nxt.val])
        else:
            ans[level-1].append(nxt.val) # ans[-1] should work too
            
        if nxt.left:
            queue.append((level + 1, nxt.left))
         
        if nxt.right:
            queue.append((level + 1, nxt.right))
            
    for i, _ in enumerate(ans):
        if i % 2 == 1:
            ans[i] = list(reversed(ans[i]))
            
    return ans
