from collections import deque, Counter

def combine(n, k):
    nums = list(range(1, n+1))

    queue = deque()
    answer = []

    queue.append([])

    while queue:
        nxt = queue.popleft()
        if len(nxt) == k:
            answer.append(nxt)
        elif nxt:
            missing_nums = Counter(nums)-Counter(nxt)
            missing_nums = [num for num in missing_nums if num > nxt[-1]]
            for num in missing_nums:
                queue.append(nxt+[num])
        else:
            for num in nums:
                queue.append([num])

    return answer

def subsets(nums):
    if not nums:
        return None

    queue = deque()
    answer = []

    queue.append([])

    while queue:
        nxt = queue.popleft()
        answer.append(nxt)

        if nxt:
            missing_nums = Counter(nums)-Counter(nxt)
            for mnum in missing_nums:
                if mnum > nxt[-1]:
                    queue.append(nxt+[mnum])
        else:
            missing_nums = nums
            for mnum in missing_nums:
                queue.append([mnum])

    return answer
