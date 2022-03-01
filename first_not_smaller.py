from typing import List

def first_not_smaller(arr, target):
    low, high = 0, len(arr)-1
    firstIndex = -1
    while low <= high:
        mid = (low+high)//2
        if arr[mid] >= target:
             # found a valid one => search left to look for a smaller one
            firstIndex = mid
            high = mid-1
        else:
            # search right
            low = mid+1
    return firstIndex

assert first_not_smaller([], 0) == -1
assert first_not_smaller([1], 0) == 0
assert first_not_smaller([0, 1], 0) == 0
assert first_not_smaller([0, 1, 5, 6, 6], 6) == 3
print("tests passed")


def first_occurrence(arr, target):
    low, high = 0, len(arr)-1
    first = -1

    while low <= high:
        mid = (low+high) // 2
        if arr[mid] == target:
            first = mid
            # search left to look for earlier index
            high = mid-1
        elif arr[mid] > target:
            # search left to look for index
            high = mid-1
        else:
            # search right to look for index
            low = mid+1

    return first


'''
Example 2

[0, 1, 5, 6, 6]
low = 0
high = 4
mid = 2

arr[mid] = 5

Example 1

[1]
low = 0
high = 0
mid = 0
target = 0

arr[mid] = 1

firstIndex = 0
'''
