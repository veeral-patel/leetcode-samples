def maxSubarray(nums):
    # Ideas
    # Two pointers - no
    # Sliding window - no
    # DP- yes
    if not nums:
        return 0

    memoized = [float("-inf")]*len(nums)

    for i, num in enumerate(nums):
        if i == 0:
            memoized[i] = num
        else:
            memoized[i] = max(memoized[i-1]+num, num)

    return max(memoized)
