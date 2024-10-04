import numpy as np

def spiral(n,m):
    A = np.zeros((n,m))
    a , i , j = 1 , 0 , 0
    while (a < m*n):
            while (j+1 < m and A[i][j+1]==0 ):
                A[i][j] = a
                a += 1
                j += 1
            while(i+1 < n and A[i+1][j]==0 ):
                A[i][j] = a
                a += 1
                i += 1 
            while (j > 0 and A[i][j-1]==0 ):
                A[i][j] = a
                a += 1
                j -= 1
            while(i > 0 and A[i-1][j]==0 ):
                A[i][j] = a
                a += 1
                i -= 1 
    A[i][j] = a
    return A

L = list(map(int, input().split()))
a = L[0]
b = L[1]
B = spiral(a,b)
for i in range(a):
    for j in range(b):
        B[i][j] = B[i][j]*i
print(B)
        
