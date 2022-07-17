def peak_of_mountain_array(arr):
    low, high = 0, len(arr)-1

    ans = -1

    while low <= high:
        mid = (low+high) // 2

        if mid == len(arr)-1: # last element
            # search left
            high = mid-1
            continue
        elif mid == 0: # first element
            # search right
            low = mid+1
            continue

        nxt = mid+1

        if arr[mid] < arr[nxt]: # increasing
            # search right
            low = mid+1
            ans = mid
        elif arr[mid] > arr[nxt]: # decreasing
            # search left
            high = mid-1

    return arr[ans]
