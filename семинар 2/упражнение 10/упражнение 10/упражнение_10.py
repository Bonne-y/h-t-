# |����� ������ ���� ����� ����� | ���(��)��(��) ��(��)��(��)��(��) ��(��)��(��) ��(��)���(��) ��(��)���(��)| 
# |����� ������ ������� ��������������� | �����(��) ��(��)����(��) ��(��)��(��)���(��) ��(��)��(��)�����(��)���(��)���|

#����, ��� �� ������������ ���������...

# | proso koleso maso lasso serso | pro(so)so(so) k�(s�)l�(s�)s�(s�) ma(so)s�(s�) l�(s�)ss�(s�) s�(s�)rs�(s�) | 
# | ��rt� paela delitsa radioactivnost | ��rt�(s�) pa(s�)ela(sa) de(se)li(si)tsa(sa) r�(s�)di(si)oakti(si)vno(s�)st |

with open('input.txt') as f:
    l = ["a", "e", "y", "u", "i", "o"]
    ans =[]

    for i in f:
        a = i

    ans.append(a[0])

    for i in range(1, len(a)):
        if a[i] not in l:
            ans.append(a[i])
        elif a[i-1] not in l and a[i-1] != " ":
            ans.append(a[i])
            ans.append("s")
            ans.append(a[i])
        else:
            ans.append(a[i])
        k = ''.join(ans)
        print(k)