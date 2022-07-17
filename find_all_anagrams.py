def find_all_anagrams(original, check):
    if not original:
        return []
    elif len(original) < len(check):
        return []

    start = 0
    end = len(check)-1

    res = []

    while end <= len(original):
        window = original[start:end+1]

        if sorted(window) == sorted(check):
            # found anagram
            res.append(start)

        start += 1
        end += 1

    return res
