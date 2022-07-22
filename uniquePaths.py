import math

def uniquePaths(m, n):
    dp = [[math.inf] * n] * m

    # You can only get to the elements in the first col one way,
    # by going straight down
    for i in range(m):
        dp[i][0] = 1

    # You can only get to the elements in the first row one way,
    # by going straight to the right
    for j in range(n):
        dp[0][j] = 1

    # All the rest, you can get either by coming down or coming from the left
    # So just add up those already computed numbers.
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]

    # And return the number for the last element in the grid
    return dp[m-1][n-1]
