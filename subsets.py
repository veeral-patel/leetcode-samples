# https://algo.monster/problems/subsets_backtracking
def subsets(nums):
    def dfs(path, level, res):
        if level == len(nums):
            res.append(path)
            return # don't forget this!

        dfs(path + [nums[level]], level+1, res)
        dfs(path, level+1, res)

    res = []
    dfs([], 0, res)
    return res
