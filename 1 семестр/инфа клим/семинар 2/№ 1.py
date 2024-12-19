a = list(map(int, input().split()))

count = 0
for i in range(1, len(a)):
    count += a[i]

s = 0
for i in range(a[0] + 1):
    s+= i

print(s - count)