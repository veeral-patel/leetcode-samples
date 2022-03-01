def find_min_rotated(arr):
    low, high = 0, len(arr)-1
    answer = 0

    while low <= high:
        mid = (low+high)//2
        # if our pivot is...
        # greater than last element
        # middle is to the right
        if arr[mid] > arr[-1]:
            low = mid+1

        # less than last element
        # middle is to the left
        else:
            answer = mid
            high = mid-1

    return answer
