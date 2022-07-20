def decode_ways(digits):
    def dfs(path, currentIndex, res):
        # check if solution
        if currentIndex == len(digits):
            res.append(path)
            return

        # recurse on next digit
        currentDigit = digits[currentIndex]
        dfs(path + [currentDigit], currentIndex+1, res)

        # recurse on next 2 digits IF there are 2 more digits
        # and next two digits are <= 26
        if currentIndex <= len(digits)-2:
            currentTwoDigits = digits[currentIndex:currentIndex+2]
            dfs(path + [currentTwoDigits], currentIndex+2, res)

    if not digits:
        return 0

    res = []
    dfs([], 0, res)
    return len(res)
