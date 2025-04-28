import heapq

def bellman_ford(G, start):
    d = {i: float('inf') for i in G}
    d[start] = 0
    for _ in range(len(G)-1):
        for node1 in d:
            for node2 in G.get(node1, {}):
                if d[node2] > d[node1] + G[node1][node2]:
                    d[node2] = d[node1] + G[node1][node2]
    for node1 in d:
        for node2 in G.get(node1, {}):
            if d[node2] > d[node1] + G[node1][node2]:
                print("Граф содержит отрицательный цикл")
                return None
    return d

def dijkstra(G,start):
    distances = {i:float('infinity') for i in G}
    distances[start] = 0
    h = [(0,start)]
    while h:
        cur_dist, cur_node = heapq.heappop(h)
        if cur_dist > distances[cur_node]:
            continue
        for neighbor, weight in G.get(cur_node, {}).items():
            distance = cur_dist + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(h,(distance,neighbor))
    return distances

def johnson(G):

    nG = {k: v.copy() for k, v in G.items()}
    nG['s'] = {}
    for n in G:
        nG['s'][n] = 0
    
    h = bellman_ford(nG, 's')
    if h is None:
        return None
    
    del h['s']
    
    weightG = {}
    for u in G:
        weightG[u] = {}
        for v in G[u]:
            weightG[u][v] = G[u][v] + h[u] - h[v]
    
    dist = {u: {} for u in G}
    
    for u in G:
        dijkstra_dist = dijkstra(weightG, u)
        for v in dijkstra_dist:
            dist[u][v] = dijkstra_dist[v] - h[u] + h[v]
    
    return dist


n = int(input()) # кол-во ребер
    G = {}

for i in range(n):
    v1, v2, w = input().split() # вершина вершина вес
    w = float(w)
    if v1 not in G:
        G[v1] = {}
    G[v1][v2] = w

result = johnson(G)

if result:
    print("Матрица кратчайших расстояний:")
        for u in sorted(result):
            print(f"{u}:", end=" ")
            for v in sorted(result[u]):
                print(f"{v}:{all_pairs_dist[u][v]:.1f}", end=" ")
            print()
