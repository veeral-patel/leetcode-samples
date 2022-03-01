from collections import Counter

def subsets(nums):
    pass

def dfs(nums, so_far, res):
    res.append(so_far)

    available = Counter(nums)-Counter(so_far)
    for num in available:
        if so_far:
            if num > so_far[-1]:
                dfs(nums, so_far+[num], res)
        else:
            dfs(nums, [num], res)
