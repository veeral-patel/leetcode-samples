import collections

def minimum_window_substring(original, check):
    if not original:
        return ""

    start = 0
    end = 0

    res = ""

    while end <= len(original):
        window = original[start:end+1]

        print(window)

        if is_subset(check, window):
            # satisfies condition
            if not res:
                res = window
            else:
                res = get_smaller(res, window)
            start += 1
        else:
            end += 1

    return res

# TODO: break ties

def is_subset(check, window):
    ccounter = collections.Counter(check)
    wcounter = collections.Counter(window)

    for kc in ccounter:
        if kc not in wcounter:
            return False
        if ccounter[kc] > wcounter[kc]:
            return False

    return True

def get_smaller(s1, s2):
    if len(s1) == len(s2):
        return min(s1, s2)
    else:
        return min(s1,s2,key=len)
