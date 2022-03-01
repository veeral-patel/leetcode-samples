# Goals
# 1) Write tests and get them to pass
# 2) Get provided tests to pass on first try
# 3) Compute TC and SC correctly

def is_isomorphic(s1, s2):
    # Two strings are isomorphic if any letter c in s1 is mapped to the same
    # letter d in s2 across both strings
    # In addition, two characters cannot map to the same character

    # Approach: build a hashmap to store the mapping between characters c in s1 and
    # characters d in s2
    if len(s1) != len(s2):
        return False

    forward = {} # s1 to s2 mapping
    backward = {} # s2 to s1 mapping

    for i in range(len(s1)):
        c, d = s1[i], s2[i]
        if c in forward:
            # If an already mapped character maps to something else,
            # then not isomorphic
            if forward[c] != d:
                return False
        else:
            forward[c] = d

        # Mapped another character to d already => not isomorphic
        if d in backward:
            if backward[d] != c:
                return False
        else:
            backward[d] = c

    return True

assert is_isomorphic("", "")
assert is_isomorphic("a", "a")
assert is_isomorphic("a", "k")
assert is_isomorphic("aaa", "bbb")
assert not is_isomorphic("aaa", "bcd")
assert not is_isomorphic("ab", "cc")
assert not is_isomorphic("wow", "aaa")
assert is_isomorphic("egg", "all")
print('tests passed')
