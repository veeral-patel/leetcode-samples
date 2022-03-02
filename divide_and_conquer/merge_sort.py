
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    n = len(arr)
    pivot = n // 2

    left = merge_sort(arr[:pivot])
    right = merge_sort(arr[pivot:])

    result = merge(left, right)

    return result

def merge(arr1, arr2):
    # Merge the two arrays using two pointers
    p1, p2 = 0, 0
    merged = []

    while p1 < len(arr1) and p2 < len(arr2):
        v1, v2 = arr1[p1], arr2[p2]
        if v1 < v2:
            merged.append(v1)
            p1 += 1
        else:
            merged.append(v2)
            p2 += 1
    
    # Add the remaining elements
    merged.extend(arr1[p1:])
    merged.extend(arr2[p2:])

    return merged

assert merge_sort([]) == []
assert merge_sort([1]) == [1]
assert merge_sort([1,2]) == [1,2]
assert merge_sort([2,1]) == [1,2]
assert merge_sort([2,1,4,2,3]) == [1,2,2,3,4]
print('tests passed')