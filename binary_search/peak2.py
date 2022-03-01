def peak(arr):
    low, high = 0, len(arr)-1

    while low <= high:
        mid = (low+high)//2

        print(arr[low], arr[high], arr[mid])

        if arr[mid] > arr[mid-1]:
            # search right
            low = mid+1
        else:
            # search left
            high = mid-1

    return high
