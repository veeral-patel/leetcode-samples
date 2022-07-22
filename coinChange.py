import math

def coinChange(coins, amount):
    # Initialize DP array
    dp = [math.inf]*(amount + 1)

    dp[0] = 0

    # Build the DP array
    # Idea is you compute the min coins needed if you take each of
    # the eligible coins (ie coins <= amount).
    for i, _ in enumerate(dp):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i-coin] + 1)


    if dp[amount] == math.inf:
        return -1

    return dp[amount]

