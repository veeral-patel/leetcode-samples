from typing import List

def find_boundary(arr: List[bool]) -> int:
    low, high = 0, len(arr)-1
    ans = -1

    while low <= high:
        mid = (low+high)//2
        if arr[mid]:
            # found a True, so update answer, search left
            ans = mid
            high = mid-1
        else:
            # search right
            low = mid+1

    return ans
