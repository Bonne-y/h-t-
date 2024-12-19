a = list(input().split())
length = int(a[0])
letters = str(a[1])

list_l = []
count = 0
word = ''

for i in range(len(letters)):
    if count < length:
        word += letters[i]
        count += 1
    else:
        list_l.append(word)
        word = letters[i]
        count = 1
list_l.append(word)

ans=''
for i in range (len(list_l)):
    for j in range(length):
        b = list_l[i]
        ans += b[-(j+1)]

print (ans)
