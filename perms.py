from collections import deque

def permutations(letters):
    if not letters:
        return None

    queue = deque()
    answer = []

    queue.append([])

    while queue:
        nxt = queue.popleft()

        if len(nxt) == len(letters):
            answer.append(nxt)
        else:
            missing = set(letters) - set(nxt)
            for missing_letter in missing:
                queue.append(nxt + [missing_letter])

    return answer

