def subarray_sum(arr, target):
    # build prefix sums array
    prefixSums = [0]*len(arr)
    for i in range(len(prefixSums)):
        if i == 0:
            prefixSums[i] = arr[i]
        else:
            prefixSums[i] = arr[i] + prefixSums[i-1]

    print(prefixSums)

    # build hashmap
    hmap = {}
    for i, prefixSum in enumerate(prefixSums):
        hmap[target-prefixSum] = i

    return hmap
