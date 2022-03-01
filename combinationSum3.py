from collections import deque, Counter

def combinations(target, k):
    nums = list(range(1, 9+1))

    if not nums:
        return []

    queue = deque()
    answer = []

    queue.append([])

    while queue:
        nxt = queue.popleft()
        if sum(nxt) == target and nxt not in answer and len(nxt) == k:
            answer.append(nxt)
        elif not nxt:
            missingNums = [num for num in nums if num <= target]
            for num in missingNums:
                queue.append([num])
        else:
            missingNums = Counter(nums)-Counter(nxt)
            missingNums = [num for num in missingNums if num >= nxt[-1]]
            missingVal = target-sum(nxt)
            for num in missingNums:
                if num <= missingVal:
                    queue.append(nxt+[num])

    return answer
