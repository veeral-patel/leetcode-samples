from collections import deque

def combinationSum(nums, target):
    if not nums:
        return []

    answer = []
    queue = deque()
    queue.append([])

    while queue:
        nxt = queue.popleft()
        if sum(nxt) == target:
            answer.append(nxt)
        elif nxt:
            missingVal = target-sum(nxt)
            for num in nums:
                if num <= missingVal and num >= nxt[-1]:
                    queue.append(nxt+[num])
        else:
            missingVal = target-sum(nxt)
            missingNums = [num for num in nums if num <= missingVal]
            for num in missingNums:
                queue.append([num])

    return answer
