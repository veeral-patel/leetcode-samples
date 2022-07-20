import math

def combinations(n, k):
    def dfs(path, res):
        # check state
        if len(path) == k:
            res.append(path)
            return

        # compute candidates
        # which are all numbers in 1, 2, ... n that are greater
        # than largest element in path
        largestInPath = path[-1] if path else -math.inf

        candidates = [num for num in range(1, n+1) if num > largestInPath]

        for candidate in candidates:
            dfs(path + [candidate], res)

    res = []
    dfs([], res)
    return res

