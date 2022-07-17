def find_min_rotated(arr):
    if not arr:
        return -1

    first = arr[0]

    low = 0
    high = len(arr)-1

    ans = 0

    while low <= high:
        mid = (low+high) // 2

        if arr[mid] < first: # smaller/left side of pivot
            # search left
            ans = mid
            high = mid-1
        elif arr[mid] >= first: # greater/right side of pivot or equals pivot
            # search right
            low = mid+1

    return ans

