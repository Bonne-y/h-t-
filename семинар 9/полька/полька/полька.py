equation = list(str(input()))


def reorder(li):
    ans = []
    memory = []
    symbol = ["*", "/", "+", "-"]
    j = 1
    f = 0
    c = -1
    for i in range (len(li)):
        if f == 0:
            if li[i] not in symbol:
                memory += li[i]
            else:
                j = 1
                while i+j <= len(li)-1 and li[i+j] not in symbol:
                    memory += li[i+j]
                    j += 1
                    f += 1
                ans += memory
                ans += li[i]
                memory = []
        else:
            f -= 1

        i += j
        while "(" in ans:
            ans.remove("(")
        while ")" in ans:
            ans.remove(")")
    return (ans)




def memorable(li):
    ans = []
    symbol = ["*", "/", "+", "-"]
    i = 0
    while i < len(li):
        if li[i] == "(":
            for j in range (len(li)-i-1, 1, -1):
                while  j <= len(li)-1 and li[j] != ")":
                    j+=1

            ans += reorder(li[i:j])
            li = li[:i] + li[j+1:]

        elif li[i] == "*" or li[i] == "/":
            l = i-1
            m = i+1
            while l >= 0 and li[l] not in symbol:
                l -= 1
            while m <= len(li)-1 and li[m] not in symbol:
                m += 1
            ans += reorder(li[l+1:m])
            li = li[:l+1] + li[m:]

        i+=1
    ans += reorder(li)
    return (ans)






print ("reverse polish: ", *memorable(equation))

