import string

def get_neighbors(begin, word_list):
    ans = []
    for i, letter in enumerate(begin):
        for new_letter in string.ascii_letters:
            new_string = begin[:i] + new_letter + begin[i+1:]
            if new_string in word_list:
                ans.append(new_string)
    return ans

def word_ladder(begin, end, word_list):
    queue = [(0, begin)] # (dist, word)
    seen = set()

    while queue:
        dist, word = queue.pop(0)

        if word == end:
            return dist

        if word not in seen:
            seen.add(word)
            for neighbor in get_neighbors(word, word_list):
                queue.append((dist + 1, neighbor))

    return -1
