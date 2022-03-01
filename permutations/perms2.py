def dfs(state):
    res = []
    if is_solution(state):
        res.append(state[:]) # e.g. add a copy of the state to final result list
        return

    for choice in choices:
        if valid(choice):
            state.add(choice) # make move
            dfs(state)
            state.remove(choice) # backtrack

dfs(root, [])

