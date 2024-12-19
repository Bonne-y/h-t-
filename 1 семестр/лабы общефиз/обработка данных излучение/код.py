with open('experiment.txt') as f: # experiment.txt - ���� � ����� ��������
    t = int(input()) # t = �� ������� ���������� (10, 20, 40, 80)
    s = []
    c = 0
    for i, line in enumerate(f):
        if i > 1 and i < 4002:
            if (i-1) % t != 0:
                c += int(line)
            else: 
                s.append(c)
                c = 0

    for i in range(len(s)//10): # ����� ��������� �� 10 �������� � ������, ������ & - ���������� �������� ������� � ����
        print(i*10,"& ", end='')
        for j in range(10):
            print (s[i*10+j], end=' & ')
        print("")
    
    a=[]
    for i in s: # ����� ���������, ����� �������, ���� �������     ��������������, �� �� ������� ������
        a.append(f'number of impulses: {i} number of cases: {s.count(i)} proportion of cases: {s.count(i)/len(s)}')
    a = sorted(a)
    for i in range(len(a)):
        print(a[i])

    q = 0
    p = (sum(s))
    for i in s:
        q+=((i-(p/50)))**2
    print ("---", q, "---")