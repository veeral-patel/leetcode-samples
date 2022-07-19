# https://algo.monster/problems/subarray_sum

# Rule of thumb for prefix sum problems
# sum(arr, i, j) = ps[j] if i = 0
#                = ps[j] - ps[i-1] otherwise
# where ps is the prefix sums array
# and sum(arr, i, j) is sum of ARR from indices i to j inclusive

def subarraySum(arr, target):
    # Build a array of prefix sums
    prefixSums = getPrefixSums(arr)

    # Check for subarrays starting from the beginning
    for j, ps in enumerate(prefixSums):
        if ps == target:
            return [0, j+1]

    # Check for other subarrays
    for j in range(len(prefixSums)):
        for i in range(j):
            if prefixSums[j]-prefixSums[i] == target:
                return [i+1,j+1]

    return []

def getPrefixSums(arr):
    if not arr:
        return []

    prefixSums = [0]*len(arr)

    for i, num in enumerate(arr):
        if i == 0:
            prefixSums[i] = arr[i]
        else:
            prefixSums[i] = prefixSums[i-1] + num

    return prefixSums
