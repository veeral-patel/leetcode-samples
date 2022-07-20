def word_break(s, words):
    if s == "":
        return True

    for word in words:
        if s.startswith(word):
            if word_break(s[len(word):], words):
                return True

    return False
