# Examples
# () => true
# (] => false
# (()) => true
# ([)) => false
# ([[[((({{{{(())}}}})))]]]) = true

def valid_parentheses(s):
    stack = []

    for c in s:
        if c in ['(', '[', '{']:
            stack.append(c)
        else:
            nxt = stack.pop()
            if c == ')' and nxt != '(':
                return False
            elif c == ']' and nxt != '[':
                return False
            elif c == '}' and nxt != '{':
                return False

    if stack:
        return False

    return True

assert valid_parentheses('()')
assert valid_parentheses('')
assert valid_parentheses('{}')
assert valid_parentheses('[]')
assert valid_parentheses('[({})]')

assert not valid_parentheses('(]')
assert not valid_parentheses('(])')
assert not valid_parentheses('(){}(){')

print("tests passed")
