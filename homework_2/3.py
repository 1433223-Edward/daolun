def is_valid_state(state):
    if (state[1] == state[2] and state[0] != state[1]) or (state[2] == state[3] and state[0] != state[2]):
        return False
    return True

def dfs(state, visited, path):
    if state == (0, 0, 0, 0):
        print(path)
        return True

    visited.add(state)
    for i in range(2):
        for j in range(4):
            new_state = list(state)
            new_state[0] ^= 1
            new_state[j] ^= i

            if tuple(new_state) not in visited and is_valid_state(new_state):
                if dfs(tuple(new_state), visited, path + [tuple(new_state)]):
                    return True

    visited.remove(state)
    return False

initial_state = (1, 1, 1, 1)
visited = set()
path = [initial_state]

dfs(initial_state, visited, path)
