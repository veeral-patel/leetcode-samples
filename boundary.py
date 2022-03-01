from typing import List

def find_boundary(arr: List[int]) -> int:
    left, right = 0, len(arr) - 1
    answer = -1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid]:
            # got True, so search left to see if we
            # can get a earlier True
            answer = mid
            right = mid-1
        else:
            # got False, so search right
            left = mid+1

    return answer

assert find_boundary([]) == -1
assert find_boundary([True]) == 0
assert find_boundary([False, True]) == 1
assert find_boundary([False, False, True]) == 2
assert find_boundary([False, False, True, True]) == 2
assert find_boundary([False, False, False]) == -1
assert find_boundary([True, True, True]) == 0
assert find_boundary([False, False, True, True, True]) == 2
print("tests passed")

'''
Example 1

arr = [False, False, True, True]

low = 0
high = 3

mid = 3 // 2 = 1

arr[mid] = arr[1] = False
arr[mid+1] = arr[2] = True

return 2


Example 2

arr = [False, True]

low = 0
high = 1
mid = 0

arr[mid] = False
arr[mid+1] = True

return 1

Example 3

arr = [True]
low = 0
high = 0
mid = 0

will fail (out of bounds error)

Example 4

arr = [False, False, True]
'''
