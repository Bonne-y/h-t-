import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv('iris_data.csv')

fig = plt.figure(figsize = (16,9))
a1 = fig.add_subplot(121)
a2 = fig.add_subplot(122)

less12 = [c for c in df['PetalLengthCm'] if c <= 1.2]
more15 = [j for j in df['PetalLengthCm'] if j > 1.5]
between = [m for m in df['PetalLengthCm'] if m > 1.2 and m <=1.5]

setosa = [c for c in df['Species'] if c == "Iris-setosa"]
versicolor = [j for j in df['Species'] if j == "Iris-versicolor"]
virginica = [m for m in df['Species'] if m == "Iris-virginica"]

a1.pie([len(less12), len(more15), len(between)], labels = ['<= 1.2', '> 1.5', '1.2 - 1.5'])
a2.pie([len(setosa), len(versicolor), len(virginica)], labels = ['setosa', 'versicolor', 'virginica'])

plt.show()
