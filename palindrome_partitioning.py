def palindromePartitioning(s):
    def dfs(path, currentIndex, res):
        if currentIndex == len(s):
            res.append(path)
            return

        for endIndex in range(currentIndex, len(s)+1):
            substring = s[currentIndex:endIndex]
            if substring and substring == substring[::-1]:
                dfs(path + [substring], endIndex, res)

    res = []
    dfs([], 0, res)
    return res
