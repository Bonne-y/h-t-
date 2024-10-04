A = list(map(int, input().split()))
a = A[0]
b = A[1]

def xy(a, b):
    if b == 0:
        return a, 1, 0
    else:
        gcd, x1, y1 = xy(b, a%b)
        x = y1
        y = x1 - (a//b)*y1
        return gcd, x, y

B=(xy(a,b))
print(*B[1::], B[0])