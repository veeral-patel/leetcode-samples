from typing import List

def threeSum(nums):
    # Ideas
    # 1) Sort then for each number run 2Sum with two pointers. O(n log n) + O(n*n) = O(n^2) T, O(1) S
    # 2) Run 2Sum for each number using hashtable. O(n^2) T, O(n^2) S
    # (Check that the TCs above are right)
    nums.sort()

    answer = set()

    # overall: O(n^2) T
    for i, num in enumerate(nums): # O(n) T
        rest = [nums[j] for j in range(len(nums)) if i != j] # O(n) T
        ts = twoSumSorted1(rest, -num) # O(n) T
        for pair in ts: # O(n) T
            triplet = pair+[num] # O(1) T
            triplet = tuple(triplet)
            if triplet not in answer:
                answer.add(triplet)

    return answer

def twoSumSorted1(nums: List[int], target: int) -> List[int]:
    # Only works for pre-sorted input arrays
    # Any number of matches, return all pairs of indices
    # O(n log n) T, O(1) S
    if not nums:
        return []
    
    start = 0
    end = len(nums)-1

    pairs = []

    while start < end:
        num1, num2 = nums[start], nums[end]
        total = num1 + num2 
        if total == target:
            pairs.append([num1, num2])
            end -= 1
        elif total < target:
            start += 1
        else:
            end -= 1

    return pairs

def twoSumSorted2(nums: List[int], target: int) -> List[int]:
    # Only works for pre-sorted input arrays
    # Exactly one match, return indices
    # O(n log n) T, O(1) S
    if not nums:
        return []
    
    start = 0
    end = len(nums)-1

    while start < end:
        num1, num2 = nums[start], nums[end]
        total = num1 + num2 
        if total == target:
            # to satisfy https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
            return [start+1, end+1]
        elif total < target:
            start += 1
        else:
            end -= 1

    return []