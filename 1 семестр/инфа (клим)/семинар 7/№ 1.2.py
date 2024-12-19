
import itertools
import numpy as np
import math
import decimal

class Vector():
    def __init__(self, x, y, z):
        assert type(float(x)) == float, 'Строка должна содержать только числа'
        assert type(float(y)) == float, 'Строка должна содержать только числа'
        assert type(float(z)) == float, 'Строка должна содержать только числа'
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)

    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y, self.z + other.z)
        elif isinstance(other, int) or isinstance(other, float):
            return Vector(self.x + other, self.y + other, self.z + other)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, other):
        if isinstance(self, Vector) and isinstance(other, Vector):
            a = (self.x, self.y, self.z)
            b = (other.x, other.y, other.z)
            return np.matmul(a, b)

        elif isinstance(self, Vector) and (isinstance(other, int) or isinstance(other, float)):
            return Vector(self.x * other, self.y * other, self.z * other)

    def __abs__(self):
        return ((self.x) ** 2 + (self.y) ** 2 + (self.z) ** 2) ** (0.5)


    def __str__(self):
        return f"x = {self.x}, y = {self.y}, z = {self.z}"
def max_square(data_list):
    square_list = []
    itertools.combinations(vectors, 3)
    for q in itertools.combinations(vectors, 3):

        x1, y1, z1 = float(q[0][0]), float(q[0][1]), float(q[0][2])
        x2, y2, z2 = float(q[1][0]), float(q[1][1]), float(q[1][2])
        x3, y3, z3 = float(q[2][0]), float(q[2][1]), float(q[2][2])

        len_1 = decimal.Decimal(math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2))
        len_2 = decimal.Decimal(math.sqrt((x2 - x3) ** 2 + (y2 - y3) ** 2 + (z2 - z3) ** 2))
        len_3 = decimal.Decimal(math.sqrt((x1 - x3) ** 2 + (y1 - y3) ** 2 + (z1 - z3) ** 2))

        p = decimal.Decimal((len_1 + len_2 + len_3) / 2)

        square = decimal.Decimal(math.sqrt(p * abs(p - len_1) * abs(p - len_2) * abs(p - len_3)))
        square_list.append(square)

    return round(max(square_list), 5)

print('Введите радиус-векторы точек(координаты) каждый в новой строчке.')
vectors = []
lines = True
while lines != []:
    lines = list(input().split())
    if lines: vectors.append(lines)

sum_vector = Vector(0, 0, 0)
for i in range(0, len(vectors)):
    sum_vector += Vector(float(vectors[i][0]), float(vectors[i][1]), float(vectors[i][2]))

center_of_mass = sum_vector * (1 / len(vectors))
print(max_square(vectors))
