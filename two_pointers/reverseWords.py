from typing import List

class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # First, reverse the words
        start = 0
        end = len(s)-1

        while start < end:
            s[start], s[end] = s[end], s[start]
            start, end = start+1, end-1

        # Then, reverse each word
        start = 0
        end = 0

        nextSpace = 0

        while end < len(s) and nextSpace < len(s):
            while nextSpace < len(s) and s[nextSpace] != " ":
                nextSpace = nextSpace+1

            while start < end:
                s[start], s[end] = s[end], s[start]
                start, end = start+1, end-1

            start, end = nextSpace+1, nextSpace+1
