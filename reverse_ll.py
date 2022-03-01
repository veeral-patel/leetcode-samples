class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Exercise: see if I can do this both recursively and iteratively

# Iterative
def reverse(node):
    prev, cur = None, node
    while cur:
        # save the next node
        # if you don't do this, the reference to the next node will be lost
        nxt = cur.next

        # point current node to previous node
        cur.next = prev

        # move forward
        prev, cur = cur, nxt

    return prev

# Recursive
def reverse2(node):
    if not node:
        return None
    elif not node.next:
        return node
    else:
        in_reverse = reverse2(node.next)
        in_reverse.next = node
        return in_reverse

node = ListNode(1, ListNode(2, ListNode(3)))
