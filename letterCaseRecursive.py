def letterCasePermutations(s):
    if not s:
        return s

    ans = []

    for c in s:
        if not ans:
            if c.isalpha():
                ans.append(c.lower())
                ans.append(c.upper())
            else:
                ans.append(c)
        else:
            for a in ans:
                if c.alpha():
                    a += c.lower()
                    a += c.upper()
                else:
                    a += str(c)

    return ans
