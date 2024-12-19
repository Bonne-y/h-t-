letters = str(input())
ans = []

#palindrome?
if len(letters)%2 == 0:
    if letters[:len(letters)//2] == letters[:len(letters)//2-1:-1]:
        ans.append(1)
    else:
        ans.append(0)
else:
    if letters[:len(letters)//2+1] == letters[:len(letters)//2-1:-1]:
        ans.append(1)
    else:
        ans.append(0)

#mirror?
list_1 = ["B", "C", "D", "F", "G", "K", "N", "P", "Q", "R", "0", "4", "6", "7", "9"]
for i in range(len(letters)):
    for j in range(14):
        if letters[i] == list_1[j]:
            ans.append(0)

reflect = []
list_2 = ["A", "H", "I", "M", "O", "T", "U", "V", "W", "X", "Y", "1", "8", "E", "J", "S", "Z", "3", "L", "2", "5"]
if len(letters)%2 == 0:
    for i in letters[:len(letters)//2]:
        for j in range(len(list_2)):
            if i == list_2[j] and j < 13:
                reflect.append(list_2[j])
            elif i == list_2[j] and j >= 13:
                if i == "E":
                    reflect.append("3")
                elif i == "J":
                    reflect.append("L")
                elif i == "S":
                    reflect.append("2")
                elif i == "Z":
                    reflect.append("5")
                elif i == "3":
                    reflect.append("E")
                elif i == "L":
                    reflect.append("J")
                elif i == "2":
                    reflect.append("S")
                elif i == "5":
                    reflect.append("Z")
else:
    for i in letters[:len(letters)//2+1]:
        for j in range(len(list_2)):
            if i == list_2[j] and j < 13:
                reflect.append(list_2[j])
            elif i == list_2[j] and j >= 13:
                if i == "E":
                    reflect.append("3")
                elif i == "J":
                    reflect.append("L")
                elif i == "S":
                    reflect.append("2")
                elif i == "Z":
                    reflect.append("5")
                elif i == "3":
                    reflect.append("E")
                elif i == "L":
                    reflect.append("J")
                elif i == "2":
                    reflect.append("S")
                elif i == "5":
                    reflect.append("Z")

refl_str = ''.join(reflect)

if len(letters)%2 == 0:
    if letters[:len(letters)//2-1:-1] == refl_str:
        ans.append(1)
    else:
        ans.append(0)
else:
    if letters[:len(letters)//2-1:-1] == refl_str:
        ans.append(1)
    else:
        ans.append(0)

if ans[0] == 1 and ans [1] == 1:
    print(f'{letters} is a mirrored palindrome.')
if ans[0] == 1 and ans [1] == 0:
    print(f'{letters} is a regular palindrome.')
if ans[0] == 0 and ans [1] == 1:
    print(f'{letters} is a mirrored string.')
if ans[0] == 0 and ans [1] == 0:
    print(f'{letters} is not a palindrome.')