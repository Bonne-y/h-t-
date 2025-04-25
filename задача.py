import math

def bellman_ford(G, start):
    d = {i: float('inf') for i in G}
    d[start] = 0
    for i in range(len(G)-1):
        for node1 in d:
            for node2 in G.get(node1, {}):
                if d[node2] > d[node1] + G[node1][node2]:
                    d[node2] = d[node1] + G[node1][node2]
    for node1 in d:
        for node2 in G.get(node1, {}):
            if d[node2] > d[node1] + G[node1][node2]:
                return True  
    return False

exchanges = [
    ('RUB', 'USD', 0.013),  # 1 RUB → 0.013 USD
    ('USD', 'EUR', 0.85),    # 1 USD → 0.85 EUR
    ('EUR', 'RUB', 90.0)     # 1 EUR → 90.0 RUB
]
n = 3 # Количество валют

G = {}
for a, b, r in exchanges:
    if a not in G:
        G[a] = {}
    G[a][b] = -math.log(r)

currency = set()
for a, b, r in exchanges:
    currency.add(a)
    currency.add(b)
for c in currency:
    if c not in G:
        G[c] = {}

if bellman_ford(G, 'RUB'):
    print("Можно")
else:
    print("Нельзя")
