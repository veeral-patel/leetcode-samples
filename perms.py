from collections import Counter

def permutations(lst):
    if not lst:
        return []

    queue = [[]]

    ans = []

    while queue:
        nxt = queue.pop(0)
        if len(nxt) == len(lst):
            ans.append(nxt)
        else:
            missing = Counter(lst) - Counter(nxt)
            for char in missing:
                queue.append(nxt + [char])

    return ans
