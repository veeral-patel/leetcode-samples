# https://leetcode.com/problems/reverse-string-ii/
class Solution:
    # What is the T.C.?
    def reverseStr(self, s: str, k: int) -> str:
        # optimization: use a string builder instead
        output = ""

        left = 0

        while left <= len(s)-1:
            if left + k > len(s)-1:
                to_reverse = s[left:]
                output = output + to_reverse[::-1]
            else:
                to_reverse = s[left:left+k]
                output = output + to_reverse[::-1]

                to_keep = s[left+k:left+2*k]
                output = output + to_keep

            left = left + 2*k

        return output

sol = Solution()
