with open('input.txt') as f:
    l = [".", "!", "?"]
    c = 0
    for i in f:
        a = i
    for i in range(1, len(a)):
        if a[i-1] in l and not a[i] in l:
            c += 1
    if a[-1] in l:
            c += 1
    print (c)
