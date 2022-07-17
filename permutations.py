def permutations(nums):
    queue = [[]]
    res = []

    while queue:
        nxt = queue.pop(0)
        if len(nxt) == len(nums):
            res.append(nxt)
        else:
            missingNums = set(nums)-set(nxt)
            for mNum in missingNums:
                queue.append(nxt+[mNum])

    return res
