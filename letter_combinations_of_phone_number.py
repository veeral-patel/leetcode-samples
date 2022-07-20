KEYBOARD = {
    '2': 'abc',
    '3': 'def',
    '4': 'ghi',
    '5': 'jkl',
    '6': 'mno',
    '7': 'pqrs',
    '8': 'tuv',
    '9': 'wxyz',
}

def letter_combinations_of_phone_number(digits):
    def dfs(path, res):
        # check if node is a solution
        if len(path) == len(digits):
            res.append(''.join(path))
            return

        # compute children and recurse
        index = len(path)
        digit = digits[index]
        candidates = KEYBOARD[digit]

        for candidate in candidates:
            dfs(path + [candidate], res)

    res = []
    dfs([], res)
    return res
