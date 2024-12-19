N = int(input())
l = list(map(int, input().split()))

for i in range(N//2):
    l.remove(max(l))
    l.remove(min(l))
    print(*l)