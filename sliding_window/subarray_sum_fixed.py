from typing import List

"""
Given an array (list) nums consisted of only non-negative integers, find the largest sum among all subarrays of length k in nums.

For example, if the input is nums = [1, 2, 3, 7, 4, 1], k = 3, then the output would be 14 as the largest length 3 subarray sum is given by [3, 7, 4] which sums to 14.
"""

def subarray_sum_fixed(nums: List[int], k: int) -> int:
    left, right = 0, k
    ans = float("-inf")
    
    while right <= len(nums):
        window = nums[left:right]
        ans = max(sum(window), ans)
        left += 1
        right += 1
        
    return ans
