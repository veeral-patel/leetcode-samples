def mono_stack(entries):
    stack = []

    for entry in entries:
        while stack and stack[-1] <= entry:
            stack.pop()

        stack.append(entry)

    return stack
