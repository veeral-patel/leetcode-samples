"""
Find the length of the longest substring of a given string without repeating characters.

Input: abccabcabcc

Output: 3

Explanation: longest substrings are abc, cab, both of length 3

Input: aaaabaaa

Output: 2

Explanation: ab is the longest substring, length 2
"""

def longest_substring_without_repeating_characters(s: str) -> int:
    left, right = 0, 1
    ans = float("-inf")
    
    while right <= len(s):
        window = s[left:right]
        if len(window) == len(set(window)): # no repeats
            ans = max(len(window), ans)
            right += 1
        else:
            left += 1
     
    return ans
