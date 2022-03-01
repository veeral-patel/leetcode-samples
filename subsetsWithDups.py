from collections import deque

def subsetsWithDups(nums):
    if not nums:
        return None

    answer = []
    queue = deque()

    queue.append([])

    while queue:
        nxt = queue.popleft()

        answer.append(nxt)

        if not nxt:
            for uniqueNum in set(nums):
                queue.append([uniqueNum])
        else:
            candidates = [num for num in nums if num >= nxt[-1]]
            for num in nxt:
                if num in candidates:
                    candidates.remove(num)
            for uniqueCandidate in set(candidates):
                queue.append(nxt+[uniqueCandidate])

    return answer