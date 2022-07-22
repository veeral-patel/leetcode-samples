def rob(nums):
    if not nums:
        return 0

    memoized = [0] * len(nums)

    for i, num in enumerate(nums):
        if i == 0 or i == 1:
            memoized[i] = nums[i]
        else:
            memoized[i] = max(memoized[:i-1]) + nums[i]

    return max(memoized)
