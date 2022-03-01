class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse(node):
    prev, cur = None, node

    while cur:
        nxt = cur.next

        cur.next = prev

        prev, cur = cur, nxt

    return prev
