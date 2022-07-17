def backspaceCompare(s, t):
    return getString(s) == getString(t)

def getString(someString):
    stack = []
    for c in someString:
        if c == '#':
            if stack:
                stack.pop()
        else:
            stack.append(c)
    return ''.join(stack)
