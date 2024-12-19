a = list(map(int, input().split()))
c_max = 0
c = 0
m = len(a) + 1
for i in a:
    c = a.count(a[i])
    if c > c_max:
        c_max = c
        c = 0
        m = i
print(a[m])