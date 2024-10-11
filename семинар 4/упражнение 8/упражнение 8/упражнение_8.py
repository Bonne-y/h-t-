import random

#создадим 2 списка
l = 10
a_1 = [random.randint(1, 50) for _ in range(l)]
a_2 = [random.randint(1, 50) for _ in range(l)]

print(f'list 1: {a_1}, list 2: {a_2}')

#создадим списки для уникальных эл-ов
ans_1 = set(a_1)
ans_2 = set(a_2)

print(f'unic in 1: {ans_1}, unic in 2: {ans_2}')

#создать список - обьединение только уникальных эл-ов
ans_3 =  ans_1.union(ans_2)

print(f'unic (1+2): {ans_3}')

#создать список - пересечение 
ans_4 = ans_1.intersection(ans_2)

print(f'1 intersec 2: {ans_4}')
 