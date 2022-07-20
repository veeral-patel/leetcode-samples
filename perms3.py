def permutations(letters):
    def dfs(path, used, res):
        # check if state is a solution
        if len(path) == len(letters):
            res.append(path)

        # make recursive calls
        for i, letter in enumerate(letters):
            if used[i]:
                continue

            # set up call
            used[i] = True
            path.append(letter)

            dfs(path, used, res)

            # roll back
            used[i] = False
            path.remove(letter)

    res = []
    permutations([], [False]*len(letters), res)
    return res

