def climbingStairs(n):
    # Ideas
    # DP

    # Thoughts
    # Either climb 1, then solve climbingStairs(n-1)
    # or climb 2, then solve climbingStairs(n-2)
    # So it's climbingStairs(n-1) + climbingStairs(n-2)

    # Base case
    # n = 0 => 0
    # n = 1 => 1
    # n = 2 => 2
    # n = 3 = cs(1) + cs(2) = 3

    # Just solve fibonacci

    # Can do it top down recursive
    # Or memoize
    # Use Fibonacci formula

    if n <= 2:
        return n

    memoized = [0]*(n+1)

    memoized[1] = 1
    memoized[2] = 2

    for i in range(3, n+1):
        memoized[i] = memoized[i-1] + memoized[i-2]

    return memoized[n]
