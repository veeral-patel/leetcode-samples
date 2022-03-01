def binarySearch(arr):
    low, high = 0, len(arr)-1
    index = -1

    while low <= high:
        mid = (low+high)//2
        if arr[mid] > arr[mid+1]:
            # right side of mountain
            index = mid
            # search left
            high = mid-1
        else:
            # left side of mountain
            # search right
            low = mid+1

    return index
