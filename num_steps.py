def num_steps(target_combo, trapped_combos):
    # Run BFS
    queue = [(0, '0000')]
    seen = set()

    while queue:
        dist, combo = queue.pop(0)

        if combo == target_combo:
            return dist

        if combo in seen:
            continue

        neighbors = get_neighbors(combo)
        for neighbor in neighbors:
            if neighbor not in trapped_combos:
                queue.append((dist+1, neighbor))

        seen.add(combo)

    return -1

def get_neighbors(combo):
    neighbors = []

    for i, c in enumerate(combo):
        copy = list(combo)

        as_int = int(c)

        lower = (as_int - 1) % 10
        copy[i] = str(lower)
        neighbors.append(''.join(copy))

        higher = (as_int + 1) % 10
        copy[i] = str(higher)
        neighbors.append(''.join(copy))

    return neighbors

