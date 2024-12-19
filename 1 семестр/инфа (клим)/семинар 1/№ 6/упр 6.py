with open('input.txt') as f:
    numbers = 0
    symbol = []
    base = 0
    for i, line in enumerate(f):
        if i == 0:
            numbers = (line.strip())
        if i == 1:
            symbol.append(line.strip())
        if i == 2:
            base = (int(line.strip())) #������� ������ � �������, ������ �������� � ��������� ������� ���������

    separate = numbers.split() #������ ����� ��������� �� ���������

    separate_10 = []
    for i in range(len(separate)):
        separate_10.append(int(separate[i], base)) #����� ���������� � 10-����

    ans = 0
    if symbol[0] == '+':
        ans = 0
    if symbol[0] == '-':
        ans = separate_10[0]*2
    if symbol[0] == '*':
        ans = 1          #����������� "�����"

    for i in range(len(separate)):
        if symbol[0] == '+':
            ans += separate_10[i]
        if symbol[0] == '-':
            ans -= separate_10[i]
        if symbol[0] == '*':
            ans = ans*separate_10[i]

ans_base = ''

while ans > 0:
    ans_base = str(ans % base) + ans_base
    ans = ans//base

f = open('output.txt', 'w')
f.write(ans_base)
f.close()
