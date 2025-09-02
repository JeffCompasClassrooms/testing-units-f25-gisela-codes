from queue import Queue

def bfs(start, goal, gen_actions):
    q = Queue()
    q.put([(start), [start]])
    visited = set([start])

    generated = 0
    expanded = 0
    max_frontier = 0

    while not q.empty():
        max_frontier = max(max_frontier, q.qsize())

        state, path = q.get()
        expanded += 1   

        if state == goal:
            return path

        actions = gen_actions(state)
        for a in actions:
            generated += 1 
            if a not in visited:
                visited.add(a)
                # q.put((a, path + [(state, a)]))
                q.put((a, path + [a]))

def depth_limited_dfs(state, goal, limit, path, visited, gen_actions):
    expanded = 1
    generated = 0
    max_frontier = len(visited)

    if state == goal:
        return path, generated, expanded, max_frontier

    if limit == 0:
        return "cutoff", generated, expanded, max_frontier

    cutoff_occurred = False
    for a in gen_actions(state):
        generated += 1
        if a not in visited:
            visited.add(a)
            result, g, e, m = depth_limited_dfs(
                a, goal, limit - 1, path + [a], visited, gen_actions
            )
            generated += g
            expanded += e
            max_frontier = max(max_frontier, m)

            if result == "cutoff":
                cutoff_occurred = True
            elif result is not None:
                return result, generated, expanded, max_frontier

    if cutoff_occurred:
        return "cutoff", generated, expanded, max_frontier
    return None, generated, expanded, max_frontier

def ids(start, goal, gen_actions):
    depth_limit = 0
    generated = 0
    expanded = 0
    max_frontier = 0

    while True:
        result, g, e, m = depth_limited_dfs(
            start, goal, depth_limit, [start], set([start]), gen_actions
        )

        generated += g
        expanded += e
        max_frontier = max(max_frontier, m)

        if result not in (None, "cutoff"):  # found path
            return result
        if result is None:  
            return None

        depth_limit += 1


