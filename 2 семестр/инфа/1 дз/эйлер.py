def dfs(G, visited, start):
    visited.append(start)
    for i in G[start]:
        if i not in visited:
            dfs(G, visited, i)

def connect(G):
    if not G:
        return True  
    visited = []
    start_node = next(iter(G))  
    dfs(G, visited, start_node)
    return len(visited) == len(G)

def path(G):
    if not is_connected(G):
        return None
    
    degrees = {n: 0 for n in G}
    for n in G:
        degrees[n] = len(G[n])
        
    odd = []
    for n in degrees:
        if degrees[n] % 2 != 0:
            odd.append(n)
    if len(odd) not in [0, 2]:
        return None
    
    if odd:
        start = odd[0]
    else:
        start = next(iter(G))

    st = [start]
    path = []
    nG = {n: set(neighbors) for n, neighbors in G.items()}

    while st:
        cur = st[-1]
        if nG[cur]:
            nextt = nG[cur].pop()
            st.append(nextt)
        else:
            path.append(st.pop())
    
    path = path[::-1]
    
    return path

G = {
    0: {1, 2},
    1: {0, 2, 3},
    2: {0, 1, 4, 5},
    3: {1, 4},
    4: {2, 3, 5},
    5: {2, 4, 6},
    6: {5}
    }
    
    euler = path(G)
    if euler:
        print("Эйлеров путь:", " → ".join(map(str, euler_path)))
    else:
        print("Эйлеров путь не существует")
