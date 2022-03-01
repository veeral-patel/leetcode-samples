from collections import Counter

def permutations(letters):
    res = []
    dfs(letters, [], res)
    return res

def dfs(letters, so_far, res):
    if len(so_far) == len(letters):
        res.append(so_far)

    else:
        available = Counter(letters)-Counter(so_far)
        for available_letter in available:
            dfs(letters, so_far+[available_letter], res)
