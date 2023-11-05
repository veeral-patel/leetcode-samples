def get_neighbors(combo, trapped_combos):
    POSSIBLE_LETTERS = {
        '0': ['1', '9'],
        '1': ['0', '2'],
        '2': ['1', '3'],
        '3': ['2', '4'],
        '4': ['3', '5'],
        '5': ['4', '6'],
        '6': ['5', '7'],
        '7': ['6', '8'],
        '8': ['7', '9'],
        '9': ['8', '0'],
    }

    ans = []
    for i, letter in enumerate(combo):
        for possible_letter in POSSIBLE_LETTERS[letter]:
            new_num = combo[:i] + possible_letter + combo[i+1:]
            if new_num not in trapped_combos:
                ans.append(new_num)

    return ans

def num_steps(target_combo: str, trapped_combos: List[str]) -> int:
    queue = [(0, '0000')] # (dist, combo)
    seen = set()
    
    while queue:
        nxt_dist, nxt_combo = queue.pop(0)
        if nxt_combo == target_combo:
            return nxt_dist
        
        if nxt_combo not in seen:
            seen.add(nxt_combo)
            for neighbor_combo in get_neighbors(nxt_combo, trapped_combos):
                queue.append((nxt_dist+1, neighbor_combo))
        
    return -1
