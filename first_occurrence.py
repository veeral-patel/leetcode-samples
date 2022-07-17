from typing import List

def find_first_occurrence(arr: List[int], target: int) -> int:
    low = 0
    high = len(arr)-1

    ans = -1

    while low <= high:
        mid = (low+high)//2
        if arr[mid] > target:
            # too big: search left
            high = mid-1
        elif arr[mid] < target:
            # too small: search right
            low = mid+1
        elif arr[mid] == target:
            # equals: set ans and search left
            ans = mid
            high = mid-1

    return ans
