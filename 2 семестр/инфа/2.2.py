def dfs(u, G, matching, visited):
    for v in G[u]:
        if v not in visited:
            visited.add(v)
            if matching[v] is None or dfs(matching[v], G, matching, visited):
                matching[v] = u
                matching[u] = v
                return True
    return False

def kuhn(G, left_nodes):
    matching = {n: None for n in G}
    for u in left_nodes:
        if matching[u] is None:  
            visited = set()
            dfs(u, G, matching, visited)
    return matching

def work(G, left_nodes):
    matching = kuhn(G, left_nodes)
    cover = set()
    for u, v in matching.items():
        if v is not None and (v, u) not in cover:
            cover.add((u, v))
    covered = {u for pair in cover for u in pair}
    for u in G:
        if u not in covered:
            for v in G[u]:  
                cover.add((u, v))
                covered.update({u, v})
                break
    return cover

G = {
    0: {3, 4},
    1: {3},
    2: {4, 5},
    3: {0, 1},
    4: {0, 2},
    5: {2}
    }
left_nodes = {0, 1, 2}
ans = work(G, left_nodes)
print("Минимальное рёберное покрытие:", ans)
