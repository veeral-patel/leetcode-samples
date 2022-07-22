import math

def lis(nums):
    # Initialize dp array
    # dp[i] = LIC ending at index i
    dp = [-math.inf]*(len(nums))

    # Remember to set initial element!
    dp[0] = 1

    # Build dp array
    for i in range(len(nums)):
        if i == 0:
            continue
        for j in range(0, i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[j]+1, dp[i])
        dp[i] = max(dp[i], 1)

    return max(dp)
