from collections import deque


def letterCasePermutation(s):
    if not s:
        return s

    queue = deque()
    answer = []

    queue.append((s, 0))

    while queue:
        perm, index = queue.popleft()

        # at the end: add to our list of results
        if index == len(s):
            answer.append(perm)
        else:
            lst = list(perm)            
            char = lst[index]

            if char.isalpha():
                lst[index] = lst[index].lower()
                with_lower = "".join(lst)
                queue.append((with_lower, index+1))

                lst[index] = lst[index].upper()
                with_upper = "".join(lst)
                queue.append((with_upper, index+1))
            else:
                queue.append((perm, index+1))

    return answer

letterCasePermutation('a1b')