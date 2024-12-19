#2 строки
a = list(map(int, input().split()))
print(a[-1], *a[:-1])