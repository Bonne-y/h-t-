import numpy as np


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
    
    
print('Введите радиус-векторы точек(координаты) каждый в новой строчке.')
vectors = []
lines = True
while lines != []:
    lines = list(input().split())
    if lines: vectors.append(lines)

sum_vector = Vector(0,0,0)
for i in range(0, len(vectors)):
    sum_vector += Vector(float(vectors[i][0]), float(vectors[i][1]), float(vectors[i][2]))

    
center_of_mass = sum_vector*(1/len(vectors))
print(str(center_of_mass))
