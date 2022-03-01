from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = self.toNum(self.toArray(l1))
        num2 = self.toNum(self.toArray(l2))
        total = num1+num2
        return self.reverse(self.toLL(str(total)))

    def reverse(self, ll):
        prev, cur = None, ll

        while cur:
            nxt = cur.next
            cur.next = prev
            prev, cur = cur, nxt

        return prev

    def toLL(self, s):
        if not s:
            return None

        firstS, restS = s[0], s[1:]

        rest = self.toLL(restS)
        first = ListNode(int(firstS), rest)

        return first

    def toNum(self, arr):
        total = 0
        for i, num in enumerate(reversed(arr)):
            total += pow(10, i)*num
        return total

    def toArray(self, ll):
        if not ll:
            return []
        return [ll.val] + self.toArray(ll.next)

    def realWay(self, l1, l2):
        p1 = l1
        p2 = l2

        result = ListNode(0) # sentinel
        rp = result

        carry = 0

        while p1 or p2 or carry:
            if not p1:
                p1 = ListNode(0)
            if not p2:
                p2 = ListNode(0)

            val = sum([p1.val, p2.val, carry]) % 10

            result.next = ListNode(val)
            result = result.next

            carry = sum([p1.val, p2.val, carry]) // 10

            p1 = p1.next
            p2 = p2.next


        return rp.next

