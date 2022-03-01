from collections import deque
from typing import Optional, List
from functools import reduce

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def pathSum(root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
    if not root:
        return []
    elif root and not root.left and not root.right:
        return [[root.val]] if root.val == targetSum else []
    else:
        leftPaths = pathSum(root.left, targetSum-root.val)
        rightPaths = pathSum(root.right, targetSum-root.val)

        fullLeftPaths = [[root.val]+path for path in leftPaths]
        fullRightPaths = [[root.val]+path for path in rightPaths]
        
        return fullLeftPaths+fullRightPaths

def pathSumDFS(root, targetSum):
    # Iterative, using a queue
    if not root:
        return []
    
    queue = deque()
    answer = []

    queue.append(([], targetSum))

    while queue:
        pathSoFar, desiredSum = queue.popleft()

        # adding initial elements to the queue
        if not pathSoFar:
            if not root.left and not root.right and root.val == desiredSum:
                answer.append([root])
            else:
                if root.left:
                    queue.append(([root, root.left], targetSum-root.val))
                if root.right:
                    queue.append(([root, root.right], targetSum-root.val))
        else:
            lastNode = pathSoFar[-1]
            if not lastNode.left and not lastNode.right and lastNode.val == desiredSum:
                answer.append(pathSoFar)
            else:
                if lastNode.left:
                    queue.append((pathSoFar+[lastNode.left], desiredSum-lastNode.val))
                if lastNode.right:
                    queue.append((pathSoFar+[lastNode.right], desiredSum-lastNode.val))
    
    # convert paths from list of nodes into list of numbers
    formatted = []
    for path in answer:
        formattedPath = []
        for node in path:
            formattedPath.append(node.val)
        formatted.append(formattedPath)

    return formatted

def getTotal(path):
    return reduce(lambda node1, node2: sum(node1.val, node2.val), path)

empty = None
one = TreeNode(5)
two = TreeNode(5, TreeNode(5), TreeNode(4, TreeNode(1), TreeNode(1)))
long = TreeNode(5, TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2))), TreeNode(8, TreeNode(13), TreeNode(4, TreeNode(5), TreeNode(1))))
pathSumDFS(two, 10)