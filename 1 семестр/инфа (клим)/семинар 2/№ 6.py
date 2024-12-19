a = list(map(int, input().split()))

c = 0

for i in a:
    for j in a:
        if i == j:
            c += 1
    if c == 1:
        print(i)
    c = 0