def wordBreak(s, wordDict):
    if not s:
        return True

    # Initialize DP array
    dp = [False]*len(s)

    # Use hashtable to speed up lookups
    wordDict2 = set(wordDict)

    # Build DP array
    # DP[i] = True if wordBreak(s[i:], wordDict) is True. False otherwise.
    for i in range(len(s)-1, -1, -1):
        if s[i:] in wordDict2:
            dp[i] = True
        else:
            for j in range(i, len(s)):
                if dp[j] and s[i:j] in wordDict2:
                        dp[i] = True


    # We return dp[0] (a boolean) b/c if dp[0] = True
    # then wordBreak(s, wordDict) is True
    return dp[0]
