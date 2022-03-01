from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        arr = self.toArray(head)
        return self.arrIsPalindrome(arr)

    def toArray(self, head):
        if not head:
            return []
        return [head.val] + self.toArray(head.next)

    def arrIsPalindrome(self, arr):
        if not arr:
            return True
        elif len(arr) == 1:
            return True
        else:
            first, last = arr[0], arr[len(arr)-1]
            return first == last and self.arrIsPalindrome(arr[1:len(arr)-1])


sol = Solution()
empty = None
one = ListNode(1)
node = ListNode(3, ListNode(4, ListNode(3)))
node2 = ListNode(3, ListNode(4, ListNode(5)))

assert sol.isPalindrome(empty)
assert sol.isPalindrome(one)
assert sol.isPalindrome(node)
assert not sol.isPalindrome(node2)
print("tests passed")
