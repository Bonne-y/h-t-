def triangle(size,symb):
        i = 1
        while (i < size/2):
            print(i*symb)
            i+=1
        if i == size/2:
            print(i*symb)
        while (i >= 1):
            print(i*symb)
            i-=1

a = list(input().split())
size = int(a[0])
symb = a[1]
triangle(size, symb)
