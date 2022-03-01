def longestValidString(s):
    if not s:
        return ''

    longest = ''
    start, end = 0, 0
    while end <= len(s):
        window = s[start:end]
        if isValid(window):
            if len(window) > len(longest):
                longest = window
            end = end + 1
        else:
            start = start + 1

    return longest

def isValid(s):
    if len(s) <= 2:
        return True

    start = 0
    end = 3

    while end <= len(s):
        window = s[start:end]

        all_as = all([c == 'a' for c in window])
        all_bs = all([c == 'b' for c in window])

        if all_as or all_bs:
            return False

        else:
            start = start + 1
            end = end + 1

    return True

assert isValid("")
assert isValid("aabb")
assert isValid("aabbaabb")
assert isValid("aabbaabbaabb")
assert not isValid("aaa")
assert not isValid("aaaa")
assert not isValid("bbbb")
print("isValid tests passed")


assert longestValidString("") == ""
assert longestValidString("aaaa") == "aa"
assert longestValidString("bbbb") == "bb"
assert longestValidString("abab") == "abab"
assert longestValidString("aabbaaaaabb") == "aabbaa"
assert longestValidString("aabbaabbaabbaaa") == "aabbaabbaabbaa"
print("longestValidString tests passed")
