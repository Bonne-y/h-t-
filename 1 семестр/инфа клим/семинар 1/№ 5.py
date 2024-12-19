N = input()
b = int(input())
c = int(input())

N_10 = int(N,b)
N_c = ''

while N_10 > 0:
    N_c = str(N_10 % c) + N_c
    N_10 = N_10//c

print(N_c)
