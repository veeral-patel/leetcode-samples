import itertools

def uniqueString(lst):
    hmap = {}
    for i, s in enumerate(lst):
        substrings = generateSubstrings(s)
        for substring in substrings:
            for j, s2 in enumerate(lst):
                if i != j:
                    substrings2 = generateSubstrings(s2)
                    if substring not in substrings2 and s not in hmap:
                        hmap[s] = substring
        if s not in hmap:
            hmap[s] = s

    return hmap

def generateSubstrings(s):
    for i, j in itertools.combinations(range(len(s)+1), 2):
        yield s[i:j]
