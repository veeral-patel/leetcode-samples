import string

def word_ladder(begin, end, word_list):
    # Run BFS
    queue = [(0, begin)]
    seen = set()

    while queue:
        dist, word = queue.pop(0)

        if word == end:
            return dist

        if word in seen:
            continue

        neighbors = get_neighbors(word, word_list)
        for neighbor in neighbors:
            queue.append((dist+1, neighbor))

        seen.add(word)

    return -1

def get_neighbors(word, word_list):
    neighbors = []

    for i, c in enumerate(word):
        for letter in string.ascii_letters:
            copy = list(word)

            copy[i] = letter

            copyAsString = ''.join(copy)

            if copyAsString in word_list:
                neighbors.append(copyAsString)

    return neighbors

