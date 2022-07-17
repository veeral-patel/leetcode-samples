def nextGreatestLetter(letters, target):
    low, high = 0, len(letters)-1

    ans = -1

    while low <= high:
        mid = (low+high) // 2
        midLetter = letters[mid]
        if isGreater(midLetter, target):
            high = mid-1
            ans = midLetter
        else:
            low = mid+1

    if ans == -1:
        return letters[0]

    return ans

# Returns true iff a > b
def isGreater(a, b):
    return a > b

def binarySearch(arr, target):
    low, high = 0, len(arr)-1
    while low <= high:
        mid = (low+high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            high = mid-1
        else:
            low = mid+1
    return -1
