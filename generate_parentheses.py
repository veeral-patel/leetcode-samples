def generate_parentheses(n):
    def dfs(path, res):
        # check solution
        if len(path) == n * 2:
            res.append(''.join(path))
            return res

        # recurse
        candidates = getCandidates(path, n)
        for candidate in candidates:
            dfs(path + [candidate], res)

    res = []
    dfs([], res)
    return res

def getCandidates(path, n):
    openCount = len([c for c in path if c == '('])

    balance = getBalance(path)

    if openCount == n:
        return [')']
    elif balance <= 0:
        return ['(']
    else:
        return ['(', ')']

def getBalance(path):
    balance = 0
    for c in path:
        if c == '(':
            balance += 1
        else:
            balance -= 1
    return balance
