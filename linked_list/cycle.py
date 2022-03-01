# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersection(self, head):
        slow = head
        fast = head

        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return slow

        return None

    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        intersection = self.getIntersection(head)

        if not intersection: # no cycle
            return None

        from_start = head
        from_intersection = intersection

        while from_start != from_intersection:
            from_start = from_start.next
            from_intersection = from_intersection.next

        return from_start

    def usingSpace(self, head):
        indices = {}

        ptr = head
        i = 0

        while ptr:
            if ptr in indices:
                # cycle
                return ptr
            else:
                indices[ptr] = i

            ptr = ptr.next
            i += 1

        return None

a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
a.next = b
b.next = c
c.next = a
