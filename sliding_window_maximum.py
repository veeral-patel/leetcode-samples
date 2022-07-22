def slidingWindowMaximum(nums, k):
    queue = []
    res = []

    for i, num in enumerate(nums):
        while queue and nums[queue[-1]] <= num:
            queue.pop(0)
        queue.append(i)

        if queue[0] == i - k:
            queue.pop(0)

        if i >= k-1:
            res.append(nums[queue[0]])

    return res
