with open('input.txt') as f:
    numbers = 0
    symbol = []
    for i, line in enumerate(f):
        if i == 0:
            numbers = (line.strip())
        if i == 1:
            symbol.append(line.strip())

    separate = []
    a = 0
    for i in range (len(numbers)):
        if (numbers[i] == ' ') == False:
            a = a*10
            a += int(numbers[i])
        else:
            separate.append(a)
            a = 0
    separate.append(a)

    ans = 0
    if symbol[0] == '+':
        ans = 0
    if symbol[0] == '-':
        ans = separate[0]*2
    if symbol[0] == '*':
        ans = 1

    for i in range(len(separate)):
        if symbol[0] == '+':
            ans += separate[i]
        if symbol[0] == '-':
            ans -= separate[i]
        if symbol[0] == '*':
            ans = ans*separate[i]
    print(ans)

f = open('output.txt', 'w')
f.write(str(ans))
f.close()