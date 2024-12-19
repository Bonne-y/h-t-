# |просо колесо м€со лассо серсо | про(со)со(со) ко(со)ле(се)со(со) м€(с€)со(со) ла(са)ссо(со) се(се)рсо(со)| 
# |јќрта пјЁль€ делитс€ рад»ќјктивность | јќрта(са) пј(са)Ёль€(са) де(се)ли(си)тс€(с€) ра(са)д»(си)ќјкти(си)вно(со)сть|

#окей, оно не воспринимает кириллицу...

# | proso koleso maso lasso serso | pro(so)so(so) kо(sо)lе(sе)sо(sо) ma(so)sо(sо) lа(sа)ssо(sо) sе(sе)rsо(sо) | 
# | јќrtа paela delitsa radioactivnost | јќrtа(sа) pa(sа)ela(sa) de(se)li(si)tsa(sa) rа(sа)di(si)oakti(si)vno(sо)st |

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