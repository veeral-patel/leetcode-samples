from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head:
            return None

        prev, cur = None, head

        while cur:
            if cur.val == val:
                if prev:
                    prev.next = cur.next
                else:
                    head = cur.next

            prev, cur = cur, cur.next

        return head

    def recursive(self, head, val):
        if not head:
            return None

        if head.val == val:
            return self.removeElements(head.next, val)
        else:
            removed = self.removeElements(head.next, val)
            head.next = removed
            return head
