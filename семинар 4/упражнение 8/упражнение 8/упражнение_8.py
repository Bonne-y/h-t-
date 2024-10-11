import random

#создадим 2 списка
l = 10
a_1 = [random.randint(1, 50) for _ in range(l)]
a_2 = [random.randint(1, 50) for _ in range(l)]

print(f'a_1: {a_1}, a_2: {a_2}')

#создадим списки для уникальных эл-ов
ans_1 = [n for n in a_1]
ans_2 = [m for m in a_2]

#оставим только уникальные в первом списке
c = 0
for i in range(len(a_1)):
    for j in range(len(ans_1)):
        if a_1[i] == ans_1[j] and i!=j:
            ans_1[i] = 0
            ans_1[j] = 0
            c += 2
for l in range(c):
    ans_1.remove(0)

#оставим только уникальные во втором списке
c = 0
for i in range(len(a_2)):
    for j in range(len(ans_2)):
        if a_2[i] == ans_2[j] and i!=j:
            ans_2[i] = 0
            ans_2[j] = 0
            c += 2
for l in range(c):
    ans_2.remove(0)

print(f'ans_1: {ans_1}, ans_2: {ans_2}')

#создать список - обьединение
a_3 = [i for i in a_1.union(a_2)]

print(a_3)
 