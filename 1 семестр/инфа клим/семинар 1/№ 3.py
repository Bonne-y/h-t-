a = list(map(int, input().split()))
c = 0
count = 0
for i in a:
    c += a[i-1]
    count += 1
print(c/count)
