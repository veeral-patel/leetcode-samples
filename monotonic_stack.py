from typing import List

def sliding_window_maximum(nums: List[int], k: int) -> List[int]:
    if not nums:
        return []

    start, end = 0, k
    window_maxes = []

    while end <= len(nums):
        window = nums[start:end]

        window_maxes.append(max(window))

        start += 1
        end += 1

    return window_maxes

assert sliding_window_maximum([], 1) == []
assert sliding_window_maximum([1], 1) == [1]
assert sliding_window_maximum([1,2], 1) == [1,2]
assert sliding_window_maximum([1,2], 2) == [2]
assert sliding_window_maximum([1,3,2,5,8,7], 3) == [3,5,8,8]
print("tests passed")
