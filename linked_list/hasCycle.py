class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def hasCycle(head):
    # Ideas
    # Two pointers. O(1) S, O(n) T
    # Hashset. O(n) S, O(n) T

    seen = set()

    ptr = head

    while ptr:
        if ptr in seen:
            return True
        else:
            seen.add(ptr)
            ptr = ptr.next

    return False

def hasCycle2(head):
    slow = head
    fast = head

    while slow and fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return False
