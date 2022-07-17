from typing import List

def search(nums: List[int], target: int) -> int:
    low, high = 0, len(nums)-1

    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            high = mid-1
        else:
            low = mid+1
    return -1
